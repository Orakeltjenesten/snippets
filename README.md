# Orakelsnippets

Dette er en Alfred workflow for effektiv bruk av snippets for HPSM.

### Forutsetninger

* MacOS 10.13(High Sierra) 
* Alfred 3 med powerpack

### Installasjon

Snippeten kommer i form av en .alfredworkflow fil. Gå til "releases" og last ned siste versjon

Dobbeltklikk på filen og den vil bli åpnet i Alfred

### Første gangs bruk

Snippeten bruker tokens for å verifisere seg mot internsidene. Din token må lagres før du bruker snippets.
Din token finner du på internsidene under "Min profil" -> "API-nøkkel". Kopier denne nøkkelen.
Du lagrer nøkkelen din med følgende Alfred kommando

```
orapelapi <din-api-nøkkel>
<ENTER>
```
Du burde få en notifikasjon om at nøkkelen ble lagret i keychain, men ikke alle får det.

### Bruk

Nøkkelordet for workflowen er bare `o` du kan gi argumenter før å søke i resultatene

```
o <søke-ord>
```

når du velger en snippet så vil den kopieres til clipbordet dit og den vil også limes inn der hvor du har markøren din.

### Tilpasning
Du kan gjøre flere tilpasninger om du skulle ønske. Det gjør du i valgpanelet til Alfred der hvor du installerte workflowen.

#### Nøkkelordet er jo altfor kort, dette er jo helt ubrukelig!
Dobbeltklikk på den øverste av de to elementene som heter "Script filter". Du kan da endre "Keyword" til det som passer inn

#### Det er så jæ**ig irriterende at den bare limer inn sånn uten videre. Slutt med det!
Dobbeltklikk på elementet som heter "Copy to Clipboard" og huk vekk "Automatically paste to front most app"

### Oppdateringer
Alfred skal i ungangpunktet gjøre dette selv&#8482;

Det kan hende du får opp "New version available: Action this item to install the update" Da klikker du på enter, så er du sikker på at du ikke blir etterlatt i workflow-steinalderen
