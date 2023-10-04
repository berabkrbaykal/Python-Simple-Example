import random

rpc = ['Taş', 'Kağıt', 'Makas']

AI = 'Yapay Zeka'
name = input('İsminizi giriniz: ')

playerScore = 0
aiScore = 0
i = 0

print("")

print('Oyun 3 turdan oluşmaktadır')

while (i < 3):

    give = input('Taş Kağıt veya Makastan bir tanesini seçiniz: ')
    print("")
    ai = (random.choice(rpc))

    if ((give.lower() != 'taş') and (give.lower() != 'kağıt') and (give.lower() != 'makas')):
        print("Taş Kağıt veya Makas'tan farklı bir değer giriniz lütfen geçerli bir değer girin")
    else:
        if (give.lower() == 'taş' and ai == 'Taş'):
            print(f'Sizin seçtiğiniz Taş Yapay Zekanın seçtiği {ai} ve kazanan yok\n')
        elif (give.lower() == 'kağıt' and ai == 'Taş'):
            print(f'Sizin seçtiğiniz Kağıt Yapay Zekanın seçtiği {ai} ve {name} kazandı\n')
            playerScore += 1
        elif (give.lower() == 'makas' and ai == 'Taş'):
            print(f'Sizin seçtiğiniz Makas Yapay Zekanın seçtiği {ai} ve {AI} kazandı\n')
            aiScore += 1

        if (give.lower() == 'taş' and ai == 'Kağıt'):
            print(f'Sizin seçtiğiniz Taş Yapay Zekanın seçtiği {ai} ve {AI} kazandı\n')
            aiScore += 1
        elif (give.lower() == 'kağıt' and ai == 'Kağıt'):
            print(f'Sizin seçtiğiniz Kağıt Yapay Zekanın seçtiği {ai} ve kazanan yok\n')
        elif (give.lower() == 'makas' and ai == 'Kağıt'):
            print(f'Sizin seçtiğiniz Makas Yapay Zekanın seçtiği {ai} ve {name} kazandı\n')
            playerScore += 1

        if (give.lower() == 'taş' and ai == 'Makas'):
            print(f'Sizin seçtiğiniz Taş Yapay Zekanın seçtiği {ai} ve {name} kazandı\n')
            playerScore += 1
        elif (give.lower() == 'kağıt' and ai == 'Makas'):
            print(f'Sizin seçtiğiniz Kağıt Yapay Zekanın seçtiği {ai} ve {AI} kazandı\n')
            aiScore += 1
        elif (give.lower() == 'makas' and ai == 'Makas'):
            print(f'Sizin seçtiğiniz Makas Yapay Zekanın seçtiği {ai} ve kazanan yok\n')
        
        i += 1


print('\n\t\tSONUÇLAR\t\t\n')

if (playerScore < aiScore):
    print(f"\n{name}'in skoru: {playerScore} \nYapay Zekanın skoru: {aiScore} \nKazanan {AI}")
elif (playerScore > aiScore):
    print(f"\n{name}'in skoru: {playerScore} \nYapay Zekanın skoru: {aiScore} \nKazanan {name}")
else:
    print(f"\n{name}'in skoru: {playerScore} \nYapay Zekanın skoru: {aiScore} \nOyun berabere")
