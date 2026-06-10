## Poglavlje 7: Email i lifecycle — kanal koji poseduješ

Svaki kanal iz prethodnih poglavlja ima gazdu koji nisi ti. Algoritam ti preko noći može uzeti organski domet, plaćeni kanali poskupljuju iz godine u godinu (Poglavlje 6), a zero-click pretraga jede klikove (Poglavlje 5). Email lista je jedini kanal koji POSEDUJEŠ: niko ti je ne može oduzeti, ne plaćaš zakup pažnje i sam biraš kad i kome šalješ. Po industrijskim procenama (Litmus/DMA), email vraća oko 36$ na svaki uloženi 1$ — najviši ROI među marketinškim kanalima. Ali taj ROI ne dolazi iz generičkog biltena, nego iz mejlova vezanih za ponašanje korisnika.

### Šta ćeš naučiti

- Zašto je email jedini kanal u tvom vlasništvu i šta to praktično znači
- Razliku između lifecycle emaila i newslettera — i zašto okidač po ponašanju pobeđuje okidač po kalendaru
- Kako da sastaviš aktivacionu sekvencu od 5 mejlova vezanu za aha-momenat svog proizvoda
- Tri dodatna lifecycle toka: churn-spasavanje, win-back i trial-istek
- Higijenska pravila koja čuvaju isporučivost i poverenje liste

### Lifecycle pobeđuje newsletter

Newsletter (bilten) šalješ po kalendaru: svima isto, svakog utorka, bez obzira na to gde se korisnik nalazi. Lifecycle email (mejl vezan za fazu životnog ciklusa korisnika) šalješ po ponašanju: registrovao se, zapeo pre aha-momenta, prestao da koristi proizvod, ističe mu trial. Industrijska procena ROI-ja od ~36$ na 1$ (Litmus/DMA) je prosek — lifecycle tokovi su deo koji taj prosek vuče naviše, jer stižu tačno u trenutku kad su relevantni.

| | Newsletter | Lifecycle email |
|---|---|---|
| Okidač | kalendar (utorak, 10h) | ponašanje (registracija, zastoj, pad upotrebe) |
| Publika | svi isto | segment u konkretnoj fazi |
| Sadržaj | novosti, blog | sledeći korak ka vrednosti |
| Cilj | održavanje pažnje | pomeranje metrike (aktivacija, konverzija, retencija) |
| Kad ga praviš | svake nedelje, ručno | jednom, pa radi sam |

Newsletter nije zabranjen — koristan je za brend i memoriju (Poglavlje 8). Ali ako biraš gde ćeš prvo uložiti vreme kao solo osnivač: lifecycle tokovi se naprave jednom i rade godinama; newsletter te svake nedelje čeka prazan.

### Aktivaciona sekvenca: 5 mejlova vezanih za aha-momenat

Aktivaciona (onboarding) sekvenca je niz mejlova posle registracije čiji je jedini posao da korisnika dovede do aha-momenta koji si definisao u Poglavlju 3 — trenutka kad proizvod isporuči prvu stvarnu vrednost. Sve drugo (funkcije, cene, priče) čeka.

Tri principa pre šablona:

1. **Dan 0 = jedan korak.** Mejl dobrodošlice ima JEDAN sledeći korak, ne turu kroz 15 funkcija. Što je kraći put do TTV (time-to-value), to bolja aktivacija — to je mejl-verzija onoga što onboarding radi u proizvodu.
2. **Nudge (podsticaj) samo ako treba.** Mejl koji gura ka aha-momentu šalje se SAMO korisniku kod kog se aha nije desio. Okidač je ponašanje, ne kalendar. Korisniku koji je već stigao do vrednosti taj mejl je šum.
3. **Konverziju traži kad ponašanje pokaže spremnost.** Poziv na plaćanje ide kad korisnik pređe PQL prag (product-qualified lead, detaljno u Poglavlju 3) — ne sedmog dana zato što je sedmi dan.

