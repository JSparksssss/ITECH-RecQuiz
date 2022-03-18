from django.test import TestCase

# Create your tests here.
from django.urls import reverse


class RemoveCourseTests(TestCase):
    def test_checkWeb(self):
        response = self.client.get(reverse('RecQuiz:my_course'))
        self.assertEqual(response.status_code,200)
