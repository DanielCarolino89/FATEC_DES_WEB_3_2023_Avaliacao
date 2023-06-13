from ast import Return
from django.db import models
from django.core.exceptions import ValidationError

PROFESSORES = [
    ('João Neto', 'João Neto'),
    ('Orlando Júnior','Orlando Júnior'),
    ('Nilton Sacco','Nilton Sacco'),
    ('Esdras da Silva','Esdras da Silva'),
]

MATERIA = [
    ('Álgebra Linear', 'Álgebra Linear'),
    ('Desenvolvimento Web III', 'Desenvolvimento Web III'),
    ('Banco de Dados Relacional', 'Banco de Dados Relacional'),
    ('Técnicas de Programação II', 'Técnicas de Programação II'),

]


def validate_min_length(value):
    if len(value) < 10:
        raise ValidationError('O campo deve ter no mínimo 10 caracteres.')


class ListaModels(models.Model):
    data = models.DateField('data')
    aluno = models.CharField('aluno', max_length=200,
                             validators=[validate_min_length])
    professor = models.CharField(
        'professor', max_length=200, choices=PROFESSORES)
    materia = models.CharField('materia',max_length=200,choices=MATERIA)

    modificado_em = models.DateTimeField(
        verbose_name='modificado em',
        auto_now_add=False, auto_now=True)

    def __str__(self):
        return "{} ({})".format(self.aluno, self.professor)
