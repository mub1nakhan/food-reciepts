from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=255,verbose_name="maxsulot nomi")
    unit_types = (
        ("g", "gramm"),
        ("kg", "kilogram"),
        ("dona", "dona"),
        ("ml","milliletr"),
        ("litr","litr")
    )
    unit = models.CharField(max_length=255, choices=unit_types,verbose_name="o'lchov birligi")
    quantity = models.PositiveIntegerField(default=1,verbose_name="miqdori")
    
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="yaratilgan vaqti")
    updated_at = models.DateTimeField(auto_now=True,verbose_name="yangilangan vaqti")
    
    def __str__(self):
        return f"{self.name} - {self.unit} {self.quantity}"
    
    
    class Meta:
        verbose_name = "Masalliq"
        verbose_name_plural = "Masalliqlar"
        ordering =["-created_at"]


class Meal(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True,blank=True)
    ingredients = models.ManyToManyField(Ingredient,blank=True)
    image = models.ImageField(upload_to='meals/')
    status_choices =(
        ("active","faol"),
        ("inactive","nofaol")

    )
    status = models.CharField(max_length=21,choices=status_choices)
    
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="yaratilgan vaqti")
    updated_at = models.DateTimeField(auto_now=True,verbose_name="yangilangan vaqti")
    
    
    def __str__(self):
        return self.name
    
     
    class Meta:
        verbose_name = "taom"
        verbose_name_plural = "taomalar"
        ordering =["-created_at"]
        
        
        
        
class Comment(models.Model):
    meal=models.ForeignKey(Meal,on_delete=models.CASCADE)
    author=models.CharField(max_length=255)
    body=models.TextField()
    
    
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="yaratilgan vaqti")
    updated_at = models.DateTimeField(auto_now=True,verbose_name="yangilangan vaqti")
    
    
    def __str__(self):
        return f"{self.author}'s - {self.body}"
    