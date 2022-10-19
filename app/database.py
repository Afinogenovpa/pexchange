from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQLALCHEMY_DATABASE_URL = "sqlite:///./sql.db"
SQLALCHEMY_DATABASE_URL = "postgresql://zxrvyczdafqtwx:6dbedc697797c7f4cb40e38f95b999eb2475c3de3879fb30ac423b59dc30bb34@ec2-54-228-32-29.eu-west-1.compute.amazonaws.com:5432/dv0h8krvnf1m4"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()