## Modul 2: Priprema okruženja: instalacija i prvo pokretanje

U Modulu 1 si naučio kako Claude Code razmišlja. Sada je vreme da ga dovedeš na svoj računar i progovoriš sa njim prvi put. Ovo poglavlje te vodi korak po korak, od otvaranja terminala (da, i to ćemo objasniti) do prvog razgovora. Na kraju ćeš imati instaliran alat, prijavljen nalog i osećaj da ovo, zapravo, nije strašno.

### Šta ćeš naučiti

- Šta je terminal i zašto ti za rad sa Claude Code treba svega nekoliko komandi
- Kako da instaliraš Claude Code (i alternativu bez terminala, desktop aplikaciju)
- Šta Claude sme da radi u folderu iz kog ga pokrećeš
- Kako da vodiš prvi, potpuno bezbedan razgovor
- Kako radi sistem dozvola i kada je bezbedno pustiti Claude-a da radi samostalno

### Šta je terminal i zašto ne treba da te plaši

Terminal je program u kom računaru daješ komande tekstom umesto klikovima. Zamisli razliku između naručivanja u restoranu pokazivanjem na slike u meniju (klikovi) i jednostavnog izgovaranja „jedan espreso, molim" (terminal). Ista kuhinja, isti rezultat, samo drugačiji način komunikacije.

Crni prozor sa trepćućim kursorom deluje kao nešto iz hakerskih filmova, ali evo dobre vesti: za rad sa Claude Code trebaće ti bukvalno dve-tri komande. Sve ostalo radiš razgovorom na srpskom. Terminal je samo ulazna vrata.

**Na Mac-u:** pritisni `Cmd + Space` (otvara se Spotlight pretraga), ukucaj `Terminal` i pritisni Enter. To je to.

**Na Windows-u:** pritisni taster Windows, ukucaj `PowerShell` (ili `Terminal` na novijim verzijama) i pritisni Enter.

Otvoriće se prozor sa tekstom i kursorom koji čeka tvoju komandu. Ne moraš ništa da razumeš od onoga što piše, samo da znaš gde kucaš.

### Instalacija: dva puta do cilja

**Put 1: Desktop aplikacija (bez terminala).** Ako ti je terminal i dalje nelagodan, Claude Code postoji i kao obična desktop aplikacija za Mac i Windows, preuzmeš je, instaliraš kao bilo koji program i radiš u poznatom prozoru. Postoje i web verzija (claude.ai/code) i ekstenzije za programerske editore, ali to ti za sada nije bitno.

**Put 2: Terminal verzija (CLI).** CLI znači „command line interface", verzija programa koja živi u terminalu. Ovaj put preporučujem, jer ćeš kroz ceo dokument raditi upravo u njoj, a instalacija traje dva minuta.

Prvo ti treba **Node.js**, besplatan program koji omogućava da se ovakvi alati pokreću na tvom računaru. Zamisli ga kao motor: ne voziš ga direktno, ali bez njega auto ne ide. Preuzmi ga sa zvaničnog sajta `nodejs.org` (uzmi verziju označenu kao LTS) i instaliraj klikovima kao bilo koji program.

Zatim u terminal ukucaj:

```
npm install -g @anthropic-ai/claude-code
```

`npm` je „prodavnica" programa koja dolazi uz Node.js, a ova komanda kaže: „preuzmi i instaliraj Claude Code tako da bude dostupan svuda na računaru". Sačekaj da se završi (može potrajati minut-dva).

### Prvo pokretanje i prijava

Claude Code se pokreće iz foldera projekta, foldera u kom su (ili će biti) fajlovi tvog proizvoda. Za prvi put, napravi prazan folder, recimo `moj-prvi-projekat`, na Desktop-u.

U terminalu uđi u taj folder i pokreni Claude:

```
cd ~/Desktop/moj-prvi-projekat
claude
```

Komanda `cd` znači „change directory", kao da u Finder-u/Explorer-u uđeš u folder dvoklikom, samo tekstom.

