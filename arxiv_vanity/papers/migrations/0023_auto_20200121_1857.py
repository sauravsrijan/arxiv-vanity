# Generated by Django 2.2.8 on 2020-01-21 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0022_remove_paper_source_file_old'),
    ]

    operations = [
        migrations.RenameField(
            model_name='render',
            old_name='is_expired',
            new_name='is_deleted',
        ),
        migrations.AlterField(
            model_name='sourcefile',
            name='bulk_tarball',
            field=models.ForeignKey(blank=True, help_text="If this source file is from arXiv's bulk download service, this is the tarball it was in. If null, this source file was downloaded individually.", null=True, on_delete=django.db.models.deletion.SET_NULL, to='papers.SourceFileBulkTarball'),
        ),
    ]
