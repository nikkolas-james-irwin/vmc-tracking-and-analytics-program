# Generated by Django 3.1.2 on 2021-04-19 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualizations', '0006_auto_20210328_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportpresets',
            name='category',
            field=models.CharField(choices=[('Benefit Chapter', 'Benefit Chapter'), ('Residential Distance from Campus', 'Residential Distance from Campus'), ('Employment', 'Employment'), ('Weekly Hours Worked', 'Weekly Hours Worked'), ('Number of Dependents', 'Number of Dependents'), ('Marital Status', 'Marital Status'), ('Gender Identity', 'Gender Identity'), ('Parent Education', 'Parent Education'), ('Break in University Attendance', 'Break in University Attendance'), ('Pell Grant', 'Pell Grant'), ('Needs Based Grants/Scholarships', 'Needs Based Grants/Scholarships'), ('Merits Based Grants/Scholarships', 'Merits Based Grants/Scholarships'), ('Federal Work Study', 'Federal Work Study'), ('Military Grants', 'Military Grants'), ('Millennium Scholarship', 'Millennium Scholarship'), ('Nevada Pre-Paid', 'Nevada Pre-Paid'), ('Best Method of Contact', 'Best Method of Contact'), ('Classification', 'Classification'), ('Major', 'Major'), ('Services', 'Services')], max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='reportpresets',
            name='custom_even_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='reportpresets',
            name='gpa_to_compare',
            field=models.CharField(choices=[('Average end term Semester GPA', 'Average end term Semester GPA'), ('Average end term Cumulative GPA', 'Average end term Cumulative GPA'), ('Average end term Attempted Credits', 'Average end term Attempted Credits'), ('Average end term Earned Credits', 'Average end term Earned Credits'), ('Average end term Cumulative Completed Credits', 'Average end term Cumulative Completed Credits')], max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='reportpresets',
            name='report_type',
            field=models.CharField(choices=[('Count visits over time', 'Count visits over time'), ('Compare GPA against demographics', 'Compare GPA against demographics')], max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='reportpresets',
            name='use_custom_event_name',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=50, null=True),
        ),
    ]
