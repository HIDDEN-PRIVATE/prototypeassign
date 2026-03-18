import csv

from django.core.management import BaseCommand

from Main.models import Course

class Command(BaseCommand):
    help = "this command adds objects to Course"

    def add_arguments(self, parser):

        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):

        path = kwargs['path']

        with open(path, 'rt', encoding='utf-8-sig') as f:

            reader = csv.reader(f, dialect='excel')

            for row in reader:

                Course.objects.create(CourseName=row[0])