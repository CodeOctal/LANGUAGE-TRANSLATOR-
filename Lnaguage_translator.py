from googletrans import Translator
def get_key(val):
        for key, value in Dict.items():
            if val == value:
                return key 
        return "key doesn't exist"

while(1):
     google= input("enter tha language:  ")
     
     if "exit" in str(google) or "bye" in str(google) or "sleep" in str(google):
         print("Ok bye")
         break
    
     Dict = {"af"	:	'Afrikaans'	,
            "ga"	:	'Irish'	,
            "sq"	:	'Albanian'	,
            "it"	:	'Italian'	,
            "ar"	:	'Arabic'	,
            "ja"	:	'Japanese'	,
            "az"	:	'Azerbaijani'	,
            "kn"	:	'Kannada'	,
            "eu"	:	'Basque'	,
            "ko"	:	'Korean'	,
            "bn"	:	'Bengali'	,
            "la"	:	'Latin'	,
            "be"	:	'Belarusian'	,
            "lv"	:	'Latvian'	,
            "bg"	:	'Bulgarian'	,
            "lt"	:	'Lithuanian'	,
            "ca"	:	'Catalan'	,
            "mk"	:	'Macedonian'	,
            "zh-CN"	:	'Chinese Simplified'	,
            "ms"	:	'Malay'	,
            "zh-TW"	:	'Chinese Traditional'	,
            "mt"	:	'Maltese'	,
            "hr"	:	'Croatian'	,
            "no"	:	'Norwegian'	,
            "cs"	:	'Czech'	,
            "fa"	:	'Persian'	,
            "da"	:	'Danish'	,
            "pl"	:	'Polish'	,
            "nl"	:	'Dutch'	,
            "pt"	:	'Portuguese'	,
            "en"	:	'English'	,
            "ro"	:	'Romanian'	,
            "eo"	:	'Esperanto'	,
            "ru"	:	'Russian'	,
            "et"	:	'Estonian'	,
            "sr"	:	'Serbian'	,
            "tl"	:	'Filipino'	,
            "sk"	:	'Slovak'	,
            "fi"	:	'Finnish'	,
            "sl"	:	'Slovenian'	,
            "fr"	:	'French'	,
            "es"	:	'Spanish'	,
            "gl"	:	'Galician'	,
            "sw"	:	'Swahili'	,
            "ka"	:	'Georgian'	,
            "sv"	:	'Swedish'	,
            "de"	:	'German'	,
            "ta"	:	'Tamil'	,
            "el"	:	'Greek'	,
            "te"	:	'Telugu'	,
            "gu"	:	'Gujarati'	,
            "th"	:	'Thai'	,
            "ht"	:	'Haitian Creole'	,
            "tr"	:	'Turkish'	,
            "iw"	:	'Hebrew'	,
            "uk"	:	'Ukrainian'	,
            "hi"	:	'Hindi'	,
            "ur"	:	'Urdu'	,
            "hu"	:	'Hungarian'	,
            "vi"	:	'Vietnamese'	,
            "is"	:	'Icelandic'	,
            "cy"	:	'Welsh'	,
            "id"	:	'Indonesian'	,
            "yi"	:	'Yiddish'	
            }
        
     sentence= str(input("say something......"))

     translator = Translator()
     translated_sentence=translator.translate(sentence,src='en',dest=get_key(google))

     print(translated_sentence.text)

     

