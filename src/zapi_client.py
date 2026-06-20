import logging
import os

import requests
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)


def send_message(name, phone):
    instance_id = os.getenv("ZAPI_INSTANCE_ID")
    token = os.getenv("ZAPI_TOKEN")
    client_token = os.getenv("ZAPI_CLIENT_TOKEN")

    if not instance_id or not token or not client_token:
        raise Exception("Credenciais da Z-API ausentes no .env")

    url = f"https://api.z-api.io/instances/{instance_id}/token/{token}/send-text"
    headers = {"Client-Token": client_token}
    payload = {
        "phone": phone,
        "message": f"Olá, {name} tudo bem com você?",
    }

    logger.info(f"Enviando mensagem para {name} ({phone})...")

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=15)
        response.raise_for_status()
        logger.info(f"Mensagem enviada com sucesso para {name}.")
        return True
    except requests.exceptions.HTTPError:
        logger.error(f"Erro ao enviar para {name}: {response.status_code} - {response.text}")
    except Exception as e:
        logger.error(f"Erro inesperado ao enviar para {name}: {e}")

    return False
