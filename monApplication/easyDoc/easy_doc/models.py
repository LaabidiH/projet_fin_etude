from django.db import models

class Personne(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mot_de_passe = models.CharField(max_length=128)

    def __str__(self):
        return self.nom    
