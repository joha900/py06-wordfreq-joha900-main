def wordfreq(text: str) -> dict:

    # Skapa en tom dictionary för att hålla frekvensen av varje ord.
    word_freq = {}

    # Här delar jag upp strängen med en metod som kallas för split metoden
    words = text.split()

    # För att texten ska loopa igenom listan och hitta likadana ord så behöver jag skapa en for loop.
    for word in words:

        # Syftet här är att se om ordet finns i dictionary, ju fler likadana ord det finns så ökar frekvensen med 1.
        if word in word_freq:
            word_freq[word] += 1
        # Om det inte finns mer än ett ord så ska frekvensen ge 1 som resultat
        else:
            word_freq[word] = 1

    return word_freq


# Här testar jag att skriva en mening med flera ord i samma mening för att få fram ett resultat.
text = "How much wood could a woodchuck chuck if a woodchuck could chuck wood"
print(wordfreq(text))
