# Projeto Django na Instância EC2 da AWS

Este é um projeto Django desenvolvido para criar um aplicativo que expõe informações da máquina virtual, como IP, hostname, AMI, sistema operacional e especificações de hardware. O objetivo é inicialmente desenvolver o projeto localmente no Windows e, posteriormente, migrá-lo para uma instância EC2 do Ubuntu 22.04 na AWS.

## Preparar ambiente de desenvolvimento no Windows

1. Configurar um ambiente virtual Python (venv):
python -m venv venv

2. Ativar o ambiente virtual:
.\venv\Scripts\activate

## Criar projeto e app em Django, testar localmente

1. Criar um novo projeto Django:
pip install django
python -m pip install --upgrade pip
django-admin startproject EC2_Proj .

2. Criar um aplicativo (app) dentro do projeto:
django-admin startapp EC2_app
 
3. Configurar o projeto:
- Editar o arquivo `settings.py` no diretório do projeto:
  - Adicionar `EC2_app` à lista `INSTALLED_APPS`.
  - Configurar `'DIRS'` para incluir o diretório `'templates'`.

4. Configurar as rotas (urls) do aplicativo:
- Criar o arquivo `urls.py` no diretório do aplicativo.
- Adicionar a rota padrão para a página inicial no arquivo `urls.py` do projeto, incluindo o caminho para o aplicativo.

5. Definir as views:
- Criar a função `home(request)` no arquivo `views.py` do aplicativo.
- Retornar o resultado renderizado do template `home.html` no diretório `templates/app/`.

6. Criar o template:
- Criar o arquivo `home.html` no diretório `templates/app/`.
- Personalizar o conteúdo do template de acordo com as necessidades do projeto.

7. Testar o aplicativo localmente:
python manage.py runserver
 
## Próximos Passos

Aqui estão os próximos passos para avançar no projeto:

1. Realizar a configuração do controle de versão do projeto, como a criação de um repositório Git e o commit inicial do código.

2. Criar uma instância EC2 na AWS com o Ubuntu 22.04.

3. Configurar a instância EC2 com as dependências necessárias, como Python e Django.

4. Migrar o projeto para a instância EC2, fazendo o upload do código e realizando as configurações necessárias no servidor.

5. Testar o projeto na instância EC2 para garantir que a página inicial do Django e o aplicativo funcionem corretamente.

**Observação:** Certifique-se de consultar a documentação oficial do Django e da AWS para obter informações mais detalhadas sobre cada etapa.
