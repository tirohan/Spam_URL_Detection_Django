from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from sklearn.ensemble import RandomForestClassifier
import joblib

# Create your models here.

class Data(models.Model):
    url = models.CharField(max_length=300, blank=True)
    # Phosphorus = models.PositiveIntegerField(null=True)
    # Potasium = models.PositiveIntegerField(null=True)
    # Temperature = models.FloatField(null=True)
    # Humidity = models.FloatField(null=True)
    # pH = models.FloatField(null=True)
    # Rainfall = models.FloatField(null=True)
    # Type = models.IntegerField(null=True)

    
    predictions = models.CharField(max_length=100, blank=True)
    # predictions_type = models.IntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        ml_model = joblib.load('ml_model/spam_detection.joblib')
        self.predictions = ml_model.predict(
            [[self.url]])
        # ml_model1 = joblib.load('ml_model/ml_soilrecommendation_model_type_updated.joblib')
        # self.predictions_type = ml_model1.predict(
        #     [[self.Nitrogen, self.Phosphorus, self.Potasium,  self.Temperature, self.Humidity, self.pH, self.Rainfall, self.Type]])
        return super().save(*args, *kwargs)

    class Meta:
        ordering = ['-date']

    #def __int__(self):
        #return self.Nitrogen
