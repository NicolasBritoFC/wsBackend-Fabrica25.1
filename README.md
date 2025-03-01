# 🪐 Rick and Morty - Jogo das Dimensões

Descubra em qual dimensão os personagens de Rick and Morty estão!  
**Tecnologias**: Django, SQLite/PostgreSQL, API Rick and Morty

---

## 📋 Pré-requisitos
- Python 3.10+
- Gerenciador de pacotes (pip)
- Acesso à internet (para consumir a API)

---

## 🚀 Começando

### 1. Clonar o repositório

git clone [URL_DO_SEU_REPOSITORIO]
cd nome-do-repositorio

2. Configurar ambiente virtual
   
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

3. Instalar dependências
   
pip install -r requirements.txt

4. Configurar banco de dados

python manage.py migrate

▶️ Executando o Projeto

python manage.py runserver


🎮 Como Jogar
1. Carregue os dados da API
Na tela inicial, clique em "Carregar Dados da API" para importar personagens, localizações e dimensões.

2. Escolha um personagem
Acesse o menu "Iniciar Jogo" e selecione um personagem.

3. Adivinhe a localização
Você terá 5 opções de localizações. Escolha a correta para ganhar!

*Dica: caso voce nao conheca muito dos personagens pode ver no ver personagens
que la tem as informações de cada personagem cadastrado com sua localização

🔧 Funcionalidades
Recurso	Descrição
Integração com API	Importa dados reais da Rick and Morty API
CRUD de Personagens	Crie, edite ou exclua personagens manualmente
Sistema de Jogo	Interface interativa com feedback imediato de acerto/erro
Estatísticas	Veja quantos personagens e localizações estão cadastrados na tela inicial
Há também a funcionalidade de adicionar personagens e editar eles 


🗂️ Estrutura do Código

meu_projeto/
├── jogo/
│   ├── models.py       # Define Personagem, Localizacao e Dimensao
│   ├── views.py        # Lógica das telas e integração com API
│   ├── urls.py         # Rotas da aplicação
│   └── templates/      # Telas HTML estilizadas
├── requirements.txt    # Dependências do projeto
└── settings.py         # Configurações do Django














