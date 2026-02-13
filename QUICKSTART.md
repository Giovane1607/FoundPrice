# 🎯 Quick Start - FoundPrice

## 🚀 Rodar Localmente (Desenvolvimento)

### Windows

**Terminal 1 - Backend:**
```powershell
# Na pasta raiz do projeto
.\start_backend.bat
```

**Terminal 2 - Frontend:**
```powershell
cd frontend
npm install  # Apenas na primeira vez
npm start
```

Acesse: **http://localhost:4200**

---

### Linux/Mac

**Terminal 1 - Backend:**
```bash
# Na pasta raiz do projeto
chmod +x start_backend.sh  # Apenas na primeira vez
./start_backend.sh
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm install  # Apenas na primeira vez
npm start
```

Acesse: **http://localhost:4200**

---

## 📦 Instalação Completa

### 1. Backend

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar (Windows)
.\venv\Scripts\activate

# Ativar (Linux/Mac)
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

### 2. Configurar API Key

Crie um arquivo `.env` na pasta `backend/`:
```env
SERP_API_KEY=sua_chave_aqui
```

Obtenha sua chave em: https://serpapi.com/

### 3. Frontend

```bash
cd frontend
npm install
```

---

## 🌐 Deploy no Render

Consulte o arquivo **[DEPLOY.md](DEPLOY.md)** para instruções completas.

**Resumo rápido:**
1. Push do código para GitHub
2. Criar Web Service no Render
3. Start Command: `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`
4. Adicionar variável `SERP_API_KEY`

---

## 🔧 Estrutura dos Imports (Render-Ready)

O projeto está configurado para funcionar tanto localmente quanto no Render com:

```python
# backend/main.py
from backend import database_utils as dbu
from backend.database import init_db

# backend/database_utils.py
from backend.database import SessionLocal, HistoricoPreco
```

✅ **Para rodar localmente:** Execute do diretório raiz
✅ **Para deploy no Render:** Funciona automaticamente

---

## 📝 Comandos Úteis

### Testar Backend
```bash
curl http://localhost:8000/api/search?q=iPhone+15
```

### Ver Documentação da API
Abra no navegador: http://localhost:8000/docs

### Rebuild Frontend
```bash
cd frontend
npm run build
```

---

## ❓ Problemas Comuns

### Backend não inicia
- Verifique se o ambiente virtual está ativado
- Confirme que o arquivo `.env` existe em `backend/`
- Teste: `python --version` (deve ser 3.8+)

### Frontend não conecta
- Backend deve estar rodando em http://localhost:8000
- Verifique CORS no `backend/main.py`

### Imports não funcionam
- Execute sempre do diretório raiz
- Use: `uvicorn backend.main:app --reload`
- NÃO use: `cd backend && uvicorn main:app`

---

**✨ Pronto! Agora é só codificar!**
