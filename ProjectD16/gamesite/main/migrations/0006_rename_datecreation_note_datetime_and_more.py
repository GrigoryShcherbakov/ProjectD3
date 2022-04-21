from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_response_user_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='dateCreation',
            new_name='datetime',
        ),
        migrations.RenameField(
            model_name='response',
            old_name='dateCreation',
            new_name='datetime',
        ),
    ]