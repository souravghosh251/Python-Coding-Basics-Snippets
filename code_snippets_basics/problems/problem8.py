letter = '''
        Dear <|Name|>,
        You are selected!
        <|Date|>
        '''

print(letter.replace("<|Name|>", "Sourav").replace("<|Date|>", "20th June 2024"))   