_TRANSLATION_TABLE = {
    "О" : "ААА",
    "Е" : "ХХХ",
    "А" : "АХАА",
    "И" : "АХХА",
    "Т" : "АХХХ",
    "Н" : "ХААХ",
    "С" : "ХАХА",
    "Р" : "ХХАХ",
    "В" : "ААХАХ",
    "Л" : "ААХХХ",
    "К" : "АХАХА",
    "М" : "ХАААХ",
    "Д" : "ХАХХХ",
    "П" : "ХХААА",
    "У" : "ААХААА",
    "Я" : "ААХААХ",
    "Ы" : "ААХХАХ",
    "З" : "АХАХХА",
    "Ь" : "АХАХХХ",
    "Ъ" : "ХААААХ",
    "Б" : "ХАХХАА",
    "Г" : "ХАХХАХ",
    "Ч" : "ХХААХХ",
    "Й" : "ААХХААХ",
    "Х" : "ХАААААА",
    "Ж" : "ХАААААХ",
    "Ю" : "ХХААХАХ",
    "Ш" : "ААХХАААА",
    "Ц" : "ХХААХААА",
    "Щ" : "ХХААХААХ",
    "Э" : "ААХХАААХА",
    "Ф" : "ААХХАААХХ",
}

def _make_trie(code_map: dict):
    root = dict()
    for word, value in code_map.items():
        current_dict = root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict[None] = value
    return root


_appendix = {}
for key, value in _TRANSLATION_TABLE.items():
    _appendix[key.lower()] = value.lower()

_TRANSLATION_TABLE = {**_TRANSLATION_TABLE, **_appendix}

_reverted_table = {v: k for k, v in _TRANSLATION_TABLE.items()}
_lang_trie = _make_trie(_reverted_table)


def w_russian_to_livesey(word: str) -> str:
    result = ""

    for char in word:
        try:
            result += _TRANSLATION_TABLE[char]
        except KeyError:
            result += char
    
    return result

def russian_to_livesey(*words):
    result = []
    for word in words:
        result.append(w_russian_to_livesey(word))
    return result


def w_livesey_to_russian(word: str) -> str:
    current_node = _lang_trie
    it = iter(word)
    translation = ""
    while True:
        if None in current_node:
            translation += current_node[None]
            current_node = _lang_trie
            continue
        try:    
            char = next(it)
            current_node = current_node[char]
        except StopIteration:
            break

    return translation

def livesey_to_russian(*words):
    result = []
    for word in words:
        result.append(w_livesey_to_russian(word))
    return result


if __name__ == '__main__':
    res = russian_to_livesey("Привет", "мир")
    print(res)
    print(livesey_to_russian(*res))