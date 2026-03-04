from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Saida
from django.db.models import Sum
from django.utils import timezone
import calendar
from datetime import date, timedelta

MESES_PT = [
    '', 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
    'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
]

def _build_semanas(ano, mes, saidas_do_mes):
    """Retorna lista de semanas (cada semana = 7 células ou None)."""
    saidas_por_dia = {}
    for s in saidas_do_mes:
        saidas_por_dia.setdefault(s.data, []).append(s)

    hoje = timezone.now().date()
    primeiro_dia = date(ano, mes, 1)
    inicio = primeiro_dia - timedelta(days=primeiro_dia.weekday())
    ultimo_dia = date(ano, mes, calendar.monthrange(ano, mes)[1])
    fim = ultimo_dia + timedelta(days=(6 - ultimo_dia.weekday()))

    semanas = []
    semana = []
    cursor = inicio
    while cursor <= fim:
        if cursor.month == mes:
            semanas_saidas = saidas_por_dia.get(cursor, [])
            semana.append({
                'dia': cursor.day,
                'data': cursor,
                'is_hoje': cursor == hoje,
                'is_passado': cursor < hoje,
                'saidas': semanas_saidas,
            })
        else:
            semana.append(None)

        if len(semana) == 7:
            semanas.append(semana)
            semana = []
        cursor += timedelta(days=1)

    if semana:
        while len(semana) < 7:
            semana.append(None)
        semanas.append(semana)

    return semanas

def saida(request):
    hoje = timezone.now().date()
    mes = int(request.GET.get('mes', hoje.month))
    ano = int(request.GET.get('ano', hoje.year))

    saidas_do_mes = Saida.objects.filter(data__month=mes, data__year=ano)
    semanas = _build_semanas(ano, mes, saidas_do_mes)

    # Navegação de mês
    if mes == 1:
        mes_anterior = {'mes': 12, 'ano': ano - 1}
    else:
        mes_anterior = {'mes': mes - 1, 'ano': ano}

    if mes == 12:
        mes_seguinte = {'mes': 1, 'ano': ano + 1}
    else:
        mes_seguinte = {'mes': mes + 1, 'ano': ano}

    # Tabela filtrada
    saidas_lista = Saida.objects.all()
    tipo_filtro = request.GET.get('tipo')
    mes_filtro  = request.GET.get('mes_filtro')
    ano_filtro  = request.GET.get('ano_filtro')

    if tipo_filtro:
        saidas_lista = saidas_lista.filter(tipo__icontains=tipo_filtro)
    if mes_filtro:
        saidas_lista = saidas_lista.filter(data__month=mes_filtro)
    if ano_filtro:
        saidas_lista = saidas_lista.filter(data__year=ano_filtro)

    total = saidas_lista.aggregate(total=Sum('valor'))['total'] or 0

    return render(request, 'saida.html', {
        'semanas': semanas,
        'mes_nome': MESES_PT[mes],
        'mes': mes,
        'ano': ano,
        'hoje': hoje,
        'mes_anterior': mes_anterior,
        'mes_seguinte': mes_seguinte,
        'saidas': saidas_lista,
        'total': total,
        'tipo_filtro': tipo_filtro or '',
        'mes_filtro': mes_filtro or '',
        'ano_filtro': ano_filtro or '',
    })


def detalhe_saida(request, pk):
    saida = get_object_or_404(Saida, pk=pk)
    return render(request, 'detalhe_saida.html', {'saida': saida})


def criar_saida(request):
    if request.method == 'POST':
        try:
            Saida.objects.create(
                tipo=request.POST.get('tipo', ''),
                valor=request.POST.get('valor') or 0,
                data=request.POST.get('data'),
                descricao=request.POST.get('descricao', ''),
            )
            messages.success(request, 'Saída registrada com sucesso!')
            return redirect('saida:saida')
        except Exception as e:
            messages.error(request, f'Erro: {str(e)}')

    return render(request, 'form_saida.html')


def editar_saida(request, pk):
    saida = get_object_or_404(Saida, pk=pk)
    if request.method == 'POST':
        saida.tipo = request.POST.get('tipo', '')
        saida.valor = request.POST.get('valor') or 0
        saida.data = request.POST.get('data')
        saida.descricao = request.POST.get('descricao', '')
        saida.save()
        messages.success(request, 'Saída atualizada!')
        return redirect('saida:detalhe_saida', pk=saida.pk)

    return render(request, 'form_saida.html', {
        'saida': saida,
        'edit': True,
    })


def deletar_saida(request, pk):
    saida = get_object_or_404(Saida, pk=pk)
    if request.method == 'POST':
        saida.delete()
        messages.success(request, 'Saída deletada!')
        return redirect('saida:saida')
    return render(request, 'deletar_saida.html', {'saida': saida})