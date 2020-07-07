from django.shortcuts import render, redirect  
from crud.forms import CrudForm  
from crud.models import Crud 
    # Create your views here.  
def emp(request):  
    if request.method == "POST":  
        form = CrudForm(request.POST)  
        if form.is_valid():  
            try:  
               form.save()  
               return redirect('/show')  
            except:  
                pass  
    else:  
        form = CrudForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    employees = Crud.objects.all()  
    return render(request,"show.html",{'employees':employees})  
def edit(request, id):  
    employee = Crud.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  
def update(request, id):  
    employee = Crud.objects.get(id=id)  
    form = CrudForm(request.POST, instance = employee)  
    if form.is_valid():  
       form.save()  
       return redirect("/show")  
    return render(request, 'edit.html', {'employee': employee})  
def destroy(request, id):  
    employee = Crud.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")  