```
AKTIVACIONA SEKVENCA — ŠABLON (5 mejlova)

MEJL 1 — Dobrodošlica
  Okidač: registracija (odmah, dan 0)
  Svrha:  jedan jedini sledeći korak ka aha-momentu
  Skica:  "Zdravo [ime] — da bi [proizvod] imao smisla, uradi ovo
          jedno: [konkretan korak, npr. 'otpremi prvi video'].
          Traje [X] minuta. [Dugme: Uradi to sada]"
          Bez liste funkcija. Bez 'upoznaj naš tim'.

MEJL 2 — Nudge ka aha-momentu
  Okidač: 48h od registracije I aha-momenat se NIJE desio
          (ako jeste — mejl se preskače)
  Svrha:  ukloniti prepreku, ne podsetiti na postojanje
  Skica:  "Video sam da si se registrovao, a nisi još [korak].
          Najčešći razlog je [prepreka X] — evo kako se rešava
          za 2 minuta: [mini-uputstvo ili 60s video]."

MEJL 3 — Social proof + use-case
  Okidač: aha-momenat se desio ILI dan 4 (šta pre nastupi)
  Svrha:  pokazati šta sledi posle prve vrednosti
  Skica:  "Evo kako [tip korisnika kao ti] koristi [proizvod]
          za [konkretan ishod]: [kratka priča sa brojkom ili
          citatom]. Tvoj sledeći korak: [use-case dubina]."

MEJL 4 — Direktno pitanje (founder ton)
  Okidač: dan 6 I aha-momenat se NIJE desio
  Svrha:  saznati šta je zaustavilo korisnika; svaki odgovor
          je besplatno istraživanje za onboarding
  Skica:  "Kratko pitanje — šta te je zaustavilo? Odgovori
          jednom rečenicom na ovaj mejl, čitam svaki odgovor.
          — [tvoje ime, osnivač]"
          Plain text, bez dizajna, reply-to = tvoj inbox.

MEJL 5 — Poziv na konverziju
  Okidač: PQL signal — ponašanje koje istorijski prethodi
          plaćanju (npr. [N] upotreba ključne funkcije,
          dostignut limit besplatnog plana)
  Svrha:  ponuditi plaćanje u trenutku dokazane vrednosti
  Skica:  "Iskoristio si [konkretna upotreba — broj iz njegovog
          naloga]. Na [plaćeni plan] dobijaš [1-2 stvari direktno
          vezane za njegovu upotrebu]. [Dugme: Pređi na Pro]"
```

Logika preskakanja (mejlovi 2 i 4 se šalju samo bez aha-momenta) je ono što sekvencu čini lifecycle sistemom, a ne drip kampanjom po kalendaru. Svaki ozbiljniji email alat ovo podržava kroz uslovne grane ili event-based okidače — biraj alat koji prima evente iz tvog proizvoda, ne samo datume.

### Ostali lifecycle tokovi (kratko)

| Tok | Okidač | Prvi potez |
|---|---|---|
| Churn-spasavanje | pad upotrebe (npr. aktivan korisnik 14 dana neaktivan) | check-in sa POMOĆI: "vidim da te nema — da li je [čest problem]? evo rešenja" — ne popust odmah |
| Win-back | otkazana pretplata / istekao nalog, 30-60 dana kasnije | šta je novo od kad je otišao + jedan razlog za povratak; tek u drugom mejlu eventualna ponuda |
| Trial-istek | 3 dana pre isteka trial-a | rezime vrednosti iz NJEGOVOG naloga ("obradio si X projekata") + šta gubi istekom + jedan CTA |

❌ Pad upotrebe → automatski mejl "Vrati se, evo 30% popusta!" — učiš korisnike da je odlazak način da dobiju popust, a ne saznaješ zašto odlaze.
✅ Pad upotrebe → "Primetio sam da nisi koristio [proizvod] dve nedelje. Najčešće je razlog [X] — evo kako se rešava. Ako je nešto drugo, odgovori na mejl." Popust je poslednja karta, ne prva.

