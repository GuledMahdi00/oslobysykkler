# Oslobysykkel
Denne applikasjonen er en sanntids tabell som bruker oslo bysykkels sitt [Rest-API](https://oslobysykkel.no/apne-data/sanntid), for å vise tilgjengelige låser og ledige sykler i en stasjon. 

## Hva Koden Består Av
Koden består av en backend som bruker det fleksible og simple programmeringsspråket python med modulene "requests" og "Flask", mens frontenden bruker "HTML", "CSS" og "JavaScript" med rammeverkene "Bootstrap" og "Jquery".

## Hvordan Kjøre Applikasjonen
1. Installer python version 3.11
2. Installer modulet "requests" med pip3 (pip3 install requests)
3. Installer modulet "Flask" med pip3 (pip3 install Flask)
4. I Prosjekt mappen kjør python filen "app.py" (python3 -m flask --app app.py run)
5. Applikasjonen bør nå kjøre og informasjonen relatert kravene er tilgjengelig gjennom en tabell på nettsiden http://localhost:5000/

## Sluttbruker
Min prioritet i oppgaven er å sørge for at sluttbrukeren kan lese og forstå innholdet hent inn fra oslo bysykkel derfor vises informasjon frem gjennom en nettside på en tabell med søkefelt for å filtrere og finne spesifikke stasjoner.
