from ast import Return
from django.db import models

PROFESSORES = [
    ('João Neto - Álgebra Linear', 'João Neto - Álgebra Linear'),
    ('Orlando Júnior - Desenvolvimento Web III',
     'Orlando Júnior - Desenvolvimento Web III'),
    ('Nilton Sacco - Banco de Dados Relacional',
     'Nilton Sacco - Banco de Dados Relacional'),
    ('Esdras da Silva - Técnicas de Programação II',
     'Esdras da Silva - Técnicas de Programação II'),
]

class ListaModels(models.Model):
    aluno = models.CharField('aluno', max_length=200,)
    professor = models.CharField('professor', max_length=200, choices=PROFESSORES)

    modificado_em = models.DateTimeField(
        verbose_name='modificado em',
        auto_now_add=False, auto_now=True)

    def __str__(self):
        return "{} ({})".format(self.aluno, self.professor)
