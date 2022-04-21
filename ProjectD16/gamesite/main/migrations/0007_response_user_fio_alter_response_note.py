
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_rename_datecreation_note_datetime_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='user_fio',
            field=models.CharField(default='ФИО не задано', max_length=64, verbose_name='ФИО_автора_объявления'),
        ),
        migrations.AlterField(
            model_name='response',
            name='note',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.note', verbose_name='Объявление'),
        ),
    ]