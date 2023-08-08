from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('it_pojmy', '0003_clanek_datum'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kategorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=100)),
                ('nazev', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='clanek',
            name='kategorie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='it_pojmy.kategorie'),
        ),
    ]