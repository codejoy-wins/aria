from django.shortcuts import render, HttpResponse, redirect

def index (request):
    request.session['counter'] = 0
    return render(request, "surve/index.html")

def process (request):
    print "Process"
    request.session['counter']+= 1
    print request.POST['name']
    print request.POST['dojo']
    print request.POST['fav']
    print request.POST['comment']
    
    request.session['name'] = request.POST['name']
    request.session['dojo'] = request.POST['dojo']
    request.session['fav'] = request.POST['fav']
    request.session['comment'] = request.POST['comment']
    

    return redirect('/result')

def result (request):
    print "result"
    return render(request, "surve/result.html")
