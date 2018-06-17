from django.test import TestCase
from django.urls import reverse
from django.db.models.query import QuerySet
from Diablo3_review.models import MyArticle

class WebsiteTestCase(TestCase):
    fixtures = ['initial.json', ]
    def test_index_page(self):
        response = self.client.get(reverse('Diablo3_review:index'))
        self.assertContains(response, "article")
        self.assertEqual(len(response.context['article']), 3)
        self.failUnlessEqual(response.status_code, 200)
        
