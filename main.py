
from writer import *


def main():
    open_notepad()
    
    type_text(greeting_text, 0)

    poo = CreatePoo()

    MovePoo(poo)

    StartCountDown()

    SurpriseGracie()

    type_text(final_message, 0.0001)

    ShowRespect()



if __name__ == "__main__":
    main()
