from febraban.cnab240.v30.result.parser import SlipParser

file = open("output.RET", "r")

responses = SlipParser.parseFile(file)

for response in responses:
    print response.identifier
    print response.status()
    print response.amountInCents