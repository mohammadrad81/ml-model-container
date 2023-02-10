from django.db import models
from django.contrib.auth import get_user_model
import numpy as np
import pickle
from sklearn.tree import DecisionTreeClassifier


class MachineLearningModel(models.Model):
    name = models.CharField(max_length=200, blank=True, default='')
    description = models.TextField(blank=True, default='')
    file = models.FileField(null=False, upload_to="ml_models/")
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def load_ml_model(self):
        with open(self.file.path, 'rb') as f:
            ml_model = pickle.load(f)
        return ml_model
    
    def save_ml_model(self, ml_model):
        with open(self.file.path, 'wb') as f:
            pickle.dump(ml_model, f)

    def fit(self, x, y=None):
        x = np.array(x)
        ml_model = self.load_ml_model()
        if y == None:
            ml_model.fit(x)
        else:
            y = np.array(y)
            ml_model.fit(x, y)
        self.save_ml_model(ml_model)

    def transform(self, x):
        x = np.array(x)
        ml_model = self.load_ml_model()
        return ml_model.transform(x).tolist()

    def fit_transform(self, x):
        x = np.array(x)
        ml_model = self.load_ml_model()
        result = ml_model.fit_transform(x).tolist()
        self.save_ml_model(ml_model)
        return result

    def predict(self, x):
        x = np.array(x)
        ml_model = self.load_ml_model()
        return ml_model.predict(x).tolist()

    def predict_proba(self, x):
        x = np.array(x)
        ml_model = self.load_ml_model()
        return ml_model.predict_proba(x).tolist()