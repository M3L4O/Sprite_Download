import requests
import pokepy as pk
import os

client = pk.V2Client()

def dowload(url, name, position):
    if url is None:
        print('Escolha inválida')
        return
    try:
        raw = requests.get(url)
        try:
            with open(f'Pokemons/{name}_{position}.png', 'wb') as image:
                image.write(raw.content)
        except:
            path = f'{os.getcwd()}/Pokemons'
            os.mkdir(path)
            with open(f'Pokemons/{name}_{position}.png', 'wb') as image:
                image.write(raw.content)

    except Exception as error:
        print(error)


def get_url(urls):
    options = {}
    options_index = []
    for key, value in urls.items():
        if value is not None:
            options[key] = value
            options_index.append(key)

    options_str = '\n'.join(f'[{index}] {key}\n' for index, key in enumerate(options_index))
    try:
        choice = options_index[int(input(f'\nQual destas opções quer baixar?\n{options_str}\n-> '))]
        return options[choice], choice
    except Exception as error:
        print(error)
        return None
   

def get_sprite():
    name = input('\nQual o nome do pokémon que você quer baixar a imagem?\n-> ')
    try:
        pokemon = client.get_pokemon(name)[0]
        urls = pokemon.sprites.__dict__
        url, position = get_url(urls)
        dowload(url, name, position)
    except Exception as error:
        print(error)


if __name__ == "__main__":
    get_sprite()