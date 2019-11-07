# Generated by Django 2.2.4 on 2019-09-26 02:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_sentence'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, default='')),
                ('bibtext', models.TextField(blank=True, default='')),
                ('license', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='', help_text='Informal name that a person prefers to be addressed by in spoken or text dialog.')),
                ('full_name', models.TextField(blank=True, default='')),
                ('first_name', models.TextField(blank=True, default='')),
                ('last_name', models.TextField(blank=True, default='')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Context',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='conversation', max_length=255)),
                ('subcontext', models.CharField(blank=True, max_length=255, null=True)),
                ('attribution', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='bot.Attribution')),
            ],
        ),
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Username',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='', help_text='Informal name that agent has named themself.')),
                ('active', models.NullBooleanField(default=False)),
                ('last_used', models.DateTimeField(help_text='Last time the username was used in a dialog (as a speaker/texter/chatter). null: presumably still being used.', null=True)),
                ('first_used', models.DateTimeField()),
                ('url', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='bot.URL')),
            ],
        ),
        migrations.CreateModel(
            name='Statement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
                ('reply', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='bot.Statement', verbose_name='statements this is an acceptable reply to')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bot.Context')),
            ],
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spoken_name', models.TextField(blank=True, default='')),
                ('bot', models.NullBooleanField(default=False)),
                ('username', models.TextField(blank=True, default='')),
                ('likelihood', models.FloatField(blank=True, default=1.0)),
                ('contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='bot.Contact')),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likelihood', models.FloatField(blank=True, default=1.0)),
                ('context', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bot.Context')),
                ('speaker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='bot.Speaker')),
            ],
        ),
        migrations.CreateModel(
            name='DialogState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bot.Context')),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='urls',
            field=models.ManyToManyField(to='bot.URL'),
        ),
        migrations.AddField(
            model_name='attribution',
            name='contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='bot.Contact'),
        ),
    ]
