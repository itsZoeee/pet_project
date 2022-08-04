import os, csv, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from mysite.models import Lost
with open("lostimporter.csv", "r", encoding="utf-8") as fp:
    csv_reader = csv.reader(fp)
    data = list(csv_reader)

for row in data:
    try:
        rec = Lost(
            name = row[0],
            variety = row[1],
            species = row[2],
            gender = row[3],
            body = row[4],
            color = row[5],
            age  = row[6],
            lostdate = row[7],
            area = row[8],
            pet_jpg = row[9],
        )
    except Exception as e:
        print(e)
    rec.save()

