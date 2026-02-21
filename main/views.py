from django.shortcuts import render,redirect

from .models import Comment,Meal




def index_view(request):
    meals = Meal.objects.filter(status = "active")
    context = {"meals":meals}
    
    return render(request, "main.html", context)


def meal_detail(request,pk):
    meal = Meal.objects.get(id=pk)
    
    
    comments = Comment.objects.filter(meal=meal).order_by("-created_at")
    context = {"meal":meal,
               "comments":comments}
    
    
    
    if request.method=="POST":
        author=request.POST.get("author")
        body=request.POST.get("body")
        
        Comment.objects.create(
            author=author,
            body=body,
            meal=meal
        )
        return redirect("meal_detail",meal.id)
    return render(request,"meal_detail.html",context)
    




def contact_veiw(request):
    return render(request, "contact.html")