import csv
from jinja2 import Environment, FileSystemLoader

environment = Environment(loader=FileSystemLoader("./"))
speakers_template = environment.get_template("template_speaker.jinja")
talk_template = environment.get_template("template_talk.jinja")

with open('comfycon_speakers.csv', newline='',encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
            content = speakers_template.render(row)
            filename = row["name"].lower().replace(" ", "-") + ".md"
            print(filename)
            with open("generated/speakers/" + filename, "w") as fh:
                fh.write(content)

with open('comfycon_talks.csv', newline='',encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
            content = talk_template.render(row)
            print(content)
            folder = ("generated/talks/" + row["event"] + "/").lower().replace(" ", "-")
            print(folder)
            filename = row["talk_name"].lower().replace(" ", "-") + ".md"
            #print(filename)
            with open(folder + filename, "w") as fh:
                fh.write(content)
    