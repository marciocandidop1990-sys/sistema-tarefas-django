# 🚀 Sistema de Tarefas - Django REST API

Projeto CRUD completo desenvolvido com Django e Django REST Framework.

Permite criar, listar, editar e deletar tarefas, com autenticação via Token.

---

## 📌 Funcionalidades

- ✅ Criar tarefas
- ✅ Listar tarefas
- ✅ Editar tarefas
- ✅ Deletar tarefas
- ✅ Marcar tarefa como concluída
- 🔐 Autenticação via Token (DRF)

---

## 🛠 Tecnologias Utilizadas

- Python
- Django
- Django REST Framework
- SQLite
- HTML
- CSS

---

## 📂 Estrutura do Projeto

```
sistema-tarefas-django/
│
├── config/                # Configurações do projeto
├── tarefas/               # App principal
├── db.sqlite3             # Banco de dados
├── manage.py
├── requirements.txt
└── README.md
```

---

## ▶️ Como Executar o Projeto

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/marciocandidop1990-sys/sistema-tarefas-django.git
```

### 2️⃣ Acesse a pasta do projeto

```bash
cd sistema-tarefas-django
```

### 3️⃣ Crie o ambiente virtual

```bash
python -m venv .venv
```

### 4️⃣ Ative o ambiente virtual

Windows:
```bash
.venv\Scripts\activate
```

Mac/Linux:
```bash
source .venv/bin/activate
```

### 5️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

### 6️⃣ Execute as migrações

```bash
python manage.py migrate
```

### 7️⃣ Crie um superusuário (opcional)

```bash
python manage.py createsuperuser
```

### 8️⃣ Rode o servidor

```bash
python manage.py runserver
```

Acesse no navegador:

```
http://127.0.0.1:8000/
```

API:

```
http://127.0.0.1:8000/api/tarefas/
```

---

## 🔐 Autenticação via Token

Para obter o token:

Endpoint:

```
POST /api/token/
```

Exemplo de JSON:

```json
{
  "username": "seu_usuario",
  "password": "sua_senha"
}
```

Resposta esperada:

```json
{
  "token": "seu_token_aqui"
}
```

Depois envie o token no Header:

```
Authorization: Token seu_token_aqui
```

---

## 📬 Endpoints da API

| Método | Endpoint              | Descrição               |
|--------|----------------------|--------------------------|
| GET    | /api/tarefas/        | Listar tarefas           |
| POST   | /api/tarefas/        | Criar nova tarefa        |
| PUT    | /api/tarefas/{id}/   | Atualizar tarefa         |
| DELETE | /api/tarefas/{id}/   | Deletar tarefa           |

---

## 👨‍💻 Autor

Marcio Candido Pinto  
Desenvolvedor Python | Django  

GitHub:  
https://github.com/marciocandidop1990-sys