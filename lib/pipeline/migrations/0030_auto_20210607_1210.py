# Generated by Django 2.2.19 on 2021-06-07 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pipeline", "0029_templaterelationship_always_use_latest"),
    ]

    operations = [
        migrations.AlterField(
            model_name="templaterelationship",
            name="descendant_template_id",
            field=models.CharField(db_index=True, max_length=32, verbose_name="子流程模板ID"),
        ),
    ]