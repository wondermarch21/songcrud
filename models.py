from django.db import models

# 
class Artiste(models.Model):
    first_name= models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    age=models.IntegerField(default=0)

class Song(models.Model):
    title=models.CharField( max_length=50)
    date released=models.models.DateTimeField(_("date released"), auto_now=False, auto_now_add=False)
    likes=models.IntegerField(default=0)
    artiste_id=models.models.ForeignKey(Artiste.Model", verbose_name=_(""), on_delete=models.CASCADE)


    class Lyric(models.Model):
        content=models.CharField(_("content"), max_length=1000)
        song_id=models.ForeignKey(Song.Model", verbose_name=_(""), on_delete=models.CASCADE)


