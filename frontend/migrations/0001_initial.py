# Generated by Django 2.2.4 on 2019-08-02 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OnlineAdmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admission_id', models.CharField(max_length=10)),
                ('student_fname', models.CharField(max_length=20)),
                ('student_lname', models.CharField(max_length=20)),
                ('student_oname', models.CharField(blank=True, max_length=20, null=True)),
                ('student_gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=7)),
                ('student_address', models.CharField(max_length=200)),
                ('student_religion', models.CharField(choices=[('Islam', 'Islam'), ('Christianity', 'Christianity')], max_length=13)),
                ('student_dob', models.DateField()),
                ('student_clss', models.CharField(max_length=50)),
                ('applicant_phone_no', models.CharField(max_length=11)),
                ('student_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('date_of_application', models.DateTimeField(auto_now_add=True)),
                ('student_passport', models.ImageField(upload_to='admission/')),
                ('status', models.CharField(choices=[('Waiting', 'Waiting'), ('Approved', 'Approved'), ('Declined', 'Declined')], default='Waiting', max_length=20)),
            ],
        ),
    ]
