from django.db import models

class SlideExplanation(models.Model):
    module_id = models.CharField(max_length=255)
    slide_number = models.IntegerField()
    explanation = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('module_id', 'slide_number')
    
    def __str__(self):
        return f"Module: {self.module_id}, Slide: {self.slide_number}"