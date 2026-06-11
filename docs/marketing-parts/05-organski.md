## Poglavlje 5: Organski rast u AI eri: budi citiran izvor

### Šta ćeš naučiti

- Zašto stara igra "rangiraj se i čekaj klik" slabi, i koja igra dolazi umesto nje
- AEO/GEO taktike: kako da postaneš izvor koji AI modeli i ljudi citiraju
- Kada programski generisane SEO i dalje radi (Zapier model) i kako da ga primeniš bez spama
- Founder-led marketing i javno građenje proizvoda: šta deliti, a šta ne
- Kako da uhvatiš nevidljive preporuke, najvredniji kanal koji ti analitika ne pokazuje

### Nova realnost: klik umire, citat raste

Prvo brojevi. Otprilike ~60% Google pretraga završava bez ijednog klika na rezultat (SparkToro/Similarweb analize, približno), korisnik dobije odgovor na samoj stranici pretrage. To su tzv. zero-click pretrage. AI Overviews (AI sažeci na vrhu Google rezultata) dodatno obaraju CTR informativnih upita, više studija iz 2024-25 pokazuje značajne padove.

Posledica je strukturna, ne kozmetička: ako ti je plan "napišem blog post, rangiram se, čekam klik", igraš igru čija se nagrada smanjuje. Nova igra glasi: **budi izvor koji AI i ljudi citiraju.** Kada ChatGPT, Perplexity ili AI Overview odgovara na pitanje iz tvoje kategorije, tvoj proizvod treba da bude deo odgovora, čak i kad klik nikad ne stigne.

Drugi pomak: AI je komodifikovao prosečan sadržaj. Tekst koji svako može da generiše za 30 sekundi vredi tačno toliko, nula. Vrednost se seli u distribuciju, brend, originalne podatke i ukus. Generički AI blog bez ugla i podataka platforme i čitaoci ignorišu. Zapamti to pre nego što pomisliš da je rešenje "50 AI tekstova mesečno".

### AEO/GEO: optimizacija za mašine koje odgovaraju

AEO/GEO (answer engine optimization / generative engine optimization) je disciplina pravljenja sadržaja koji AI sistemi mogu da razumeju, izvuku i citiraju. Konkretne poluge:

| Taktika | Šta konkretno radiš | Zašto radi |
|---|---|---|
| Jasne definicije pojmova | Na svakoj ključnoj stranici: pojam + definicija u 1-2 rečenice, odmah ispod naslova | AI modeli izvlače čiste, samostalne definicije |
| Strukturirani podaci | Schema.org oznake (FAQ, Product, HowTo) kao JSON-LD u `<head>` prodajne stranice i stranica dokumentacije; proveri Google Rich Results testom | Mašinski čitljiv kontekst o tome šta si i šta radiš |
| Originalni podaci | Mini-istraživanje koje samo ti imaš (vidi recept ispod) | Magnet za linkove i AI citate, niko drugi nema taj broj |
| Prisustvo na izvorima koje modeli čitaju | Dokumentacija, G2, Reddit, YouTube, uredno, ažurno, sa pravim imenom proizvoda | Modeli uče iz tih izvora; ako te tamo nema, ne postojiš |
| llms.txt | Fajl u root-u sajta koji AI alatima daje sažet, strukturisan pregled proizvoda (primer ispod) | Standard u nastajanju, jeftino za postaviti, postavi ga |

Za llms.txt ti ne treba ništa više od ovoga, običan markdown fajl na adresi `tvojsajt.com/llms.txt`:

```
# [Ime proizvoda]

> [Jedna rečenica: šta proizvod radi i za koga, npr. "Alat koji
> malim timovima automatski pravi izveštaje iz X podataka."]

## Dokumentacija
- [Vodič za početak](https://tvojsajt.com/docs/start): od registracije do prve vrednosti
## Cene
- [Pricing](https://tvojsajt.com/cenovnik): planovi i šta koji uključuje
## Use-case stranice
- [Use case](https://tvojsajt.com/use-case): za koga i koji problem rešava
```

Najjača poluga sa liste su **originalni podaci**. Recept za mini-istraživanje koje SaaS sa 50 korisnika može da napravi za jedan dan:

