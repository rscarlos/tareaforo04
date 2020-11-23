# Generated by Django 3.1.3 on 2020-11-23 00:10

import administracion.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CanchaModel',
            fields=[
                ('canchaId', models.AutoField(db_column='cancha_id', primary_key=True, serialize=False, unique=True)),
                ('canchaPrecio', models.DecimalField(db_column='cancha_prec', decimal_places=2, max_digits=5)),
                ('canchaDesc', models.CharField(db_column='cancha_desc', max_length=50)),
                ('estado', models.BooleanField(db_column='estado', default=True)),
                ('createAt', models.DateTimeField(auto_now_add=True, db_column='created_at')),
                ('updateAt', models.DateTimeField(auto_now=True, db_column='updated_at')),
            ],
            options={
                'db_table': 't_cancha',
            },
        ),
        migrations.CreateModel(
            name='ClienteModel',
            fields=[
                ('clienteId', models.AutoField(db_column='cli_id', primary_key=True, serialize=False, unique=True)),
                ('clienteNomb', models.CharField(db_column='cli_nomb', max_length=50)),
                ('clienteCel', models.CharField(db_column='cli_cel', max_length=12)),
                ('estado', models.BooleanField(db_column='estado', default=True)),
                ('createAt', models.DateTimeField(auto_now_add=True, db_column='created_at')),
                ('updateAt', models.DateTimeField(auto_now=True, db_column='updated_at')),
            ],
            options={
                'db_table': 't_cliente',
            },
        ),
        migrations.CreateModel(
            name='LocalModel',
            fields=[
                ('localId', models.AutoField(db_column='local_id', primary_key=True, serialize=False, unique=True)),
                ('localNomb', models.CharField(db_column='local_nomb', max_length=50)),
                ('localDir', models.CharField(db_column='local_dir', max_length=100, unique=True)),
                ('estado', models.BooleanField(db_column='estado', default=True)),
                ('createAt', models.DateTimeField(auto_now_add=True, db_column='created_at')),
                ('updateAt', models.DateTimeField(auto_now=True, db_column='updated_at')),
            ],
            options={
                'db_table': 't_local',
            },
        ),
        migrations.CreateModel(
            name='TipoCanchaModel',
            fields=[
                ('tipoCanchaId', models.AutoField(db_column='tc_id', primary_key=True, serialize=False, unique=True)),
                ('tipoCanchaDesc', models.CharField(db_column='tc_desc', max_length=50)),
                ('estado', models.BooleanField(db_column='estado', default=True)),
                ('createAt', models.DateTimeField(auto_now_add=True, db_column='created_at')),
                ('updateAt', models.DateTimeField(auto_now=True, db_column='updated_at')),
            ],
            options={
                'db_table': 't_tipocancha',
            },
        ),
        migrations.CreateModel(
            name='TipoClienteModel',
            fields=[
                ('tipoClienteId', models.AutoField(db_column='tcli_id', primary_key=True, serialize=False, unique=True)),
                ('tipoClienteDesc', models.CharField(db_column='tcli_desc', max_length=50)),
                ('tipoClientePrecio', models.DecimalField(db_column='tcli_prec', decimal_places=2, max_digits=5)),
                ('estado', models.BooleanField(db_column='estado', default=True)),
                ('createAt', models.DateTimeField(auto_now_add=True, db_column='created_at')),
                ('updateAt', models.DateTimeField(auto_now=True, db_column='updated_at')),
            ],
            options={
                'db_table': 't_tipocliente',
            },
        ),
        migrations.CreateModel(
            name='ReservaModel',
            fields=[
                ('reservaId', models.AutoField(db_column='res_id', primary_key=True, serialize=False, unique=True)),
                ('reservaHoraInicio', models.DateTimeField(db_column='res_inicio')),
                ('reservaHoraFin', models.DateTimeField(db_column='res_fin')),
                ('reservaPrecio', models.DecimalField(db_column='res_prec', decimal_places=2, max_digits=5)),
                ('estado', models.BooleanField(db_column='estado', default=True)),
                ('createAt', models.DateTimeField(auto_now_add=True, db_column='created_at')),
                ('updateAt', models.DateTimeField(auto_now=True, db_column='updated_at')),
                ('canchaId', models.ForeignKey(db_column='cancha_id', on_delete=django.db.models.deletion.PROTECT, related_name='reservasCancha', to='administracion.canchamodel')),
                ('clienteId', models.ForeignKey(db_column='cli_id', on_delete=django.db.models.deletion.PROTECT, related_name='reservasCliente', to='administracion.clientemodel')),
            ],
            options={
                'db_table': 't_reserva',
            },
        ),
        migrations.AddField(
            model_name='clientemodel',
            name='tipoclienteId',
            field=models.ForeignKey(db_column='tcli_id', on_delete=django.db.models.deletion.PROTECT, related_name='clienteTipoCliente', to='administracion.tipoclientemodel'),
        ),
        migrations.AddField(
            model_name='canchamodel',
            name='localId',
            field=models.ForeignKey(db_column='local_id', on_delete=django.db.models.deletion.PROTECT, related_name='canchasLocal', to='administracion.localmodel'),
        ),
        migrations.AddField(
            model_name='canchamodel',
            name='tipocanchaId',
            field=models.ForeignKey(db_column='tc_id', on_delete=django.db.models.deletion.PROTECT, related_name='canchasTipoCancha', to='administracion.tipocanchamodel'),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('usuId', models.AutoField(db_column='usu_id', primary_key=True, serialize=False)),
                ('usuCorreo', models.EmailField(db_column='usu_correo', max_length=254, unique=True)),
                ('usuNombre', models.CharField(db_column='usu_nombre', max_length=50)),
                ('usuFono', models.CharField(db_column='usu_fono', max_length=15)),
                ('usuCumple', models.DateField(blank=True, db_column='usu_cumple', null=True)),
                ('password', models.TextField(db_column='usu_pass', null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_login', models.DateTimeField(null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 't_usuario',
            },
            managers=[
                ('objects', administracion.models.ManejoUsuario()),
            ],
        ),
    ]
