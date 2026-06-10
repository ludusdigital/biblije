## Modul 11: Majstorstvo promptovanja — 10 pravila

Do sada si naučio ceo proces: od ideje, preko plana, do lansiranja. Ovaj modul je tvoja brusilica — deset pravila koja razdvajaju prompt koji "nekako prođe" od prompta koji iz prve da tačno ono što si zamislio. Nijedno pravilo nije teorija; svako je nastalo iz situacije u kojoj je neko izgubio sat vremena jer je rekao premalo, previše ili pogrešnim redom. Formulu savršenog prompta upoznao si u Modulu 6 — ovde je razlažemo na zanatske detalje.

### Šta ćeš naučiti

- Kako da svaki zadatak definišeš tako da Claude tačno zna kada je "gotovo"
- Kako da ograničenjima i referencama sprečiš da Claude radi više (ili manje) nego što treba
- Kada da tražiš plan, a kada da ideš direktno
- Kako da od Claude-a dobiješ dokaz umesto uveravanja
- Kako da ispravke pretvoriš u trajna pravila, da iste stvari ne objašnjavaš dvaput

### Pravilo 1: Kriterijum prihvatanja u svakom zadatku

Claude radi dok ne ispuni ono što je tražio — ali ako ne kažeš kako izgleda "gotovo", on sam odlučuje gde da stane. Kriterijum prihvatanja je kao spisak primopredaje sa majstorom: bez njega, "renovirano kupatilo" znači šta god majstor misli da znači.

❌ Loš prompt:

```
Sredi formu za prijavu na newsletter.
```

✅ Dobar prompt:

```
Sredi formu za prijavu na newsletter. Gotovo je kada:
1. Prazno polje za email prikazuje poruku "Unesi email adresu" na srpskom
2. Neispravan email (bez @) prikazuje "Email adresa nije ispravna"
3. Posle uspešne prijave forma se zameni porukom "Hvala, na listi si!"
4. `npm test` prolazi bez grešaka
```

Razlika: prvi prompt prepušta Claude-u da pogađa šta "sredi" znači, a drugi mu daje merljivu liniju cilja koju i ti i on možete da proverite.

### Pravilo 2: Reci za šta optimizuješ

Svaka odluka u kodu je kompromis — brzina ili čitljivost, jednostavnost ili fleksibilnost. Ako ne kažeš šta ti je prioritet, Claude bira sam, često "za svaki slučaj" gradeći više nego što ti treba.

❌ Loš prompt:

```
Dodaj upload profilne slike.
```

✅ Dobar prompt:

```
Dodaj upload profilne slike. Optimizuj za jednostavnost — ovo je MVP
sa najviše 100 korisnika. Najprostije rešenje koje radi; ne dodavaj
keširanje, obradu slika ni biblioteke koje nisam tražio.
```

Razlika: rečenica "optimizuj za jednostavnost" pretvorila je otvoren zadatak u zadatak sa jasnim kompasom, pa nema prebukiranih rešenja koja kasnije moraš da održavaš.

### Pravilo 3: Eksplicitna ograničenja

Claude je vredan — ponekad previše. Ako ne kažeš šta NE sme da dira, može usput da "popravi" i stvari koje su radile. Ograničenja su kao traka kojom moler oblepi prozore: definišu gde se posao završava.

❌ Loš prompt:

```
Promeni boju dugmadi u plavu.
```

✅ Dobar prompt:

```
Promeni boju glavnih dugmadi u plavu (#2563EB). Ograničenja:
- Menjaj samo fajl sa temom, ne pojedinačne komponente
- Ne diraj boje teksta ni pozadine
- Ne dodavaj nove biblioteke i ne menjaj postojeće testove
```

Razlika: ograničenja su pretvorila "promeni boju" iz poziva na renoviranje celog interfejsa u hirurški precizan zahvat na jednom mestu.

### Pravilo 4: Daj reference

