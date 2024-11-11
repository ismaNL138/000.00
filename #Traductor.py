jh#Traductor
print("Hola, Bienvenido a este superincreible traductor")
print("-----------Traductor de saludos-----------")
print("Opciones:")
print("1.   Traducir saludos Español - Ingles")
print("2.   Traducir saludos Español - Frances")
print("3.   Traducir saludos Español - Aleman")
print("4.   Traducir saludos Español - Ruso")
print("5.   Traducir saludos Español - Japones")
print("-------------Elije una opcion:------------")
idioma = int(input(""))
print("------------------------------------------")
if idioma == 1:
    print("Puedes traducir alguna de las siguientes palabras:")
    print("Hola \n Buenas \n Buenos Días \n Buenas Tardes \n Buenas Noches \n Bienvenido \n Saludos \n ¿Que tal? \n ¿Como va todo? \n ¿Que onda?")
    ingw = input("Escriba la palabra a traducir:   ")
    if ingw == 'Hola':
        print("Hi / Hello")
    elif ingw == 'Buenas':
        print("Hello Good")
    elif ingw == 'Buenos Días':
        print("Good Morning")
    elif ingw == 'Buenas Tardes':
        print("Good Afternoon")
    elif ingw == 'Buenas Noches':
        print(" Good Night")
    elif ingw == 'Bienvenido':
        print("Welcome")
    elif ingw == 'Saludos':
        print("Greetings")
    elif ingw == '¿Que tal?':
        print("How are you?")
    elif ingw == '¿Como va todo?':
        print("How's everything going?")
    elif ingw == "¿Que onda?":
        print("What's up?")

elif idioma == 2:
    print("Puedes traducir alguna de las siguientes palabras:")
    print("Hola \n Buenas \n Buenos Días \n Buenas Tardes \n Buenas Noches \n Bienvenido \n Saludos \n ¿Qué tal? \n ¿Cómo va todo? \n ¿Qué onda?")
    palabra = input("Escriba la palabra a traducir: ")
    if palabra == 'Hola':
        print("Bonjour")
    elif palabra == 'Buenas':
        print("Salut")
    elif palabra == 'Buenos Días':
        print("Bonjour")
    elif palabra == 'Buenas Tardes':
        print("Bon après-midi")
    elif palabra == 'Buenas Noches':
        print("Bonne nuit")
    elif palabra == 'Bienvenido':
        print("Bienvenue")
    elif palabra == 'Saludos':
        print("Salutations")
    elif palabra == '¿Qué tal?':
        print("Comment ça va?")
    elif palabra == '¿Cómo va todo?':
        print("Comment ça se passe?")
    elif palabra == '¿Qué onda?':
        print("Quoi de neuf?")


elif idioma == 3:
    print("Puedes traducir alguna de las siguientes palabras:")
    print("Hola \n Buenas \n Buenos Días \n Buenas Tardes \n Buenas Noches \n Bienvenido \n Saludos \n ¿Qué tal? \n ¿Cómo va todo? \n ¿Qué onda?")
    palabra = input("Escriba la palabra a traducir: ")
    if palabra == 'Hola':
        print("Hallo")
    elif palabra == 'Buenas':
        print("Guten Tag")
    elif palabra == 'Buenos Días':
        print("Guten Morgen")
    elif palabra == 'Buenas Tardes':
        print("Guten Nachmittag")
    elif palabra == 'Buenas Noches':
        print("Gute Nacht")
    elif palabra == 'Bienvenido':
        print("Willkommen")
    elif palabra == 'Saludos':
        print("Grüße")
    elif palabra == '¿Qué tal?':
        print("Wie geht's?")
    elif palabra == '¿Cómo va todo?':
        print("Wie läuft alles?")
    elif palabra == '¿Qué onda?':
        print("Was geht ab?")

elif idioma == 4:
    print("Puedes traducir alguna de las siguientes palabras:")
    print("Hola \n Buenas \n Buenos Días \n Buenas Tardes \n Buenas Noches \n Bienvenido \n Saludos \n ¿Qué tal? \n ¿Cómo va todo? \n ¿Qué onda?")
    palabra = input("Escriba la palabra a traducir: ")
    if palabra == 'Hola':
        print("Здравствуйте (Zdravstvuyte)")
    elif palabra == 'Buenas':
        print("Привет (Privet)")
    elif palabra == 'Buenos Días':
        print("Доброе утро (Dobroye utro)")
    elif palabra == 'Buenas Tardes':
        print("Добрый день (Dobryy den')")
    elif palabra == 'Buenas Noches':
        print("Доброй ночи (Dobroy nochi)")
    elif palabra == 'Bienvenido':
        print("Добро пожаловать (Dobro pozhalovat')")
    elif palabra == 'Saludos':
        print("Приветствия (Privetstviya)")
    elif palabra == '¿Qué tal?':
        print("Как дела? (Kak dela?)")
    elif palabra == '¿Cómo va todo?':
        print("Как идут дела? (Kak idut dela?)")
    elif palabra == '¿Qué onda?':
        print("Что нового? (Chto novogo?)")

elif idioma == 5:
    print("Puedes traducir alguna de las siguientes palabras:")
    print("Hola \n Buenas \n Buenos Días \n Buenas Tardes \n Buenas Noches \n Bienvenido \n Saludos \n ¿Qué tal? \n ¿Cómo va todo? \n ¿Qué onda?")
    palabra = input("Escriba la palabra a traducir: ")
    if palabra == 'Hola':
        print("こんにちは (Konnichiwa)")
    elif palabra == 'Buenas':
        print("こんにちは (Konnichiwa)")
    elif palabra == 'Buenos Días':
        print("おはようございます (Ohayou gozaimasu)")
    elif palabra == 'Buenas Tardes':
        print("こんにちは (Konnichiwa)")
    elif palabra == 'Buenas Noches':
        print("おやすみなさい (Oyasumi nasai)") 
    elif palabra == 'Bienvenido':
        print("ようこそ (Youkoso)")
    elif palabra == 'Saludos':
        print("挨拶 (Aisatsu)")
    elif palabra == '¿Qué tal?':
        print("お元気ですか？ (Ogenki desu ka?)")
    elif palabra == '¿Cómo va todo?':
        print("調子はどうですか？ (Choushi wa dou desu ka?)")
    elif palabra == '¿Qué onda?':
        print("何か新しいことはありますか？ (Nanika atarashii koto wa arimasu ka?)")

else:
    print("Opcion no valida")