from django.db import models
from django.contrib.auth import get_user_model
import numpy as np
import pickle
from sklearn.tree import DecisionTreeClassifier


class MachineLearningModel(models.Model):
    name = models.CharField(max_length=200, blank=True, default='')
    description = models.TextField(blank=True, default='')
    file = models.FileField(null=False)

    def load(self):
        ml_model = pickle.load(self.file)
        return ml_model

    def fit(self, x, y=None):
        x = np.array(x)
        ml_model = self.load()
        if y == None:
            ml_model.fit(x)
        else:
            y = np.array(y)
            ml_model.fit(x, y)
        pickle.dump(ml_model, self.file.path)

    def transform(self, x):
        x = np.array(x)
        ml_model = self.load()
        return ml_model.transform(x).tolist()

    def fit_transform(self, x):
        x = np.array(x)
        ml_model = self.load()
        result = ml_model.fit_transform(x).tolist()
        pickle.dump(ml_model, self.file.path)
        return result

    def predict(self, x):
        x = np.array(x)
        ml_model = self.load()
        return ml_model.predict(x).tolist()

    def predict_proba(self, x):
        x = np.array(x)
        ml_model = self.load()
        return ml_model.predict_proba(x).tolist()