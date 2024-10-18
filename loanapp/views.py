from django.shortcuts import render, redirect
from django.http import JsonResponse
# Create your views here.
from .forms import AmountForm,DesiredAmountForm


def index(request):
    if request.method == 'POST':
        form = AmountForm(request.POST)
        if form.is_valid():
            include_terms = form.cleaned_data.get('includeTerms', '')
           
            
            render(request,"index.html",{'form': form})
            

    else:
        form = AmountForm()
    
    return render(request,"index.html",{'form': form})



def amountform(request):
    if request.method == "POST":
        form = DesiredAmountForm(request.POST)
        if form.is_valid():
            include_terms = form.cleaned_data.get('includeTerms', '')
            return redirect("second-yes")

    else:
        form = DesiredAmountForm()
        result = "We would be charging $200/month after this. (1 YEAR PRICE LOCK)"

    return render(request,"amountform.html",{'form': form,'result':result})




def success(request):

    context = {"result":"Starting the financing application."}

    return render(request,"success.html",context)




def thankyou(request):
    context = {"result":"We would contact you for payment detail soon"}

    return render(request,"thankyou.html",context)