**Napomena za Windows:** ako dobiješ grešku da folder ne postoji, tvoj Desktop je verovatno u OneDrive-u (podrazumevano na novijim Windows računarima), probaj `cd ~/OneDrive/Desktop/moj-prvi-projekat`. Još lakše: u Explorer-u uđi u folder, desni klik na praznu površinu i izaberi „Open in Terminal", terminal se otvara već u pravom folderu.

Pri prvom pokretanju Claude će te provesti kroz **prijavu**, samo prati uputstva na ekranu.

### Folder kao radni prostor: kome daješ ključeve

Claude Code može da čita i menja fajlove u folderu u kom radi. Pokretanje Claude-a u nekom folderu je zato kao davanje ključeva stana majstoru: to je prostor u kom mu dozvoljavaš da radi. Pritom ne radi ništa na svoju ruku, pre potencijalno opasnih akcija pita te za odobrenje (o tome detaljnije malo niže). Za foldere koje si sam napravio ili projekte koje poznaješ, nema razloga za brigu. Oprez je potreban samo ako si preuzeo tuđi, nepoznat projekat sa interneta: tada prvo zamoli Claude-a da ti objasni šta se u folderu nalazi, pre nego što mu dozvoliš bilo šta drugo.

### Prvi razgovor: tri bezbedna prompta

Sada si u razgovoru. Kucaš poruke, Claude odgovara. Evo tri probe koje ništa ne menjaju na računaru, savršene za zagrevanje:

```
Objasni mi šta vidiš u ovom folderu. Ja nisam programer,
pa mi objasni jednostavnim jezikom.
```

```
Planiram da napravim [opiši svoju ideju u jednoj rečenici].
Šta bi predložio da prvo uradimo? Nemoj još ništa da menjaš,
samo mi ispričaj plan.
```

```
Koje alate imaš na raspolaganju i šta sve umeš da uradiš
u ovom projektu? Odgovori kratko, kao da pričaš sa početnikom.
```

Primeti šablon u drugom promptu: izričito kažeš „nemoj još ništa da menjaš". To je tvoja moć kao direktora, ti odlučuješ kada se prelazi sa priče na delo. Za ozbiljnije planiranje postoji i poseban plan mode, o kom detaljno govorimo u Modulu 5.

Ako Claude krene u pogrešnom smeru, pritisni `Esc`, prekida ga usred rada i odmah možeš da ga preusmeriš novim uputstvom.

### Sistem dozvola: zašto te Claude stalno nešto pita

Brzo ćeš primetiti da Claude pre određenih akcija traži tvoje odobrenje: „Mogu li da pokrenem ovu komandu?", „Mogu li da izmenim ovaj fajl?". To nije znak da je nesiguran, to je sigurnosni sistem. Claude pita pre potencijalno opasnih akcija, da slučajno ne obriše ili izmeni nešto bez tvog znanja. Kao novi zaposleni koji proverava sa šefom pre nego što pošalje imejl klijentu.

Vremenom prekidi postaju zamorni, pa postoje tri načina da ih smanjiš:

1. **Lista dozvoljenih komandi**, u fajlu `.claude/settings.json` čuva se spisak komandi koje su unapred odobrene, pa za njih Claude više ne pita.
2. **Komanda `/fewer-permission-prompts`**, ukucaš je, a Claude analizira vaš dosadašnji rad i sam predloži listu bezbednih komandi za odobrenje. Ne moraš ručno da sastavljaš ništa.
3. **Auto mode**, režim u kom Claude automatski odobrava alate i radi autonomno, bez zastajkivanja.

**Kada je auto mode bezbedan?** Tek kada imaš sigurnosnu mrežu, a ona se zove git. Git je sistem koji pamti svaku sačuvanu verziju tvog projekta (svaki commit je kao snimak stanja), pa se svaka promena može vratiti unazad. Detaljno ga postavljamo u Modulu 3. Pravilo glasi: **bez git-a, bez auto mode-a.** Sa git-om, najgore što može da se desi jeste da vratiš projekat na prethodni snimak, i ništa nije izgubljeno.

### Vežba

