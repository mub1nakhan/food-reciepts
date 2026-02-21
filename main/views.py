from django.shortcuts import render

from .models import Ingredient,Meal



def index_view(request):
    meals = Meal.objects.filter(status = "active")
    context = {"meals":meals}
    
    return render(request, "main.html", context)


def meal_detail(request,pk):
    meal = Meal.objects.get(id=pk)
    
    context = {"meal":meal}
    
    
    return render(request,"meal_detail.html",context)
    




def contact_veiw(request):
    return render(request, "contact.html")