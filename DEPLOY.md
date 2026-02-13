# 🚀 Guia de Deploy - FoundPrice

## 📋 Checklist Pré-Deploy

- [ ] Código commitado no GitHub
- [ ] Chave SerpAPI obtida (https://serpapi.com/)
- [ ] Conta no Render criada (https://render.com/)
- [ ] Requirements.txt na raiz do projeto
- [ ] Arquivo .env configurado localmente (não commitar!)

---

## 🌐 Deploy no Render

### Passo 1: Preparar o Repositório

```bash
git add .
git commit -m "Deploy: Configuração para Render"
git push origin main
```

### Passo 2: Criar Web Service no Render

1. Acesse https://dashboard.render.com/
2. Clique em **"New +"** → **"Web Service"**
3. Conecte seu repositório GitHub
4. Selecione o repositório **FoundPrice**

### Passo 3: Configurar o Serviço

**Configurações Básicas:**
- **Name**: `foundprice-api` (ou nome de sua preferência)
- **Environment**: `Python 3`
- **Region**: `Oregon (US West)` ou mais próximo
- **Branch**: `main`

**Build & Deploy:**
- **Root Directory**: (deixe vazio - usa a raiz)
- **Build Command**: 
  ```bash
  pip install -r requirements.txt
  ```
- **Start Command**: 
  ```bash
  uvicorn backend.main:app --host 0.0.0.0 --port $PORT
  ```

### Passo 4: Variáveis de Ambiente

Na seção **Environment Variables**, adicione:

| Key | Value |
|-----|-------|
| `SERP_API_KEY` | sua_chave_serpapi_aqui |
| `PYTHON_VERSION` | `3.11.0` (opcional) |

### Passo 5: Deploy

1. Clique em **"Create Web Service"**
2. Aguarde o build (2-5 minutos)
3. Seu backend estará disponível em:
   ```
   https://foundprice-api.onrender.com
   ```

---

## 🔧 Configurar Frontend

Atualize o arquivo `frontend/src/environments/environment.prod.ts`:

```typescript
export const environment = {
  production: true,
  apiUrl: 'https://foundprice-api.onrender.com'
};
```

---

## ✅ Testar Deploy

### Teste 1: Health Check
```bash
curl https://foundprice-api.onrender.com/
```

### Teste 2: API de Busca
```bash
curl "https://foundprice-api.onrender.com/api/search?q=iPhone+15"
```

### Teste 3: Browser
Abra no navegador:
```
https://foundprice-api.onrender.com/docs
```

---

## 🐛 Troubleshooting

### ❌ Erro: "Module not found"
**Solução**: Verifique se os imports estão no formato:
```python
from backend.database import ...
from backend import database_utils as dbu
```

### ❌ Erro: "Application not found"
**Solução**: Confirme o Start Command:
```bash
uvicorn backend.main:app --host 0.0.0.0 --port $PORT
```

### ❌ Erro: "Database locked"
**Solução**: Adicione no `backend/database.py`:
```python
engine = create_engine(
    "sqlite:///./foundprice.db", 
    connect_args={"check_same_thread": False, "timeout": 30}
)
```

### ❌ CORS Error no Frontend
**Solução**: Verifique `backend/main.py`:
```python
app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"],  # Em produção, especifique o domínio
    allow_methods=["*"], 
    allow_headers=["*"]
)
```

---

## 📊 Monitoramento

### Logs em Tempo Real
1. Acesse o Dashboard do Render
2. Clique no seu serviço
3. Aba **"Logs"**

### Métricas
- CPU/Memory usage disponível no dashboard
- Configurar alertas para downtime

---

## 💰 Plano Gratuito

**Render Free Tier inclui:**
- ✅ 750 horas/mês
- ✅ 512 MB RAM
- ✅ HTTPS automático
- ⚠️ App hiberna após 15min inativo
- ⚠️ Cold start (15-30s na primeira requisição)

**Para evitar hibernação:**
- Upgrade para plano pago ($7/mês)
- Ou use cronjob para ping a cada 10 minutos

---

## 🔄 Auto-Deploy (Opcional)

O Render detecta automaticamente commits na branch `main`.

Para usar o arquivo `render.yaml`:
1. Já criado na raiz do projeto
2. Deploy automático ao fazer push

---

## 📧 Suporte

Se encontrar problemas:
1. Verifique os logs no Render
2. Teste localmente primeiro
3. Consulte: https://render.com/docs

---

**✨ Deploy completo! Seu FoundPrice está no ar!**
