import logging
import os

from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
logger = logging.getLogger(__name__)


def get_contacts():
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")

    if not url or not key:
        raise Exception("SUPABASE_URL ou SUPABASE_KEY nao encontrados no .env")

    client = create_client(url, key)

    logger.info("Buscando contatos no Supabase...")
    response = client.table("contacts").select("name, phone").limit(3).execute()

    contatos = response.data

    if not contatos:
        logger.warning("Nenhum contato encontrado.")
        return []

    logger.info(f"{len(contatos)} contato(s) encontrado(s).")
    return contatos
