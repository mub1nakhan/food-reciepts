from django.shortcuts import render, redirect
from .models import Meal, Comment,Ingredient



def index_view(request):

    meals = Meal.objects.filter(status="active")

    context = {
        "meals": meals
    }

    return render(request, "main.html", context)


def meal_detail(request, pk):

    meal = Meal.objects.get(id=pk)

    comments = Comment.objects.filter(meal=meal).order_by("-created_at")

    if request.method == "POST":

        author = request.POST.get("author")

        body = request.POST.get("body")

        Comment.objects.create(
            meal=meal,
            author=author,
            body=body
        )

        return redirect("meal_detail", meal.id)

    context = {
        "meal": meal,
        "comments": comments
    }

    return render(request, "meal_detail.html", context)


def contact_veiw(request):

    return render(request, "contact.html")

def meals_view(request):

    meals = Meal.objects.all()

    context = {
        "meals": meals
    }

    return render(request, "meals.html", context)


def add_meal(request):

    ingredients = Ingredient.objects.all()

    if request.method == "POST":

        name = request.POST.get("name")
        description = request.POST.get("description")
        image = request.FILES.get("image")

        meal = Meal.objects.create(
            name=name,
            description=description,
            image=image
        )

        selected_ingredients = request.POST.getlist("ingredients")

        meal.ingredients.set(selected_ingredients)

        return redirect("meals")

    context = {
        "ingredients": ingredients
    }

    return render(request, "add_meal.html", context)