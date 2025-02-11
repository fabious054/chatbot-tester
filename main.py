from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import time
import tkinter as tk
from tkinter import messagebox

# Função para fechar a janela e continuar o script
def continuar():
    root.destroy()

# Configuração da interface gráfica
root = tk.Tk()
root.title("WhatsApp QR Code")
root.geometry("300x100")

label = tk.Label(root, text="Escaneie o QR code e clique em Continuar")
label.pack(pady=10)

continuar_button = tk.Button(root, text="Continuar", command=continuar)
continuar_button.pack(pady=10)

# Inicializa o driver do Selenium
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com')

# Exibe a janela e espera o usuário clicar em "Continuar"
root.mainloop()

# Após o usuário clicar em "Continuar", o script continua
print("Continuando com o script...")

# Função para enviar uma mensagem
def enviar_mensagem():
    try:
        # Localiza a caixa de mensagem e envia a mensagem
        message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
        message_box.send_keys("Oi")
        message_box.send_keys(Keys.ENTER)
        time.sleep(3)  # Aguarda a mensagem ser enviada
        print("Mensagem 'Oi' enviada para Мама.")
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")

# Função para aplicar o filtro "Não Lidas"
def aplicar_filtro_nao_lidas():
    try:
        # Localiza o botão "Não Lidas" e clica nele
        unread_button = driver.find_element(By.ID, 'unread-filter')
        unread_button.click()
        print("Filtro 'Não Lidas' aplicado com sucesso.")
    except Exception as e:
        print(f"Erro ao aplicar o filtro 'Não Lidas': {e}")

# Função para verificar conversas não lidas
def verificar_conversas_nao_lidas():
    try:
        # Localiza todas as conversas não visualizadas
        chat_elements = driver.find_elements(By.XPATH, '//div[contains(@class, "x10l6tqk") and contains(@class, "xh8yej3") and contains(@class, "x1g42fcv")]')

        if chat_elements:
            print(f"Total de conversas não visualizadas: {len(chat_elements)}")
            for index, chat in enumerate(chat_elements):
                # Extrai o nome do usuário
                contact_name_element = chat.find_element(By.XPATH, './/span[contains(@class, "x1iyjqo2") and contains(@class, "x6ikm8r") and contains(@class, "x10wlt62") and contains(@class, "x1n2onr6") and contains(@class, "xlyipyv") and contains(@class, "xuxw1ft") and contains(@class, "x1rg5ohu") and contains(@class, "_ao3e")]')
                contact_name = contact_name_element.text
                print(f"{index + 1}. {contact_name}")

                # Verifica se o contato é "Мама"
                if contact_name == "Мама":
                    print(f"Contato especial encontrado: {contact_name}")
                    # Clica na conversa para abri-la
                    chat.click()
                    time.sleep(2)  # Aguarda a conversa carregar
                    # Envia a mensagem "Oi"
                    enviar_mensagem()
                    break  # Sai do loop após enviar a mensagem
        else:
            print("Nenhuma conversa não visualizada encontrada.")
    except Exception as e:
        print(f"Erro ao procurar conversas não visualizadas: {e}")

# Aplica o filtro "Não Lidas" uma vez no início
aplicar_filtro_nao_lidas()

# Loop infinito para verificar novas mensagens não lidas
try:
    while True:
        # Verifica as conversas não lidas
        verificar_conversas_nao_lidas()

        # Atualiza a página para recarregar as conversas
        driver.refresh()
        print("Página atualizada. Reaplicando o filtro 'Não Lidas'...")
        time.sleep(5)  # Aguarda a página carregar

        # Reaplica o filtro "Não Lidas"
        aplicar_filtro_nao_lidas()

        # Aguarda um tempo antes de verificar novamente (ex: 10 segundos)
        time.sleep(10)
except KeyboardInterrupt:
    print("Script interrompido pelo usuário.")
finally:
    # Fechar o navegador ao sair
    driver.quit()