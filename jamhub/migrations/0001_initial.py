# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Role'
        db.create_table('jamhub_role', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('jamhub', ['Role'])

        # Adding model 'Instrument'
        db.create_table('jamhub_instrument', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
        ))
        db.send_create_signal('jamhub', ['Instrument'])

        # Adding model 'DAW'
        db.create_table('jamhub_daw', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
        ))
        db.send_create_signal('jamhub', ['DAW'])

        # Adding model 'Profile'
        db.create_table('jamhub_profile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('jamhub', ['Profile'])

        # Adding M2M table for field roles on 'Profile'
        m2m_table_name = db.shorten_name('jamhub_profile_roles')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('profile', models.ForeignKey(orm['jamhub.profile'], null=False)),
            ('role', models.ForeignKey(orm['jamhub.role'], null=False))
        ))
        db.create_unique(m2m_table_name, ['profile_id', 'role_id'])

        # Adding M2M table for field instruments on 'Profile'
        m2m_table_name = db.shorten_name('jamhub_profile_instruments')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('profile', models.ForeignKey(orm['jamhub.profile'], null=False)),
            ('instrument', models.ForeignKey(orm['jamhub.instrument'], null=False))
        ))
        db.create_unique(m2m_table_name, ['profile_id', 'instrument_id'])

        # Adding M2M table for field software on 'Profile'
        m2m_table_name = db.shorten_name('jamhub_profile_software')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('profile', models.ForeignKey(orm['jamhub.profile'], null=False)),
            ('daw', models.ForeignKey(orm['jamhub.daw'], null=False))
        ))
        db.create_unique(m2m_table_name, ['profile_id', 'daw_id'])

        # Adding model 'Project'
        db.create_table('jamhub_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('num_stars', self.gf('django.db.models.fields.IntegerField')()),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('genre', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('jamhub', ['Project'])

        # Adding M2M table for field artist on 'Project'
        m2m_table_name = db.shorten_name('jamhub_project_artist')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['jamhub.project'], null=False)),
            ('profile', models.ForeignKey(orm['jamhub.profile'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'profile_id'])


    def backwards(self, orm):
        # Deleting model 'Role'
        db.delete_table('jamhub_role')

        # Deleting model 'Instrument'
        db.delete_table('jamhub_instrument')

        # Deleting model 'DAW'
        db.delete_table('jamhub_daw')

        # Deleting model 'Profile'
        db.delete_table('jamhub_profile')

        # Removing M2M table for field roles on 'Profile'
        db.delete_table(db.shorten_name('jamhub_profile_roles'))

        # Removing M2M table for field instruments on 'Profile'
        db.delete_table(db.shorten_name('jamhub_profile_instruments'))

        # Removing M2M table for field software on 'Profile'
        db.delete_table(db.shorten_name('jamhub_profile_software'))

        # Deleting model 'Project'
        db.delete_table('jamhub_project')

        # Removing M2M table for field artist on 'Project'
        db.delete_table(db.shorten_name('jamhub_project_artist'))


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('codename',)", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'jamhub.daw': {
            'Meta': {'ordering': "['name']", 'object_name': 'DAW'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'jamhub.instrument': {
            'Meta': {'ordering': "['name']", 'object_name': 'Instrument'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'jamhub.profile': {
            'Meta': {'object_name': 'Profile'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instruments': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['jamhub.Instrument']", 'symmetrical': 'False'}),
            'roles': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['jamhub.Role']", 'symmetrical': 'False'}),
            'software': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['jamhub.DAW']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'jamhub.project': {
            'Meta': {'object_name': 'Project'},
            'artist': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['jamhub.Profile']", 'symmetrical': 'False'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'genre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'num_stars': ('django.db.models.fields.IntegerField', [], {})
        },
        'jamhub.role': {
            'Meta': {'object_name': 'Role'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['jamhub']