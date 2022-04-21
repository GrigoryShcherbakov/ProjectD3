
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_remove_response_user_response_user_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='user_response',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='id_пользователя_отклика'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='response',
            name='user_author',
            field=models.TextField(verbose_name='id_автора_объявления'),
        ),
    ]