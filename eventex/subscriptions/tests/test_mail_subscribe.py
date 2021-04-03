from django.core import mail
from django.test import TestCase


class SubscribeMail(TestCase):
    def setUp(self):
        data = dict(name='Thais Martins', cpf='12345678901',
                    email='thais@gmail.com', phone='11-96633-3338')
        self.resp = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com', 'thais@gmail.com']

        self.assertEqual(expect,  self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Thais Martins',
            '12345678901',
            'thais@gmail.com',
            '11-96633-3338'
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
