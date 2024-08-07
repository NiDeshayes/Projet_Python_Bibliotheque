from django.test import TestCase
from django.utils import timezone
from .models import Membre, Media, Emprunt


class BibliothequeTests(TestCase):

    def setUp(self):
        self.membre = Membre.objects.create(nom='Doe', prenom='John')
        self.media1 = Media.objects.create(titre='Livre 1', type_media='Livre')
        self.media2 = Media.objects.create(titre='CD 1', type_media='CD')
        self.media3 = Media.objects.create(titre='DVD 1', type_media='DVD')
        self.media4 = Media.objects.create(titre='Jeu de plateau 1', type_media='Jeu de plateau')

    def test_emprunter_media(self):
        emprunt1 = Emprunt.objects.create(membre=self.membre, media=self.media1)
        emprunt2 = Emprunt.objects.create(membre=self.membre, media=self.media2)
        emprunt3 = Emprunt.objects.create(membre=self.membre, media=self.media3)

        self.assertEqual(self.membre.emprunts_actifs, 3)
        self.assertTrue(self.media1.disponible is False)
        self.assertTrue(self.media2.disponible is False)
        self.assertTrue(self.media3.disponible is False)

        with self.assertRaises(ValueError):
            Emprunt.objects.create(membre=self.membre, media=self.media4)

    def test_rendre_media(self):
        emprunt = Emprunt.objects.create(membre=self.membre, media=self.media1)
        emprunt.date_retour = timezone.now()
        emprunt.save()

        self.assertEqual(self.membre.emprunts_actifs, 0)
        self.assertTrue(self.media1.disponible is True)
