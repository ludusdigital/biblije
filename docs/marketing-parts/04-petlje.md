## Poglavlje 4: Rast petlje: motor umesto levka

### Šta ćeš naučiti

- Zašto je levak (funnel) linearan trošak koji se prazni, a petlja motor koji se sam hrani
- Kako da AARRR mapom dijagnostikuješ gde ti rast curi pre nego što gradiš bilo šta novo
- Četiri tipa rast petlji, svaki sa studijom slučaja i skicom koraka koju možeš kopirati
- K-faktor formulu i realna očekivanja od viralnosti (spojler: K>1 skoro niko nema)
- Test od jednog pitanja za izbor PRVE petlje za tvoj proizvod

### Prvo dijagnoza: AARRR mapa

Pre nego što juriš novi kanal, utvrdi gde gubiš ljude koje već imaš. Dave McClure-ovi „pirate metrics" AARRR su dijagnostička mapa celog puta korisnika:

| Faza | Pitanje | Primer metrike |
|---|---|---|
| Acquisition | Kako ljudi saznaju za tebe? | posete → registracije |
| Activation | Da li brzo dožive vrednost? | % koji stigne do aha-momenta (Poglavlje 3) |
| Zadržavanje | Da li se vraćaju? | odlasci kupaca, nedeljna aktivnost |
| Preporuka | Da li dovode druge? | pozivnice po korisniku |
| Revenue | Da li plaćaju? | konverzija u plaćeno, MRR |

Pravilo dijagnoze: popravljaj fazu koja najviše curi, počev od dna. petlja preporuka na proizvodu sa lošom retencijom samo brže izbacuje korisnike iz bureta bez dna (detaljno u Poglavlju 3).

### Problem levka: linearan je i troši se

Levak ima jedan smer: sipaš pažnju na vrh (sadržaj, oglasi, lansiranje), deo iscuri na svakom koraku, i sledećeg meseca kreneš od nule. Svaki novi korisnik traži novi ulaz, rast je plaćen svaki put iznova.

Petlja (Reforge koncept) radi drugačije: **izlaz jednog ciklusa je ulaz sledećeg**. Korisnik koji prođe kroz proizvod proizvede nešto, pozivnicu, javni link, šablon, rezultat alata, što dovede sledećeg korisnika. Rast se slaže kao kamata na kamatu: isti mesečni napor daje sve veći rezultat, jer baza koja „vrti" petlju raste.

Postoje četiri tipa petlji koje SaaS realno može da pokrene.

### Tip 1: Viralna / petlja preporuka

**Studija slučaja (široko citirano):** Dropbox program preporuka, obe strane dobiju dodatni skladišni prostor (GB), i onaj ko poziva i onaj ko prihvati. Rast sa ~100.000 na ~4.000.000 korisnika za 15 meseci. Ključ: nagrada je u valuti proizvoda (prostor), pa privlači ljude koji proizvod stvarno žele, a ne lovce na keš.

Formula viralnosti, **K-faktor = broj pozivnica po korisniku × stopa konverzije pozivnice**. Primer računa: ako prosečan korisnik pošalje 2 pozivnice i svaka peta konvertuje, K = 2 × 0,2 = 0,4.

Realna očekivanja: K > 1 (samoodrživ viralni rast) je izuzetno redak. Ali i K od 0,3–0,5 značajno obara efektivni CAC, svaki plaćeni korisnik „besplatno" dovuče još pola korisnika.

```
SKICA: petlja preporuka
1. Korisnik doživi vrednost (aha-momenat)     → metrika: % aktiviranih
2. Proizvod ponudi pozivnicu u pravom trenutku → metrika: % koji pošalje
3. Primalac otvori namensku prodajnu stranicu   → metrika: CTR pozivnice
4. Primalac se registruje (obe strane nagrada) → metrika: konverzija pozivnice
5. Novi korisnik stigne do aha-momenta         → nazad na korak 1
```

### Tip 2: Upotreba kao distribucija

**Istorijski primer (široko citirano):** Hotmail 1996, potpis „P.S. I love you. Get your free e-mail at Hotmail" u svakom poslatom imejlu doveo je ~12 miliona korisnika za ~18 meseci. Sama upotreba proizvoda bila je reklama.

Moderni primeri: Calendly i Loom, svaki poslat link za zakazivanje i svaki podeljen snimak izlažu brend novim ljudima, i to u radnom kontekstu gde primalac ima isti problem. Korisnik ne mora ništa dodatno da uradi: distribucija je nusproizvod posla koji ionako radi.

Mini verzija za tvoj proizvod: **„powered by" bedž** na svemu što korisnik deli ili objavljuje (izveštaj, embed, javna stranica, izvezeni fajl), na besplatnom planu obavezan, na plaćenom opcioni. To je i blagi motiv za upgrade.

### Tip 3: Sadržajna / petlja sadržaja koji prave korisnici (UGC)

**Studije slučaja (široko citirano):** Notion i Figma, korisnici prave šablone i sadržaj zajednice (sadržaj koji prave korisnici (UGC, user-generated content), ne firma), objavljuju ih u galerijama i zajednici, a novi korisnici ih nalaze, registruju se da bi ih koristili, i vremenom naprave svoje. Zajednica postaje odbrambena prednost koju konkurencija ne može lako kopirati.

Uslov da radi: rezultat korisnikovog rada mora biti **koristan nekom drugom** (šablon, konfiguracija, radni tok, unapred podešen obrazac). Tvoj posao je da napraviš mesto za objavljivanje (galerija na sajtu), trenje objavljivanja svedeš na jedan klik i najbolje primerke aktivno promovišeš. Srodna mašina, programski generisane SEO stranice, detaljno u Poglavlju 5.

