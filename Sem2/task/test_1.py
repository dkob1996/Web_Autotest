import yaml
from module import Site


with open ("/Users/dmitrii_kobozev/Desktop/Web_Autotests/Sem2/task/testdata.yaml") as f:
    testdata = yaml.safe_load(f)
site = Site(testdata["address"])


def test_step1():
    x_selector_1 = """//*[@id="login"]/div[1]/label/input"""
    input1 = site.find_element('xpath', x_selector_1)
    input1.send_keys('test')
    x_selector_2 = """//*[@id="login"]/div[2]/label/input"""
    input2 = site.find_element('xpath', x_selector_2)
    input2.send_keys('test')
    btn_selector = "button"
    btn = site.find_element('css', btn_selector)
    btn.click()
    x_selector_3 = """//*[@id="app"]/main/div/div/div[2]/h2"""
    err_label = site.find_element('xpath', x_selector_3)
    res = err_label.text
    site.close()
    assert res == '401'


