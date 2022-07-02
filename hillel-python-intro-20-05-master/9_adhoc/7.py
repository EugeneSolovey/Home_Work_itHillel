s = """
Дана строка текста.
Посчитайте сколько в этом тексте предложений, учитывая, что предложения разделяются точкой. Так же учтите тот факт, что точка может выступать только разделителем и не использоваться в конце последнего предложения, как мы часто делаем на письме.
"""
empty_s = ""
nodot_s = "Hi Mark"

for text in map(str.strip, (s, empty_s, nodot_s)):
    #text = text.strip()
    sentence_count = text.count(".")
    if text and not text.endswith("."):  # sentence_count[-1] != "."
        sentence_count += 1
    print("Basic count:", sentence_count)

