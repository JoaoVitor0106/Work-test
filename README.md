# b2bflow - Envio de mensagens WhatsApp

Script Python que lê contatos do Supabase e envia mensagens via Z-API.

A mensagem enviada é: `"Olá, <nome_contato> tudo bem com você?"`

---

## Configuração do Supabase

1. Crie uma conta em [supabase.com](https://supabase.com) e um novo projeto
2. No **SQL Editor**, crie a tabela de contatos:

```sql
CREATE TABLE contacts (
  id    bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  name  text NOT NULL,
  phone text NOT NULL
);
```

3. Insira os contatos (número no formato `5511999999999`):

```sql
INSERT INTO contacts (name, phone) VALUES
  ('João Silva', '5511999990001'),
  ('Maria Souza', '5511999990002');
```

4. Em **Settings > API**, copie a **Project URL** e a **anon key**

---

## Configuração da Z-API

1. Crie uma conta em [z-api.io](https://z-api.io)
2. Crie uma instância e escaneie o QR Code com seu WhatsApp
3. Copie o **Instance ID**, **Token** e **Client Token** do painel

---

## Variáveis de ambiente

Crie um arquivo `.env` na raiz com base no `.env.example`:

```env
SUPABASE_URL=https://xxxx.supabase.co
SUPABASE_KEY=sua-anon-key

ZAPI_INSTANCE_ID=sua-instance-id
ZAPI_TOKEN=seu-token
ZAPI_CLIENT_TOKEN=seu-client-token
```

---

## Como rodar

```bash
pip install -r requirements.txt
python main.py
```
