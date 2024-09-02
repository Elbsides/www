import csv
import os
import sys


def render_speakers(speakers, links=None):
    if speakers == '':
        return ''
    if '|' in speakers:
        speakers = speakers.split('|')
        if links:
            links = links.split('|')
            return ', '.join([f"({speaker.strip()})[{link.strip()}]" for speaker, link in zip(speakers, links)])
        else:
            return ', '.join([f"{speaker.strip()}" for speaker in speakers])
    if links:
        return f"({speakers})[{links}]"
    else:
        return f"{speakers}"


def ms_break_line(record):
    return f"| {record['start']} | | {record['title']} |"

def md_talk_line(record):
    return f"| {record['start']} | {render_speakers(record['speaker'], record['speakerlink'])} | ({record['title']})[{record['titlelink']}] |"

def md_administrivia_line(record):
    return f"| {record['start']} | {render_speakers(record['speaker'], record['speakerlink'])} | {record['title']} |"

def md_keynote_line(record):
    return f"| {record['start']} | {render_speakers(record['speaker'], record['speakerlink'])} | Keynote: ({record['title']})[{record['titlelink']}] |"

def main(input_file):
    md_schedule = ["| Time | Speaker | Title |","| ---- | ------- | ----- |"]
    video_schedule = []
    directory = os.path.dirname(input_file)
    file_name = os.path.splitext(os.path.basename(input_file))[0]
    # print(directory, file_name)
    with open(input_file, 'r', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for record in list(reader):
            # print(record)
            if record["type"] == "talk":
                md_schedule.append(md_talk_line(record))
            elif record["type"] == "keynote":
                md_schedule.append(md_keynote_line(record))
            elif record["type"] == "break":
                md_schedule.append(ms_break_line(record))
            elif record["type"] == "administrivia":
                md_schedule.append(md_administrivia_line(record))

            if record["type"] == "administrivia" or record["type"] == "talk" or record["type"] == "keynote":
                title_lines = []
                title = record['title']
                while len(title) > 40:
                    split_index = title[:40].rfind(' ')
                    if split_index == -1:
                        split_index = 40
                    title_lines.append(title[:split_index].strip())
                    title = title[split_index:].strip()
                title_lines.append(title)

                start_time = record['start']
                duration = record['duration']
                start_hour, start_minute = map(int, start_time.split(':'))
                duration_hour, duration_minute = map(int, duration.split(':'))

                end_hour = start_hour + duration_hour
                end_minute = start_minute + duration_minute

                if end_minute >= 60:
                    end_hour += 1
                    end_minute -= 60

                # end_time = f"{end_hour:02d}:{end_minute:02d}"
                start_to_end = f"{start_hour:02d}:{start_minute:02d}-{end_hour:02d}:{end_minute:02d}"
                video_schedule += [f"{start_to_end}\t{title_line}" for title_line in title_lines]
                video_schedule.append(f"{start_to_end}\t - {render_speakers(record['speaker'])}")
                video_schedule.append("")

    with open(os.path.join(directory, f"{file_name}.md"), 'w', encoding="utf-8") as f:
        f.write("\n".join(md_schedule))

    # print("\n".join(video_schedule))
    with open(os.path.join(directory, f"{file_name}.txt"), 'w', encoding="utf-8") as f:
        f.write("\n".join(video_schedule))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        if not os.path.exists(input_file):
            print(f"File {input_file} does not exist.")
            sys.exit(1)
        if not os.path.isfile(input_file):
            print(f"{input_file} is not a file.")
            sys.exit(1)
        if not os.path.splitext(input_file)[1] == '.csv':
            print("Please provide a CSV file as input.")
            sys.exit(1)
    else:
        print("Please provide the input file path as a command line argument.")
        sys.exit(1)
    main(input_file)
