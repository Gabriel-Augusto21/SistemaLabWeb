from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from .models import Laboratorio

def laboratorio(request):
    laboratorios = Laboratorio.objects.all()
    return render(request, 'laboratorio.html', {'laboratorios': laboratorios})

def detalhe_laboratorio(request, pk):
    laboratorio = get_object_or_404(Laboratorio, pk=pk)
    return render(request, 'detalhe_laboratorio.html', {'laboratorio': laboratorio})

def criar_laboratorio(request):
    if request.method == 'POST':
        try:
            Laboratorio.objects.create(
                nome=request.POST.get('nome'),
                email=request.POST.get('email'),
                telefone=request.POST.get('telefone'),
                cnpj=request.POST.get('cnpj'),
                endereco=request.POST.get('endereco')
            )
            messages.success(request, 'Laboratório criado com sucesso!')
            return redirect('laboratorio:laboratorio')
        except Exception as e:
            messages.error(request, f'Erro: {str(e)}')
    return render(request, 'form_laboratorio.html')

def editar_laboratorio(request, pk):
    laboratorio = get_object_or_404(Laboratorio, pk=pk)
    if request.method == 'POST':
        laboratorio.nome = request.POST.get('nome')
        laboratorio.email = request.POST.get('email')
        laboratorio.telefone = request.POST.get('telefone')
        laboratorio.cnpj = request.POST.get('cnpj')
        laboratorio.endereco = request.POST.get('endereco')
        laboratorio.save()
        messages.success(request, 'Laboratório atualizado!')
        return redirect('laboratorio:detalhe_laboratorio', pk=laboratorio.pk)
    return render(request, 'form_laboratorio.html', {'laboratorio': laboratorio, 'edit': True})

def deletar_laboratorio(request, pk):
    laboratorio = get_object_or_404(Laboratorio, pk=pk)
    if request.method == 'POST':
        laboratorio.delete()
        messages.success(request, 'Laboratório deletado!')
        return redirect('laboratorio:laboratorio')
    return render(request, 'deletar_laboratorio.html', {'laboratorio': laboratorio})
