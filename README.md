# 🎮 FoundPrice

**O fim da dúvida na hora de comprar!**

FoundPrice é uma plataforma que compara preços de produtos em tempo real usando a API do Google Shopping, ajudando você a encontrar as melhores ofertas com segurança.

## 🚀 Funcionalidades

✅ **Busca Inteligente** - Pesquisa produtos em várias lojas brasileiras  
✅ **Análise de Confiabilidade** - Identifica lojas seguras vs arriscadas  
✅ **Histórico de Preços** - Visualiza variações de preço em gráfico  
✅ **Validador de Mercado** - Detecta ofertas suspeitas (possíveis golpes)  
✅ **Modo Escuro** - Interface adaptável para melhor experiência  

---

## 📋 Pré-requisitos

- **Python 3.8+**
- **Node.js 18+** e **npm**
- **Conta SerpAPI** (chave gratuita em https://serpapi.com/)

---

## 🛠️ Instalação

### 1️⃣ Clone o repositório

```bash
git clone <url-do-repositorio>
cd FoundPrice
```

### 2️⃣ Configure o Backend (Python/FastAPI)

```bash
cd backend

# Crie um ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instale as dependências
pip install -r requirement.txt

# Configure a API Key
# Copie o arquivo .env.example para .env
copy .env.example .env   # Windows
# ou
cp .env.example .env     # Linux/Mac

# Edite o arquivo .env e adicione sua chave da SerpAPI:
# SERP_API_KEY=sua_chave_aqui
```

### 3️⃣ Configure o Frontend (Angular)

```bash
cd ../frontend

# Instale as dependências
npm install
```

---

## ▶️ Como Rodar

### **Backend (Local)**

**Opção 1 - Rodar do diretório raiz (Recomendado para Render):**
```bash
# Ative o ambiente virtual
.\venv\Scripts\activate   # Windows
# ou
source venv/bin/activate  # Linux/Mac

# Rode o backend
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

**Opção 2 - Rodar de dentro da pasta backend:**
```bash
cd backend
.\venv\Scripts\activate   # Windows
uvicorn main:app --reload
```

O backend estará rodando em: **http://localhost:8000**

### **Frontend**

Em outro terminal, no diretório `frontend`:

```bash
npm start
```

O frontend estará rodando em: **http://localhost:4200**

---

## 🚀 Deploy no Render

### **Backend**

1. Faça push do código para o GitHub
2. No Render, crie um novo Web Service
3. Conecte seu repositório
4. Configure:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`
5. Adicione a variável de ambiente:
   - `SERP_API_KEY`: sua_chave_serpapi

O arquivo `render.yaml` já está configurado para deploy automático!

### **Frontend**

Pode ser hospedado no Vercel, Netlify ou Render Static Site.

---

## 📁 Estrutura do Projeto

```
FoundPrice/
│
├── backend/              # API FastAPI
│   ├── main.py          # Endpoints principais
│   ├── database.py      # Configuração do SQLite
│   ├── database_utils.py # Funções de banco de dados
│   ├── requirement.txt  # Dependências Python
│   ├── .env.example     # Exemplo de variáveis de ambiente
│   └── foundprice.db    # Banco de dados (criado automaticamente)
│
└── frontend/            # Interface Angular
    ├── src/
    │   └── app/
    │       ├── app.component.ts    # Lógica principal
    │       ├── app.component.html  # Interface
    │       └── app.component.css   # Estilos
    └── package.json     # Dependências Node
```

---

## 🔧 Endpoints da API

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/api/search?q={produto}` | Busca produtos e salva histórico |
| GET | `/api/analise-produto?q={produto}` | Retorna dados para gráfico de preços |
| GET | `/api/comparar-vendas?q={produto}` | Calcula métricas e detecta ofertas suspeitas |

---

## 🎨 Tecnologias Utilizadas

### Backend
- **FastAPI** - Framework web moderno e rápido
- **SQLAlchemy** - ORM para banco de dados
- **SQLite** - Banco de dados leve
- **SerpAPI** - API do Google Shopping
- **python-dotenv** - Gerenciamento de variáveis de ambiente

### Frontend
- **Angular 19** - Framework web moderno
- **Chart.js** - Gráficos interativos
- **HttpClient** - Requisições HTTP
- **TypeScript** - Tipagem estática

---

## ⚠️ Importante

1. **Nunca commite o arquivo `.env`** - Ele contém sua API key!
2. A chave gratuita da SerpAPI tem limite de requisições
3. O banco de dados é criado automaticamente no primeiro uso
4. Para resetar o histórico, delete o arquivo `foundprice.db`

---

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

---

## 📝 Licença

Este projeto é de código aberto e está disponível sob a licença MIT.

---

## 🐛 Problemas Conhecidos

- Algumas lojas podem retornar links de redirecionamento do Google
- A validação de confiabilidade é baseada em uma lista pré-definida

---

## 📧 Contato

Dúvidas ou sugestões? Abra uma issue no repositório!

---

**Desenvolvido com ❤️ para ajudar você a economizar!**
