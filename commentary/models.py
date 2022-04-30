from django.db import models

# Create your models here.
class Comm(models.Model):
    title= models.CharField(max_length=200,blank=True,null=True)
    audio_file = models.FileField(blank=True,null=True)
    # audio_link = models.CharField(max_length=200,blank=True,null=True)
    
    

    def __str__(self):
        return self.title
        
    # def delete(self, using: Any = ..., keep_parents: bool = ...) -> Tuple[int, Dict[str, int]]:
    #     return super().delete(using, keep_parents)
