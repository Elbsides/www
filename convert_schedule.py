"""Fetch and convert pretalx conference schedule XML to Markdown format."""
import xml.etree.ElementTree as ET
import re
import os
from html import unescape

def escape_md(text):
    """Escape Markdown table cell content as needed."""
    # Only | is problematic in table cells; escape it
    return text.replace('|', '&#124;')

def strip_html(text):
    """Remove HTML tags and unescape entities."""
    # Remove tags
    text = re.sub(r'<[^>]+>', '', text)
    return unescape(text).strip()

def make_speaker_link(person_id, name, base_url, conference_acronym):
    # /[name](base_url/acronym/speaker/person_id/)
    info_url = f"{base_url}/{conference_acronym}/speaker/{person_id}/"
    return f"[{escape_md(name)}]({info_url})"

def make_internal_reference(name):
    """Create an internal Markdown link for a given name."""
    # Convert name to lowercase, replace spaces with hyphens, and remove non-alphanumeric characters
    link = make_internal_link(name)
    return f"[{escape_md(name)}]({link})"

def make_talk_link(title, url):
    return f"[{escape_md(title)}]({url})"

def make_internal_link(heading_title):
    """Create an internal Markdown link for a given heading title."""
    # Convert heading title to lowercase, replace spaces with hyphens, and remove non-alphanumeric characters
    anchor = heading_title.lower()
    # Remove characters that are not alphanumeric, spaces, or dashes
    anchor = re.sub(r'[^\w\s-]', '', anchor)
    # Replace spaces with dashes
    anchor = anchor.replace(' ', '-')

    # link = re.sub(r'[^a-z0-9\-]', '', heading_title.lower().replace(' ', '-'))
    return f"#{anchor}"

def main(xml_file, year):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Get conference info
    conf_info = root.find("conference")
    base_url = conf_info.find("base_url").text.strip()
    acronym = conf_info.find("acronym").text.strip()

    # Index all speakers: {person_id: set(name, ...)}
    speaker_info = {} # id: name

    # Will store event table rows and full info blocks
    events = []

    # Index for later reference in info sections
    speaker_event_map = {}  # person_id: set(event_guids)
    event_speaker_map = {}  # event_guid: [person_id1, ...]

    # Parse event data
    for day in root.findall(".//day"):
        for room in day.findall("room"):
            for event in room.findall("event"):
                event_dict = {}
                event_dict['guid'] = event.get('guid')
                event_dict['id'] = event.get('id')
                event_dict['start'] = event.find('start').text
                event_dict['title'] = event.find('title').text
                event_dict['url'] = event.find('url').text
                event_dict['abstract'] = (event.find('abstract').text or "").strip()
                event_dict['type'] = event.find('type').text or ""
                event_dict['slug'] = event.find('slug').text or ""
                event_dict['duration'] = event.find('duration').text or ""
                event_dict['room'] = event.find('room').text or ""
                persons = []
                for person in event.find('persons').findall('person'):
                    pid = person.get('id')
                    name = strip_html(person.text or "")
                    speaker_info[pid] = name
                    persons.append(pid)
                    # Map speaker -> events
                    speaker_event_map.setdefault(pid, set()).add(event_dict['guid'])
                event_speaker_map[event_dict['guid']] = persons
                event_dict['persons'] = persons
                events.append(event_dict)

    with open(os.path.join(str(year), 'includes', 'schedule.md'), 'w', encoding='utf-8') as f:
        # Markdown Table Header
        f.write("# Program\n\n")
        f.write("| start time | speaker | title |\n")
        f.write("| ------------ | --------- | ----- |\n")

        for ev in events:
            # Compose speakers column
            if ev['persons']:
                speakers_column = ", ".join(
                    # make_speaker_link(pid, speaker_info[pid], base_url, acronym)
                    make_internal_reference(speaker_info[pid])
                    for pid in ev['persons']
                )
            else:
                speakers_column = ""
            # Compose title column
            # title_column = make_talk_link(ev['title'], ev['url'])
            title_column = make_internal_reference(ev['title'])
            # Compose time
            start_column = ev['start']
            # Print row
            f.write(f"| {escape_md(start_column)} | {speakers_column} | {title_column} |\n")

        # --- Speaker Info Sections ---
        f.write("\n# Speakers\n\n")
        for pid, name in speaker_info.items():
            f.write(f"## {name}\n\n")
            print(make_internal_link(name))
            url = f"{base_url}/{acronym}/speaker/{pid}/"
            # f.write(f"- **Profile:** [{url}]({url})\n")
            # List talks this speaker is in
            guids = speaker_event_map.get(pid, [])
            if guids:
                f.write("- **Talks:**\n")
                for guid in guids:
                    # Find event by guid
                    evs = [ev for ev in events if ev['guid'] == guid]
                    for ev in evs:
                        # talk_url = ev['url']
                        # f.write(f"  - [{ev['title']}]({talk_url}) ({ev['start']})\n")
                        f.write(f"  - {make_internal_reference(ev['title'])} ({ev['start']})\n")
            f.write("\n")
            f.write(f'---\n<span style="float: right">[&Sigma;](#speakers)&ensp;[&Pi;](#program)&ensp;[&Delta;](/{year}/)</span>\n\n')

        # --- Talk Info Sections ---
        f.write("\n# Talks\n\n")
        for ev in events:
            f.write(f"## {ev['title']}\n\n")
            print(make_internal_link(ev['title']))
            f.write(f"**Start time:** {ev['start']}\n")
            f.write(f"\n**Duration:** {ev['duration']}\n")
            # f.write(f"\n**Room:** {ev['room']}\n")
            # Speakers
            if ev['persons']:
                f.write("\n**Speaker(s):**\n")
                for pid in ev['persons']:
                    f.write(f"- {make_internal_reference(speaker_info[pid])}\n")
            # Abstract
            f.write("\n**Abstract:**\n")
            f.write(strip_html(ev['abstract'])+"\n")
            f.write("\n")
            # f.write(f"\n**Talk info:** [{ev['url']}]({ev['url']})\n\n")
            f.write(f'---\n<span style="float: right">[&Sigma;](#speakers)&ensp;[&Pi;](#program)&ensp;[&Delta;](/{year}/)</span>\n\n')
            # f.write("---\n\n")

if __name__ == "__main__":
    # Change to your input XML file, e.g. 'schedule.xml'
    main('schedule.xml', 2025)
