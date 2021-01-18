from django.db import models
from django.conf import settings
# Create your models here.
CATEGORY_CHOICES = (
    ('1', 'SELF-ANALYSIS'),
    ('2', 'INTUITION'),
    ('3', 'MEDITATION'),
    ('4', 'AMBITION'),
    ('5', 'PRIDE'),
    ('6', 'LEADERSHIP'),
    ('7', 'CONVERSATION'),
    ('8', 'AFFILIATION'),
    ('9', 'SOLIDARITY'),
    ('10', 'AUTONOMY'),
    ('11', 'FREEDOM'),
    ('12', 'SOLITUDE'),
    ('13', 'AMUSEMENT'),
    ('14', 'EROTICISM'),
    ('15', 'PLAYFULNESS'),
    ('16', 'ORDERLINESS'),
    ('17', 'PLANNING'),
    ('18', 'PRECISION'),
    ('19', 'INNOVATION'),
    ('20', 'ABSTRACTION'),
    ('21', 'REFLECTION'),
    ('22', 'CONFORMITY'),
    ('23', 'TRADITION'),
    ('24', 'SECURITY'),
    ('25', 'DEVOTION'),
    ('26', 'HARMONY'),
    ('27', 'RESPECT'),
    ('28', 'RESPONSE'),
    ('29', 'REVENGE'),
    ('30', 'ANGER'),
    ('31', 'TEMERITY'),
    ('32', 'ADVENTURE'),
    ('33', 'VARIETY'),
    ('34', 'JOVIALITY'),
    ('35', 'VIVACITY'),
    ('36', 'OPTIMISM'),
)


class Question(models.Model):
    question = models.CharField(max_length=150, null=True)
    subscale = models.CharField(
        choices=CATEGORY_CHOICES, max_length=2, null=True)

    def __str__(self) -> str:
        return f'{self.question} {self.subscale}'


class Answer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, null=True)
    answer = models.IntegerField(null=True)

    def __str__(self) -> str:
        return f'answer {self.answer} to question {self.question.subscale}'
