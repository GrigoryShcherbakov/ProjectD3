from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_response_user_fio_alter_response_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Отклик отклоне'),
        ),
        migrations.AlterField(
            model_name='response',
            name='content',
            field=models.TextField(verbose_name='Контент отклика'),
        ),
        migrations.AlterField(
            model_name='response',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата отклика'),
        ),
    ]