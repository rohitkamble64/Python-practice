Letter = '''Dear <|Name|>,
You're selected!
<|Date|>'''

print(Letter.replace("<|Name|>", "Rohit").replace("<|Date|>", "24/05/2028"))  #chaining