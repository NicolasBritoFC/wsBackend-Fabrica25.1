from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Personagem, Localizacao, Dimensao
from .forms import PersonagemForm
import requests
from django.contrib import messages
import random
from django.db.models import Q

def tela_inicial(request):
    context = {
        'personagens': Personagem.objects.all(),
        'localizacoes': Localizacao.objects.all()
    }
    return render(request, 'jogo/tela_inicial.html', context)

def menu_jogo(request):
    personagens = Personagem.objects.all()
    return render(request, 'jogo/menu_jogo.html', {'personagens': personagens})

def deletar_personagem(request, personagem_id):
    try:
        personagem = Personagem.objects.get(id=personagem_id)
        personagem.delete()
        messages.success(request, 'Personagem deletado com sucesso!')
    except Personagem.DoesNotExist:
        messages.error(request, 'Personagem não encontrado')
    return redirect('listar_personagens')

def jogar(request, personagem_id):
    try:
        personagem = Personagem.objects.get(id=personagem_id)
        localizacao_correta = personagem.localizacao
        
        # Pegar 4 localizações aleatórias que não sejam a correta
        outras_localizacoes = Localizacao.objects.filter(
            ~Q(id=localizacao_correta.id)
        ).order_by('?')[:4]
        
        # Combinar e embaralhar
        opcoes = list(outras_localizacoes)
        opcoes.append(localizacao_correta)
        random.shuffle(opcoes)

    except Personagem.DoesNotExist:
        return HttpResponse('Personagem não encontrado')
    
    localizacoes =  Localizacao.objects.all()

    if request.method == 'POST':
        escolha_id = request.POST.get('escolha')
        if int(escolha_id) == personagem.localizacao.id:
            return render(request,'jogo/resultado.html',{'ganhou': True})
        else:
            return render(request,'jogo/resultado.html',{'ganhou': False})
        
    return render(request, 'jogo/jogar.html', {'personagem': personagem,'localizacoes': opcoes  })# Agora só 5 opções


def criar_personagem(request):
    if request.method == 'POST':
        form = PersonagemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tela_inicial')
    else:
        form = PersonagemForm()
    return render(request, 'jogo/formulario_personagem.html', {'form': form})


def editar_personagem(request, personagem_id):
    try:
        personagem = Personagem.objects.get(id=personagem_id)
    except Personagem.DoesNotExist:
        return HttpResponse('Personagem não encontrado')
    
    if request.method == 'POST':
        form = PersonagemForm(request.POST, instance=personagem)
        if form.is_valid():
            form.save()
            return redirect('tela_inicial')
    else:
        form = PersonagemForm(instance=personagem)
    return render(request, 'jogo/formulario_personagem.html', {'form': form})

# views.py
def listar_personagens(request):
    personagens = Personagem.objects.select_related('localizacao__dimensao').all()
    return render(request, 'jogo/listar_personagens.html', {'personagens': personagens})

# views.py
def popular_dados_api(request):
    if request.method == 'POST':
        try:
            # Limpar dados existentes
            Dimensao.objects.all().delete()
            Localizacao.objects.all().delete()
            Personagem.objects.all().delete()
            
            url = 'https://rickandmortyapi.com/api/character'
            while url:
                response = requests.get(url)
                response.raise_for_status()
                data = response.json()
                
                for char in data['results']:
                    # Criar dimensão
                    dimensao_nome = char['origin']['name'] or "Desconhecida"
                    dimensao, _ = Dimensao.objects.get_or_create(nome=dimensao_nome)
                    
                    # Criar localização
                    localizacao_nome = char['location']['name'] or "Desconhecida"
                    localizacao, _ = Localizacao.objects.get_or_create(nome=localizacao_nome,dimensao=dimensao)

                    # Criar personagem
                    Personagem.objects.create(nome=char['name'],localizacao=localizacao
                    )
                
                url = data['info']['next']  # Próxima página

            messages.success(request, 'Dados carregados com sucesso!')
            return redirect('tela_inicial')
            
        except Exception as e:
            messages.error(request, f'Erro: {str(e)}')
            return redirect('tela_inicial')
    
    return render(request, 'jogo/confirmar_popular.html')


# Create your views here.
