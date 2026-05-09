import os
from dotenv import load_dotenv

load_dotenv()

# Getting Config from the ENV file
# Relational Database like Postgres, mysql

RD_SERVICE=os.getenv("RD_SERVICE")
RD_USER=os.getenv("RD_USER")
RD_PASSWORD=os.getenv("RD_PASSWORD")
RD_HOST= os.getenv("RD_HOST")
RD_PORT= os.getenv("RD_PORT")
RD_DATABASE = os.getenv("RD_DATABASE")

# Non Relation Database like mongodb

NRD_USER = os.getenv("NRD_USER")
NRD_PASSWORD = os.getenv("NRD_PASSWORD")
NRD_HOST = os.getenv("NRD_HOST")
NRD_PORT = os.getenv("NRD_PORT")
NRD_DATABASE = os.getenv("NRD_DATABASE")

# Async Database URL
RD_DATABASE_URL = f"{RD_SERVICE}+asyncpg://{RD_USER}:{RD_PASSWORD}@{RD_HOST}:{RD_PORT}/{RD_DATABASE}"

# Sync Database URL
SYNC_RD_DATABASE_URL = f"{RD_SERVICE}://{RD_USER}:{RD_PASSWORD}@{RD_HOST}:{RD_PORT}/{RD_DATABASE}"

# Non Relation Database URL
NRD_DATABASE_URL = f"{RD_SERVICE}://{NRD_USER}:{NRD_PASSWORD}@{NRD_HOST}:{NRD_PORT}/{NRD_DATABASE}"

# Middleware configs

# Cors Middleware
Origins=["*"]
AllowCredentials=True
AllowedMethods= ["*"]
AllowedHeaders= ["*"]

# Trusted Host Middleware

Hosts = ["*"]