from django.test import TestCase
from .models import ListaModels
from datetime import datetime

class IndexTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_200(self):
        self.assertEqual(200, self.resp.status_code)

    def test_Texto(self):
        self.assertContains(self.resp, 'NAC')

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'index.html')

class AtividadeModelTest(TestCase):
    def setUp(self):
        self.cadastro = ListaModels(
            aluno='Aluno de teste',
            professor='Orlando Júnior - Desenvolvimento Web III',
        )
        self.cadastro.save()

    def test_criado(self):
        self.assertTrue(ListaModels.objects.exists())

    def test_criado_somente_um(self):
        self.assertTrue(len(ListaModels.objects.all()) == 1)

    def test_modificado_em(self):
        self.assertIsInstance(self.cadastro.modificado_em, datetime)

