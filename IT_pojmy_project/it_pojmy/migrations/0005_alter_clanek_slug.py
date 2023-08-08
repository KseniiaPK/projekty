from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('it_pojmy', '0004_kategorie_clanek_kategorie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clanek',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]