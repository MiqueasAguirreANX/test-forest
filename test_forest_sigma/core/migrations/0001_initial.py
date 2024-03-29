# Generated by Django 2.2.13 on 2021-01-22 13:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=150, null=True)),
                ('subscale', models.CharField(blank=True, choices=[('1', 'SELF-ANALYSIS'), ('2', 'INTUITION'), ('3', 'MEDITATION'), ('4', 'AMBITION'), ('5', 'PRIDE'), ('6', 'LEADERSHIP'), ('7', 'CONVERSATION'), ('8', 'AFFILIATION'), ('9', 'SOLIDARITY'), ('10', 'AUTONOMY'), ('11', 'FREEDOM'), ('12', 'SOLITUDE'), ('13', 'AMUSEMENT'), ('14', 'EROTICISM'), ('15', 'PLAYFULNESS'), ('16', 'ORDERLINESS'), ('17', 'PLANNING'), ('18', 'PRECISION'), ('19', 'INNOVATION'), ('20', 'ABSTRACTION'), ('21', 'REFLECTION'), ('22', 'CONFORMITY'), ('23', 'TRADITION'), ('24', 'SECURITY'), ('25', 'DEVOTION'), ('26', 'HARMONY'), ('27', 'RESPECT'), ('28', 'RESPONSE'), ('29', 'REVENGE'), ('30', 'ANGER'), ('31', 'TEMERITY'), ('32', 'ADVENTURE'), ('33', 'VARIETY'), ('34', 'JOVIALITY'), ('35', 'VIVACITY'), ('36', 'OPTIMISM')], max_length=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Randomized',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('random', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.IntegerField(null=True)),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
