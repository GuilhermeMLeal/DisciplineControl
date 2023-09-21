# API Controle de Disciplina

Este é um projeto de API para controle de disciplinas e alunos com tarefas determinadas.

## Visão Geral

Este projeto oferece uma API para gerenciar disciplinas e alunos. Você pode adicionar, editar, listar e excluir disciplinas e alunos usando esta API.

## Requisitos

- Python 3.x
- Django 4.2.4
- Django Rest Framework 3.x

## Configuração do Ambiente

Siga as etapas abaixo para configurar o ambiente de desenvolvimento:

1. **Clone o repositório:**

git clone origin https://github.com/GuilhermeMLeal/API_Controle_Diciplina.git

2. **Ativando o ambiente virtual no terminal**
python -m venv .env
./.venv/Scripts/activate

3. **Instalando o requirements.txt para obter todas as dependências**
pip install -r requirements.txt

4. **Crie um projeto para você personalizar todas as configurações do seu "projeto"**
django-admin startproject core .

5. **Crie um App, para desenvolvimento (parte de um todo)**
python manage.py startapp nome/app

**PRONTO AGORA VOCÊ ESTÁ PRONTO PARA PERSONALIZAR O SEU PROJETO**

**COMANDO IMPORTANTES:**
git manage.py runserver -- para rodar a aplicação
git manage.py makemigrations -- efetuar toda a formatação do banco
git manage.py migrate -- mandar para o banco efetivamente
   
