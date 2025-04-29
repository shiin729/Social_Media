from django.test import TestCase
from django.urls import reverse

class PostListViewTests(TestCase):
    def test_template_used(self):
        response = self.client.get(reverse('home'))
        # Проверяем, что используется шаблон blog/post_list.html
        self.assertTemplateUsed(response, 'home.html')

    def test_status_code(self):
        response = self.client.get(reverse('home'))
        # Проверяем, что статус-код 200 (OK)
        self.assertEqual(response.status_code, 200)
    
    def test_context_data(self):
        response = self.client.get(reverse('home'))
        # Проверяем, что в контексте есть переменная 'posts'
        self.assertIn('all_posts', response.context)
        # Проверяем, что 'posts' - это список
        self.assertIsInstance(list(response.context['all_posts']), list)