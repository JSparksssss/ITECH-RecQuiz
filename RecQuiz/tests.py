from django.test import TestCase

# Create your tests here.
from django.urls import reverse


class RemoveCourse(TestCase):
    def test_remove_course(self):
        response = self.client.get(reverse('RecQuiz:remove_course'))
        self.assertEqual(response.status_code,200)