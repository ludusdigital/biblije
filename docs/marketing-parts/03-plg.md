## Poglavlje 3: Proizvod kao marketing — PLG i aktivacija

Najjeftiniji marketinški kanal koji imaš je onaj koji već gradiš: sam proizvod. PLG (product-led growth) znači da proizvod preuzima posao marketinga i prodaje — korisnik se sam registruje, sam doživi vrednost, sam pozove kolege i sam plati. Slack, Dropbox, Calendly, Notion i Figma su rasli upravo ovako. Za tebe, solo osnivača bez budžeta, ovo je poglavlje sa najvećim povraćajem: svaka izmena ovde je kod koji možeš isporučiti danas, ne kampanja koju moraš platiti.

### Šta ćeš naučiti

- Zašto je aktivacija (drugo A iz AARRR mape) tačka najvećeg uticaja za mali tim
- Kako da nađeš svoj aha-momenat iz podataka, a ne iz mašte
- Kako da izmeriš TTV i skratiš ga sa tri konkretne tehnike
- Kako da izabereš freemium ili free trial na osnovu industrijskih brojki
- Kako da definišeš PQL pravilo koje ponašanje pretvara u signal za naplatu

### Gde PLG udara: aktivacija

Pirate metrics AARRR (Dave McClure) deli put korisnika na pet koraka: Acquisition (kako te nađu), Activation (kako dožive vrednost), Retention (kako ostaju), Referral (kako te preporuče), Revenue (kako plate). Većina osnivača troši energiju na prvo A, a curi im drugo. Aktivacija je trenutak kad se registracija pretvori u korisnika — i sve nizvodno (retencija, preporuke, prihod) zavisi od nje. Growth petlje koje grade na ovome detaljno obrađuje Poglavlje 4; ovde popravljaš motor pre nego što sipaš gorivo.

### Aha-momenat: definiši ga iz podataka

Aha-momenat je akcija (ili prag akcija) posle koje korisnik po pravilu ostaje. Javno poznati primeri: Facebook je rano otkrio da korisnik koji doda 7 prijatelja za 10 dana ostaje; kod Slacka je tim koji pošalje ~2000 poruka praktično zadržan.

Tvoj aha-momenat ne pogađaš — izvodiš ga poređenjem ponašanja:

```
Procedura: nađi svoj aha-momenat (potrebna ti je samo event analitika)

1. Uzmi korisnike registrovane pre 30+ dana i podeli ih u dve grupe:
   ZADRŽANI  = aktivni i danas
   OTIŠLI    = nestali posle prve 1-2 nedelje
2. Za obe grupe izlistaj akcije iz PRVE 2 NEDELJE
   (kreirao projekat, pozvao kolegu, izvezao rezultat, povezao integraciju…)
3. Pitanje: šta su ZADRŽANI uradili rano, a OTIŠLI nisu?
4. Kandidat-akcije pretvori u hipotezu sa pragom i rokom:
   "Korisnik koji [akcija] bar [N puta] u prvih [X dana] ostaje."
5. Proveri na sledećoj kohorti registracija — pa tek onda gradi onboarding oko toga.
```

Bitno: aha-momenat je korelacija koju tretiraš kao hipotezu, ne kao zakon. Testiraš je tako što onboarding gura korisnike ka toj akciji, pa gledaš da li retencija kohorte raste (disciplina eksperimenta — Poglavlje 10).

### TTV: izmeri, pa skraćuj

TTV (time-to-value) je vreme od registracije do prve stvarne vrednosti — što kraće, to bolja aktivacija. Prvo izmeri: timestamp registracije minus timestamp prve aha-akcije, medijana po kohorti. Ako je medijana "nikad" za većinu korisnika, to je tvoj problem broj jedan.

Tri tehnike skraćivanja, redom po snazi:

1. **Manje koraka podešavanja.** Svaki ekran između registracije i vrednosti je mesto odustajanja. Sve što nije neophodno za prvu vrednost — pomeri posle nje.
2. **Demo podaci.** Korisnik ne sme da gleda prazan ekran dok ne unese svoje podatke. Učitaj primer-projekat koji odmah pokazuje šta proizvod radi.
3. **Šabloni umesto praznog platna.** "Počni od nule" je za eksperte; novi korisnik bira između 3-5 gotovih šablona i menja, ne gradi.

❌ Registracija → izbor plana → podešavanje profila → pozovi tim → podesi integracije → prazan dashboard
✅ Registracija → šablon ili demo podaci → prva vrednost za 2 minuta → tek ONDA: "hoćeš da sačuvaš ovo? Podesi nalog."

### Onboarding: vodič, ne tutorijal

Onboarding (uvođenje novog korisnika) ima jedan zadatak: dovesti korisnika do aha-akcije najkraćim putem. Dva obrasca koja rade:

- **Checklist obrazac.** Vidljiva lista od 3-5 koraka sa progresom ("2/5 završeno"), gde je svaki korak akcija ka aha-momentu — ne tura kroz funkcije. Ljudi završavaju započete liste.
- **Empty states kao vodič.** Svaki prazan ekran je prilika: umesto "Nema podataka", piše šta korisnik dobija kad uradi akciju + dugme koje je pokreće odmah tu.

Princip iznad svega: **prva vrednost PRE traženja podešavanja.** Ne traži integracije, ne traži pozivanje tima, ne traži karticu — dok korisnik nije svojim očima video zašto bi se trudio.

### Freemium ili free trial: odluči brojkama

