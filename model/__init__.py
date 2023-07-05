from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base , sessionmaker

engine = create_engine("mysql+pymysql://hair_studio_ivana:lozinka@mysql:3306/hair_studio_ivana" , connect_args={'unix_socket': None})
Session = sessionmaker(bind=engine)

session = Session()
Base = declarative_base()
