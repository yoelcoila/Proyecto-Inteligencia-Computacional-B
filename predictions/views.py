from django.shortcuts import render
import joblib
import numpy as np
import os
from django.conf import settings

# Ruta absoluta al archivo del modelo
model_path = os.path.join(settings.BASE_DIR, 'predictions', 'regression_model.pkl')
model = joblib.load(model_path)

def predict(request):
    prediction = None
    if request.method == 'POST':
        # Obtener los valores del formulario
        if coemissions<0:
            coemissions = (-1)*float(request.POST.get('coemissions'))
        engine_size = float(request.POST.get('engine_size'))
        cylinders = float(request.POST.get('cylinders'))

        # Realizar la predicción
        prediction = model.predict(np.array([[coemissions, engine_size, cylinders]]))
        prediction = prediction[0]

    return render(request, 'predict.html', {'prediction': prediction})
