import time
cont = str(input('Para iniciar a contagem digite \033[36menter:\033[m '))
for c in range (10,-1,-1):
    print(c)
    time.sleep(0.5)
print('\033[34m***Feliz ano novo***')