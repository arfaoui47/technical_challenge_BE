from django.db import models
from django.utils import timezone


class VocabularyCatalogue(models.Model):
    vocabulary_id   = models.AutoField(primary_key=True)
    vocabulary_name = models.CharField(max_length=256, blank=True)
    creation_date   = models.DateTimeField(blank=True)

    def save(self, *args, **kwargs):
        if not self.vocabulary_id:
            self.creation_date = timezone.now()
        return super(VocabularyCatalogue, self).save(*args, **kwargs)


class Book(models.Model):
    book_id          = models.AutoField(primary_key=True)
    vocabulary       = models.OneToOneField(VocabularyCatalogue, on_delete=models.CASCADE)
    title            = models.CharField(max_length=256, blank=True)
    author           = models.CharField(max_length=256, blank=True)
    content          = models.TextField()
    isbn             = models.CharField(max_length=256, null=True)
    publication_date = models.DateTimeField(null=True)


class Word(models.Model):
    word_id       = models.AutoField(primary_key=True)
    value         = models.CharField(max_length=256)
    vocabulary    = models.ForeignKey(VocabularyCatalogue, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(blank=True)

    def save(self, *args, **kwargs):
        if not self.word_id:
            self.creation_date = timezone.now()
        return super(Word, self).save(*args, **kwargs)
