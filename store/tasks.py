# from time import sleep
# from celery import shared_task
# from .models import ProductImage
# from django.core.files import File
# from django.core.files.storage import FileSystemStorage
# import PIL.Image as Image
# import io
# import base64
# import os

# @shared_task
# def upload(product_id, file_name):

#     print('Uploading image...')

#     sleep(10)
    
#     storage = FileSystemStorage()

#     with open(f'media/{file_name}', mode='rb') as file:
        
#         picture = File(file)

#         instance = ProductImage(product_id=product_id, image=picture)

#         instance.save()


#     storage.delete(file_name)

#     print('Uploaded!')
