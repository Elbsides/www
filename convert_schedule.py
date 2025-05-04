"""Fetch and convert pretalx conference schedule JSON to Markdown format."""
import json
import re
import os
from io import TextIOWrapper
from typing import Set, Dict
from datetime import datetime, timedelta
import urllib.request
from html import unescape


def escape_md(text: str) -> str:
    """Escape Markdown table cell content as needed."""
    # Only | is problematic in table cells; escape it
    return text.replace('|', '&#124;')


def strip_html(text: str) -> str:
    """Remove HTML tags and unescape entities."""
    # Remove tags
    text = re.sub(r'<[^>]+>', '', text)
    return unescape(text).strip()


def make_internal_reference(name: str) -> str:
    """Create an internal Markdown link for a given name."""
    # Convert name to lowercase, replace spaces with hyphens, and remove non-alphanumeric characters
    link = make_internal_link(name)
    return f"[{escape_md(name)}]({link})"


def make_internal_link(heading_title: str) -> str:
    """Create an internal Markdown link for a given heading title."""
    # Convert heading title to lowercase, replace spaces with hyphens, and remove non-alphanumeric characters
    anchor = heading_title.lower()
    # Remove characters that are not alphanumeric, spaces, or dashes
    anchor = re.sub(r'[^\w\s-]', '', anchor)
    # Replace spaces with dashes
    anchor = anchor.replace(' ', '-')
    return f"#{anchor}"


def write_schedule_version(version: str, f: TextIOWrapper) -> None:
    """Write the schedule version to the Markdown file."""
    f.write(f"\nThis is version {version} of the schedule.\n")


def create_networking_event(last_event: Dict) -> Dict:
    """Create a networking event entry."""
    networking_start_time = last_event['start_time'] + last_event['duration_time']
    networking_event = {
            'guid': 'networking-hour',
            'id': 'networking-hour',
            'start': networking_start_time.strftime('%H:%M'),
            'title': 'Networking Hour',
            'url': '',
            'abstract': 'An hour dedicated to networking, discussions and drinks.',
            'type': 'Networking',
            'slug': 'networking-hour',
            'duration': '01:00',
            'room': 'Elbkuppel',
            'start_time': networking_start_time,
            'duration_time': timedelta(hours=1),
            'persons': []
        }
    return networking_event


def write_program_break(f: TextIOWrapper, current_time: datetime) -> None:
    """Write a break entry in the program."""
    if current_time.hour < 12:
        break_type = "morning"
    elif 12 <= current_time.hour < 14:
        break_type = "lunch"
    else:
        break_type = "afternoon"
    f.write(f"| {escape_md(current_time.strftime('%H:%M'))} | &nbsp; | {break_type} break |\n")


def write_program_entry(f: TextIOWrapper, ev: Dict) -> None:
    """Write an event entry in the program."""
    if ev['persons']:
        speakers_column = ", ".join(
            make_internal_reference(p["name"])
                for p in ev['persons']
        )
    else:
        speakers_column = ""
    start_column = ev['start']
    title_column = make_internal_reference(ev['title'])
    f.write(f"| {escape_md(start_column)} | {speakers_column} | {title_column} |\n")


def write_program_header(f: TextIOWrapper) -> None:
    """Write the header for the program section."""
    f.write("# Program\n\n")
    f.write("| start time | speaker | title |\n")
    f.write("| ------------ | --------- | ----- |\n")


def get_avatar(person: Dict, year) -> str:
    """Download the avatar from pretalx to the correct directory and return a local link to it."""
    if person['avatar']:
        link = os.path.join('assets', str(year), 'avatars', person['avatar'].split('/')[-1])
        if os.path.exists(link):
            return link
        # avatar_path = os.path.join('www', link)
        os.makedirs(os.path.dirname(link), exist_ok=True)
        print(f"Downloading {person['avatar']} to {link}")
        r, message = urllib.request.urlretrieve(person['avatar'], link)
        print(r)
        return link
    else:
        return None