Rečenica "uradi kao u fajlu X" jača je od tri pasusa opisa. Claude može da pročita postojeći fajl i preuzme iz njega sto detalja koje ti nikad ne bi nabrojao: raspored, stil, imenovanje, strukturu.

❌ Loš prompt:

```
Napravi stranicu "O nama". Treba da ima naslov na vrhu, ispod njega
tekst u dve kolone, margine sa strane kao na ostatku sajta, isti font,
dugme na dnu u stilu ostalih dugmadi, i da lepo izgleda na telefonu...
```

✅ Dobar prompt:

```
Napravi stranicu "O nama" po istom šablonu kao postojeća stranica
"Kontakt" (`src/app/kontakt/page.tsx`): isti raspored, isti stil
naslova i dugmadi, isto ponašanje na telefonu. Sadržaj ću ti dati posle.
```

Razlika: umesto da prepričavaš dizajn rečima (i nešto sigurno izostaviš), pokazao si na živi primer koji već sadrži sve odgovore.

### Pravilo 5: Jedan zadatak po sesiji

Sesija je jedan razgovor, a kontekst razgovora se puni kao radni sto — što više nepovezanih stvari na njemu, veća šansa da se nešto pomeša. Tri zadatka u jednom promptu znače da Claude deli pažnju, a tebi je teže da proveriš svaki posebno.

❌ Loš prompt:

```
Popravi bag sa prijavom, dodaj tamnu temu i napiši mi tekst za
landing stranicu.
```

✅ Dobar prompt:

```
Samo jedan zadatak: popravi bag gde se aplikacija zamrzne kada
korisnik tri puta unese pogrešnu lozinku. Gotovo je kada mogu pet
puta da unesem pogrešnu lozinku i svaki put dobijem poruku o grešci.
```

…a zatim `/clear` pa sledeći zadatak u svežoj sesiji.

Razlika: jedan zadatak znači punu pažnju, čistu proveru i čist commit — a `/clear` između zadataka drži radni sto prazan.

### Pravilo 6: Plan za veliko — direktno za malo

Za sitnice je plan gubljenje vremena; za velike stvari je preskakanje plana kockanje. Plan mode (uključuje se prečicom Shift+Tab, koja kruži kroz režime rada) tera Claude-a da prvo istraži i predloži plan, bez menjanja fajlova dok ne odobriš — detaljno u Modulu 5.

❌ Loš prompt (za velik zadatak, bez plana):

```
Dodaj kompletan sistem naplate pretplata sa mesečnim i godišnjim
paketima.
```

✅ Dobar prompt:

```
Prvo napravi plan, ne menjaj ništa dok ne odobrim. Za sistem naplate
pretplata (mesečni i godišnji paket) reci mi: koje fajlove menjaš,
kojim redosledom, šta je najrizičniji deo i šta predlažeš da ostavimo
za kasnije.
```

Razlika: plan ti je dao priliku da loše odluke oboriš na papiru, gde je ispravka besplatna, umesto u kodu, gde košta.

### Pravilo 7: Prekidaj rano

Čim vidiš da je Claude krenuo pogrešnim smerom, pritisni `Esc` — to ga prekida usred rada i odmah možeš da ga preusmeriš. Čekanje da završi pa ispravljanje je kao da pustiš taksistu da te odveze do pogrešne adrese jer ti je neprijatno da ga prekineš.

❌ Loš pristup (deset minuta ćutanja, pa):

```
Sve ovo što si napravio je pogrešno. Nisam hteo novu stranicu.
Obriši sve i počni ispočetka.
```

✅ Dobar pristup (`Esc` posle prvih redova, pa):

```
Stani — pogrešan smer. Ne treba mi nova stranica za podešavanja,
nego izmena postojeće na /podesavanja. Dodaj sekciju "Notifikacije"
na dno te stranice.
```

Razlika: rani prekid je sačuvao i vreme i kontekst — Claude još pamti zadatak i samo ga preusmeravaš, umesto da čistiš pogrešno urađen posao.

