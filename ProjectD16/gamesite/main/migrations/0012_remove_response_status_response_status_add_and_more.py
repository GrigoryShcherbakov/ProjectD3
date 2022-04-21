rom django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_remove_response_user_fio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='response',
            name='status',
        ),
        migrations.AddField(
            model_name='response',
            name='status_add',
            field=models.BooleanField(default=False, verbose_name='Статус отклика - принят'),
        ),
        migrations.AddField(
            model_name='response',
            name='status_del',
            field=models.BooleanField(default=False, verbose_name='Статус отклика - отклонен'),
        ),
    ]