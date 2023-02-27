from django.test import TestCase
from django.urls import reverse


class SiteViewTest(TestCase):
    def setUp(self):
        self.pages = [
            "about",
            "start",
            "why",
            "comfort",
            "legs",
            "hands",
            "back",
            "chest",
            "shoulders",
            "head",
            "exercises",
            "sources",
            "contact",
        ]

    def test_view_base_url(self):
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)

    def test_view_index_route(self):
        resp = self.client.get(reverse("index"))
        self.assertEqual(resp.status_code, 200)

    def test_view_page_route(self):
        resp = self.client.get(reverse("page", args=["about"]))
        self.assertEqual(resp.status_code, 200)

    def test_view_all_page_routes(self):
        for page in self.pages:
            resp = self.client.get(reverse("page", args=["why"]))
            self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        for page in self.pages:
            resp = self.client.get(reverse("page", args=[page]))
            self.assertTemplateUsed(resp, "layout.html")
