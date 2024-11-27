from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configurar o WebDriver com o WebDriver Manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Passo 1: Acessar a URL
    driver.get("https://habitacao.caixa.gov.br/siopiweb-web/simulaOperacaoInternet.do?method=inicializarCasoUso&pk_campaign=habitacao&pk_kwd=direct&pk_source=redirect")

    # Esperar a página carregar
    time.sleep(2)  # Ajuste conforme necessário

    #Clica da opção Pessoa Física
    #<input type="radio" name="pessoa" value="F" onclick="simuladorInternet.selecionarTipoPessoa();" id="pessoaF">
    #driver.find_element('xpath','/html/body/div[1]/form/div/fieldset[1]/ul/li[2]/ul/li[1]/label/input').click()
    driver.find_element(By.ID, "pessoaF").click()

    # Localizar o campo Tipo de Imovel
    #<input type="text" id="tipoImovel_input" class="ui-autocomplete-input ui-widget ui-widget-content ui-corner-left combobox" autocomplete="off" style="width: 262.4px;">
    campo_tipo_imovel = driver.find_element(By.ID, "tipoImovel_input")

    # Espere até que o elemento seja clicável
    wait = WebDriverWait(driver, 1)  # Espere até 10 segundos
    campo_tipo_imovel = wait.until(EC.visibility_of_element_located((By.ID, "tipoImovel_input")))    
    wait = WebDriverWait(driver, 1)  # Espere até 10 segundos
    #campo_tipo_imovel = wait.until(EC.element_to_be_clickable((By.ID, "tipoImovel_input")))

    # Limpar o campo (caso haja algum valor preenchido)
    campo_tipo_imovel.clear()

    # Digitar "Residencial" no campo
    campo_tipo_imovel.send_keys("Residencial")
    
    # Aguardar um curto período para o autocomplete carregar as opções
    time.sleep(1)

    # Usar a seta para baixo para selecionar a opção "Residencial"
    #campo_tipo_imovel.send_keys(Keys.ARROW_DOWN)

    # Pressionar Enter para confirmar a seleção
    #campo_tipo_imovel.send_keys(Keys.ENTER)
    campo_tipo_imovel.send_keys(Keys.TAB)
    campo_tipo_imovel.send_keys(Keys.TAB)

    # Esperar para visualizar a interação
    time.sleep(1)
    

finally:
    # Fechar o navegador
    driver.quit()
