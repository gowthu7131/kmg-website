from django.test import TestCase, Client
from django.urls import reverse
from core.models import ContactInquiry


class KMGViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/home.html')
        self.assertTemplateUsed(response, 'core/base.html')
        self.assertContains(response, 'KMG GARMENTS')
        self.assertContains(response, 'viewport')

    def test_about_page(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/about.html')
        self.assertContains(response, 'About Us')

    def test_products_page(self):
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/products.html')
        self.assertContains(response, 'COMPANY PRODUCTS')

    def test_contact_page_get(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/contact.html')
        self.assertContains(response, 'Contact Us')

    def test_contact_form_post_valid(self):
        data = {
            'name': 'Ramesh Kumar',
            'email': 'ramesh@example.com',
            'message': 'Interested in bulk towel orders.',
        }
        response = self.client.post(reverse('contact'), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('contact'))

        inquiry = ContactInquiry.objects.filter(email='ramesh@example.com').first()
        self.assertIsNotNone(inquiry)
        self.assertEqual(inquiry.name, 'Ramesh Kumar')
        self.assertEqual(inquiry.message, 'Interested in bulk towel orders.')

    def test_contact_form_post_invalid(self):
        data = {
            'name': 'Ramesh Kumar',
            'email': '',
            'message': '',
        }
        response = self.client.post(reverse('contact'), data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ContactInquiry.objects.count(), 0)
