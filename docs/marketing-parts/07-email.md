## Poglavlje 7: Imejl i životni ciklus korisnika: kanal koji poseduješ

Svaki kanal iz prethodnih poglavlja ima gazdu koji nisi ti. Algoritam ti preko noći može uzeti organski domet, plaćeni kanali poskupljuju iz godine u godinu (Poglavlje 6), a pretraga bez klika (zero-click) jede klikove (Poglavlje 5). Imejl lista je jedini kanal koji POSEDUJEŠ: niko ti je ne može oduzeti, ne plaćaš zakup pažnje i sam biraš kad i kome šalješ. Po industrijskim procenama (Litmus/DMA), imejl vraća oko 36$ na svaki uloženi 1$, najviši povraćaj ulaganja (ROI) među marketinškim kanalima. Ali taj povraćaj ulaganja ne dolazi iz generičkog biltena, nego iz imejlova vezanih za ponašanje korisnika.

### Šta ćeš naučiti

- Zašto je imejl jedini kanal u tvom vlasništvu i šta to praktično znači
- Razliku između imejlova kroz životni ciklus korisnika i biltena, i zašto okidač po ponašanju pobeđuje okidač po kalendaru
- Kako da sastaviš aktivacionu sekvencu od 5 imejlova vezanu za aha-momenat svog proizvoda
- Tri dodatna toka kroz životni ciklus korisnika: sprečavanje odlazaka kupaca, povratak neaktivnih korisnika i istek probnog perioda
- Higijenska pravila koja čuvaju isporučivost i poverenje liste

### Imejl po ponašanju korisnika pobeđuje bilten

Bilten šalješ po kalendaru: svima isto, svakog utorka, bez obzira na to gde se korisnik nalazi. Imejl kroz životni ciklus korisnika (imejl vezan za fazu životnog ciklusa korisnika) šalješ po ponašanju: registrovao se, zapeo pre aha-momenta, prestao da koristi proizvod, ističe mu probni period. Industrijska procena povraćaja ulaganja od ~36$ na 1$ (Litmus/DMA) je prosek, tokovi kroz životni ciklus korisnika su deo koji taj prosek vuče naviše, jer stižu tačno u trenutku kad su relevantni.

| | Bilten | Imejl kroz životni ciklus korisnika |
|---|---|---|
| Okidač | kalendar (utorak, 10h) | ponašanje (registracija, zastoj, pad upotrebe) |
| Publika | svi isto | segment u konkretnoj fazi |
| Sadržaj | novosti, blog | sledeći korak ka vrednosti |
| Cilj | održavanje pažnje | pomeranje metrike (aktivacija, konverzija, zadržavanje korisnika) |
| Kad ga praviš | svake nedelje, ručno | jednom, pa radi sam |

Bilten nije zabranjen, koristan je za brend i memoriju (Poglavlje 8). Ali ako biraš gde ćeš prvo uložiti vreme kao solo osnivač: tokovi kroz životni ciklus korisnika se naprave jednom i rade godinama; bilten te svake nedelje čeka prazan.

### Aktivaciona sekvenca: 5 imejlova vezanih za aha-momenat

Aktivaciona (uvođenje korisnika) sekvenca je niz imejlova posle registracije čiji je jedini posao da korisnika dovede do aha-momenta koji si definisao u Poglavlju 3, trenutka kad proizvod isporuči prvu stvarnu vrednost. Sve drugo (funkcije, cene, priče) čeka.

Tri principa pre šablona:

1. **Dan 0 = jedan korak.** Imejl dobrodošlice ima JEDAN sledeći korak, ne turu kroz 15 funkcija. Što je kraći put do TTV (time-to-value), to bolja aktivacija, to je imejl-verzija onoga što uvođenje korisnika radi u proizvodu.
2. **Nudge (podsticaj) samo ako treba.** Imejl koji gura ka aha-momentu šalje se SAMO korisniku kod kog se aha nije desio. Okidač je ponašanje, ne kalendar. Korisniku koji je već stigao do vrednosti taj imejl je šum.
3. **Konverziju traži kad ponašanje pokaže spremnost.** Poziv na plaćanje ide kad korisnik pređe PQL prag (product-qualified lead, detaljno u Poglavlju 3), ne sedmog dana zato što je sedmi dan.

