from source.sprites import get_sprite


def menu():
    choice = int(input('[1] Baixar sprites.\n[0] Sair\n-> '))
    if choice == 1:
        get_sprite()
    elif choice == 0:
        return False
    else:
        print('Escolha inválida!\n')
    return True


def main():
    while menu():
        pass


if __name__ == "__main__":
    main()