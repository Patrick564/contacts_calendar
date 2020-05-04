from django.shortcuts import render


def index(request):
    return render(request, 'contact_list/index.html')


def add(request):
    return render(request, 'contact_list/add.html')


def update(request):
    return render(request, 'contact_list/update.html')


class Add():
    pass


class Update():
    pass


class Favorite():
    pass


class Filed():
    pass


class Download():
    pass
