from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from actions.habitacao_actions import HabitacaoActions

def main():
    # Configurar o WebDriver com o WebDriver Manager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        # Acessar a URL
        driver.get("https://habitacao.caixa.gov.br/siopiweb-web/simulaOperacaoInternet.do?method=inicializarCasoUso&pk_campaign=habitacao&pk_kwd=direct&pk_source=redirect")

        # Realizar ações na página
        habitacao = HabitacaoActions(driver)
        habitacao.realizar_simulacao()

        # Aguarda para visualizar o resultado
        input("Pressione Enter para sair...")

    finally:
        # Fechar o navegador
        driver.quit()

if __name__ == "__main__":
    main()
