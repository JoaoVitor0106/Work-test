import logging

from src.supabase_client import get_contacts
from src.zapi_client import send_message

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
logger = logging.getLogger(__name__)


def main():
    logger.info("Iniciando envio de mensagens...")

    contatos = get_contacts()

    if not contatos:
        logger.warning("Nenhum contato para processar.")
        return

    for contato in contatos:
        nome = contato.get("name", "").strip()
        telefone = contato.get("phone", "").strip()

        if not nome or not telefone:
            logger.warning(f"Contato invalido, pulando: {contato}")
            continue

        send_message(name=nome, phone=telefone)

    logger.info("Processo finalizado.")


if __name__ == "__main__":
    main()
