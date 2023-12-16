from django.http import HttpResponse  
# importing task from tasks.py file  
from .task import test_func  
  
# Create your views here.  
  
def test(request):  
    # call the test_function using delay, calling task  
    test_func.delay()  
    return HttpResponse("Done")  