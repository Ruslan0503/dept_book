from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Customer, Product, Order, OrderItem,historyTurnDept
from django.contrib import messages
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

# There is Home
def homeFunc(request):
    customers = Customer.objects.filter(deptor=True)
    q = request.GET.get('q') if request.GET.get('q')!=None else ''
    if q == 'dept':
        customers = Customer.objects.filter(deptor=True).order_by('-dept')
    elif q == 'manyTime':
        customers = Customer.objects.filter(deptor=True).order_by('dateReturn')
    else:
        customers = Customer.objects.filter(deptor=True)
    products = Product.objects.all()
    
    context = {
        'products':products,
        'customers':customers,
        'q':q,
    }
    return context


@api_view(['GET'])
def homeAPI(request):
    context = homeFunc(request)
    products = context['products']
    customers = context['customers']
    senderCon = {}
    pr = []
    cus = []
    for i in products:
        pr.append({i.name:i.price})
    senderCon.update({'products':pr}) 
    for i in customers:
        cus.append({
            'name':i.name,
            'adress':i.adress,
            'phone_number':i.phone_number,
            'passport_number':i.password_number,
            'dept':i.dept,
            'returned_dept':i.returned_dept,
        })
    senderCon.update({'customer':cus})    
    return Response(senderCon)
    
def home(request):
    context = homeFunc(request)
    return render(request,'index.html', context)

# There is Home

#There is add Customer

def addCustomerFunc(request):
    try:
        data = request.data
    except:
        data = json.loads(request.body.decode('utf-8'))
    name = data['name']
    adress = data['adress']
    phone_number = data['phone_number']
    passpord_number = data['passport_number']
    try:
        customer = Customer.objects.create(
        name=name,
        adress=adress,
        phone_number=phone_number,
        password_number=passpord_number,
        )
        customer.save()
        with open('static/js/index.js', 'r') as file:
            lines = file.readlines()
            lines.insert(1, '"'+name+'",'+'\n') 
        with open('static/js/index.js', 'w') as file:
            file.writelines(lines)        
    except:
        return ('Bu nom allaqachon mavjud')
    return ("Qo'shildi..")          

@api_view(['POST'])
def addCustomerAPI(request):
    message = addCustomerFunc(request)
    return Response(message)


def add_customer(request):
    if request.method == 'POST':
        message = addCustomerFunc(request)
    return JsonResponse({'message':message})    

#There is add Customer

# there is write debt

def writerDebtFunc(request):
    try:
        datas = request.data
    except:
        datas = json.loads(request.body.decode('utf-8'))
    who_is = datas['who']
    dept = float(datas['dept'])
    del datas['who']
    del datas['dept']
    try:
        who = Customer.objects.get(name=who_is)
    except:
        return ("Bunday foydalanuvchi yo'q")    
    who.dept+=dept
    who.deptor = True
    who.save()
    order = Order.objects.create(who=who)
    for i in datas:
        product = Product.objects.get(name=i)
        quantity = datas[i]
        OrderItem.objects.create(
            who = who,
            order = order,
            product = product,
            quantity=quantity,
        )
    return ('Added..')            

@api_view(['POST'])
def write_deptAPI(request):
    message = writerDebtFunc(request)
    return Response(message)

def write_dept(request):
    if request.method == 'POST':
        message = writerDebtFunc(request)
    return JsonResponse({'message':message})

# there is write debt


def Customerdata(request,id):
    customer = Customer.objects.get(id=id)
    context = {
        'customer':customer,
    }
    return render(request, 'customerdata.html', context)


# There is turnDept functions
def turnDeptFunc(request):
    try:
        datas = request.data
    except:
        datas = json.loads(request.body.decode('utf-8'))
    id = int(datas['id'])
    
    customer = Customer.objects.get(id=id)
    customer.dept-=float(datas['sum'])
    customer.returned_dept+=float(datas['sum'])
    customer.save()
    if(customer.dept<=0):
        customer.deptor=False
        customer.save()
    try:
        historyTurnDept.objects.create(
        who = customer,
        quantity= float(datas['sum']),
        )
    except:
        pass    
    return ('done')    

@api_view(['POST'])
def turnDeptAPI(request):
    message = turnDeptFunc(request)
    return Response(message)

def turnDept(request):
    if request.method == 'POST':
        message = turnDeptFunc(request)    
    return JsonResponse({'message':message})


def showHistory(request,id):
    who = "" 
    try: 
        customer = Customer.objects.get(id=id) 
        orders = Order.objects.filter(who=customer) 
        who = customer.name 
    except: 
        return HttpResponse('Biron narsa hato') 
     
    context = { 
        'data':orders, 
        'who':who, 
        'customer':customer, 
    }
    return render(request,'history.html', context)