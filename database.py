from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///./todo.db")
Base = declarative_base()

class ToDo(Base):
    __tablename__ = "todo"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)

"""
def get_db():
    engine = create_engine("sqlite:///./todo.db")
    Base.metadata.create_all(bind=engine)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


if __name__ == "__main__":
    get_db()
"""