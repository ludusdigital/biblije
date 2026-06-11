# Claude Code Biblija: Od ideje do digitalnog proizvoda

## Modul 0: Dobrodošlica

Dobro došao. Ako čitaš ovo, verovatno imaš ideju, za aplikaciju, alat, servis, nešto što bi rešilo problem tebi ili tvojim klijentima, ali nemaš programersko znanje da je sam napraviš. Do skoro, tvoje opcije su bile: nauči da programiraš (godine), zaposli programera (skupo), ili odustani (najčešće). Ovaj dokument postoji zato što se pojavila četvrta opcija, i ona menja sve.

### Kome je ovaj dokument namenjen

Pišemo za tebe ako si:

- **Preduzetnik** koji želi da napravi i lansira sopstveni proizvod, bez čekanja na tehničkog suosnivača.
- **Kreativac**, dizajner, pisac, video editor, koji ima viziju alata, ali ne i kod kojim bi je ostvario.
- **Menadžer** koji želi da razume, prototipira i isporučuje digitalna rešenja, umesto da ih samo naručuje.

Jedino što pretpostavljamo jeste da znaš da koristiš računar na nivou svakodnevnog rada: fajlovi, folderi, web pregledač. Ne pretpostavljamo da si ikada otvorio terminal, onaj crni prozor u koji se kucaju komande, niti da znaš šta je kod. Sve ćemo objasniti kad dođe na red, i to jezikom koji ima smisla.

### Obećanje

Na kraju ovog dokumenta umećeš samostalno da:

1. pretvoriš svoju ideju u jasnu specifikaciju proizvoda,
2. izgradiš funkcionalan web proizvod uz Claude Code,
3. proveriš njegov kvalitet i bezbednost,
4. lansiraš ga na internet, na pravu adresu, za prave korisnike,
5. održavaš ga i unapređuješ posle lansiranja.

To nije marketinška fraza. Svaki modul ima vežbu koju odmah izvodiš, i svaki korak ima proverljiv kriterijum: ili radi, ili ne radi. Do kraja kursa imaćeš živ proizvod, ne sertifikat.

### Centralna ideja: ti si direktor

Claude Code je alat kompanije Anthropic dostupan kao terminal aplikacija i desktop aplikacija (Mac i Windows) na tvom računaru, kao web verzija na claude.ai/code, i kao ekstenzija (dodatak) za programerske editore, i koji ume da piše, menja, testira i pokreće kod, kompletne aplikacije, od početka do kraja.

Najkorisniji način da o njemu razmišljaš: **Claude Code je tvoj kompletan razvojni tim.** U njemu sede programer koji piše kod, arhitekta koji bira kako će sistem biti složen, tester koji proverava da li sve radi, i DevOps inženjer, osoba koja se brine da proizvod stigne na internet i tamo ostane živ.

A ko si onda ti? **Ti si direktor proizvoda.** Direktor ne mora da zna da vari čelik da bi vodio fabriku. Direktor mora da zna dve stvari:

1. **ŠTA se pravi**, koji problem rešavamo, za koga, i kako proizvod treba da se ponaša.
2. **KAKO ZNAMO DA JE GOTOVO**, koji je proverljiv kriterijum da je posao završen.

Sve između, **KAKO** se to tehnički izvodi, rešava tvoj tim, dakle Claude. Tvoj posao nije da razumeš svaki red koda, kao što posao direktora nije da razume svaki šraf. Tvoj posao je da postavljaš jasne zahteve, tražiš dokaze i donosiš odluke. Ceo ovaj dokument te uči upravo tome.

Pogledaj razliku između zahteva koji direktor ne bi smeo da potpiše i onog koji bi:

❌ „Napravi mi sajt za moju agenciju."

✅ Ovako izgleda zahtev direktora:

```
Napravi početnu stranicu za moju agenciju za video produkciju.
Sadržaj: naslov, kratak opis usluga, tri reference sa slikama,
kontakt forma (ime, imejl, poruka).
Gotovo je kada: stranica se otvara u pregledaču bez grešaka,
forma odbija prazna polja, i pošalješ mi snimak ekrana kako izgleda
na telefonu i na velikom ekranu.
```

Prvi zahtev prepušta sve odluke slučaju. Drugi definiše ŠTA i KAKO ZNAMO DA JE GOTOVO, i zato dobija upotrebljiv rezultat. Formulu ovakvih zahteva razrađujemo detaljno u Modulu 6 i Modulu 11.

### Šta ćeš naučiti iz celog dokumenta

- Kako Claude Code „razmišlja": šta pamti, šta zaboravlja, i kako da mu daš trajna uputstva.
- Kako da pripremiš računar i projekat tako da svaka izmena bude bezbedna i povratna.
- Kako da od magle u glavi dođeš do specifikacije koju i ti i Claude razumete isto.
- Ritam rada kojim se grade ozbiljni proizvodi: mali zadatak → provera → sledeći zadatak.
- Kako da pustiš Claude-a da radi samostalno, ali pod tvojim ogradama.
- Kako se proverava kvalitet i bezbednost koda koji nisi sam napisao.
- Kako se proizvod lansira, nadgleda i razvija posle lansiranja.

