from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_response_status_alter_response_content_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='response',
            old_name='user_author',
            new_name='user_note',
        ),
        migrations.AlterField(
            model_name='response',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Статус отклика'),
        ),
    ]