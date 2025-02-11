from whatsapp_web import WhatsApp

# Criar uma instância do WhatsApp
wp = WhatsApp()

# Conectar ao WhatsApp Web e escanear o QR Code (feito manualmente uma vez)
wp.start()

# Função para responder automaticamente a mensagens
def on_message_received(msg):
    print(f"Mensagem recebida: {msg['body']}")
    if "Oi" in msg['body']:
        wp.send_message(msg['sender'], "Olá! Como posso ajudar?")
    elif "Problema" in msg['body']:
        wp.send_message(msg['sender'], "Desculpe pela confusão. Estamos resolvendo!")
    # Adicione outras condições aqui conforme necessário

# Defina o método para monitorar mensagens
wp.on_message(on_message_received)

# Manter o script rodando para receber mensagens
wp.run()

# Fechar a sessão após o uso
wp.close()