```
MINI-ISTRAŽIVANJE, recept:
1. Izvuci anonimizovan, agregiran podatak iz svog proizvoda
   (npr. "prosečno trajanje X kod naših korisnika", "najčešći Y po segmentu")
2. Ili anketiraj svoj ICP: 5 pitanja, 30-50 odgovora je dovoljno za ugao
3. Objavi kao stranicu sa: naslov sa brojem, metodologija (2 rečenice),
   1-2 grafikona, jasan zaključak u jednoj rečenici na vrhu
4. Distribuiraj: lični profil osnivača + relevantne zajednice + lista imejl adresa
```

Niko ne može da generiše tvoj podatak, to je jedini sadržaj imun na komodifikaciju.

### Programmatic SEO koji i dalje radi

Programmatic SEO znači automatski generisane stranice za long-tail upite (duge, specifične pretrage sa malo konkurencije). Kanonski primer: Zapier i hiljade stranica tipa "X + Y integracija", jedan od glavnih organskih kanala kompanije (široko citirano).

Model radi i u AI eri, ali samo uz etički test: **svaka stranica mora imati stvarnu vrednost za stvarnog korisnika.**

❌ 2.000 stranica "najbolji [alat] za [grad]" sa istim template tekstom i promenjenim imenom grada, spam koji pretrage i modeli prepoznaju i ignorišu.

✅ Stranica "[tvoj proizvod] + [konkretan alat]" koja sadrži: šta integracija tačno radi, 3 stvarna use-case-a, snimak ekrana podešavanja, ograničenja. Korisna i da Google ne postoji.

Test pre lansiranja: otvori 5 nasumičnih generisanih stranica. Da li bi svaku poslao korisniku kao odgovor na pitanje? Ako ne, ne objavljuj.

### Marketing koji vodi osnivač: lični profil > nalog firme

Algoritmi LinkedIn-a i X-a favorizuju lične profile, profil osnivača nosi domet koji nalozi kompanije nemaju. Za solo osnivača ovo je asimetrična prednost: nemaš marketinški tim, ali imaš nešto što korporacija ne može da kopira, proces iz prve ruke.

Build in public obrazac (graditi javno, primeri: Buffer, levelsio):

| Deli | Ne deli |
|---|---|
| Metrike sa kontekstom (MRR, odlasci kupaca, vidi Poglavlje 1) | Podatke korisnika, čak ni anonimne ako su prepoznatljivi |
| Lekcije iz neuspeha ("probao X, nije radilo, evo zašto") | Hvalisanje bez pouke ("rekordan mesec!") |
| Proces odluka (zašto si izabrao cenu, kanal, funkcionalnost) | Planove koje konkurencija može da pretekne pre tebe |
| Pitanja publici (stvarna, ne angažovanje-bait) | Generičke motivacione objave, to je AI flood u ljudskom obliku |

Format koji se ponavlja, šablon nedeljne objave:

```
[BROJ ili DOGAĐAJ iz ove nedelje]
[Šta sam očekivao vs. šta se desilo]
[Jedna lekcija u jednoj rečenici]
[Pitanje za čitaoce, opciono]
```

Jedan format, jedan kanal, svake nedelje. Doslednost tuče genijalnost, algoritam i publika nagrađuju ritam.

### Nevidljive preporuke i G2 higijena

Nevidljive preporuke = preporuke u kanalima koje analitika ne vidi: privatne Slack/WhatsApp grupe, DM-ovi, usmeno. Veliki deo B2B preporuka dešava se upravo tamo. Tvoja analitika će reći "direktan saobraćaj", a istina je da te je neko preporučio u grupi.

Operativno rešenje, pitanje o izvoru koje korisnik sam popunjava (praksa koju je popularizovao Refine Labs / Chris Walker): obavezno polje pri registraciji.

```
Pitanje u registracija formi (obavezno, slobodan unos):
"Kako si čuo/la za nas?"
```

Slobodan tekst, ne padajući meni, odgovori tipa "neko te pomenuo u Slack grupi za osnivače" vrede zlata i ne staju ni u jednu unapred ponuđenu opciju. Pregledaj odgovore jednom nedeljno; oni će ti pokazati koji kanal stvarno radi.

