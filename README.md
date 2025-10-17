# Django Recipe Application

![Tests](https://github.com/your-username/your-repo/workflows/Tests%20and%20Quality%20Checks/badge.svg)
![Deploy](https://github.com/your-username/your-repo/workflows/Deploy%20to%20Production/badge.svg)

Uma aplicação Django completa para gerenciar receitas com sistema de autenticação, interface administrativa e API REST.

## 🚀 Deploy Automatizado

Este projeto utiliza GitHub Actions para deploy automatizado. Consulte [DEPLOY.md](DEPLOY.md) para instruções de configuração.

## 🧪 Testes

Execute os testes localmente:
```bash
python manage.py test
```

Com coverage:
```bash
coverage run manage.py test
coverage report
```

## 📝 Anotações do Curso

# Git and Git Hub
ssh-keygen

# 1- Creating Enviroment 
python -m env env
.\venv\Scripts\activate 

# 2 - Creating the Project 
pip install django 
python.exe -m pip install --upgrade pip  (optional)

django-admin --help (if want know more about commands)
django-admin startproject project . (note: I used . for created my folders in root on the project )

python manage.py runserver 

python manage.py migrate  (make your migration when necessary )



# About testing
-- For use coverage:
    pip install coverage
    coverage run -m pytest

-- for visualization:
    coverage html (crete a folder htmlvoc (into this folder you can access the file index.com ))



# Server 
```
sudo apt update -y
sudo apt upgrade -y
sudo apt autoremove -y
sudo apt install build-essential -y
sudo apt install python3.9 python3.9-venv python3.9-dev -y
sudo apt install nginx -y
sudo apt install certbot python3-certbot-nginx -y
sudo apt install postgresql postgresql-contrib -y
sudo apt install libpq-dev -y
sudo apt install git
```

# Postgres 
sudo apt install postgresql postgresql-contrib -y

### Configurações

```
sudo -u postgres psql

# Criando um super usuário
CREATE ROLE usuario WITH LOGIN SUPERUSER CREATEDB CREATEROLE PASSWORD 'senha';

# Criando a base de dados
CREATE DATABASE basededados WITH OWNER usuario;

# Dando permissões
GRANT ALL PRIVILEGES ON DATABASE basededados TO usuario;

# Saindo
\q

sudo systemctl restart postgresql
```

Caso queira mais detalhes: https://youtu.be/VLpPLaGVJhI  
Mais avançado: https://youtu.be/FZaEukN_raA



## Configurando o git

```
git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main
```

## Criando um repositório no servidor

Um repositório bare é um repositório transitório (como se fosse um github).

```
mkdir -p ~/app_bare
cd ~/app_bare
git init --bare
cd ~
```

Criando o repositório da aplicação

```
mkdir -p ~/app_repo
cd ~/app_repo
git init
git remote add origin ~/app_bare
git add . && git commit -m 'Initial'
cd ~
```

No seu computador local, adicione o bare como remoto:

```
git remote add app_bare cursodjangoserver:~/app_bare
git push app_bare <branch>
```

No servidor, em app_repo, faça pull:

```
cd ~/app_repo
git pull origin <branch>
```


## Criando o ambiente virtual

```
cd  ~/app_repo
git pull origin main
python3.10 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
pip install psycopg2
pip install gunicorn
```