```
AKTIVACIONA SEKVENCA, ŠABLON (5 imejlova)

MEJL 1, Dobrodošlica
  Okidač: registracija (odmah, dan 0)
  Svrha:  jedan jedini sledeći korak ka aha-momentu
  Skica:  "Zdravo [ime], da bi [proizvod] imao smisla, uradi ovo
          jedno: [konkretan korak, npr. 'otpremi prvi video'].
          Traje [X] minuta. [Dugme: Uradi to sada]"
          Bez liste funkcija. Bez 'upoznaj naš tim'.

MEJL 2, Nudge ka aha-momentu
  Okidač: 48h od registracije I aha-momenat se NIJE desio
          (ako jeste, imejl se preskače)
  Svrha:  ukloniti prepreku, ne podsetiti na postojanje
  Skica:  "Video sam da si se registrovao, a nisi još [korak].
          Najčešći razlog je [prepreka X], evo kako se rešava
          za 2 minuta: [mini-uputstvo ili 60s video]."

MEJL 3, Društveni dokaz + use-case
  Okidač: aha-momenat se desio ILI dan 4 (šta pre nastupi)
  Svrha:  pokazati šta sledi posle prve vrednosti
  Skica:  "Evo kako [tip korisnika kao ti] koristi [proizvod]
          za [konkretan ishod]: [kratka priča sa brojkom ili
          citatom]. Tvoj sledeći korak: [use-case dubina]."

MEJL 4, Direktno pitanje (ton osnivača)
  Okidač: dan 6 I aha-momenat se NIJE desio
  Svrha:  saznati šta je zaustavilo korisnika; svaki odgovor
          je besplatno istraživanje za uvođenje korisnika
  Skica:  "Kratko pitanje, šta te je zaustavilo? Odgovori
          jednom rečenicom na ovaj imejl, čitam svaki odgovor., [tvoje ime, osnivač]"
          Običan tekst, bez dizajna, reply-to = tvoj inbox.

MEJL 5, Poziv na konverziju
  Okidač: PQL signal, ponašanje koje istorijski prethodi
          plaćanju (npr. [N] upotreba ključne funkcije,
          dostignut limit besplatnog plana)
  Svrha:  ponuditi plaćanje u trenutku dokazane vrednosti
  Skica:  "Iskoristio si [konkretna upotreba, broj iz njegovog
          naloga]. Na [plaćeni plan] dobijaš [1-2 stvari direktno
          vezane za njegovu upotrebu]. [Dugme: Pređi na Pro]"
```

Logika preskakanja (imejlovi 2 i 4 se šalju samo bez aha-momenta) je ono što sekvencu čini sistemom vezanim za životni ciklus korisnika, a ne kap-po-kap kampanjom po kalendaru. Svaki ozbiljniji imejl alat ovo podržava kroz uslovne grane ili zasnovane na događajima okidače, biraj alat koji prima događaje iz tvog proizvoda, ne samo datume.

### Ostali tokovi kroz životni ciklus korisnika (kratko)

| Tok | Okidač | Prvi potez |
|---|---|---|
| Odlasci kupaca-spasavanje | pad upotrebe (npr. aktivan korisnik 14 dana neaktivan) | check-in sa POMOĆI: "vidim da te nema, da li je [čest problem]? evo rešenja", ne popust odmah |
| Povratak neaktivnih korisnika | otkazana pretplata / istekao nalog, 30-60 dana kasnije | šta je novo od kad je otišao + jedan razlog za povratak; tek u drugom imejlu eventualna ponuda |
| Istek probnog perioda | 3 dana pre isteka probnog perioda | rezime vrednosti iz NJEGOVOG naloga ("obradio si X projekata") + šta gubi istekom + jedan poziv na akciju |

❌ Pad upotrebe → automatski imejl "Vrati se, evo 30% popusta!", učiš korisnike da je odlazak način da dobiju popust, a ne saznaješ zašto odlaze.
✅ Pad upotrebe → "Primetio sam da nisi koristio [proizvod] dve nedelje. Najčešće je razlog [X], evo kako se rešava. Ako je nešto drugo, odgovori na imejl." Popust je poslednja karta, ne prva.

