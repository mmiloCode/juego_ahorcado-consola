import random

WORDS_LIST = [
    "árbol", "amor", "agua", "aire", "animal", "aprender", "bailar", "canción", "comida", "caminar",
    "cielo", "color", "corazón", "cuerpo", "dinero", "dolor", "felicidad", "familia", "fruta", "fuego",
    "guitarra", "hermano", "hoja", "invierno", "luz", "mañana", "montaña", "mundo", "naturaleza", "nieve",
    "noche", "océano", "pájaro", "paz", "planeta", "playa", "poesía", "pueblo", "reír", "sueño",
    "tiempo", "trabajo", "universo", "viajar", "vida", "viento", "amistad", "risa", "libertad", "sonrisa",
    "sombra", "alegría", "canción", "casa", "campo", "ciudad", "beso", "juego", "río", "ciencia",
    "tecnología", "fruta", "amable", "rápido", "lento", "fuerte", "débil", "alto", "bajo", "inteligente",
    "simple", "complicado", "feliz", "triste", "enamorado", "misterio", "sorpresa", "trabajo", "éxito", "fracaso",
    "abrazo", "aventura", "brillante", "búsqueda", "calma", "capacidad", "destino", "esperanza", "fantasía", "generosidad",
    "humildad", "imaginación", "juventud", "lealtad", "maravilla", "nacimiento", "optimismo", "paciencia", "riqueza", "sabiduría",
    "ternura", "valentía", "victoria", "independencia", "compañía", "creatividad", "determinación", "fascinación", "inspiración", "pensamiento",
    "reflexión", "tranquilidad", "vulnerabilidad", "abundancia", "gratitud", "serenidad", "unión", "nacimiento", "evolución", "revolución",
    "prosperidad", "descubrimiento", "exploración", "innovación", "transformación", "armonía", "equilibrio", "pasión", "aventura",
    "amabilidad", "curiosidad", "esperanza", "imaginación", "felicidad", "amor"
    ]



def choise_letter():
    while True:
        user_letter = input("\nLetra: ")
        if user_letter.isdigit():
            print("No jugamos con números...")
        else:
            if len(user_letter) > 1:
                print("Debes ingresar un caracter a la vez.")
            elif user_letter.strip() == "":
                print("Escribe algo")
            else:
                break
    return user_letter



def show_display(user_letters, word, tries):
    display = [letter if letter in user_letters else "_" for letter in word]
    if tries > 1: print(f"Te quedan {tries} intentos")
    elif tries == 1: print(f"Sólo te queda {tries} intento")
    print("\n" + " ".join(display))
    return display






def main():

    while True:


        word = random.choice(WORDS_LIST)
        tries = 5
        user_letters = ""

        menu = "==============================\
            \nJUEGO DEL AHORCADO\
            \n=============================="
        
        print(menu)



        display = show_display(user_letters, word, tries)

        while tries >= 1:
            if display.count("_") == 0:
                break
            user_letter = choise_letter()

            print("------------------------------------")

            if user_letter.upper() in word.upper():
                user_letters += user_letter
            else:
                print("Letra incorrecta")
                tries -= 1
            
            display = show_display(user_letters, word, tries)
        
        print("------------------------------------")
        if tries <= 0:
            print("\nPerdiste. La palabra era:", word)
        else:
            print("\n¡Ganaste!")
        print("\n------------------------------------")
        
        op = input("¿Volver a jugar? (Y/N): ")

        if op.lower() == "n":
            break
        

if __name__ == "__main__":
    main()
