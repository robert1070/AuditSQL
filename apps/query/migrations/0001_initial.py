# Generated by Django 2.1.7 on 2019-04-09 02:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MysqlPrivBlacklist',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='主键id')),
                ('schema', models.CharField(default='', max_length=128, verbose_name='库名')),
                ('table', models.CharField(default='*', max_length=128, verbose_name='表名')),
                ('columns', models.CharField(default='*', max_length=4096, verbose_name='列名')),
                ('comment', models.CharField(default='', max_length=255, verbose_name='描述')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '库表黑名单',
                'verbose_name_plural': '库表黑名单',
                'db_table': 'auditsql_mysql_priv_blacklist',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='MySQLQueryLog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='主键id')),
                ('user', models.CharField(max_length=30, verbose_name='用户名')),
                ('host', models.CharField(max_length=128, verbose_name='目标数据库地址')),
                ('database', models.CharField(max_length=32, verbose_name='目标数据库')),
                ('envi', models.SmallIntegerField(default=1, verbose_name='环境')),
                ('query_sql', models.TextField(default='', verbose_name='查询SQL')),
                ('query_time', models.CharField(default='', max_length=128, verbose_name='查询时间，单位s')),
                ('query_status', models.CharField(default='', max_length=2048, verbose_name='查询状态，成功或失败的原因')),
                ('affect_rows', models.IntegerField(default=0, verbose_name='影响行数')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='查询时间')),
            ],
            options={
                'verbose_name': '查询日志',
                'verbose_name_plural': '查询日志',
                'db_table': 'auditsql_sql_query_log',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='MysqlUserGroupMap',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='主键id')),
                ('group', models.CharField(default='', max_length=128, verbose_name='MySQL用户组名')),
                ('schema', models.CharField(default='', max_length=128, verbose_name='库')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '库表权限组',
                'verbose_name_plural': '库表权限组',
                'db_table': 'auditsql_mysql_usergroup_map',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='QueryBusinessGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='主键id')),
                ('group', models.CharField(default='', max_length=128, verbose_name='业务组名')),
                ('schema', models.CharField(default='', max_length=128, verbose_name='关联库')),
                ('tables', models.TextField(verbose_name='关联表')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('config', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='orders.MysqlConfig', verbose_name='关联主机')),
                ('map_mysqluser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='query.MysqlUserGroupMap', verbose_name='映射的mysql用户')),
            ],
            options={
                'verbose_name': '库表业务组',
                'verbose_name_plural': '库表业务组',
                'db_table': 'yops_query_business_group',
                'default_permissions': (),
            },
        ),
    ]
