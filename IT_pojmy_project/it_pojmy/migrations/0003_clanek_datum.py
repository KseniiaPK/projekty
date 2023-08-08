from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('it_pojmy', '0002_clanek'),
    ]

    operations = [
        migrations.AddField(
            model_name='clanek',
            name='datum',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]