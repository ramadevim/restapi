from django.shortcuts import render
from django.views.generic import View
from .models import Employee
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .utils import is_json
from .forms import EmpForm
import json
#1.using json functions to get the data
class EmployeeCBV1(View):
    def get(self,request,id,*args,**kwargs):
        emp=Employee.objects.get(id=id)
        emp_data={
            'eno':emp.eno,
            'ename':emp.ename,
            'esal':emp.esal,
            'eaddr':emp.eaddr,
        }
        json_data=json.dumps(emp_data)

        return HttpResponse(json_data,content_type='application/json')

from django.http import HttpResponse
from django.core.serializers import serialize
#
# #2.django serializer data it provides models and id and fields unwantes data also provided in end of output
# #convert python to json direct
class EmployeeCBV(View):
    def get(self,request,id,*args,**kwargs):
        emp=Employee.objects.get(id=id)
        json_data=serialize('json',[emp,],fields=('eno','ename','eaddr'))
        return HttpResponse(json_data,content_type='application/json')
from .mixins import HttpMixin
#user defined errors
@method_decorator(csrf_exempt,name='dispatch')
class EmployeeCBV3(HttpMixin,View):
    def get_object_by_id(self,id):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            emp = None
        return emp
    def get(self,request,id,*args,**kwargs):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            json_data=json.dumps({'msg':'the employee details not exist pls check the id '})
            return self.render_to_http_response(json_data,status=404)
        else:
            json_data = serialize('json', [emp, ])
            return self.render_to_http_response(json_data)

    def put(self,request,id,*args,**kwargs):
        emp=self.get_object_by_id(id)
        if emp is None:
            json_data = json.dumps({'msg': 'no matched record resource found,not perform to update '})
            return self.render_to_http_response(json_data, status=404)
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg': 'pls send vaid json data'})
            return self.render_to_http_response(json_data, status=400)
        provided_data = json.loads(data)
        original_data={
            'eno':emp.eno,
            'ename':emp.ename,
            'esal':emp.esal,
            'eaddr':emp.eaddr,
        }
        original_data.update(provided_data,instance=emp)
        form = EmpForm(original_data)
        if form.is_valid():
            form.save()
            json_data = json.dumps({'msg': 'Resource updated successfully'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data, status=400)
    def delete(self,request,id,*args,**kwargs):
        emp = self.get_object_by_id(id)
        if emp is None:
            json_data = json.dumps({'msg': 'no matched record resource found,not possible to delete the record '})
            return self.render_to_http_response(json_data, status=404)
        # t=emp,delete()
        # print(t)
        status,deleted_item=emp.delete()
        if status == 1:
             json_data = json.dumps({'msg': 'resource deleted successfully '})
             return self.render_to_http_response(json_data)
        json_data = json.dumps({'msg': 'unable to delete pls try again '})
        return self.render_to_http_response(json_data)



#
# #user defined errors
class EmployeeCBV4(View):
    def get(self,request,id,*args,**kwargs):
        emp = Employee.objects.get(id=id)
        json_data = serialize('json', [emp, ])
        return HttpResponse(json_data,content_type='application/json')


#
# #qs like model
class EmployeelistCBV(View):
    def get(self,request,*args,**kwargs):
        qs=Employee.objects.all()
        json_data=serialize('json',qs)
        return HttpResponse(json_data,content_type='application/json')



#
# #3.convert json to python dict
class EmployeelistCBV1(View):
    def get(self,request,*args,**kwargs):
        qs=Employee.objects.all()
        json_data=serialize('json',qs)
        p_data=json.loads(json_data)
        final_list=[]
        for obj in p_data:
            emp_data=obj['fields']
            final_list.append(emp_data)
        json_data=json.dumps(final_list)
        return HttpResponse(json_data,content_type='application/json')


# #using mixins(like multiple inheritance) we are calling mixin class serialize
from .mixins import Serialize,HttpMixin
#
@method_decorator(csrf_exempt,name='dispatch')
class EmployeelistCBV2(HttpMixin,Serialize,View):
    def get(self,request,*args,**kwargs):
        qs=Employee.objects.all()
        json_data=self.add(qs)
        return HttpResponse(json_data,content_type='application/json')

    def post(self, request, *args, **kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'pls send vaid json data'})
            return self.render_to_http_response(json_data,status=400)
        empdata=json.loads(data)
        form=EmpForm(empdata)
        if form.is_valid():
            form.save()
            json_data = json.dumps({'msg': 'Resource created successfully'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data, status=400)


class EmployeelistCBV3(Serialize,View):
    def get(self,request,*args,**kwargs):
        try:
            qs=Employee.objects.all()
        except Employee.DoesNotExist:
            json_data=json.dumps({'msg':'the employee details not exist pls check the id '})
        else:
            json_data=self.add(qs)
        return HttpResponse(json_data,content_type='application/json')




#using one endpoint to get with id and without id
@method_decorator(csrf_exempt,name='dispatch')
class EmployeecrudCBV(HttpMixin,Serialize,View):
    def get_object_by_id(self,id):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            emp = None
        return emp
    def get(self,request,*args,**kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg': 'pls send valid json data'})
            return self.render_to_http_response(json_data, status=400)
        pdata=json.loads(data)
        id=pdata.get('id',None)
        if id is not None:
            emp=self.get_object_by_id(id)
            if emp is None:
                json_data=json.dumps({'msg':'the resource not available  with matched id'})
                return self.render_to_http_response(json_data,status=404)
            json_data = serialize( 'json',[emp,])
            return self.render_to_http_response(json_data)
        qs=Employee.objects.all()
        json_data=serialize('json',qs)
        return self.render_to_http_response(json_data)

    def post(self, request, *args, **kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'pls send vaid json data'})
            return self.render_to_http_response(json_data,status=400)
        empdata=json.loads(data)
        form=EmpForm(empdata)
        if form.is_valid():
            form.save()
            json_data = json.dumps({'msg': 'Resource created successfully'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data, status=400)

    def put(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg': 'pls send vaid json data'})
            return self.render_to_http_response(json_data, status=400)
        pdata=json.loads(data)
        id=pdata.get('id',None)
        if id is None:
            json_data=json.dumps({'msg':'To perform updation id is mandatory pls provide'})
            return self.render_to_http_response(json_data,status=404)
        emp=self.get_object_by_id(id)
        if emp is None:
            json_data=json.dumps({'msg':'the requested id is not available with matched id so its not possible to update '})
            return self.render_to_http_response(json_data)
        provide_data=json.loads(data)
        original_data={
            'eno':emp.eno,
            'ename':emp.ename,
            'esal':emp.esal,
            'eaddr':emp.eaddr,
        }
        original_data.update(provide_data)
        form = EmpForm(original_data,instance=emp)
        if form.is_valid():
            form.save()
            json_data = json.dumps({'msg': 'Resource Update successfully'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data, status=400)

    def delete(self, request,*args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg': 'pls send valid json data'})
            return self.render_to_http_response(json_data, status=400)
        pdata = json.loads(data)
        id = pdata.get('id', None)
        if id is not None:
            emp1 = self.get_object_by_id(id)
            if emp1 is None:
                json_data = json.dumps({'msg': 'the resource not available  with matched id'})
                return self.render_to_http_response(json_data, status=404)
            # emp1.delete()
            status, deleted_item = emp1.delete()
            if status == 1:
                json_data = json.dumps({'msg': 'resource deleted successfully '})
                return self.render_to_http_response(json_data)
            json_data = json.dumps({'msg': 'unable to delete pls try again '})
            return self.render_to_http_response(json_data)
        json_data = json.dumps({'msg': 'To perform deletion id is mandatory pls provide'})
        return self.render_to_http_response(json_data, status=404)


