Freemium = besplatan plan zauvek, sa ograničenjima. Free trial = pun proizvod na ograničeno vreme. Industrijski rasponi iz anketa OpenView / Lenny's Newsletter:

| Model | Konverzija u plaćeno | Broj prijava | Kada ima smisla |
|---|---|---|---|
| Freemium | tipično 2-5% | najveći | proizvod sa viralnom/mrežnom komponentom; besplatni korisnici su distribucija (Poglavlje 4) |
| Trial bez kartice | ~8-12% | srednji | vrednost vidljiva za par dana; želiš širok ulaz uz pristojnu konverziju |
| Trial sa karticom | 40%+ | drastično manji | uska, kvalifikovana publika koja zna šta hoće; spreman si da žrtvuješ obim za nameru |

Pravilo izbora: freemium biraj samo ako besplatan korisnik radi marketing za tebe (deli linkove, poziva tim, izlaže brend). Ako besplatni korisnici samo troše tvoje resurse i ne šire proizvod — trial. Cena i pakovanje su posebna, potcenjena poluga (videti ProfitWell nalaz u Poglavlju 1).

### PQL: ponašanje kao signal za naplatu

PQL (product-qualified lead) je potencijalni kupac kvalifikovan ponašanjem u proizvodu, ne formularom. Umesto da pitaš "koliko je velika tvoja firma", gledaš šta su uradili. Primer pravila:

```
PQL pravilo (primer za kolaboracioni SaaS):
  nalog sa 3+ aktivna korisnika
  I 10+ kreiranih dokumenata u prvih 14 dana
  I udario u limit besplatnog plana bar jednom
  → spreman za razgovor o naplati / in-app ponudu nadogradnje

Akcija kad se pravilo okine:
  - in-app poruka sa konkretnim limitom koji su dotakli
  - email osnivača (lifecycle sekvenca — Poglavlje 7)
```

Tvoje PQL pravilo izvedi iz istog poređenja kohorti kao aha-momenat: šta su uradili nalozi koji su platili, pre nego što su platili?

### Retencija: temelj na kome sve stoji

Akvizicija u proizvod koji curi je sipanje vode u bure bez dna. Poboljšanje retencije deluje složeno (compounding) na sve metrike — LTV raste, CAC payback se skraćuje, preporuke se množe. Brzi test temelja je Sean Ellis PMF test: ako bar 40% aktivnih korisnika kaže da bi bili "veoma razočarani" da proizvod nestane, imaš signal product-market fita; ispod toga, popravljaj proizvod i aktivaciju pre nego što skaliraš bilo koji kanal iz Dela II.

### Primena odmah

Napravi fajl `docs/marketing/aktivacija.md` u repou svog proizvoda sa tri stavke:

```
# Aktivacija — [proizvod], [datum]

## 1. Hipoteza aha-momenta
"Korisnik koji [akcija] bar [N puta] u prvih [X dana] ostaje."
Osnova: poređenje zadržanih vs otišlih iz poslednjih 30 dana (procedura iznad).

## 2. Trenutni TTV
Medijana vremena registracija → prva aha-akcija: ___
% korisnika koji NIKAD stignu do aha-akcije: ___

## 3. Jedna izmena onboardinga koja skraćuje TTV
Izmena: (npr. demo podaci umesto praznog ekrana)
Metrika odluke, zapisana UNAPRED: TTV medijana / % aktiviranih kohorte
Rok provere: +14 dana
```

Deliverable: popunjen fajl + isporučena izmena. Ovaj fajl kasnije postaje input za eksperimentalni log (Poglavlje 10) i za rutine marketinškog OS-a (Poglavlje 12).

### Najčešće greške

1. **Aha-momenat izmišljen u glavi, ne izveden iz podataka.** Rešenje: uvek poređenje kohorti zadržani vs otišli; bez analitike događaja nemaš PLG, imaš nadu.
2. **Onboarding kao tura kroz funkcije.** Korisnika ne zanima gde je koje dugme — zanima ga njegov rezultat. Rešenje: svaki korak checkliste vodi ka aha-akciji ili leti napolje.
3. **Traženje podešavanja pre vrednosti.** Integracije, profil, kartica — sve posle prve vrednosti. Rešenje: pregledaj svoj tok registracije i prebroj ekrane pre prve vrednosti; cilj je da ih bude što manje.
4. **Freemium bez distribucione logike.** Besplatan plan koji nikoga ne dovodi je čist trošak. Rešenje: ili besplatni korisnici šire proizvod, ili pređi na trial.
5. **Skaliranje akvizicije preko proizvoda koji curi.** Rešenje: prvo Sean Ellis test i retencione kohorte, pa tek onda budžet i kanali.

### Kontrolna lista

- [ ] Event analitika beleži ključne akcije korisnika (registracija, core akcije, poziv kolege, izvoz)
- [ ] Upoređene kohorte zadržanih i otišlih iz prve 2 nedelje
- [ ] Hipoteza aha-momenta zapisana u formatu "akcija × N × X dana"
- [ ] Izmerena medijana TTV i % korisnika koji nikad stignu do vrednosti
- [ ] Nijedan ekran podešavanja ne stoji pre prve vrednosti
- [ ] Prazan ekran zamenjen demo podacima ili šablonima
- [ ] Onboarding checklist od 3-5 koraka vodi ka aha-akciji
- [ ] Odluka freemium vs trial doneta po tabeli, ne po osećaju
- [ ] PQL pravilo definisano i okida konkretnu akciju (in-app poruka / email)
- [ ] Sean Ellis test poslat aktivnim korisnicima pre ulaganja u kanale rasta
