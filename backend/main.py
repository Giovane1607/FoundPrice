from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import os
from dotenv import load_dotenv
from backend import database_utils as dbu
from backend.database import init_db

load_dotenv()
init_db()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://foundprice.com.br",
        "https://www.foundprice.com.br",
        "http://localhost:4200"  # Para testes locais
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/search")
def search(q: str):
    print(f"\n🔎 Nova busca iniciada: {q}")
    key = os.getenv("SERP_API_KEY")
    url = f"https://serpapi.com/search.json?engine=google_shopping&q={q}&api_key={key}&gl=br&hl=pt-br&curr=BRL"
    
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        results = data.get("shopping_results", [])
        
        # Lista atualizada para evitar o erro de "Tudo em Risco"
        varejistas_confiaveis = [
            "amazon", "mercado livre", "magalu", "magazine luiza", "casas bahia", 
            "kabum", "pichau", "nissei", "havan", "netshoes", "shopee", 
            "fast shop", "terabyte", "meugameusado"
        ]
        
        processed = []
        for item in results:
            source_original = item.get("source", "Desconhecido")
            source_lower = source_original.lower()
            
            # Captura o link real da loja (evita o redirecionamento interno do Google)
            link_direto = item.get("link") or item.get("product_link") or "#"
            
            p = {
                "title": item.get("title", "Sem Nome"),
                "price": item.get("extracted_price", 0),
                "source": source_original,
                "link": link_direto,
                "confiavel": any(v in source_lower for v in varejistas_confiaveis) or ".com.br" in source_lower
            }
            processed.append(p)
        
        if processed:
            dbu.salvar_historico(processed)
            
        return processed
    except Exception as e:
        print(f"❌ Erro: {e}")
        return []

@app.get("/api/analise-produto")
def get_analise(q: str):
    return dbu.buscar_dados_grafico(q)

@app.get("/api/comparar-vendas")
def comparar_vendas(q: str):
    return dbu.buscar_metricas(q)