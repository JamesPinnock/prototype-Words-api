import requests, pprint

while True:

    try:

        word = input("Enter in a word: ")

        response = requests.get("https://wordsapiv1.p.rapidapi.com/words/{}/typeOf".format(word),
          headers={
            "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com",
            "X-RapidAPI-Key": "8ce8b4b8demshbcaf0a187fc92b7p1edb83jsna9a0c50b83b5"
          }
        )
        #
        # response = requests.get("https://wordsapiv1.p.rapidapi.com/words/pet/typeOf",
        #   headers={
        #     "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com",
        #     "X-RapidAPI-Key": "8ce8b4b8demshbcaf0a187fc92b7p1edb83jsna9a0c50b83b5"
        #   }
        # )

        printed = response.json()

        pprint.pprint(f"{word} is a type of " + printed['typeOf'][0])

    except:
        print("Not valid")
        # raise Exception("Not valid")

    finally:
        pass