### Kako da koristiš ovaj dokument

Dokument je kurs. Čitaj module **redom**, svaki se oslanja na prethodne. Svaki modul (osim ovog uvodnog) ima istu strukturu: šta ćeš naučiti, gradivo sa primerima promptova koje možeš odmah da iskopiraš, vežbu koju izvodiš na svom računaru, najčešće greške, kontrolnu listu i tri pitanja za proveru znanja.

Najvažniji savet: **ne preskači vežbe.** Čitanje o vožnji ne uči te da voziš. Petnaest minuta vežbe vredi više od sat vremena čitanja.

Mapa kursa:

| Modul | Tema |
|---|---|
| 0 | **Dobrodošlica**: kome je namenjen, mentalni okvir „ti si direktor", tri pravila uspeha |
| 1 | **Mentalni model**: sesije, kontekst, `CLAUDE.md`, princip dokaza i merljivosti |
| 2 | **Priprema okruženja**: terminal, instalacija, prijava, dozvole, prvi razgovor |
| 3 | **Temelji projekta**: git, GitHub, `/init` i `CLAUDE.md`, testovi/lint/build kao merni instrumenti, CI |
| 4 | **Od ideje do specifikacije**: brainstorm koji te izaziva, MVP rezanje, `docs/spec.md` |
| 5 | **Planiranje i arhitektura**: plan mode, tehničke odluke bez tehničkog znanja |
| 6 | **Ritam razvoja**: ciklus po jednoj funkcionalnosti, formula savršenog prompta |
| 7 | **Autonomni rad**: `/goal`, `/loop`, `/schedule`, zaštitne ograde |
| 8 | **Kvalitet i bezbednost**: `/code-review`, `/security-review`, `/simplify`, čitanje nalaza |
| 9 | **Lansiranje**: Vercel, env varijable, domen, kontrolna lista pre lansiranja |
| 10 | **Život posle lansiranja**: monitoring, rutine, backlog, iteracije |
| 11 | **Majstorstvo promptovanja**: 10 pravila sa ❌/✅ primerima |
| 12 | **Ekosistem**: plugin-ovi, skill-ovi, MCP konektori |
| 13 | **Kada stvari krenu naopako**: simptom → dijagnoza → lek |
| Dodaci | Cheat-tabela komandi, šabloni promptova, rečnik pojmova |
| Za predavače | Kako iz dokumenta izvesti kurs: radionice, završni projekat |

Usput ćeš sretati engleske termine koji su standard u ovom poslu, *commit*, *deploy*, *feature*, *backlog*. Zadržavamo ih u originalu jer ćeš ih tako sretati svuda, ali svaki objašnjavamo pri prvom pominjanju, a svi su sakupljeni u rečniku u Dodacima.

### Tri pravila uspeha

Ako iz celog dokumenta poneseš samo tri stvari, neka budu ove. Sve ostalo je razrada.

**Pravilo 1: Merljivost.** Sve što tražiš mora imati proverljiv kriterijum gotovosti. „Napravi da bude lepo" niko ne može da proveri, ni Claude, ni ti. „Forma odbija prazan imejl i prikazuje poruku o grešci" može da se proveri za deset sekundi. Pre nego što pošalješ zahtev, zapitaj se: *kako ću znati da je ovo gotovo?* Ako nemaš odgovor, zahtev nije spreman.

**Pravilo 2: Mali koraci.** Sekvenca malih, verifikovanih zadataka uvek pobeđuje jedan džinovski. „Napravi mi celu aplikaciju" zvuči efikasno, ali kad nešto u toj planini ne radi, ne znaš ni gde da gledaš. Deset malih zadataka, gde posle svakog proveriš rezultat, znači da greška nikad nije dalje od poslednjeg koraka. Ovo je isti princip po kom se gradi kuća: temelj, pa zid, pa krov, i pregled posle svake faze.

**Pravilo 3: Dokaz umesto poverenja.** Kada Claude kaže „gotovo je, sve radi", to je tvrdnja, ne dokaz. Direktor ne potpisuje na reč. Uvek traži dokaz: rezultat testa, snimak ekrana stranice, log (zapis onoga što se zaista dogodilo pri izvršavanju). Claude ume da pokrene aplikaciju, klikće po njoj i napravi snimak ekrana, iskoristi to. Rečenica koju ćeš najčešće dodavati na kraj svojih zahteva glasi:

```
Kad završiš, dokaži mi da radi: pokreni testove i pošalji rezultat,
i napravi snimak ekrana stranice u pregledaču.
```

Ova tri pravila nisu nepoverenje prema alatu, ona su način na koji svaki dobar direktor vodi svaki dobar tim, ljudski ili AI.

Spreman? U Modulu 1 ulazimo u glavu tvog novog tima: šta Claude pamti, šta zaboravlja, i kako da mu središ radno okruženje da te razume iz prve.
