redaction = '***'
separator = ';'
def f(x): return f"{x.group(1)} = {redaction}{separator}"


fields = ['ssn', 'password']
print(f(fields))
