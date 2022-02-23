# import json
# from store.models import ProductImage


# class CustomJsonEncoder(json.encoder.JSONEncoder):
#     def default(self, o):
#         if isinstance(o, ProductImage):  
#             data = {
#                 'product_id': o.product,
#                 'image': o.image
#             }          
#             return data
#         else:
#             return super().default(o)

# def my_loads(obj):
#     return json.loads(obj, object_hook=json.JSONDecoder)

# def custom_dumps(obj):
#     return json.dumps(obj, cls=CustomJsonEncoder)
