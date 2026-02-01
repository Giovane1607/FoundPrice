from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    "sqlite:///./foundprice.db", 
    connect_args={"check_same_thread": False, "timeout": 30}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class HistoricoPreco(Base):
    __tablename__ = "historico"
    id = Column(Integer, primary_key=True, index=True)
    produto = Column(String)
    preco = Column(Float)
    loja = Column(String)
    link = Column(String) # Coluna para o "Ir para Loja"
    data_busca = Column(String)

def init_db():
    Base.metadata.create_all(bind=engine)