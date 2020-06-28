import json
from ibm_watson import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    iam_apikey='TFLKKzCDBUaC6JsRHmrDVrQWLbToHTwzRgkPsR5bGMSK')

url = 'https://www.hola.com/imagenes/estar-bien/20190820147813/razas-perros-pequenos-parecen-grandes/0-711-550/razas-perro-pequenos-grandes-a.jpg'

classes_result = visual_recognition.classify(url=url).get_result()
print(json.dumps(classes_result, indent=2))