G2/Capterra higijena: B2B kupci konsultuju peer recenzije pre razgovora sa prodajom. Popunjen profil sa svežim recenzijama je higijena, ne opcija, i dodatno, to su izvori koje AI modeli čitaju (AEO efekat). Minimalan proces: posle svakog aha-momenta (Poglavlje 3) zamoli zadovoljnog korisnika za recenziju; cilj je stalan dotok, ne kampanja jednom godišnje.

```
ŠABLON MOLBE (poruka u aplikaciji ili imejl, odmah posle aha-momenta):
"Vidim da si upravo [konkretan rezultat, npr. poslao prvi izveštaj].
Ako ti je [proizvod] pomogao, recenzija na G2 nam znači više nego
što misliš, traje 3 minuta: [link]. Hvala!"
```

Zajednica kao dugoročnija odbrambena prednost koju konkurencija teško kopira (dbt, Notion, Figma) detaljnije je obrađena u Poglavlju 4.

### Primena odmah

Izaberi **jedan** organski kanal, ne tri, jedan, na osnovu toga gde tvoj ICP (Poglavlje 2) stvarno provodi vreme. Popuni i sačuvaj ovaj plan za narednih 30 dana:

```
ORGANSKI PLAN, 30 DANA
Kanal:           (npr. LinkedIn lični profil / programski generisane stranice / YouTube)
Zašto baš taj:   (gde je moj ICP, jedna rečenica, sa dokazom)
Format:          (npr. nedeljna build-in-public objava po šablonu iznad)
Ritam:           (npr. 2x nedeljno, ponedeljak i četvrtak)
Metrika uspeha:  (jedna! npr. broj registracijaa sa odgovorom "video objavu"
                  u pitanje o izvoru koje korisnik sam popunjava polju)
Datum provere:   (danas + 30 dana)
```

Rezultat rada: popunjen plan + postavljeno "Kako si čuo/la za nas?" polje u registracija formi. Bez tog polja nećeš znati da li plan radi.

### Najčešće greške

1. **Svi kanali odjednom.** Solo osnivač na LinkedIn-u, X-u, YouTube-u i blogu istovremeno = osrednji svuda. Rešenje: jedan kanal, 90 dana, pa tek onda odluka o drugom.
2. **AI flood generičkih tekstova.** Komodifikovan sadržaj ne donosi ništa, ni rang, ni citate, ni poverenje. Rešenje: manje komada, više originalnih podataka i ličnog ugla.
3. **Merenje samo klikova.** Nevidljive preporuke ne ostavlja trag u analitici, pa kanal izgleda "mrtav" iako dovodi najbolje korisnike. Rešenje: pitanje o izvoru koje korisnik sam popunjava polje, pregledano nedeljno.
4. **Objavljivanje sa naloga firme.** Algoritmi favorizuju lične profile; nalog firme bez lica dobija deo dometa. Rešenje: osnivač objavljuje lično, nalog firme deli i pojačava.
5. **Programmatic spam.** Hiljade template stranica bez vrednosti ubijaju kredibilitet celog domena. Rešenje: test "da li bih ovu stranicu poslao korisniku kao odgovor?" pre objave.

### Kontrolna lista

- [ ] Ključni pojmovi moje kategorije imaju jasnu definiciju (1-2 rečenice) na mom sajtu
- [ ] Schema.org strukturirani podaci postavljeni na prodajnoj stranici i stranicama dokumentacije
- [ ] llms.txt fajl postavljen u root sajta
- [ ] Definisano jedno mini-istraživanje sa podatkom koji samo ja imam (rok: ovaj mesec)
- [ ] G2/Capterra profil popunjen + proces za stalan dotok recenzija posle aha-momenta
- [ ] "Kako si čuo/la za nas?" polje (slobodan unos) u registracija formi
- [ ] Izabran JEDAN organski kanal, format i ritam, plan za 30 dana popunjen
- [ ] Lični profil osnivača aktivan sa nedeljnim build-in-public ritmom
- [ ] Ako radim programski generisane SEO: 5 nasumičnih stranica prošlo test stvarne vrednosti
