from django.test import TestCase
from eventex.subscriptions.models import Subscription
from datetime import datetime

class SubscriptionModelsTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Thais Martins',
            cpf='12345678901',
            email='thais@gmail.com',
            phone='11-96622-3338'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto created_at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Thais Martins', str(self.obj))
