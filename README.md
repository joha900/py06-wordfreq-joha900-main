# Uppgift 06 - Wordfreq

# Syfte

Att utveckla förmågan att använda dictionaries för att analysera textdata och stärka kunskaperna i strängmanipulation.

# Inför uppgiften

Se till att du känner till:

- De grundläggande datatyperna i Python, inklusive strängar, listor och dictionaries.
- Hur man använder loopar, både `for`-loopar och `while`-loopar.
- Hur man skapar funktioner.
- Olika strängmetoder, exempelvis `.split()`.

# Beskrivning

Skapa en funktion med namnet `wordfreq` i filen [uppgift.py](./uppgift.py) som tar emot en sträng som input och ger tillbaka en dictionary med ordfrekvenser som output.

Det dictionary som returneras ska ha de unika orden från strängen som nycklar och hur många gånger varje ord förekommer i strängen som värden.

## Funktionen `wordfreq`

En funktion som tar in en text och returnerar en dictionary med orden i texten som nycklar och antal gånger de förekommer i texten som värden. För att separera ord i
strängen, anta att ord separeras av ett mellanslag.

- Signatur: `wordfreq(text: str) -> dict`
- Positionella argument:
  - `text` (float): Blah blah
- Utskrift: Inget!
- Returvärde: Ett dictionary där nycklarna är unika ord från
  strängen och värdena är antalet gånger dessa ord förekommer. Om den givna
  strängen är tom, ska funktionen returnera ett tomt dictionary.

## Tips

- Använd `.split()`-metoden för att dela upp strängen i en lista av ord baserad
  på mellanslag.
- Loopa sedan igenom listan av ord och använd ett dictionary för att hålla reda på
  frekvensen av varje ord.
- Var noga med att hantera fall där strängen är tom på ett korrekt sätt.

### Exempel

1. Anrop: `wordfreq("hej hej på dig")`

- Utskrift: Inget!
- Returvärde `{'hej': 2, 'på': 1, 'dig': 1}`

2. Anrop: `wordfreq("ett två tre två")`

- Utskrift: Inget!
- Returvärde `{'ett': 1, 'två': 2, 'tre': 1}`

3. Anrop: `wordfreq("")`

- Utskrift: Inget!
- Returvärde `{}`

4. Anrop: `wordfreq("python programmering python")`

- Utskrift: Inget!
- Returvärde `{'python': 2, 'programmering': 1}`

5. Anrop: `wordfreq("test test test")`

- Utskrift: Inget!
- Returvärde `{'test': 3}`

# Inlämningsinstruktioner

För att lämna in din uppgift, vänligen följ dessa steg:

1. Använd GitHub Classroom och klona ditt uppgiftsrepository:

   - Om du läser det här i `README.md` har du redan börjat med uppgiften genom att klicka på en länk från din utbildare och klonat ditt uppgiftsrepository.

2. Lös uppgiften:

   - Din lösning ska skapas genom att ändra i de filer som nämns i uppgiftsbeskrivningen. Följ instruktionerna där för var du ska lägga in din kod.

3. Automatiska "smoke tests":

   - Kör uppgiftens "smoke tests" lokalt på din dator.

     - För Bash: Kör skriptet `.smoke/run`
     - För PowerShell: Kör skriptet `.smoke/run.ps1`

   - När du skickar in din kod körs dessa tester automatiskt. En grön bock betyder att de gick igenom, medan ett rött kryss betyder att något gick fel (för att se vad som gick fel måste du tyvärr köra testerna lokalt).

4. Lämna in med Git:

   - När du är klar, använd `git add .`, `git commit` och sedan `git push` för att skicka in ditt arbete till GitHub.

5. Feedback och granskning från utbildaren:

   - När dina "smoke tests" får en grön bock väntar du på feedback från din utbildare. Utbildaren kan vilja att du ändrar något eller godkänna din uppgift direkt. Vänta med att slå ihop din kod ("Merge") tills uppgiften är godkänd.

   - Om utbildaren vill att du ändrar något, läs noggrant och gör de ändringar som behövs.

   - När uppgiften är godkänd och det inte finns mer att diskutera, kan du göra "Merge" med din "Feedback"-pull request. Men, vänta alltid tills du har fått ett godkännande.

6. Starta diskussioner i "Feedback"-pull requesten:

   - Utnyttja möjligheten att diskutera uppgiftens kod i din "Feedback"-pull request. Det är ett bra sätt att lära sig genom att ställa frågor, be om förklaringar eller diskutera lösningar och respons med din utbildare.
