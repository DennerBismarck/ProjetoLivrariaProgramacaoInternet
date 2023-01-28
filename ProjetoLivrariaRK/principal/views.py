from django.shortcuts import render, redirect
from principal.form import livroform, LoginForm
from principal.models import livros
# Create your views here.

#View do index
def index(request):
    return render(request,"index.html")

#Views CRUD
def create(request):
    formLivro = livroform(request.POST or None)
    if formLivro.is_valid() :
        formLivro.save()
        return redirect("read")    
    pacote = {"formLivro": formLivro}
    return render(request, "crud.html", pacote)

def read(request):
    livroslistar = livros.objects.all().order_by('titulo')
    busca = request.GET.get('busca')
    if busca:
        livroslistar = livros.objects.filter(titulo__icontains=busca).order_by('titulo')
    return render(request, "listagem.html", {"livros":livroslistar})

def update(request, id):
    livro = livros.objects.get(pk=id)
    formLivro = livroform(request.POST or None, instance=livro)
    if formLivro.is_valid() :
        formLivro.save()
        return redirect("read")    
    pacote = {"formLivro": formLivro}
    return render(request, "crud.html", pacote)

def delete(request, id):
    livro = livro.objects.get(pk=id)
    livro.delete()
    return redirect("read")

#View do sobre
def sobre(request):
    return render(request,"sobre.html")

#View da página de login
def login(request):
    form = LoginForm()
    return render(request, 'login.html', {'form': form})