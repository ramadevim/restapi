#
# DUMP DATA
#
#
# (env) C:\Users\maxgen\django proj\withoutrest>python manage.py dumpdata myapp.Employee
# [{"model": "myapp.employee", "pk": 1, "fields": {"eno": 100, "ename": "rama", "esal": 1000.0, "eaddr": "
# hyderabad"}}, {"model": "myapp.employee", "pk": 2, "fields": {"eno": 200, "ename": "sai", "esal": 2000.0
# , "eaddr": "hyd"}}, {"model": "myapp.employee", "pk": 3, "fields": {"eno": 300, "ename": "murali", "esal
# ": 3000.0, "eaddr": "pune"}}, {"model": "myapp.employee", "pk": 4, "fields": {"eno": 400, "ename": "rama
# devi", "esal": 4000.0, "eaddr": "pune"}}]
# (env) C:\Users\maxgen\django proj\withoutrest>python manage.py dumpdata myapp.Employee --indent 4
# [
# {
#     "model": "myapp.employee",
#     "pk": 1,
#     "fields": {
#         "eno": 100,
#         "ename": "rama",
#         "esal": 1000.0,
#         "eaddr": "hyderabad"
#     }
# },
# {
#     "model": "myapp.employee",
#     "pk": 2,
#     "fields": {
#         "eno": 200,
#         "ename": "sai",
#         "esal": 2000.0,
#         "eaddr": "hyd"
#     }
# },
# {
#     "model": "myapp.employee",
#     "pk": 3,
#     "fields": {
#         "eno": 300,
#         "ename": "murali",
#         "esal": 3000.0,
#         "eaddr": "pune"
#     }
# },
# {
#     "model": "myapp.employee",
#     "pk": 4,
#     "fields": {
#         "eno": 400,
#         "ename": "ramadevi",
#         "esal": 4000.0,
#         "eaddr": "pune"
#     }
# }
# ]
#
# (env) C:\Users\maxgen\django proj\withoutrest>python manage.py dumpdata myapp.Employee --format json  --
# indent 4
# [
# {
#     "model": "myapp.employee",
#     "pk": 1,
#     "fields": {
#         "eno": 100,
#         "ename": "rama",
#         "esal": 1000.0,
#         "eaddr": "hyderabad"
#     }
# },
# {
#     "model": "myapp.employee",
#     "pk": 2,
#     "fields": {
#         "eno": 200,
#         "ename": "sai",
#         "esal": 2000.0,
#         "eaddr": "hyd"
#     }
# },
# {
#     "model": "myapp.employee",
#     "pk": 3,
#     "fields": {
#         "eno": 300,
#         "ename": "murali",
#         "esal": 3000.0,
#         "eaddr": "pune"
#     }
# },
# {
#     "model": "myapp.employee",
#     "pk": 4,
#     "fields": {
#         "eno": 400,
#         "ename": "ramadevi",
#         "esal": 4000.0,
#         "eaddr": "pune"
#     }
# }
# ]
#env) C:\Users\maxgen\django proj\withoutrest>python manage.py dumpdata myapp.Employee --format xml  --i
# ndent 4
# <?xml version="1.0" encoding="utf-8"?>
# <django-objects version="1.0">
#     <object model="myapp.employee" pk="1">
#         <field name="eno" type="IntegerField">100</field>
#         <field name="ename" type="CharField">rama</field>
#         <field name="esal" type="FloatField">1000.0</field>
#         <field name="eaddr" type="CharField">hyderabad</field>
#     </object>
#     <object model="myapp.employee" pk="2">
#         <field name="eno" type="IntegerField">200</field>
#         <field name="ename" type="CharField">sai</field>
#         <field name="esal" type="FloatField">2000.0</field>
#         <field name="eaddr" type="CharField">hyd</field>
#     </object>
#     <object model="myapp.employee" pk="3">
#         <field name="eno" type="IntegerField">300</field>
#         <field name="ename" type="CharField">murali</field>
#         <field name="esal" type="FloatField">3000.0</field>
#         <field name="eaddr" type="CharField">pune</field>
#     </object>
#     <object model="myapp.employee" pk="4">
#         <field name="eno" type="IntegerField">400</field>
#         <field name="ename" type="CharField">ramadevi</field>
#         <field name="esal" type="FloatField">4000.0</field>
#         <field name="eaddr" type="CharField">pune</field>
#     </object>
# </django-objects>
# (env) C:\Users\maxgen\django proj\withoutrest>