Za tokove probnog perioda drži na umu industrijske raspone iz anketa (OpenView / Lenny's Bilten): probni period bez kartice konvertuje ~8-12%, sa obaveznom karticom 40%+ ali uz drastično manje prijava, istek probnog perioda sekvenca je poluga koja te raspone pomera, pa je meri kao eksperiment (Poglavlje 10).

### Higijena: pravila koja drže listu živom

- **Jedan poziv na akciju po imejlu.** Imejl sa tri dugmeta je imejl bez cilja. Ako ne možeš da kažeš koju JEDNU akciju imejl traži, ne šalji ga.
- **Tekst kao da piše čovek čoveku.** Običan tekst ili minimalan dizajn, prvo lice, kratke rečenice. Imejl koji liči na bilten se skenira; imejl koji liči na poruku se čita.
- **Lako odjavljivanje.** Vidljiv unsubscribe link u jednom kliku. Korisnik koji ne može da se odjavi klikne "spam", a to ubija isporučivost ka svima ostalima na listi.
- **Adresa za odgovor vodi u pravo sanduče.** Odgovori na imejlove kroz životni ciklus korisnika su najjeftinije istraživanje korisnika koje postoji, ne šalji sa adrese na koju korisnik ne može da odgovori.
- **Lista se gradi, ne kupuje.** Kupljena lista = spam prijave + uništen domen. Svaka adresa na listi je tu jer se sama prijavila.

### Primena odmah

Napiši svoju aktivacionu sekvencu od 5 imejlova po šablonu iznad. Rezultat rada: fajl `imejlovi/aktivaciona-sekvenca.md` u svom marketinškom repozitorijumu (struktura repozitorijuma u Poglavlju 12), gde za svaki imejl piše: okidač (konkretan događaj iz TVOG proizvoda, vezan za aha-momenat koji si definisao u Poglavlju 3), svrha u jednoj rečenici, naslov imejla, ceo tekst imejla i jedan poziv na akciju. Pravilo provere: za imejlove 2 i 4 mora pisati uslov preskakanja ("ne šalje se ako…"), a za imejl 5 konkretan PQL prag sa brojem. Ako aha-momenat i PQL prag još nemaš definisane, to je signal da se prvo vratiš na Poglavlje 3, ne da pišeš imejlove napamet.

### Najčešće greške

1. **Sekvenca po kalendaru umesto po ponašanju.** "Dan 1, dan 3, dan 7" svima isto, korisnik koji je već aktiviran dobija uputstva za početnike. Rešenje: svaki imejl posle dobrodošlice ima uslov ponašanja (poslat samo ako se X jeste/nije desilo).
2. **Tura kroz 15 funkcija u imejlu dobrodošlice.** Korisnik ne zapamti ništa i ne uradi ništa. Rešenje: dan 0 = jedan korak ka aha-momentu; sve ostalo dolazi kasnije, kad zasluži kontekst.
3. **Popust kao prvi odgovor na pad upotrebe.** Trenira korisnike na popuste i maskira pravi uzrok odlazaka kupaca. Rešenje: prvo check-in sa pomoći i pitanjem; popust tek kao poslednji korak povratak neaktivnih korisnika toka.
4. **Tri poziva na akciju i pet linkova po imejlu.** Klik se raspe, ne meriš ništa. Rešenje: jedan imejl = jedna akcija = jedno dugme; sve ostalo izbaci.
5. **No-reply adresa i sakriven unsubscribe.** Gubiš najjeftiniji povratna informacija kanal i skupljaš spam prijave. Rešenje: reply-to = tvoj inbox, odjava u jednom kliku u futeru.

### Kontrolna lista

- [ ] Imejl alat prima događaje iz proizvoda (zasnovane na događajima okidači, ne samo datumi)
- [ ] Aha-momenat i PQL prag definisani (Poglavlje 3) i prevedeni u konkretne događaje
- [ ] Aktivaciona sekvenca od 5 imejlova napisana u `imejlovi/aktivaciona-sekvenca.md`
- [ ] Imejlovi 2 i 4 imaju uslov preskakanja vezan za aha-momenat
- [ ] Imejl 5 ima konkretan PQL okidač sa brojem, ne "dan 7"
- [ ] Svaki imejl ima tačno jedan poziv na akciju
- [ ] Adresa za odgovore vodi u pravo sanduče; odjava je vidljiva u jednom kliku
- [ ] Odlasci kupaca-spasavanje tok postavljen: pad upotrebe → pomoć, ne popust
- [ ] Imejl o isteku probnog perioda koristi podatke iz korisnikovog naloga, ne generički tekst
- [ ] Konverzija svakog toka se meri i ulazi u dnevnik eksperimenata (Poglavlje 10)
