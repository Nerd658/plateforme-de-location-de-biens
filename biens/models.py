from django.db import models


from django.contrib.auth.models import User
# Create your models here.
class Bien(models.Model):
    CATEGORIES = [
        ('Immobilier ', 'Immobilier '),
        ('Véhicules', 'Véhicules'),
        ('Équipement de maison', 'Équipement de maison'),
        ('Événements et loisirs', 'Événements et loisirs'),
        ('Instruments de musique', 'Instruments de musique'),
        ('Matériel de voyage', 'Matériel de voyage'),
        ('Mode et accessoires', 'Mode et accessoires'),
        ('Électronique et Multimédia', 'Électronique et Multimédia'),
    ]

    titre = models.CharField(max_length=255)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    categorie = models.CharField(max_length=50, choices=CATEGORIES)
    photo = models.ImageField(upload_to='biens/')
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)  
    date_creation = models.DateTimeField(auto_now_add=True)
    disponibilite = models.BooleanField(default=True)  
    
    
    date_debut_disponibilite = models.DateField()  
    date_fin_disponibilite = models.DateField()    
    def __str__(self):
        return self.titre
    


