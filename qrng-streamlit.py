#!/usr/bin/env python
# coding: utf-8

# In[ ]:
try:
    import random as rand
    from typing import Dict, List, Union
    import numpy as np
    import requests
    import streamlit as st

    _ANU_PARAMS: Dict[str, Union[int, str]] = {
        "length": 1,
        "type": "hex16",
        "size": 8,
    }
    _ANU_URL: str = "https://qrng.anu.edu.au/API/jsonI.php"


    def get_qrand_int64() -> List[int]:
        """Get quantum random int64s from the ANU API."""
        response = requests.get(_ANU_URL, _ANU_PARAMS)
        response.raise_for_status()
        r_json = response.json()

        if r_json["success"]:
            return [int(number, 16) for number in r_json["data"]]
        else:
            raise RuntimeError(
                "The 'success' field in the ANU response was False."
            )
    #print(len(get_qrand_int64()))
except:
    st.write("failure")

try:
    test = st.text_input("What random sort do you want? Enter the corresponding number. 1) Flip a coin 2) Select individuals from a group")    
except:
    st.write("failure_input")
    
while(True):
    try:
        randomMethod = st.text_input("What random sort do you want? Enter the corresponding number. 1) Flip a coin 2) Select individuals from a group")
        #st.text("you chose: ", type(randomMethod), randomMethod)
        st.write(type(randomMethod.title()))
        if randomMethod.title() == "1":
            no_flips = st.text_input("Flip how many times?: ", key ="1")
            for i in range(int(no_flips.title())):
                rand.seed(get_qrand_int64()[0])
                coin = rand.randint(0, 1)
                if coin == 0:
                    st.write("tails")
                if coin == 1:
                    st.write("heads")

        if randomMethod.title() == "2":
            list_chance = []
            nameChance_dict = {}
            no_individuals = st.text_input("How many individuals?: ", key = "2")

            for j in range(int(no_individuals.title())):
                name = st.text_input("Name: ",  key = "nombre")
                rand.seed(get_qrand_int64()[0])
                chance = rand.random()
                while chance == any in list_chance:
                    rand.seed(get_qrand_int64()[0])
                    chance = rand.random()
                nameChance_dict[chance] = name.title()
                list_chance.append(chance)
                new = np.asarray(list_chance)
            choose_how_many = st.number_input("How many individuals must be selected?: ", key = "3")
            # print(new, type(new))
            sorted_list = np.argsort(new)
            # print(sorted_list)

            for k in range(int(choose_how_many.title())):
                st.write(nameChance_dict[new[sorted_list[len(sorted_list) - 1 - k]]])
    except:
        st.text("error")
        continue


# In[ ]:




