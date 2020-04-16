from django.test import TestCase
from django.shortcuts import resolve_url as r


class CoreTest(TestCase):
    def setUp(self):
        self.response = self.client

    def test_home_get_status_ok(self):
        expect = self.response.get(r('/'))
        self.assertEqual(200, expect.status_code)

    def test_template_used(self):
        expect = self.response.get(r('/'))
        self.assertTemplateUsed(expect, 'blog/index.html')

