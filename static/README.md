# Agenda

Projeto Agenda - curso do Prof. Otávio Miranda 


## Projeto apenas para fins **didáticos** não é um projeto **"real"** ##

> ### Deploy Temporário no GCP(google cloud platform) [nginx e gunicorn] ###


> Desenvolvido com Django 2.2.7 - Python 3.7.5 - MariaDB/MySQL 10.1.43

-------------------------------------------------------------------------

## Como testar? ##

```
git clone git@github.com:Hp2501/Agenda.git
cd Agenda
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Obs: configurar o *__python-decouple__* e *__dj_database_url__*


[como configurar](https://samuelgoncalves.com.br/configurar-sua-aplicacao-django-para-ler-dados-diferentes-por-ambiente/)


## Como acessar as páginas? ##

```
\accounts\login
\accounts\logout
\accounts\cadastro
\accounts\dashboard
```

## Conhecimentos aplicados no Projeto ##


* Criação do projeto
* Criação dos Models
* Django admin
* Exibir valores nas wiews
* Exibir um único contato
* Levantar erros 404
* Usando condicionais
* Paginação
* Ordenar e Filtrar valores
* Adicionar campo de pesquisa
* Adicionar campo imagem (pillow)
* Menssagens com Django Messagens
* Sistema de login
* Cadastro de usuário
* Páginas login, logout e dashboard
* Verificando usuários logados
* Formulários para Models


## Libs usadas: ##

* [django](https://www.djangoproject.com/)

* [pillow](https://pypi.org/project/Pillow/)  

* [python decouple](https://github.com/henriquebastos/python-decouple "Henrique Bastos")  

* [dj_database_url](https://pypi.org/project/dj-database-url/)  

------------------------------------------------------------------------