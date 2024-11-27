from pages.home_page import HomePage
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.by import By
import time

class HabitacaoActions:
    def __init__(self, driver):
        self.home_page = HomePage(driver)

    def realizar_simulacao(self):
        time.sleep(1)
        # Seleciona a opção "Pessoa Física"
        self.home_page.select_pessoa_fisica()

        # Preenche o tipo de imóvel como "Residencial"
        campo = self.home_page.preencher_tipo_imovel("Residencial")

        # Preenche o tipo de financiamento
        campo = self.home_page.preencher_tipo_financiamento("Aquisição de Imóvel Novo")
        
        # Preenche o valor do imovel
        campo = self.home_page.preencher_valor_imovel(35100000)

        # Preenche UF
        campo = self.home_page.preencher_uf('PR')
        
        # Preenche Cidade
        campo = self.home_page.preencher_cidade('MANDAGUARI')

        # Proxima etapa 
        self.home_page.clicar_botao_proxima_etapa()


        
        