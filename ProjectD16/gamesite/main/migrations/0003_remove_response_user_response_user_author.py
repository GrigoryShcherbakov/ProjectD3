
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_rename_note_id_response_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='response',
            name='user',
        ),
        migrations.AddField(
            model_name='response',
            name='user_author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='id_автора_объявления'),
            preserve_default=False,
        ),
    ]