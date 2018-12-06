from febraban.cnab240.itau.slipV30 import SlipParser

file = open("output.RET", "r")

responses = SlipParser.parseFile(file)

for response in responses:
    print response.identifier
    print response.status()
    print response.amountInCents
    print response.content
    print response.contentText()