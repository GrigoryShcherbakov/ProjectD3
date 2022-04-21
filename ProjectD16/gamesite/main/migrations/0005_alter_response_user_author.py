
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_response_user_response_alter_response_user_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='user_author',
            field=models.IntegerField(default=0, verbose_name='id_автора_объявления'),
        ),
    ]