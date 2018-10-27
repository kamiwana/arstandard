from django.db import models
import os
from django.core.files.storage import FileSystemStorage
import vws
import io
from vuforia.models import *
import json
from django.contrib import messages
from django.core.exceptions import ValidationError

def ios_asset_bundle_rename(instance, filename):
  filename = '{}.{}'.format(instance.target_name, 'asset')
  return os.path.join('marker/ios/', filename)

def ios_manifest_rename(instance, filename):
  filename = '{}.{}'.format(instance.target_name, 'manifest')
  return os.path.join('marker/ios/', filename)

def android_asset_bundle_rename(instance, filename):
  filename = '{}.{}'.format(instance.target_name, 'asset')
  return os.path.join('marker/android/', filename)

def android_manifest(instance, filename):
  filename = '{}.{}'.format(instance.target_name, 'manifest')
  return os.path.join('marker/android/', filename)

class OverwriteStorage(FileSystemStorage):
    def _save(self, name, content):
        if self.exists(name):
            self.delete(name)
        return super(OverwriteStorage, self)._save(name, content)

    def get_available_name(self, name, max_length=None):
        return name

def rename(instance, filename):
  filename = '{}.{}'.format(instance.target_name, 'manifest')
  return os.path.join('marker/android/', filename)

# Create your models here.

class Marker(models.Model):
  marker_image = models.ImageField(blank=False, upload_to='marker/image/', verbose_name='Marker(JPG)')
  target_name = models.CharField(unique=True,max_length=100)
  target_id =models.CharField(max_length=100,unique=True)
  width = models.IntegerField()
  ios_asset_bundle = models.FileField(blank=True, upload_to=ios_asset_bundle_rename,max_length=500, storage=OverwriteStorage())
  ios_manifest = models.FileField(blank=True, upload_to=ios_manifest_rename,max_length=500, storage=OverwriteStorage())
  android_asset_bundle = models.FileField(blank=True, upload_to=android_asset_bundle_rename,max_length=500, storage=OverwriteStorage())
  android_manifest = models.FileField(blank=True, upload_to=android_manifest,max_length=500, storage=OverwriteStorage())
  date_modified = models.DateTimeField(auto_now=True)

  class Meta:
    db_table = 'marker'

#  def save(self, *args, **kwargs):