1. Instaliraj Claude Code: preuzmi Node.js sa `nodejs.org`, zatim u terminalu pokreni `npm install -g @anthropic-ai/claude-code`. (Alternativa: instaliraj desktop aplikaciju.)
2. Napravi prazan folder `proba-claude` na Desktop-u.
3. U terminalu uđi u njega (`cd ~/Desktop/proba-claude`; na Windows-u sa OneDrive-om `cd ~/OneDrive/Desktop/proba-claude`) i pokreni `claude`.
4. Prođi kroz prijavu prateći uputstva na ekranu.
5. Postavi prvi prompt: `Objasni mi šta vidiš u ovom folderu i šta bi predložio da prvo uradimo. Nemoj ništa da menjaš.`
6. Vodi razgovor 5–10 minuta: pitaj ga šta ume, opiši mu neku svoju ideju, traži da ti objasni neki pojam koji ti nije jasan.
7. Za kraj, ukucaj `/clear` da obrišeš kontekst, i čestitaj sebi: vodio si prvi razgovor sa svojim AI saradnikom.

### Najčešće greške

1. **„Komanda `claude` ne radi posle instalacije."** Najčešće je dovoljno da zatvoriš terminal i otvoriš nov prozor, tek tada terminal „vidi" novoinstalirane programe. Ako i dalje ne radi, proveri da li je Node.js instaliran: ukucaj `node --version`.
2. **Pokretanje Claude-a iz pogrešnog foldera.** Claude radi u folderu iz kog je pokrenut. Ako ga pokreneš sa Desktop-a umesto iz foldera projekta, videće sve tvoje fajlove sa Desktop-a. Uvek prvo `cd` u folder projekta, pa onda `claude`.
3. **Slepo potvrđivanje svih dozvola bez čitanja.** Na početku čitaj šta Claude traži, tako učiš šta on zapravo radi. Klik na „odobri" bez čitanja je kao potpisivanje ugovora bez gledanja.
4. **Uključivanje auto mode-a pre nego što postoji git.** Bez sigurnosne mreže, greška u autonomnom radu nema dugme za poništavanje. Prvo Modul 3, pa tek onda autonomija.
5. **Odustajanje zbog prve poruke o grešci.** Crveni tekst u terminalu nije katastrofa, to je informacija. Kopiraj celu poruku i nalepi je Claude-u uz pitanje: `Dobio sam ovu grešku, objasni mi šta znači i kako da je rešim.` Rešavanje problema je detaljno u Modulu 13.

### Kontrolna lista

- [ ] Otvorio sam terminal (Mac: Spotlight → Terminal; Windows: PowerShell)
- [ ] Instalirao sam Node.js sa `nodejs.org`
- [ ] Instalirao sam Claude Code (`npm install -g @anthropic-ai/claude-code`) ili desktop aplikaciju
- [ ] Napravio sam folder za probu i pokrenuo `claude` iz njega
- [ ] Prošao sam kroz prijavu pri prvom pokretanju
- [ ] Vodio sam prvi razgovor sa bar dva probna prompta
- [ ] Znam čemu služi `Esc` (prekid) i `/clear` (sveža sesija)
- [ ] Razumem zašto Claude traži dozvole i kada je auto mode bezbedan

### Proveri znanje

**1. Šta je terminal i koliko komandi ti realno treba za rad sa Claude Code?**

Terminal je program u kom računaru daješ komande tekstom umesto klikovima. Za Claude Code dovoljno je par komandi: instalacija, `cd` za ulazak u folder i `claude` za pokretanje, sve ostalo je razgovor.

**2. Šta dozvoljavaš Claude-u kada ga pokreneš u nekom folderu?**

Da u tom folderu čita i menja fajlove, kao davanje ključeva majstoru, s tim što pre potencijalno opasnih akcija pita za odobrenje. Za sopstvene foldere bez brige; za nepoznate projekte sa interneta prvo traži objašnjenje sadržaja.

**3. Kada je bezbedno uključiti auto mode?**

Tek kada projekat ima git kao sigurnosnu mrežu, tada se svaka Claude-ova promena može vratiti na prethodni snimak (commit). Bez git-a, bez auto mode-a.
