from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('it_pojmy', '0005_alter_clanek_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Komentar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=100)),
                ('obsah', models.CharField(max_length=500)),
                ('clanek', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='it_pojmy.clanek')),
            ],
        ),
    ]