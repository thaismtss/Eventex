from django.core import mail
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


class SubscribeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/inscricao/')

    def test_get(self):
        """GET /inscricao/ must return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Must use subscriptions/subscription_form.html"""
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def test_html(self):
        """Html must contains tags"""
        tags = (
            ('<form', 1),
            ('<input', 6),
            ('type="text"', 3),
            ('type="email"', 1),
            ('type="submit"', 1))
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

    def test_csrf(self):
        """Html must contain csrf"""
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Context must have subscription form"""
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)


class SubscriptionValidPostTest(TestCase):
    def setUp(self):
        data = dict(name='Thais Martins', cpf='12345678901', email='thais@gmail.com', phone='11-96633-3338')
        self.resp = self.client.post('/inscricao/', data)

    def test_post(self):
        """Valid POST"""
        self.assertEqual(302, self.resp.status_code)

    def test_send_subscribe_mail(self):
        self.assertEqual(1, len(mail.outbox))
    
    def test_save_subscription(self):
        self.assertTrue(Subscription.objects.exists())



class SubscriptionInvalidPostTest(TestCase):
    def setUp(self):
        self.resp = self.client.post('/inscricao/', {})

    def test_post(self):
        """Invalid Post"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_has_form_error(self):
        form = self.resp.context['form']
        self.assertTrue(form.errors)
    
    def test_dont_save_subscription(self):
        self.assertFalse(Subscription.objects.exists())


class SubscribeMessageSuccess(TestCase):
    def test_message(self):
        data = dict(name='Thais Martins', cpf='12345678901',
                    email='thais@gmail.com', phone='11-96633-3338')

        response = self.client.post('/inscricao/', data, follow=True)
        self.assertContains(response, 'Inscrição realizada com sucesso!')
