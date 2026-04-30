from febraban.cnab240.itau.charge.result.parser import SlipParser
from febraban.cnab240.itau.sispag import PaymentParser


file = open("Teste.RET", "r")

responses = SlipParser.parseFile(file)

for response in responses:
    print("-------------------------------------------------------------------")
    print(response.identifier)
    print(response.authentication)
    print(response.status())
    print(response.amountInCents)
    print(response.type)
    print(response.contentText())
    print("-------------------------------------------------------------------")