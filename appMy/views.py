from django.shortcuts import render, redirect
from appUser.models import Profile
from appMy.models import *
from django.contrib import messages
from django.http import JsonResponse


def indexPage(request):
   context = {}
   return render(request, 'index.html',context)

def profileLogin(request, pid):
   
   if Profile.objects.filter(user=request.user, id=pid).exists():
      # kullanıcın tüm profillerinin plogin değerini false yapar
      Profile.objects.filter(user=request.user).update(plogin=False)
      profile = Profile.objects.filter(user=request.user).get(id=pid)
      profile.plogin = True
      profile.save()
      return redirect('indexBrowsePage')
   else:
      messages.error(request, "Hatalı url yönlendirmesi")
      return redirect("loginUser")

def indexBrowsePage(request):
   # get hata verir önlem al, her kullanıcının kendi profillerine giriş yapabilmeli
   profile = Profile.objects.filter(user=request.user).get(plogin=True)
   netflix = Netflix.objects.all()
   categories = Category.objects.all()

   categories_with_netflix = []
    
   for category in categories:
        netflix_in_category = netflix.filter(category=category)
        if netflix_in_category:
            categories_with_netflix.append({
                'category': category,
                'netflix': netflix_in_category,
            })
   context = {
      "profile":profile,
      "categories_with_netflix": categories_with_netflix,
   }
   return render(request, 'indexbrowse.html',context)

def seriesPage(request):
    series = Series.objects.all()
    categories = Category.objects.all()

    categories_with_series = [] # her kategoriye ait series öğelerinin bulunduğu liste
    
    for category in categories:
        series_in_category = series.filter(category=category) # her kategoriye ait series öğelerini filtreler ve kategori ile eşleşmesini sağlar
        if series_in_category:
            categories_with_series.append({ # listeye kategori ve kategorilere ait seriesları ekler
                'category': category,
                'series': series_in_category,
            })

    context = {
        "categories_with_series": categories_with_series,
    }

    return render(request, 'lists/series.html', context)

def moviesPage(request):

   movies = Movies.objects.all()
   categories = Category.objects.all()
   
   categories_with_movies = []

   for category in categories:
        movies_in_category = movies.filter(category=category)
        if movies_in_category:
            categories_with_movies.append({
                'category': category,
                'movies': movies_in_category,
            })

   context = {
        "categories_with_movies": categories_with_movies,
    }

   return render(request, 'lists/movies.html', context)

def popularPage(request):

   popular = Popular.objects.all()
   categories = Category.objects.all()
   
   categories_with_popular = []

   for category in categories:
        popular_in_category = popular.filter(category=category)
        if popular_in_category:
            categories_with_popular.append({
                'category': category,
                'popular': popular_in_category,
            })

   context = {
        "categories_with_popular": categories_with_popular,
    }

   return render(request, 'lists/popular.html', context)

def mylistPage(request):
    if request.user.is_authenticated:
        mylist = MyList.objects.filter(profile__user=request.user)
    else:
        mylist = []

    context = {
        "mylist": mylist,
    }
    return render(request, 'lists/mylist.html', context)

def add_mylist(request, card_id):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        mylist, created = MyList.objects.get_or_create(profile=profile, card_id=card_id)
        if created:
            return JsonResponse({"message": "Kart başarıyla eklendi"})
        else:
            return JsonResponse({"message": "Kart zaten ekli"})
    else:
        return JsonResponse({"error": "Kullanıcı girişi yapmalısınız"})


# def remove_from_mylist(request, id):
#     if request.user.is_authenticated:
#         try:
#             mylist = MyList.objects.get(pk=id)