from django.shortcuts import render
from django.utils import timezone
from servico.models import Servico
import calendar
from datetime import date

MESES = [
    'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
    'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
]


def cronograma(request):
    hoje = date.today()

    ano = int(request.GET.get('ano', hoje.year))
    mes = int(request.GET.get('mes', hoje.month))

    if mes < 1:
        mes = 12
        ano -= 1
    elif mes > 12:
        mes = 1
        ano += 1

    primeiro_dia = date(ano, mes, 1)
    ultimo_dia = date(ano, mes, calendar.monthrange(ano, mes)[1])

    # Serviços com entrega prevista neste mês (exceto cancelados)
    servicos_mes = Servico.objects.filter(
        data_prevista_saida__gte=primeiro_dia,
        data_prevista_saida__lte=ultimo_dia,
    ).select_related('dentista', 'cliente').exclude(status='CAN')

    # Agrupar por dia
    dias_servicos = {}
    for s in servicos_mes:
        dia = s.data_prevista_saida.day
        dias_servicos.setdefault(dia, []).append(s)

    # Montar semanas
    semanas = []
    for semana in calendar.monthcalendar(ano, mes):
        linha = []
        for dia in semana:
            if dia == 0:
                linha.append(None)
            else:
                data_dia = date(ano, mes, dia)
                linha.append({
                    'dia': dia,
                    'data': data_dia,
                    'servicos': dias_servicos.get(dia, []),
                    'is_hoje': data_dia == hoje,
                    'is_passado': data_dia < hoje,
                })
        semanas.append(linha)

    return render(request, 'cronograma.html', {
        'semanas': semanas,
        'mes_nome': MESES[mes - 1],
        'ano': ano,
        'mes': mes,
        'hoje': hoje,
        'mes_anterior': {'mes': mes - 1 if mes > 1 else 12, 'ano': ano if mes > 1 else ano - 1},
        'mes_seguinte': {'mes': mes + 1 if mes < 12 else 1, 'ano': ano if mes < 12 else ano + 1},
    })


def dia_detalhe(request, ano, mes, dia):
    from datetime import date
    data_dia = date(ano, mes, dia)
    hoje = date.today()

    servicos = Servico.objects.filter(
        data_prevista_saida=data_dia,
    ).select_related('dentista', 'cliente').exclude(status='CAN').order_by('dentista__nome')

    return render(request, 'dia_detalhe.html', {
        'data': data_dia,
        'servicos': servicos,
        'hoje': hoje,
        'is_passado': data_dia < hoje,
        'is_hoje': data_dia == hoje,
    })