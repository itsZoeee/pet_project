import os, csv, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from mysite.models import Adopt
with open("adoptimporter.csv", "r", encoding="utf-8") as fp:
    csv_reader = csv.reader(fp)
    data = list(csv_reader)

for row in data:
    try:
        rec = Adopt(
            species = row[0],
            breed = row[1],
            sex = row[2],
            size = row[3],
            color = row[4],
            age = row[5],
            ligation  = row[6],
            vaccine = row[7],
            location = row[8],
            pic = row[9],
        )
    except Exception as e:
        print(e)
    rec.save()