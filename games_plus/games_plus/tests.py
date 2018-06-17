from django.test import TestCase
from django.urls import reverse
from django.db.models.query import QuerySet
from games_review.models import Game

class WebsiteTestCase(TestCase):
    fixtures = ['initial.json', ]
    def test_index_page(self):
        response = self.client.get(reverse('games_review:index'))
        self.assertContains(response, "Latests games")
        self.assertEqual(type(response.context['latest_games']), QuerySet)
        self.assertEqual(len(response.context['latest_games']), 3)
        self.failUnlessEqual(response.status_code, 200)
        self.assertTemplateUsed('games/list.html')
    def test_post_page(self):
        # Published news
        game = Game.objects.first()
        response = self.client.get(reverse('games_review:post', kwargs={'slug': game.slug}))
        self.assertContains(response, game.name)
        self.assertEqual(type(response.context['game']), Game)
        self.failUnlessEqual(response.status_code, 200)
        self.assertTemplateUsed('news/index.html')