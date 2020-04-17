from django.test import TestCase
from core.models import Project


class ModelTest(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
            title='My first project',
            description='A web development project.',
            technology='Django',
            image='img/teste.png'
        )
