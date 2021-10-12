from selenium import webdriver
import time

senha = input("Insira sua senha: ")

browser = webdriver.Chrome()

main_page = browser.current_window_handle

browser.get('https://portalth.algarnet.com.br/Algar/Produtos/SAAA/Principal2.aspx?amb_selecionado=0&abrir_nova_janela=N&eh_mdesigner=N&nome_portal=634C3649335370516551633D')
browser.find_element_by_xpath('//*[@id="txtLogin"]').send_keys('0337770')
browser.find_element_by_xpath('//*[@id="txtSenha"]').send_keys(senha)
browser.find_element_by_xpath('//*[@id="btnEntrar"]').click()
time.sleep(10)
browser.get('https://portalth.algarnet.com.br/Algar/ASS_MDADOS_CONTROLEJORNADA.aspx')
time.sleep(10)
browser.find_element_by_xpath('//*[@id="imagem0"]').click()
time.sleep(10)

for handle in browser.window_handles:
    if handle != main_page:
        login_page = handle

browser.switch_to.window(login_page)
browser.find_element_by_xpath('//*[@id="Button2"]').click()
