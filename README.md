# API Controle de Disciplina

Este é um projeto de API para controle de alunos, disciplinas, tarefas e suas relações.

## Visão Geral

Este projeto oferece um conjunto de ferramentas para controle de instâncias das entidades e suas relações. Nessa API você pode adicionar, editar, listar, excluir e muito mais funcionalidades.

## Requisitos

- Python 3.11.5
- Django 4.2.4
- Django Rest Framework 3.14.0
- Postman (para testar a API)

### Observação: Todos estarão no requirements.txt, ou seja, quando estiver com o ambiente virtual, os requisitos serão supridos automaticamente após a instalação.


## Configuração do Ambiente
Para iniciarmos o projeto, precisamos seguir algumas etapas para o seu funcionamento.
Siga as etapas abaixo para configurar o ambiente de desenvolvimento:

1. **Crie uma pasta**
```
 mkdir api_controle_disciplina
```
2. **Entre na pasta**
```
 cd samu
```

3. **Clone o repositório:**
```
git clone origin https://github.com/GuilhermeMLeal/API_Controle_Diciplina.git
```
4. **Abra o projeto**
 Observação: Caso estiver no VSCode
```
code .
```

5. **Ativando o ambiente virtual no terminal**
 Ative o terminal na sua IDE, logo após execute os seguintes comandos:
```
python -m venv .env
./.env/Scripts/activate
```

6. **Instalando o requirements.txt para obter todas as dependências**
```
pip install -r requirements.txt
```

7. **Pronto, apenas execute esse comando e execute no seu navegador o endereço dito, ou até, se tiver o software Postman, execute o arquivo JSON disponibilizado**
```
python manage.py runserver
```
### Para você interessado em fazer modificações importantes, execute esses comandos abaixo:

**Comandos Importantes:**

- `python manage.py runserver`: Inicia o servidor para rodar a aplicação.
- `python manage.py makemigrations`: Executa a formatação do banco de dados.
- `python manage.py migrate`: Aplica as migrações ao banco de dados.

Lembre-se de executar esses comandos no terminal dentro do diretório do projeto para realizar as ações necessárias.

