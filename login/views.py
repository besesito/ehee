from django.shortcuts import render
from django.contrib import auth


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            username = request.POST['username']
            auth.login(request, user)
            return render(request, 'raport/home.html')
        else:
            return render(request, 'login/login.html', {'info': "😂 Skleroza? Próbuj dalej! 🤣"})
    else:
        return render(request, 'login/login.html')
