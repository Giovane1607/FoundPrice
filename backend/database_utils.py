from database import SessionLocal, HistoricoPreco
from datetime import datetime

def salvar_historico(resultados):
    db = SessionLocal()
    try:
        print(f"--- Salvando {len(resultados)} produtos no banco ---")
        registros = [
            HistoricoPreco(
                produto=item['title'],
                preco=item['price'],
                loja=item['source'],
                link=item['link'],
                data_busca=datetime.now().strftime("%d/%m/%Y %H:%M")
            ) for item in resultados
        ]
        db.bulk_save_objects(registros)
        db.commit()
        print("✔ Dados salvos com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao salvar: {e}")
    finally:
        db.close()

def buscar_dados_grafico(nome_produto):
    db = SessionLocal()
    try:
        termo = nome_produto.split()[0] if nome_produto else ""
        print(f"--- Buscando gráfico para termo: {termo} ---")
        
        registros = db.query(HistoricoPreco).filter(HistoricoPreco.produto.contains(termo)).all()
        print(f"Encontrados {len(registros)} registros no histórico.")

        comparativo = {}
        for r in registros:
            if r.loja not in comparativo or r.preco < comparativo[r.loja]:
                comparativo[r.loja] = r.preco
        
        retorno = {"labels": list(comparativo.keys()), "valores": list(comparativo.values())}
        print(f"Dados formatados para o gráfico: {retorno}")
        return retorno
    finally:
        db.close()

def buscar_metricas(nome_produto):
    db = SessionLocal()
    try:
        termo = nome_produto.split()[0] if nome_produto else ""
        print(f"--- Calculando métricas para: {termo} ---")
        
        historico = db.query(HistoricoPreco).filter(HistoricoPreco.produto.contains(termo)).all()
        if not historico:
            print("⚠ Nenhum dado encontrado para comparação.")
            return {"error": "Sem dados"}
        
        precos = [h.preco for h in historico]
        media = sum(precos) / len(precos)
        precos_seguros = [p for p in precos if p > (media * 0.45)]
        menor_legitimo = min(precos_seguros) if precos_seguros else min(precos)
        
        print(f"Média: {media} | Menor Seguro: {menor_legitimo}")
        return {
            "media_mercado": media,
            "menor_legitimo": menor_legitimo,
            "alerta_golpe": any(p < (media * 0.35) for p in precos)
        }
    finally:
        db.close()