from selenium import webdriver
import time

senha = input("Insira sua senha: ")
browser = webdriver.Chrome()
browser.get('https://portalth.algarnet.com.br/Algar/Produtos/SAAA/Principal2.aspx?amb_selecionado=0&abrir_nova_janela=N&eh_mdesigner=N&nome_portal=634C3649335370516551633D')
browser.find_element_by_xpath('//*[@id="txtLogin"]').send_keys('0337770')
browser.find_element_by_xpath('//*[@id="txtSenha"]').send_keys(senha)
browser.find_element_by_xpath('//*[@id="btnEntrar"]').click()
browser.get('https://portalth.algarnet.com.br/Algar/ASS_MDADOS_CONTROLEJORNADA.aspx')
time.sleep(3)
browser.find_element_by_xpath('//*[@id="imagem0"]').click()
time.sleep(10)
browser.find_element_by_xpath('//*[@id="Button2"]').click()

#<input id="Button2" class="BotaoAchatado" onclick="javascript: window.close()" type="button" value="   Fechar   " name="Submit2">