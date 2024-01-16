from Myproject.models import pesticidelist
from django.shortcuts import render
from keras.models import load_model
from django.http import HttpResponseBadRequest
from keras.preprocessing.image import ImageDataGenerator
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.http import HttpResponseRedirect
from .models import Feedback
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import FeedbackForm
import base64
from django.views.decorators.csrf import csrf_protect
from keras.preprocessing import image
from PIL import Image
import numpy as np

def home(request):
    return render(request, 'index.html')

@csrf_protect
def leafImage(request):
    if request.method == 'POST':
        try:
            if 'image' in request.FILES:
                input_image = request.FILES['image']
                model_Type = request.POST['selectmodel']
                print(model_Type)
                fs = FileSystemStorage()
                temp_path = fs.save(input_image.name, input_image)
                img_url = fs.url(temp_path)

                if model_Type == "resnet152v2":
                   model = load_model("./savedModels/resnet_model.h5")
                   print("jpt")
                   img = Image.open(input_image)
                   img = img.resize((256, 256))
                   img = np.array(img) / 255.0
                   img = np.expand_dims(img, axis=0)
                    
                   train_datagen = ImageDataGenerator(
                        rescale=1./255,
                        shear_range=0.2,
                        zoom_range=0.2,
                        horizontal_flip=True
                    )

                   train_generator = train_datagen.flow_from_directory(
                        directory='C://Users//Susmi//OneDrive//Desktop//7th sem//project//tomato//train',
                        target_size=(256, 256),
                        batch_size=32,
                        class_mode="categorical"
                    )
                   
                else:
                   print("Samaima")
                   model = load_model("./savedModels/plant_disease_Cnn.h5")
                   print("thapa")
                   img = Image.open(input_image)
                   img = img.resize((224, 224))
                   img = np.array(img) / 255.0
                   img = np.expand_dims(img, axis=0)

                   train_datagen = ImageDataGenerator(
                    rescale=1./255,
                    shear_range=0.2,
                    zoom_range=0.2,
                    horizontal_flip=True
                   )
                   train_generator = train_datagen.flow_from_directory(
                    directory='C://Users//Susmi//OneDrive//Desktop//7th sem//project//tomato//train',
                    target_size=(224, 224),
                    batch_size=32,
                    class_mode="categorical"
                   )

                classes = sorted(['Tomato___Bacterial_spot', 'Tomato___Leaf_Mold', 'Tomato___Target_Spot', 'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite',
                   'Tomato___Late_blight', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___Early_blight', 'Tomato___healthy'])

                prediction = model.predict(img)
                classresult = np.argmax(prediction)
                disease_name = classes[classresult]

                if disease_name != "Tomato___healthy":
                 pesticide_name = pesticidelist.objects.get(dname=disease_name).pname
                 disease_descriptions = pesticidelist.objects.get(dname=disease_name).ddesc

                 print(disease_name)
                 print('hello')
                 print(prediction)

                 return render(request, 'result.html', {
                    'imagesurl': img_url,
                    'disease_name': disease_name,
                    'descriptions': disease_descriptions,
                    'pesticides_name': pesticide_name,
                    'model_type': model_Type
                 })
                else :
                    return render(request,'result.html',{'imagesurl':img_url,'disease_name':'healthy'})
        except KeyError:
          return HttpResponseBadRequest("Please select image and model")
        return render(request, 'index.html')
def submit_feedback(request):
 if request.method == 'POST':
  name = request.POST.get('name')
  feedback = request.POST.get('feedback')
  userfeedback = Feedback(name=name, feedback=feedback)
  userfeedback.save()
  return render(request, 'feedback.html', {'message': 'Thank you for your feedback ' + name + '!'})
 else:
   return render(request, 'result.html')
def view_graph(request):
    return render(request,'resnet_cm.html')
def view_conv2d_matrix(request):
    return render(request,'conv2d_cm.html')
def view_resnet_graph(request):
    return render(request,'resnet_acc.html')
def view_conv2d_graph(request):
    return render(request,'conv2d_acc.html')
def view_model_detail(request):
    return render(request,'allresult.html')