def parse(data: Dict, year: int) -> None:
    """Parse JSON data and convert it to Markdown format."""
    speaker_info = {}  # id: name
    speaker_event_map: dict[str, Set] = {}  # person_id: set(event_guids)
    event_speaker_map = {}  # event_guid: [person_id1, ...]
    avatars = {}  # person_id: avatar_url
    speaker_list = set()
    biographies: Dict[str, str] = {} # person_id: biography

    # Parse the JSON data
    schedule = data['schedule']
    version = schedule['version']
    events = schedule['conference']['days'][0]['rooms']['Elbkuppel']
    for event in events:
        event['backup'] = False
        event['start_time'] = datetime.strptime(event['start'], "%H:%M")
        d = datetime.strptime(event['duration'], "%H:%M")
        event['duration_time'] = timedelta(minutes=d.minute, hours=d.hour)
        persons = []
        for person in event['persons']:
            pid = person["guid"]
            speaker_info[pid] = strip_html(person["name"])
            persons.append(pid)
            speaker_list.add(person["name"])
            if "avatar" in person and person["avatar"]:
                # Download avatar
                avatars[pid] = get_avatar(person, year)
            if not(person.get('biography') is None or person.get('biography') == 'None'):
                biographies[pid] = strip_html(person.get("biography", ""))
            # Map speaker -> events
            speaker_event_map.setdefault(pid, set()).add(event['guid'])
        event_speaker_map[event['guid']] = persons
    backups = schedule['conference']['days'][0]['rooms']['Backup']
    for event in backups:
        event['backup'] = True
        persons = []
        for person in event['persons']:
            pid = person["guid"]
            speaker_info[pid] = strip_html(person["name"])
            persons.append(pid)
            speaker_list.add(person["name"])
            if "avatar" in person and person["avatar"]:
                # Download avatar
                avatars[pid] = get_avatar(person, year)
            if not(person.get('biography') is None or person.get('biography') == 'None'):
                biographies[pid] = strip_html(person.get("biography", ""))
            # Map speaker -> events
            speaker_event_map.setdefault(pid, set()).add(event['guid'])
        event_speaker_map[event['guid']] = persons

    with open(os.path.join(str(year), 'includes', 'schedule.md'), 'w', encoding='utf-8') as f:
        # Markdown Table Header
        write_program_header(f)
        current_time = None
        for ev in events:
            # Compose speakers column
            if current_time and ev['start_time'] > current_time:
                # Add empty row for breaks
                write_program_break(f, current_time)
            # Compose time
            write_program_entry(f, ev)
            current_time = ev['start_time'] + ev['duration_time']
        write_program_entry(
            f,
            create_networking_event(
                max(events, key=lambda ev: ev['start_time'] + ev['duration_time'])
            )
        )
        write_schedule_version(version, f)

        # --- Speaker Info Sections ---
        f.write("\n# Speakers\n\n")
        f.write(', '.join([make_internal_reference(s) for s in sorted(speaker_list)])+"\n\n")
        # Sort speaker_info by name
        sorted_speaker_info = dict(sorted(speaker_info.items(), key=lambda item: item[1]))
        for pid, name in sorted_speaker_info.items():
            f.write(f"## {name}\n\n")
            if pid in avatars:
                f.write(f'<img src="/{avatars[pid]}" alt="{name}" width="150"  style="float: right;">\n\n')
            if pid in biographies:
                f.write("**Biography:**\n\n")
                f.write(strip_html(biographies[pid])+"\n\n")
            # List talks this speaker is in
            guids: Set = speaker_event_map.get(pid, set())
            f.write("- **Talks:**\n")
            for guid in guids:
                # Find event by guid
                evs = [ev for ev in events+backups if ev['guid'] == guid]
                for ev in evs:
                    # talk_url = ev['url']
                    # f.write(f"  - [{ev['title']}]({talk_url}) ({ev['start']})\n")
                    if ev['backup']:
                        f.write(f"  - Backup talk: {make_internal_reference(ev['title'])}\n")
                    else:
                        f.write(f"  - {make_internal_reference(ev['title'])} ({ev['start']})\n")
            f.write("\n")
            f.write(f'---\n<span style="float: right">[&Sigma;](#speakers)&ensp;[&Pi;](#program)&ensp;[&Delta;](/{year}/)</span>\n\n')

        # --- Talk Info Sections ---
        f.write("\n# Talks\n\n")
        for ev in events+backups:
            f.write(f"## {ev['title']}\n\n")
            if ev['room'] == 'Backup':
                f.write("**Backup talk**\n\n")
            else:
                f.write(f"**Start time:** {ev['start']}\n")
                f.write(f"\n**Duration:** {ev['duration']}\n")
            # f.write(f"\n**Room:** {ev['room']}\n")
            # Speakers
            if ev['persons']:
                f.write("\n**Speaker(s):**\n")
                for p in ev['persons']:
                    f.write(f"- {make_internal_reference(speaker_info[p['guid']])}\n")
            # Abstract
            f.write("\n**Abstract:**\n")
            f.write(strip_html(ev['abstract'])+"\n")
            f.write("\n")
            # f.write(f"\n**Talk info:** [{ev['url']}]({ev['url']})\n\n")
            f.write(f'---\n<span style="float: right">[&Sigma;](#speakers)&ensp;[&Pi;](#program)&ensp;[&Delta;](/{year}/)</span>\n\n')


if __name__ == "__main__":
    YEAR = 2025

    headers = {
        'Accept': 'application/json',
    }
    req = urllib.request.Request(
        f'https://pretalx.com/elbsides-{YEAR}/schedule/export/schedule.json',
        headers=headers
    )
    with urllib.request.urlopen(req) as response:
        schedule_data = json.loads(response.read().decode('utf-8'))

    parse(schedule_data, YEAR)
