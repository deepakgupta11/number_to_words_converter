from num2words import num2words

def number_to_words_hindi(n):
    if n == 0:
        return "शून्य"

    if n < 0:
        return "ऋण " + number_to_words_hindi(abs(n))

    words_up_to_100 = [
        "शून्य", "एक", "दो", "तीन", "चार", "पाँच", "छह", "सात", "आठ", "नौ", "दस",
        "ग्यारह", "बारह", "तेरह", "चौदह", "पंद्रह", "सोलह", "सत्रह", "अठारह", "उन्नीस", "बीस",
        "इक्कीस", "बाईस", "तेईस", "चौबीस", "पच्चीस", "छब्बीस", "सत्ताईस", "अट्ठाईस", "उनतीस", "तीस",
        "इकतीस", "बत्तीस", "तैंतीस", "चौंतीस", "पैंतीस", "छत्तीस", "सैंतीस", "अड़तीस", "उनतालीस", "चालीस",
        "इकतालीस", "बयालीस", "तैंतालीस", "चवालीस", "पैंतालीस", "छियालीस", "सैंतालीस", "अड़तालीस", "उनचास", "पचास",
        "इक्यावन", "बावन", "तिरेपन", "चौवन", "पचपन", "छप्पन", "सत्तावन", "अट्ठावन", "उनसठ", "साठ",
        "इकसठ", "बासठ", "तिरेसठ", "चौंसठ", "पैंसठ", "छियासठ", "सड़सठ", "अड़सठ", "उनहत्तर", "सत्तर",
        "इकहत्तर", "बहत्तर", "तिहत्तर", "चौहत्तर", "पचहत्तर", "छिहत्तर", "सतहत्तर", "अठहत्तर", "उनासी", "अस्सी",
        "इक्यासी", "बयासी", "तिरासी", "चौरासी", "पचासी", "छियासी", "सत्तासी", "अट्ठासी", "नवासी", "नब्बे",
        "इक्यानवे", "बानवे", "तिरानवे", "चौरानवे", "पचानवे", "छियानवे", "सत्तानवे", "अट्ठानवे", "निन्यानवे", "सौ"
    ]

    if n <= 100:
        return words_up_to_100[n]

    words = []

    if n >= 10000000:
        crores = n // 10000000
        words.extend(number_to_words_hindi(crores).split())
        words.append("करोड़")
        n %= 10000000

    if n >= 100000:
        lakhs = n // 100000
        words.extend(number_to_words_hindi(lakhs).split())
        words.append("लाख")
        n %= 100000

    if n >= 1000:
        thousands = n // 1000
        words.extend(number_to_words_hindi(thousands).split())
        words.append("हज़ार")
        n %= 1000

    if n >= 100:
        hundreds = n // 100
        words.append(words_up_to_100[hundreds])
        words.append("सौ")
        n %= 100

    if n > 0:
        words.extend(number_to_words_hindi(n).split())

    return " ".join(words).strip()

def number_to_words(number, lang):
    if lang == 'en':
        return num2words(number, lang='en')
    elif lang == 'hi':
        return number_to_words_hindi(number)

