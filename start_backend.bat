@echo off
echo ========================================
echo   FoundPrice Backend - Iniciando...
echo ========================================
echo.

REM Ativa o ambiente virtual
call venv\Scripts\activate

echo [OK] Ambiente virtual ativado
echo.
echo Iniciando servidor FastAPI...
echo Backend rodara em: http://localhost:8000
echo.

REM Roda o uvicorn do diretório raiz
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