### Tip 4: Free-tool petlja

**Studija slučaja (široko citirano):** HubSpot Website Grader, besplatan alat koji rešava mali, konkretan problem (oceni mi sajt) i hrani glavni proizvod kao mamac za kontakt, odnosno besplatan sadržaj ili alat zbog kog neko ostavlja imejl. „Marketing kroz besplatan alat": alat se deli i linkuje sam, jer daje trenutnu vrednost bez registracije.

Za tebe kao graditelja ovo je najjeftinija petlja za pokretanje: mali alat (kalkulator, analizator, generator) koji rešava jedan korak problema tvog ICP-a (Poglavlje 2) je vikend projekta vredan posao, a most ka glavnom proizvodu („tvoj rezultat je X, glavni alat rešava i Y") ugrađuješ u sam rezultat.

| Petlja | Kako se širi | Uslov da radi | Glavna metrika |
|---|---|---|---|
| Preporuka | korisnik poziva korisnika | nagrada u valuti proizvoda, dobra zadržavanje korisnika | K-faktor |
| Upotreba = distribucija | proizvodov rezultat nosi brend | rezultat se prirodno deli s drugima | novi korisnici po podeljenom rezultatu |
| Sadržajna / UGC | korisnici prave sadržaj | rezultat koristan drugima + mesto objave | registracije iz galerije/zajednice |
| Free-tool | alat se deli i linkuje | trenutna vrednost bez registracije | korišćenja alata → registracije |

### Kako izabrati PRVU petlju

Ne biraš petlju koja ti se sviđa, nego onu koja **prirodno izvire iz načina na koji se proizvod već koristi**. Test od jednog pitanja:

> Da li rezultat korisnikovog rada u mom proizvodu neko drugi vidi?

- Vidi ga (link, dokument, embed, snimak) → upotreba-kao-distribucija + „powered by" bedž.
- Rezultat je ponovo upotrebljiv (šablon, unapred podešen obrazac, radni tok) → petlja sadržaja koji prave korisnici (UGC).
- Proizvod je bolji kad ga koristi više ljudi zajedno → preporuka.
- Ništa od toga → petlja besplatnog alata, jer jedina ne zavisi od postojećeg ponašanja, dograđuješ je sa strane.

❌ „Dodaćemo program preporuka jer je Dropbox tako porastao", na proizvodu koji se koristi solo i čiji rezultat niko ne vidi.
✅ „Naši korisnici svaki dan šalju klijentima izveštaje iz alata, stavljamo bedž sa linkom u podnožje izveštaja i merimo klikove."

### Primena odmah

Skiciraj jednu petlju za svoj proizvod i sačuvaj je kao `docs/marketing/petlja-01.md` u repozitorijumu. Šablon:

```markdown
# Petlja: [tip] za [proizvod]

Korak 1: [šta se desi]        → metrika: [šta meriš]
Korak 2: [šta se desi]        → metrika: ...
Korak 3: [šta se desi]        → metrika: ...
Korak 4: [novi korisnik ulazi] → nazad na korak 1

Najslabija karika: [korak koji se najverovatnije kida i zašto]
Prvi eksperiment: [najmanja izmena koja testira najslabiju kariku]
Bazna linija: [trenutne vrednosti metrika, pre ikakvih podsticaja]
```

Obavezno: svaki korak ima svoju metriku i događaj u analitici PRE nego što petlju pustiš. Petlja koju ne meriš po koracima je petlja kojoj ne znaš gde puca. Eksperimente nad njom vodi ritmom iz Poglavlja 10.

### Najčešće greške

1. **Preporuke pre zadržavanja korisnika.** Petlja na proizvodu koji curi samo brže razočara više ljudi. Rešenje: prvo aktivacija i zadržavanje korisnika (Poglavlje 3), pa tek onda pozivnice.
2. **Očekivanje K > 1.** Samoodrživa viralnost je izuzetno retka. Rešenje: planiraj petlju kao amortizer CAC-a (K 0,3–0,5 je odličan rezultat), ne kao jedini kanal.
3. **Nagrada u kešu umesto u proizvodu.** Keš privlači lovce na nagrade koji odu posle isplate. Rešenje: nagrada u valuti proizvoda (prostor, krediti, meseci plana), obostrana, Dropbox lekcija.
4. **Petlja bez merenja koraka.** Vidiš samo da „ne radi", ne i gde. Rešenje: događaj za svaki korak skice, pa popravljaj najslabiju kariku, jednu po jednu.
5. **Kopiranje tuđe petlje koja ne izvire iz tvog proizvoda.** Rešenje: test od jednog pitanja iznad, ako rezultat korisnika niko ne vidi, ne forsiraj deljenje, kreni od free-tool petlje.

### Kontrolna lista

- [ ] Prošao sam AARRR mapu i znam koja faza najviše curi
- [ ] Odgovorio sam na test: da li rezultat korisnikovog rada neko drugi vidi?
- [ ] Izabrao sam jedan tip petlje koji prirodno izvire iz upotrebe proizvoda
- [ ] Skicirao sam petlju u `docs/marketing/petlja-01.md` sa metrikom za svaki korak
- [ ] Označio sam najslabiju kariku i definisao prvi eksperiment za nju
- [ ] Svaki korak petlje ima događaj u analitici pre pokretanja
- [ ] Zabeležio sam baznu liniju metrika pre uvođenja podsticaja
- [ ] Ako radim preporuka: nagrada je obostrana i u valuti proizvoda
