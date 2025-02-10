from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BankModel(Base):
    __tablename__ = "banks"

    bank_id = Column(Integer, primary_key=True, index=True)
    bank_name = Column(String(100), nullable=False)
    active = Column(Integer, server_default="1", index=True)

    def __init__(self, **kwargs):
        self.bank_name = kwargs.get("bank_name")
