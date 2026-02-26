from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Cliente

def cliente(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente.html', {'clientes': clientes})

def detalhe_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'detalhe_cliente.html', {'cliente': cliente})

def criar_cliente(request):
    if request.method == 'POST':
        try:
            Cliente.objects.create(
                nome=request.POST.get('nome'),
                tipo=request.POST.get('tipo'),
                cpf_cnpj=request.POST.get('cpf_cnpj'),
                email=request.POST.get('email'),
                telefone=request.POST.get('telefone'),
                endereco=request.POST.get('endereco'),
                cidade=request.POST.get('cidade'),
                estado=request.POST.get('estado')
            )
            messages.success(request, 'Cliente criado com sucesso!')
            return redirect('cliente:cliente')
        except Exception as e:
            messages.error(request, f'Erro: {str(e)}')
    return render(request, 'form_cliente.html', {'tipos': Cliente.TIPO_CHOICES})

def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.nome = request.POST.get('nome')
        cliente.tipo = request.POST.get('tipo')
        cliente.cpf_cnpj = request.POST.get('cpf_cnpj')
        cliente.email = request.POST.get('email')
        cliente.telefone = request.POST.get('telefone')
        cliente.endereco = request.POST.get('endereco')
        cliente.cidade = request.POST.get('cidade')
        cliente.estado = request.POST.get('estado')
        cliente.save()
        messages.success(request, 'Cliente atualizado!')
        return redirect('cliente:detalhe_cliente', pk=cliente.pk)
    return render(request, 'form_cliente.html', {'cliente': cliente, 'edit': True, 'tipos': Cliente.TIPO_CHOICES})

def deletar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        messages.success(request, 'Cliente deletado!')
        return redirect('cliente:cliente')
    return render(request, 'deletar_cliente.html', {'cliente': cliente})
