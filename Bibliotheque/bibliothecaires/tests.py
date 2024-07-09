from django.test import TestCase
from .models import Media, Emprunteur

class MediaTestCase(TestCase):
    def setUp(self):
        self.emprunteur = Emprunteur.objects.create(name="Test Emprunteur")
        self.media = Media.objects.create(name="Test Media", auteur="Auteur", type_media="Livre")

    def test_emprunt_media(self):
        self.media.emprunter(self.emprunteur)
        self.assertFalse(self.media.disponible)
        self.assertEqual(self.media.emprunteur, self.emprunteur)

    def test_retour_media(self):
        self.media.emprunter(self.emprunteur)
        self.media.retourner()
        self.assertTrue(self.media.disponible)
        self.assertIsNone(self.media.emprunteur)
