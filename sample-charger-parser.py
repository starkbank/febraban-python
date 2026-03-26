from febraban.cnab240.itau.sispag import PaymentParser
from febraban.cnab240.itau.charge.result.parser import SlipParser

file = open("Teste.RET", "r")

responses = SlipParser.parseFile(file)

for response in responses:
    if "Andreia Nobre Veloso".upper() in response.contentText():
        print(response.status())
        print("-------------------------------------------------------------------")
    # print(response.contentText())
    # print("-------------------------------------------------------------------")