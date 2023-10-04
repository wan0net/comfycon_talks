import openpyxl_dictreader
import re
from jinja2 import Environment, FileSystemLoader

# Setup templates for Jinja
environment = Environment(loader=FileSystemLoader("./"))
speakers_template = environment.get_template("template_speaker.jinja")
talk_template = environment.get_template("template_talk.jinja")

# Load xlsx file and create objectts from them
speakers = openpyxl_dictreader.DictReader("comfycon_master.xlsx", "comfycon_speakers")
talks = openpyxl_dictreader.DictReader("comfycon_master.xlsx", "comfycon_talks")

for row in speakers:
    try:
        if row["name"] is not None:
            content = speakers_template.render(row)
            filename = row["name"].lower().replace(" ", "-") + ".md"
            with open("generated/speakers/" + filename, "w") as fh:
                fh.write(content)
                print("Created Speaker Profile: " + row["name"])
    except:
        print("Error with creating speaker: " + row["name"])

for row in talks:
    try:
        if row["talk_name"] is not None:
            content = talk_template.render(row)
            folder = ("generated/talks/" + row["event"] + "/").lower().replace(" ", "-")
            filename = row["talk_name"].lower().replace(" ", "-") + ".md"
            filename = clean = re.sub(r"[/\\?%*:|\"<>\x7F\x00-\x1F]", "-", filename)
            #print(filename)
            with open(folder + filename, "w") as fh:
                fh.write(content)
                print("Created Talk Profile: " + row["talk_name"])
    except Exception as e:
        print(e)
        print("Error with creating talk: " + row["talk_name"])
