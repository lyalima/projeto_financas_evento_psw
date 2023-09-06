from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Conta
from django.contrib import messages
from django.contrib.messages import constants

def home(request):
    return render(request, 'home.html')


def gerenciar(request):
    return render(request, 'gerenciar.html')


def cadastrar_conta_banco(request):
    #pegar as informações que o usuário preencheu
    apelido = request.POST.get('apelido')
    banco = request.POST.get('banco')
    tipo = request.POST.get('tipo')
    valor = request.POST.get('valor')
    icone = request.FILES.get('icone')

    #validação de preenchimento de campos
    if len(apelido.strip()) == 0 or len(valor.strip()) == 0:
        messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
        return redirect('/perfil/gerenciar')

    #atribuir as informações recebidas aos campos da tabela do banco de dados
    conta = Conta(
        apelido = apelido, 
        banco = banco,
        tipo = tipo,
        valor = valor,
        icone = icone
    )

    #salvar as informações no banco de dados
    conta.save()

    messages.add_message(request, constants.SUCCESS, 'Conta cadastrada com sucesso')
    return redirect('/perfil/gerenciar')