### Pravilo 8: Za odluke traži opcije + preporuku

Kad pitaš "šta je najbolje?", dobiješ jedan odgovor koji ne umeš da preispitaš. Kad tražiš opcije sa preporukom, dobiješ i odluku i razloge — pa kao direktor odlučuješ informisano, bez tehničkog znanja.

❌ Loš prompt:

```
Koja baza podataka je najbolja?
```

✅ Dobar prompt:

```
Treba mi baza za listu čekanja: čuvam email adrese i datum prijave,
očekujem do 10.000 unosa. Daj mi 2-3 opcije sa prednostima i manama
ZA MOJ SLUČAJ, pa preporuči jednu i obrazloži u dve rečenice.
Optimizuj za jednostavnost održavanja — radim sam.
```

Razlika: kontekst + zahtev za opcijama pretvorili su generičan odgovor "zavisi" u odluku skrojenu za tvoju situaciju, koju razumeš i možeš da braniš.

### Pravilo 9: Traži dokaz, a ne tvrdnju

"Trebalo bi da radi" nije dokaz — to je nada. Claude može da pokrene testove, podigne dev server, klikće po aplikaciji u browseru i napravi screenshot. Traži to, kao što od majstora tražiš da pred tobom odvrne slavinu pre nego što platiš.

❌ Loš prompt:

```
Jesi li siguran da forma sada radi?
```

✅ Dobar prompt:

```
Dokaži da forma radi: pokreni `npm test` i pokaži mi izlaz. Zatim
pokreni aplikaciju, popuni formu ispravnim podacima i napravi
screenshot poruke o uspehu. Pa probaj i sa neispravnim emailom i
pokaži screenshot poruke o grešci.
```

Razlika: umesto uveravanja dobio si test izlaz i screenshotove — dokaze koje i sam možeš da pogledaš, bez ijednog reda koda (princip dokaza iz Modula 1).

### Pravilo 10: Svaku ponovljenu ispravku upiši u CLAUDE.md

Claude ne pamti ništa između sesija — osim fajla `CLAUDE.md` i memorije. Ako istu ispravku kucaš drugi put, to nije poruka za razgovor, to je pravilo za `CLAUDE.md`. Najbrži način: počni poruku znakom `#` i Claude napomenu trajno zabeleži.

❌ Loš pristup (treći put ove nedelje):

```
Opet si napisao poruke o greškama na engleskom. Prevedi ih na srpski.
```

✅ Dobar pristup:

```
# Svi tekstovi u interfejsu i sve poruke o greškama pišu se na
srpskom jeziku, latinicom. Nikada na engleskom.
```

Razlika: prva poruka ispravlja jedan slučaj i nestaje sa sesijom, a druga postaje trajno pravilo koje svaka buduća sesija učitava automatski.

### Vežba

Uzmi ovaj namerno loš prompt i provuci ga kroz pravila:

```
Sredi stranicu sa cenama da bude bolja.
```

Ako tvoj projekat nema stranicu sa cenama, primeni isti postupak na bilo koju svoju stranicu — zameni "stranicu sa cenama" onom koju imaš.

1. Otvori projekat i pokreni `claude` (ili desktop aplikaciju).
2. Prepiši prompt tako da ima kriterijum prihvatanja (Pravilo 1): šta tačno znači "bolja"? Npr. "tri paketa jedan pored drugog, srednji istaknut".
3. Dodaj za šta optimizuješ (Pravilo 2) — npr. "optimizuj za jasnoću, posetilac za 5 sekundi mora da vidi razliku između paketa".
4. Dodaj ograničenja (Pravilo 3) — šta ne sme da se menja (cene, tekstovi, ostale stranice).
5. Dodaj referencu (Pravilo 4) — "stil kartica kao na početnoj stranici".
6. Pošalji prompt. Dok Claude radi, drži prst na `Esc` — ako krene pogrešno, prekini i preusmeri (Pravilo 7).
7. Na kraju traži dokaz (Pravilo 9): screenshot stranice na desktopu i na telefonu.
8. Ako si Claude-a morao nešto da ispravljaš, a slutiš da će se ponoviti — upiši pravilo porukom koja počinje sa `#` (Pravilo 10).

