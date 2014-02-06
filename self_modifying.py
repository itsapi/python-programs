with open('self_modifying.py', 'w') as this:
    this.write('with open("self_modifying.py", "w") as this:\n\tthis.write("print(\'hi\')")')