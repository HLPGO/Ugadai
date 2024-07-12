import random
from word_list import word_list
from display_hangman import display_hangman

def get_word(t):
    # t1 = t.upper()
    return random.choice(t)

def play(word):
    print('Давайте играть. Загадано слово на русском языке, маленькими буквами.')
    print(display_hangman(6))
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    word_completion = list(word_completion)
    print('Загадано слово из', len(word), 'букв', ' '.join(word_completion))
    guessed = False                    # сигнальная метка
    guessed_letters = []               # список уже названных букв
    guessed_words = []                 # список уже названных слов
    tries = 6                          # количество попыток
    while tries > 0:
        print('Введите букву или слово целиком. Чтобы прервать игру наберите 777')
        s = input()
        if s == '777':
            break
        if len(s) > 1:
            if len(s) == len(word):
                if s == word:
                    print('Вы угадали. Конец игры.')
                    break
                else:
                    if s in guessed_words:
                        print('это слово уже называли')
                    else:
                        print('Вы не угадали, использована попытка.')
                        tries = tries - 1
                        guessed_words.append(s)
                        print(display_hangman(tries))                    
            else:
                print('неправильный ввод, повторите')
        else:
            if s in guessed_letters:
                print('Эта буква уже была. Попытка не потрачена.')
            else:
                c = 0
                for i in range(len(word)):
                    if word[i] == s:
                        word_completion[i] = s
                        c = c + 1
                if c == 0:
                    tries = tries - 1
                    print('Такой буквы нет, использована попытка. Осталось попыток:', tries)
                    print(display_hangman(tries))
                    print(' '.join(word_completion))
                    guessed_letters.append(s)
                else:
                    print('Есть такая буква, открыто букв:', c)
                    guessed_letters.append(s)
                    if ''.join(word_completion) == word:
                        print('Вы угадали последнюю букву и выиграли! Загаданное слово:', ' '.join(word_completion))
                        print('Конец игры.')
                        break
                    else:
                        print(' '.join(word_completion))
                        print('Бонусная попытка. Оталось попыток:', tries)
                        print(display_hangman(tries))
                # tries = tries - 1
                # display_hangman(tries)                
    else:
        print('Вы исчерпали все попытки')
        # print(display_hangman(0))
        print('Загаданное слово:', word)

# print(display_hangman(0))
while True:
    word = get_word(word_list)
    play(word)
    print('Хотите продолжить играть? д/н')
    wish = input()
    if wish == 'д':
        True
    else:
        print('Пока!')
        break
    
    