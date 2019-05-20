# Generated by Django 2.2 on 2019-05-18 02:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=20, verbose_name='课程id')),
                ('course_name', models.CharField(max_length=20, verbose_name='课程名称')),
                ('start_time', models.DateTimeField(verbose_name='开始时间')),
                ('end_time', models.DateTimeField(verbose_name='结束时间')),
                ('lecturer', models.CharField(max_length=20, verbose_name='讲师')),
                ('meeting_room', models.CharField(max_length=20, verbose_name='会议室号')),
                ('meeting_room_pwd', models.CharField(max_length=20, verbose_name='会议室密码')),
            ],
            options={
                'verbose_name_plural': '课程',
            },
        ),
        migrations.CreateModel(
            name='Phone_code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=11)),
                ('code', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='MeetPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent_id', models.CharField(max_length=30, verbose_name='代理商代号')),
                ('company', models.CharField(max_length=30, verbose_name='培训人名称')),
                ('phone', models.CharField(max_length=30, verbose_name='手机号')),
                ('area', models.CharField(max_length=30, verbose_name='区域')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Meet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent_id', models.CharField(max_length=30, verbose_name='代理商代号')),
                ('company', models.CharField(max_length=30, verbose_name='培训人名称')),
                ('phone', models.CharField(max_length=30, verbose_name='手机号')),
                ('area', models.CharField(max_length=30, verbose_name='区域')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Course')),
            ],
        ),
    ]
