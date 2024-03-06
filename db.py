from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sql_url="mysql+mysqlconnector://root:12345@localhost:3306/UmakantDetails"
engine=create_engine(sql_url,pool_recycle=1800)
Session=sessionmaker (autocommit=False, autoflush=False, bind=engine)