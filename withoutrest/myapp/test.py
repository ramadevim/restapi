import requests
import json
#GET
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='json/'
#id check one by one
def get_respone(id):
    resp=requests.get(BASE_URL+ENDPOINT+id+'/')
    print(resp.json())
    print(resp.status_code)
id=input('enter a num')
get_respone(id)
# #all with model name and id
# def get_all():
#     resp = requests.get('http://127.0.0.1:8000/json1' )
#     print(resp.json())
#     print(resp.status_code)
# get_all()
# #using jaon by num format
# def get_all2():
#     resp = requests.get('http://127.0.0.1:8000/json2' )
#     print(resp.json())
#     print(resp.status_code)
#
#
# #using mixin
# def get_all3():
#     resp = requests.get('http://127.0.0.1:8000/json3' )
#     print(resp.json())
#     print(resp.status_code)
#
#
#
# #using error finding using views
# BASE_URL1='http://127.0.0.1:8000/'
# ENDPOINT1='error/'
# def get_all4(id):
#     resp = requests.get(BASE_URL1+ENDPOINT1+id+'/' )
#     print(resp.json())
#     print(resp.status_code)
#
#
# #errors in here without uisng views
# BASE_URL2='http://127.0.0.1:8000/'
# ENDPOINT2='error1/'
# def get_all5(id):
#     resp = requests.get(BASE_URL2+ENDPOINT2+id+'/' )
#     # 1.if resp.status_code in range(200,300):
#     #2.
#     if resp.status_code == requests.codes.ok:
#         print(resp.json())
#     else:
#         print('something goes wrong')
#
#
#
# #POST
# import json
# BASE_URL3='http://127.0.0.1:8000/'
# ENDPOINT3='json3/'
# def create_resource():
#     new_emp={
#         'eno':600,
#         'ename':'rm',
#         'esal':50000,
#         'eaddr':'pune',
#     }
#     resp = requests.post(BASE_URL3+ENDPOINT3,data=json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json())
#
# BASE_URL4 = 'http://127.0.0.1:8000/'
# ENDPOINT4 = 'error/'
#
# def update_resource(id):
#         new_emp = {
#             'esal': 7000,
#             'eaddr': 'hyd',
#         }
#         resp = requests.put(BASE_URL4 + ENDPOINT4+str(id)+'/', data=json.dumps(new_emp))
#         print(resp.status_code)
#         print(resp.json())
#
# BASE_URL5 = 'http://127.0.0.1:8000/'
# ENDPOINT5 = 'error/'
#
# def delete_resource(id):
#         resp = requests.delete(BASE_URL4 + ENDPOINT4+str(id)+'/' )
#         print(resp.status_code)
#         print(resp.json())
# delete_resource(7)
# update_resource(6)
# create_resource()
# get_respone(id)
# get_all()
# get_all2()
# get_all3()
# get_all4()
# get_all5()




# BASE_URL6 = 'http://127.0.0.1:8000/'
# ENDPOINT6 = 'api/'
#
# def get_resource(id=None):
#     data={}
#     if id is not None:
#         data={
#             'id':id
#         }
#     resp = requests.get(BASE_URL6 + ENDPOINT6 , data=json.dumps(data))
#     print(resp.status_code)
#     print(resp.json())
# get_resource(1)
#
#
# def create_resource():
#     new_emp={
#         'eno':600,
#         'ename':'sahitya',
#         'esal':50000,
#         'eaddr':'pune',
#     }
#     resp = requests.post(BASE_URL6+ENDPOINT6,data=json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json())
# # create_resource()
#
#
# # def update_resource(id):
# #         new_emp = {
# #             'id':id,
# #             'esal': 7000,
# #             'eaddr': 'hyd',
# #         }
# #         resp = requests.put(BASE_URL6 + ENDPOINT6, data=json.dumps(new_emp))
# #         print(resp.status_code)
# #         print(resp.json())
#
# # update_resource(11)
#
# def delete_resource(id):
#     data={
#         'id':id
#     }
#     resp = requests.delete(BASE_URL6 + ENDPOINT6, data=json.dumps(data))
#     print(resp.status_code)
#     print(resp.json())
#
# delete_resource(10)
#