Uporedi rezultat sa onim što bi dobio od prvobitnog prompta. Razlika je tvoj napredak.

### Najčešće greške

1. **Roman umesto prompta.** Deset pasusa konteksta u kojima se zadatak izgubi. Rešenje: struktura — jedan red šta, kriterijum gotovog, ograničenja, referenca. Sve preko toga je šum.
2. **Prompt-pregovaranje posle lošeg rezultata.** Pet poruka "ne, mislio sam…" u istoj sesiji puni kontekst pogrešnim pokušajima. Rešenje: posle dva neuspela kruga, `/clear` i nov, bolji prompt iz početka — sa onim što si naučio iz neuspeha.
3. **Kriterijum koji se ne može proveriti.** "Da bude profesionalno" niko ne može da izmeri, ni ti ni Claude. Rešenje: prevedi utisak u nešto vidljivo — "isti razmaci kao na početnoj", "test prolazi", "screenshot pokazuje X".
4. **Pitanje koje već sadrži odgovor.** "Je l' da da je ovo dobro rešenje?" — Claude će se rado složiti. Rešenje: pitaj neutralno — "koje su mane ovog rešenja?" ili traži opcije + preporuku (Pravilo 8).
5. **Ispravljanje umesto zapisivanja.** Istu stilsku primedbu kucaš svake sesije ispočetka. Rešenje: drugi put kad nešto ispravljaš, to je signal za `#` poruku i `CLAUDE.md` (Pravilo 10).

### Kontrolna lista

Pre nego što pošalješ važan prompt, proveri:

- [ ] Postoji kriterijum prihvatanja — znam tačno kako izgleda "gotovo"
- [ ] Rekao sam za šta optimizujem (brzina, jednostavnost, izgled…)
- [ ] Naveo sam šta NE sme da se menja
- [ ] Gde postoji dobar primer u projektu, pokazao sam na njega umesto da opisujem
- [ ] U prompt sam stavio jedan zadatak, ne tri
- [ ] Za velik zadatak tražim plan pre koda; za sitnicu idem direktno
- [ ] Spreman sam da pritisnem `Esc` čim vidim pogrešan smer
- [ ] Za odluke tražim opcije sa preporukom, ne "šta je najbolje"
- [ ] Tražim dokaz (test izlaz, screenshot, log), ne tvrdnju
- [ ] Ponovljene ispravke upisujem u `CLAUDE.md` porukom sa `#`

### Proveri znanje

**1. Zašto je "Gotovo je kada `npm test` prolazi i screenshot pokazuje poruku o uspehu" bolji kriterijum od "da sve radi kako treba"?**

Zato što je proverljiv: i ti i Claude možete objektivno da utvrdite da li je ispunjen. "Radi kako treba" je utisak, a utisak ne može da se izmeri — pa svako od vas dvoje može da ga tumači drugačije.

**2. Claude je krenuo da pravi novu stranicu, a ti si hteo izmenu postojeće. Šta radiš i zašto baš tada?**

Pritisneš `Esc` odmah, čim primetiš pogrešan smer, i u sledećoj poruci ga preusmeriš. Što ranije prekineš, manje pogrešnog posla ima da se čisti, a Claude još drži ceo zadatak u kontekstu pa je preusmeravanje trenutno.

**3. Treći put ove nedelje ispravljaš Claude-a da dugmad piše malim slovima. Šta je pravi potez?**

Pošalješ poruku koja počinje znakom `#` (npr. `# Tekst na dugmadima uvek malim slovima`) — Claude to trajno zabeleži, pa pravilo važi u svim budućim sesijama i više ga ne objašnjavaš.
