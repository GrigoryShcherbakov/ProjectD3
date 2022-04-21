from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0009_rename_user_author_response_user_note_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='response',
            name='user_note',
        ),
        migrations.AlterField(
            model_name='response',
            name='user_response',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='id_автора_отклика'),
        ),
    ]