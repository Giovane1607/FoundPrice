from sqlalchemy.orm import Session
from database import HistoricoPreco

class AnalisadorPrecos:
    @staticmethod
    def obter_estatisticas(db: Session, nome_produto: str):
        registros = db.query(HistoricoPreco).filter(
            HistoricoPreco.produto.contains(nome_produto)
        ).all()

        if not registros:
            return None

        precos = [r.preco for r in registros]
        menor_preco = min(precos)
        maior_preco = max(precos)
        preco_atual = registros[-1].preco
        
        variacao = ((preco_atual - menor_preco) / menor_preco) * 100 if menor_preco > 0 else 0
        
        return {
            "menor_preco_historico": menor_preco,
            "maior_preco_historico": maior_preco,
            "preco_atual": preco_atual,
            "variacao_percentual": round(variacao, 2),
            "total_registros": len(registros)
        }

    @staticmethod
    def preparar_grafico(db: Session, nome_produto: str):
        registros = db.query(HistoricoPreco).filter(
            HistoricoPreco.produto.contains(nome_produto)
        ).order_by(HistoricoPreco.id.asc()).all()

        return {
            "datas": [r.data_busca for r in registros],
            "precos": [r.preco for r in registros]
        }