#The complete project can be found on Github: https://github.com/HotPaper77/PokemonProject_Elvis_GBAGUIDI
import streamlit as st
import requests
import numpy as np
from PIL import Image
import random



def fetch(session, url):
    try:
        result = session.get(url)
        return result.json()
    except Exception:
        return {}



icon = Image.open("pokeball_icon.png")

def main():
    st.set_page_config(page_title="Quel est ce Pokemon?", page_icon=icon)
    st.title("Devinez quel est ce Pokemon?")
    session = requests.Session()

    if 'key' not in st.session_state:
        st.session_state['round']
        st.session_state['round'] = 0
        st.session_state['answser'] =""

    def pokemon_generator():
        pokemon_random_id = random.randint(1, 858)
        pokemon_species_data = fetch(session, f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_random_id}/")
        pokemon_name = pokemon_species_data["name"]
        global pokemon_name_translated
        pokemon_name_translated = pokemon_species_data["names"][4]["name"]

        pokemon_data = fetch(session, f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/")
        pokemon_image_url = pokemon_data["sprites"]["other"]["official-artwork"]["front_default"]

        if pokemon_data:
            st.write(pokemon_name_translated)
            st.image(pokemon_image_url)
            # st.image(data['download_url'], caption=f"Author: {data['author']}")
        else:
            st.error("Error")
    def round_result():
        st.session_state['round'] += 1
        pokemon_name_translated = ""
        st.session_state['answser'] = pokemon_name_translated


    play = st.button("Jouer",on_click= round_result)

    if st.session_state['round'] % 2 == 0 :
        with st.form("my_form"):
            pokemon_generator()
            st.write(st.session_state['round'])
            user_answer = st.text_input("Réponse",placeholder="ex.Pikachu")
            global submitted
            submitted = st.form_submit_button("Envoyer",on_click=round_result)

            if submitted:
                st.write(st.session_state['answser'])
    elif st.session_state['round'] % 2 == 0 and st.session_state['round'] >=1 :
        st.write("lol")

if __name__ == '__main__':
    main()
