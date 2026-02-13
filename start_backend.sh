#!/bin/bash

echo "========================================"
echo "   FoundPrice Backend - Iniciando..."
echo "========================================"
echo ""

# Ativa o ambiente virtual
source venv/bin/activate

echo "[OK] Ambiente virtual ativado"
echo ""
echo "Iniciando servidor FastAPI..."
echo "Backend rodará em: http://localhost:8000"
echo ""

# Roda o uvicorn do diretório raiz
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
