from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class HomePage(BasePage):
    #<input type="radio" name="pessoa" value="F" onclick="simuladorInternet.selecionarTipoPessoa();" id="pessoaF">
    RADIO_PESSOA_FISICA = (By.ID, "pessoaF")

    #<input type="text" id="tipoImovel_input" class="ui-autocomplete-input ui-widget ui-widget-content ui-corner-left combobox" autocomplete="off" style="width: 262.4px;">
    CAMPO_TIPO_IMOVEL = (By.ID, "tipoImovel_input")

    #<input type="text" id="grupoTipoFinanciamento_input" class="ui-autocomplete-input ui-widget ui-widget-content ui-corner-left combobox" autocomplete="off" style="width: 277.4px;">
    CAMPO_TIPO_FINANCIAMENTO = (By.ID, "grupoTipoFinanciamento_input")

    #<input type="text" name="valorImovel" maxlength="25" value="0,00" id="valorImovel" style="width:70%;" class="field-d input-money maskMoedaSemPrefix">
    CAMPO_VALOR = (By.ID, "valorImovel")

    #<input type="text" id="uf_input" class="ui-autocomplete-input ui-widget ui-widget-content ui-corner-left combobox" autocomplete="off" style="width: 63.4px;">
    CAMPO_UF = (By.ID, "uf_input")

    #<input type="text" id="cidade_input" class="ui-autocomplete-input ui-widget ui-widget-content ui-corner-left combobox" autocomplete="off" style="width: 157.4px;">
    CAMPO_CIDADE = (By.ID, "cidade_input")

    #<div class="div_button submit-d submit-blue" id="btn_next1"><i class="font-icon i-down-dir"></i> Próxima etapa</div>
    BTN_NEXT1 = (By.ID, "btn_next1")

    def clicar_botao_proxima_etapa(self):
        botao = self.driver.find_element(*self.BTN_NEXT1)
        #botao = self.driver.find_element(By.ID, "btn_next1")
        botao.click()

    def select_pessoa_fisica(self):
        self.wait_and_click(*self.RADIO_PESSOA_FISICA)

    def preencher_tipo_imovel(self, texto):
        time.sleep(1)
        # Garante que o campo esteja visível e clicável
        self.wait.until(EC.visibility_of_element_located(self.CAMPO_TIPO_IMOVEL))
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable(self.CAMPO_TIPO_IMOVEL))
        # Usa JavaScript para garantir a visibilidade, caso necessário
        campo = self.driver.find_element(*self.CAMPO_TIPO_IMOVEL)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", campo)
        time.sleep(1)
        campo.clear()
        campo.send_keys(texto)
        time.sleep(1)
        campo.send_keys(Keys.TAB)
        campo.send_keys(Keys.TAB)    

        #campo.send_keys(Keys.ARROW_DOWN)
        #campo.send_keys(Keys.ENTER)
        #campo.click()
        return campo

    def preencher_tipo_financiamento(self, texto):
        time.sleep(1)
        # Garante que o campo esteja visível e clicável
        self.wait.until(EC.visibility_of_element_located(self.CAMPO_TIPO_FINANCIAMENTO))
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable(self.CAMPO_TIPO_FINANCIAMENTO))
        # Usa JavaScript para garantir a visibilidade, caso necessário
        campo = self.driver.find_element(*self.CAMPO_TIPO_FINANCIAMENTO)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", campo)
        time.sleep(1)
        campo.clear()
        campo.send_keys(texto)
        time.sleep(1)
        campo.send_keys(Keys.TAB)
        campo.send_keys(Keys.TAB)  

        return campo

    def preencher_uf(self, texto):
        time.sleep(1)
        # Garante que o campo esteja visível e clicável
        self.wait.until(EC.visibility_of_element_located(self.CAMPO_UF))
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable(self.CAMPO_UF))
        # Usa JavaScript para garantir a visibilidade, caso necessário
        campo = self.driver.find_element(*self.CAMPO_UF)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", campo)
        time.sleep(1)
        campo.clear()
        campo.send_keys(texto)
        time.sleep(1)
        campo.send_keys(Keys.TAB)
        campo.send_keys(Keys.TAB)  
        return campo

    def preencher_cidade(self, texto):
        time.sleep(1)
        # Garante que o campo esteja visível e clicável
        self.wait.until(EC.visibility_of_element_located(self.CAMPO_CIDADE))
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable(self.CAMPO_CIDADE))
        # Usa JavaScript para garantir a visibilidade, caso necessário
        campo = self.driver.find_element(*self.CAMPO_CIDADE)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", campo)
        time.sleep(1)
        campo.clear()
        campo.send_keys(texto)
        time.sleep(1)
        campo.send_keys(Keys.TAB)
        campo.send_keys(Keys.TAB)  
        return campo          

    def preencher_valor_imovel(self, valor):
        # Garante que o campo esteja visível e clicável
        self.wait.until(EC.visibility_of_element_located(self.CAMPO_VALOR))
        #self.wait.until(EC.element_to_be_clickable(self.CAMPO_VALOR))

        campo = self.driver.find_element(*self.CAMPO_VALOR)

        # Rola até o elemento para garantir que esteja visível (recomendado)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", campo)

        # Limpa o campo e insere o valor
        campo.clear()
        campo.send_keys(str(valor)) # Converte o valor para string
        return campo 

    