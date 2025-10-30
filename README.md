# 🍳 **Recipe Management System**

> **Sistema completo de gerenciamento de receitas com Django e Django REST Framework**

[![Django](https://img.shields.io/badge/Django-5.2.4-green.svg)](https://djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org/)
[![DRF](https://img.shields.io/badge/DRF-3.16.1-red.svg)](https://www.django-rest-framework.org/)
[![JWT](https://img.shields.io/badge/JWT-Authentication-orange.svg)](https://github.com/jazzband/djangorestframework-simplejwt)

---

## 📋 **Índice**

- [🎯 Sobre o Projeto](#-sobre-o-projeto)
- [✨ Funcionalidades](#-funcionalidades)
- [🛠️ Tecnologias](#️-tecnologias)
- [⚡ Instalação](#-instalação)
- [🔧 Configuração](#-configuração)
- [🧪 Testes](#-testes)
- [ API](#-api)
- [🖼️ Screenshots](#️-screenshots)

---

## 🎯 **Sobre o Projeto**

Sistema web para gerenciamento de receitas culinárias com interface moderna e API REST completa. Desenvolvido com Django, oferece funcionalidades para criar, editar, buscar e categorizar receitas, além de sistema de autenticação JWT para integração com aplicações externas.

---

## ✨ **Funcionalidades**

- � **Sistema de usuários** com autenticação completa
- 🍽️ **CRUD de receitas** com upload de imagens
- 🏷️ **Categorias e tags** para organização
- 🔍 **Sistema de busca** por título e filtros
- 📱 **API REST** com autenticação JWT
- 🧪 **Cobertura de testes** superior a 90%
- 📄 **Paginação** inteligente
- 🎨 **Interface responsiva**

---

## 🛠️ **Tecnologias**

### **Backend**
- **Django 5.2.4** - Framework web
- **Django REST Framework 3.16.1** - API REST
- **JWT Authentication** - Autenticação segura
- **Pillow** - Processamento de imagens
- **SQLite/PostgreSQL** - Banco de dados

### **Testes**
- **Pytest 8.4.1** - Framework de testes
- **Coverage 7.10.6** - Cobertura de código
- **Selenium 4.35.0** - Testes funcionais
- **Faker 37.4.2** - Dados de teste

---

## ⚡ **Instalação**

### **Pré-requisitos**
- Python 3.10+
- Git

### **1. Clone o Repositório**
```bash
git clone https://github.com/lordrodrigoo/Django.git
cd Django
```

### **2. Crie um ambiente virtual**
```bash
python -m venv venv

# Ativar (Linux/Mac)
source venv/bin/activate
```

### **3. Instale as Dependências**
```bash
pip install -r requirements.txt
```

### **4. Configure o Ambiente**
```bash
cp .env-example .env
# Edite o arquivo .env conforme necessário
```

### **5. Execute as Migrações**
```bash
python manage.py migrate
```

### **6. Crie um Superusuário**
```bash
python manage.py createsuperuser
```

### **7. Execute o Servidor**
```bash
python manage.py runserver
```

🎉 **Pronto!** Acesse: http://127.0.0.1:8000

---

## 🔧 **Configuração**

### **LEIA O .env-example**


### **Para Produção (PostgreSQL)**
```bash
# Instalar PostgreSQL
sudo apt install postgresql postgresql-contrib libpq-dev
pip install psycopg2-binary

# Configurar no .env
DATABASE_URL=postgresql://user:password@localhost:5432/database_name
```

---

## 🧪 **Testes**

### **Executar Testes**
```bash
# Todos os testes
pytest

# Testes específicos
pytest recipes/tests/
pytest -k "api"
```

### **Coverage**
```bash
# Executar com coverage
coverage run -m pytest

# Relatório no terminal
coverage report

# Relatório HTML
coverage html
# Abrir: htmlcov/index.html
```

---

## 📱 **API**

### **Autenticação JWT**
```bash
# Obter token
curl -X POST http://127.0.0.1:8000/recipes/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "user", "password": "pass"}'
```

### **Endpoints Principais**
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/recipes/api/v2/` | Listar receitas |
| POST | `/recipes/api/v2/` | Criar receita |
| GET | `/recipes/api/v2/{id}/` | Detalhe da receita |
| PATCH | `/recipes/api/v2/{id}/` | Atualizar receita |
| DELETE | `/recipes/api/v2/{id}/` | Deletar receita |

### **Exemplo de Uso**
```bash
# Listar receitas
curl -H "Authorization: Bearer SEU_TOKEN" \
  http://127.0.0.1:8000/recipes/api/v2/

# Filtrar por categoria
curl -H "Authorization: Bearer SEU_TOKEN" \
  "http://127.0.0.1:8000/recipes/api/v2/?category_id=1"
```

---

## 🖼️ **Screenshots**

> **📸 Adicione suas capturas de tela aqui**

### **Página Principal**
<!-- ![Home](screenshots/home.png) -->

### **Lista de Receitas**
<!-- ![Recipes](screenshots/recipes.png) -->

### **API Response**
<!-- ![API](screenshots/api.png) -->

---

## 🌐 **Deploy**

### **Preparação para Produção**

#### **1. Configurar Banco PostgreSQL**
```bash
sudo apt install postgresql postgresql-contrib libpq-dev
sudo -u postgres psql
CREATE ROLE recipe_user WITH LOGIN SUPERUSER PASSWORD 'senha_segura';
CREATE DATABASE recipe_db WITH OWNER recipe_user;
\q
```

#### **2. Configurar Ambiente**
```env
# .env produção
DEBUG=False
SECRET_KEY=sua-secret-key-segura
DATABASE_URL=postgresql://recipe_user:senha_segura@localhost:5432/recipe_db
ALLOWED_HOSTS=seu-dominio.com
```

#### **3. Deploy no Servidor**
```bash
# Instalar dependências
pip install gunicorn psycopg2-binary

# Migrar e coletar estáticos
python manage.py migrate
python manage.py collectstatic --noinput

# Executar com Gunicorn
gunicorn project.wsgi:application --bind 0.0.0.0:8000
```

#### **4. Nginx (Opcional)**
Configure Nginx como proxy reverso para domínio personalizado e SSL.

---


## 📄 **Licença**

Este projeto está sob a licença MIT. Veja [LICENSE](LICENSE) para detalhes.

---