Za trial tokove drži na umu industrijske raspone iz anketa (OpenView / Lenny's Newsletter): trial bez kartice konvertuje ~8-12%, sa obaveznom karticom 40%+ ali uz drastično manje prijava — trial-istek sekvenca je poluga koja te raspone pomera, pa je meri kao eksperiment (Poglavlje 10).

### Higijena: pravila koja drže listu živom

- **Jedan CTA po mejlu.** Mejl sa tri dugmeta je mejl bez cilja. Ako ne možeš da kažeš koju JEDNU akciju mejl traži, ne šalji ga.
- **Tekst kao da piše čovek čoveku.** Plain text ili minimalan dizajn, prvo lice, kratke rečenice. Mejl koji liči na newsletter se skenira; mejl koji liči na poruku se čita.
- **Lako odjavljivanje.** Vidljiv unsubscribe link u jednom kliku. Korisnik koji ne može da se odjavi klikne "spam" — a to ubija isporučivost ka svima ostalima na listi.
- **Reply-to je pravi inbox.** Odgovori na lifecycle mejlove su najjeftiniji user research koji postoji — ne šalji sa no-reply adrese.
- **Lista se gradi, ne kupuje.** Kupljena lista = spam prijave + uništen domen. Svaka adresa na listi je tu jer se sama prijavila.

### Primena odmah

Napiši svoju aktivacionu sekvencu od 5 mejlova po šablonu iznad. Deliverable: fajl `emails/activation-sequence.md` u svom marketing repou (struktura repoa u Poglavlju 12), gde za svaki mejl piše: okidač (konkretan event iz TVOG proizvoda, vezan za aha-momenat koji si definisao u Poglavlju 3), svrha u jednoj rečenici, subject linija, ceo tekst mejla i jedan CTA. Pravilo provere: za mejlove 2 i 4 mora pisati uslov preskakanja ("ne šalje se ako…"), a za mejl 5 konkretan PQL prag sa brojem. Ako aha-momenat i PQL prag još nemaš definisane — to je signal da se prvo vratiš na Poglavlje 3, ne da pišeš mejlove napamet.

### Najčešće greške

1. **Sekvenca po kalendaru umesto po ponašanju.** "Dan 1, dan 3, dan 7" svima isto — korisnik koji je već aktiviran dobija uputstva za početnike. Rešenje: svaki mejl posle dobrodošlice ima uslov ponašanja (poslat samo ako se X jeste/nije desilo).
2. **Tura kroz 15 funkcija u mejlu dobrodošlice.** Korisnik ne zapamti ništa i ne uradi ništa. Rešenje: dan 0 = jedan korak ka aha-momentu; sve ostalo dolazi kasnije, kad zasluži kontekst.
3. **Popust kao prvi odgovor na pad upotrebe.** Trenira korisnike na popuste i maskira pravi uzrok churna. Rešenje: prvo check-in sa pomoći i pitanjem; popust tek kao poslednji korak win-back toka.
4. **Tri CTA i pet linkova po mejlu.** Klik se raspe, ne meriš ništa. Rešenje: jedan mejl = jedna akcija = jedno dugme; sve ostalo izbaci.
5. **No-reply adresa i sakriven unsubscribe.** Gubiš najjeftiniji feedback kanal i skupljaš spam prijave. Rešenje: reply-to = tvoj inbox, odjava u jednom kliku u futeru.

### Kontrolna lista

- [ ] Email alat prima evente iz proizvoda (event-based okidači, ne samo datumi)
- [ ] Aha-momenat i PQL prag definisani (Poglavlje 3) i prevedeni u konkretne evente
- [ ] Aktivaciona sekvenca od 5 mejlova napisana u `emails/activation-sequence.md`
- [ ] Mejlovi 2 i 4 imaju uslov preskakanja vezan za aha-momenat
- [ ] Mejl 5 ima konkretan PQL okidač sa brojem, ne "dan 7"
- [ ] Svaki mejl ima tačno jedan CTA
- [ ] Reply-to vodi u pravi inbox; unsubscribe vidljiv u jednom kliku
- [ ] Churn-spasavanje tok postavljen: pad upotrebe → pomoć, ne popust
- [ ] Trial-istek mejl koristi podatke iz korisnikovog naloga, ne generički tekst
- [ ] Konverzija svakog toka se meri i ulazi u eksperiment log (Poglavlje 10)
