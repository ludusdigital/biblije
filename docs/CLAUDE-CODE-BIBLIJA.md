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


---

## Modul 1: Mentalni model: kako Claude Code „razmišlja"

Ovo je najvažnije poglavlje u celom dokumentu. Sve ostalo, komande, alati, trikovi, ima smisla tek kada razumeš kako Claude Code funkcioniše iznutra. Dobra vest: ne treba ti nikakvo tehničko znanje. Treba ti samo jedna dobra analogija, i držaćemo se nje do kraja.

### Šta ćeš naučiti

- Centralnu analogiju: Claude kao genijalan saradnik sa ograničenom radnom memorijom
- Šta su sesija, kontekst i tokeni, i zašto kraće sesije daju bolje rezultate
- Čemu služi `CLAUDE.md` i zašto je to najvažniji fajl u tvom projektu
- Princip „ti si direktor": definišeš ŠTA i KADA je gotovo, ne KAKO
- Princip „veruj, ali traži dokaz" i zašto su testovi kompas autonomnog rada

### Genijalan saradnik koji svako jutro počinje ispočetka

Zamisli da si zaposlio saradnika koji je neverovatno sposoban: programira na svim jezicima, dizajnira, piše, istražuje, radi brzo i nikad se ne žali. Ali ima jednu neobičnu osobinu, **svako jutro dolazi na posao bez ijednog sećanja na juče**. Ne pamti šta ste dogovorili, šta je radio, ni zašto.

Jedino što ponese sa sobom jeste **priručnik firme** koji mu ostaviš na stolu. Ako u priručniku piše šta je projekat, kako se pokreće i koja su pravila, on za pet minuta opet zna sve što mu treba. Ako priručnik ne postoji, svako jutro počinje od nule i ponavlja jučerašnje greške.

To je Claude Code. Genijalan, vredan, ali bez trajne memorije između razgovora. Taj priručnik se zove `CLAUDE.md`, vratićemo se na njega za koji minut.

### Sesija: jedan razgovor, jedna radna memorija

**Sesija** je jedan razgovor sa Claude-om, od trenutka kad ga pokreneš do trenutka kad razgovor zatvoriš. Sve što se dogodi unutar sesije (tvoje poruke, fajlovi koje je Claude pročitao, kod koji je napisao, greške koje je video) čini njegov **kontekst**, radnu memoriju tog razgovora.

Ključno je razumeti: kontekst nije beskonačan. To je kao radni sto, prostran, ali ipak sto. Dok je na njemu nekoliko urednih fascikli, saradnik radi sjajno. Kad nagomilaš sto papira iz pet različitih projekata, počinje da gubi nit: zaboravlja šta ste rekli na početku, meša zadatke, pravi greške koje ranije ne bi.

Zato važi praktično pravilo koje ćeš sretati kroz ceo kurs:

> **Kraće, fokusirane sesije daju bolji rezultat od jedne maratonske.** Jedna sesija = jedan zadatak ili jedna tema.

Kad završiš zadatak, ne nastavljaj u istom razgovoru sa potpuno novom temom. Imaš dve komande za higijenu konteksta:

- `/clear`, briše kontekst i počinje svežu sesiju. Koristi kad prelaziš na novi zadatak.
- `/compact`, sažima dugačak razgovor da oslobodi prostor, a zadrži suštinu. Koristi kad si usred posla, a razgovor se odužio.

### Tokeni: jedinica prostora za razmišljanje

Verovatno ćeš negde sresti reč **token**. Najjednostavnije: token je jedinica „prostora za razmišljanje". Svaka tvoja poruka, svaki fajl koji Claude pročita, svaki njegov odgovor, sve to zauzima tokene, kao što papiri zauzimaju mesto na radnom stolu.

Ne moraš da ih brojiš ni da ih razumeš dublje od toga. Dovoljno je da znaš: prostor je ograničen, pa ga ne trošiš na nebitno. To je još jedan razlog za kratke, fokusirane sesije.

### CLAUDE.md: priručnik koji novi član tima pročita prvog dana

Sećaš se priručnika sa početka? `CLAUDE.md` je običan tekstualni fajl u folderu tvog projekta koji Claude **automatski učitava na početku svake sesije**. To i trajna memorija (napomene zabeležene porukom koja počinje sa `#`) jedino su što pouzdano preživljava između razgovora.

Šta u njemu treba da piše? Isto što bi rekao novom članu tima prvog radnog dana:

- Šta je ovaj projekat i kome služi
- Kako se pokreće i kako se proverava da li radi
- Pravila i konvencije („dugmad su uvek plava", „tekstovi su na srpskom")
- Odluke koje ste već doneli, da ih ne preispituje svaki put

Ne moraš da ga pišeš ručno, komanda `/init` generiše `CLAUDE.md` analizom tvog projekta (detaljno u Modulu 3). A kad usred rada zaključiš nešto što želiš da Claude trajno zapamti, samo počni poruku znakom tastera `#`:

```
# Svi tekstovi u aplikaciji su na srpskom, latinica. Nikad ćirilica, nikad engleski.
```

Claude tu napomenu trajno beleži, pa je zna i u svim budućim sesijama.

### Ti si direktor: definiši ŠTA, ne KAKO

Dobar direktor ne stoji programeru iza leđa i ne diktira mu svaki red koda, niti bi umeo. Dobar direktor kaže **šta** treba da se napravi i **po čemu će se znati da je gotovo**. To je tvoja uloga.

❌ Loš prompt (mikromenadžment nečega što ne razumeš):

```
Napravi React komponentu sa useState hookom (React mehanizmom za pamćenje stanja) koja preko fetch API-ja
poziva endpoint i renderuje listu.
```

✅ Dobar prompt (jasan cilj + kriterijum gotovosti):

```
Korisnik treba da vidi listu svojih prethodnih porudžbina, od najnovije
ka najstarijoj. Gotovo je kada: (1) lista se prikazuje na stranici
"Moje porudžbine", (2) ako porudžbina nema, piše "Još nemaš porudžbina",
(3) pokažeš mi snimak ekrana obe situacije.
```

Primeti šta se desilo: nisi rekao nijednu tehničku reč, a zadatak je precizniji nego u prvom primeru. Kriterijum gotovosti, „po čemu ću znati da je završeno", najmoćniji je alat netehničkog direktora. Formulu savršenog prompta razrađujemo detaljno u Modulu 6.

### Veruj, ali traži dokaz

Claude je vredan saradnik, ali kao i svaki saradnik, ume da kaže „gotovo je, radi" a da nije baš proverio. Zato uvedi gvozdeno pravilo: **tvrdnja bez dokaza se ne računa**.

Dokaz je nešto što možeš da vidiš svojim očima:

- **rezultat testa** (npr. ispis da je svih 12 testova prošlo),
- **snimak ekrana** ekrana na kom se vidi da funkcija radi,
- **log**, ispis programa koji pokazuje šta se stvarno dogodilo.

Claude Code može sam da pokrene tvoju aplikaciju i proveri je u pregledaču: da klikće, popunjava forme i napravi snimak ekrana. Iskoristi to, umesto „jesi li siguran da radi?", traži:

```
Pokreni aplikaciju, prođi kroz prijavu kao novi korisnik i pokaži mi
snimak ekrana ekrana posle uspešne prijave. Zatim pokreni testove i
pokaži mi ispis.
```

### Testovi: kompas autonomnog rada

**Test** je mali automatski program koji proverava da li tvoja aplikacija radi ispravno, kao kontrolor kvaliteta koji svaki proizvod pregleda po istoj listi, svaki put, za par sekundi.

Zašto su testovi toliko važni baš tebi, koji kod ne čitaš? Zato što bez njih **Claude sam sebi sudi**. Napiše kod, pogleda ga i kaže „izgleda dobro", a ti nemaš način da proveriš. Sa testovima postoji objektivan, merljiv sudija: testovi ili prolaze ili ne prolaze, i to vidiš crno na belo.

To postaje presudno kad Claude radi autonomno, bez tebe (Modul 7): testovi su kompas po kom se ravna i merilo po kom staje. Bez kompasa, autonoman rad je lutanje. Kako da dobiješ testove a da ih ne pišeš sam, u Modulu 3.

### Vežba

Proveri novi mentalni model na delu, korak po korak:

1. Otvori Claude Code u bilo kom folderu (i prazan je u redu).
2. Napiši mu: `Zapamti za ovaj razgovor: moja omiljena boja je tirkizna.`
3. Postavi par nevezanih pitanja, pa pitaj: `Koja je moja omiljena boja?`, znaće, jer je to ista sesija.
4. Ukucaj `/clear`, pa ponovo pitaj za omiljenu boju. Neće znati, kontekst je obrisan. Upravo si video granicu radne memorije.
5. Sada napiši: `# Moja omiljena boja je tirkizna.`, pa opet `/clear` i pitaj. Ovog puta zna, jer si upisao u trajnu memoriju.
6. Za kraj, formuliši jedan zadatak iz svog posla po formuli: šta treba da se desi + tri kriterijuma gotovosti + koji dokaz tražiš. Sačuvaj ga, koristićeš ga u Modulu 6.

### Najčešće greške

1. **Maratonska sesija za pet različitih tema.** Rezultat: Claude meša zadatke i „zaboravlja" dogovore s početka. Rešenje: jedan zadatak = jedna sesija; između zadataka `/clear`, usred dugog zadatka `/compact`.
2. **Očekivanje da Claude pamti jučerašnji razgovor.** Ne pamti, to nije kvar, tako radi. Rešenje: sve trajno važno ide u `CLAUDE.md` ili u poruku koja počinje sa `#`.
3. **Mikromenadžovanje tehničkih detalja.** Diktiraš „kako" iz polovičnog znanja i vezuješ Claude-u ruke. Rešenje: definiši šta i kriterijum gotovosti, a izbor alata prepusti njemu.
4. **Prihvatanje „gotovo je" bez dokaza.** Rešenje: uvek traži test, snimak ekrana ili log. Bez dokaza, posao nije završen.
5. **Prepun `CLAUDE.md` sa svim i svačim.** Priručnik od 200 strana niko ne čita, i troši dragocene tokene u svakoj sesiji. Rešenje: samo ono što novi član tima zaista mora da zna prvog dana.

### Kontrolna lista

- [ ] Umem svojim rečima da objasnim analogiju „genijalan saradnik bez trajne memorije"
- [ ] Znam šta su sesija, kontekst i tokeni i zašto kraće sesije rade bolje
- [ ] Znam kada koristim `/clear`, a kada `/compact`
- [ ] Znam čemu služi `CLAUDE.md` i kako sa `#` trajno zabeležim napomenu
- [ ] Moji zadaci imaju kriterijum gotovosti, a ne tehnička uputstva
- [ ] Ne prihvatam „gotovo je" bez testa, snimka ekrana ili loga

### Proveri znanje

**1. Zašto Claude na početku nove sesije ne zna ništa o jučerašnjem dogovoru, i šta je jedini pouzdan način da to „preživi"?**

Claude nema trajnu memoriju između sesija, svaki razgovor počinje od nule. Preživljava samo ono što je zapisano: `CLAUDE.md` (učitava se na početku svake sesije) i napomene zabeležene porukom koja počinje sa `#`.

**2. Koja je razlika između `/clear` i `/compact`?**

`/clear` briše ceo kontekst i počinje svežu sesiju, koristi se pri prelasku na novi zadatak. `/compact` sažima dosadašnji razgovor da oslobodi prostor, ali zadržava suštinu, koristi se usred dugog zadatka.

**3. Zašto su testovi posebno važni kada Claude radi autonomno?**

Bez testova Claude sam ocenjuje sopstveni rad („izgleda dobro"), a ti to ne možeš da proveriš. Testovi daju objektivan, merljiv kriterijum, prolaze ili ne prolaze, pa autonoman rad dobija kompas i jasan uslov završetka.


---

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


---

## Modul 3: Temelji projekta: git, CLAUDE.md i merni instrumenti

U Modulu 2 si pripremio okruženje i vodio prvi razgovor sa Claude-om. Pre nego što počneš da gradiš proizvod, treba ti tri stvari koje grade svaki ozbiljan projekat: vremenska mašina (git), zajednička memorija (`CLAUDE.md`) i kontrolna tabla (testovi, lint i build). Bez njih radiš naslepo, sa njima možeš da letiš.

### Šta ćeš naučiti

- Zašto sa git-om ništa ne može da se nepovratno pokvari, i kako te to oslobađa straha
- Kako da koristiš git i GitHub prirodnim jezikom, bez učenja ijedne git komande
- Šta je `/init`, šta `CLAUDE.md` treba da sadrži i kako da ga održavaš
- Zašto PRVO tražiš merne instrumente (testovi, lint, build), pre prve funkcionalnosti
- Šta je CI i zašto želiš automatsku kontrolu svake izmene

### Git: vremenska mašina za tvoj projekat

Git je alat koji pravi snimke stanja celog projekta. Svaki snimak se zove **commit**, fotografija svih fajlova u jednom trenutku, sa kratkim opisom šta se promenilo. Projekat sa git-om je dokument sa beskonačnim "Undo" dugmetom: u svakom trenutku možeš da se vratiš na bilo koji raniji snimak.

Ovo je najvažnija psihološka činjenica celog kursa: **dok god redovno praviš commit-e, ništa ne može da se nepovratno pokvari.** Claude je obrisao pola koda? Vratiš se na jučerašnji snimak. Nova funkcionalnost je sve polomila? Vratiš se na stanje od pre sat vremena. Strah od "šta ako nešto upropastim" nestaje, a bez njega ćeš se usuditi da eksperimentišeš.

**GitHub** je nešto drugo, mada povezano: sef u oblaku. Git čuva snimke na tvom računaru; GitHub čuva njihovu kopiju na internetu. Mesto gde GitHub čuva tvoj projekat zove se **repozitorijum** (skraćeno: repozitorijum), jedan projekat = jedan repozitorijum. Ako ti laptop padne u kadu, projekat je bezbedan. GitHub je kasnije i mesto odakle se aplikacija lansira (Modul 9) i gde rade automatske provere (CI, na kraju ovog modula).

### Ne moraš da naučiš git komande

Ovo je deo koji laici najčešće ne veruju: **nikada ne moraš da ukucaš nijednu git komandu.** Claude ih zna sve. Ti samo kažeš šta hoćeš, prirodnim jezikom:

```
Napravi commit sa svim trenutnim izmenama. Opiši u poruci šta smo uradili.
```

```
Vrati projekat na stanje od pre sat vremena. Nešto smo pokvarili
i hoću da krenemo ispočetka od poslednje verzije koja je radila.
```

```
Napravi mi GitHub repozitorijum za ovaj projekat i pošalji sve commit-e tamo.
```

Tvoja jedina disciplina je **navika**: commit svaki put kad bi te zabolelo da izgubiš ono što je upravo urađeno. Da te Claude na to podseća, upiši pravilo u trajnu memoriju porukom koja počinje sa `#`:

```
# Posle svake završene i proverene funkcionalnosti predloži commit sa jasnom porukom.
```

### /init i CLAUDE.md: memorija projekta

Iz Modula 1 znaš da Claude između sesija ne pamti ništa, osim fajla `CLAUDE.md`, koji se učitava na početku svake sesije. To je pisana memorija projekta: svaki novi razgovor počinje kao novi zaposleni koji je prvo pročitao priručnik firme.

Komanda `/init` generiše početni `CLAUDE.md` analizom projekta, pokreni je čim projekat dobije prve fajlove. Ali generisani fajl je samo početak; najvredniji deo dodaješ ti. Dobar `CLAUDE.md` sadrži:

- **Opis proizvoda**: šta aplikacija radi i za koga, u dve-tri rečenice
- **Ključne odluke**: "koristimo X za bazu", "interfejs je na srpskom", "ciljamo mobilne korisnike"
- **Konvencije**: kako se šta imenuje, gde šta stoji, šta je zabranjeno
- **Komande**: kako se pokreću testovi, lint, build, dev server

Održavanje je jednostavno: kad god u razgovoru donesete važnu odluku, reci:

```
Ovo je važna odluka za ceo projekat. Zabeleži u CLAUDE.md da sva plaćanja
idu preko Stripe-a i da cene uvek prikazujemo u dinarima.
```

Loš `CLAUDE.md` je onaj u koji niko ništa ne upisuje, posle mesec dana Claude radi po pravilima koja više ne važe. Tretiraj ga kao živ dokument, ne kao formalnost.

### Merni instrumenti: kontrolna tabla tvog aviona

Sada najvažniji deo modula. Pilot bez instrumenata ne zna ni visinu, ni brzinu, ni da li motor gori, leti naslepo. Ti si u istoj poziciji: ne čitaš kod, pa ne možeš pogledom da proceniš da li nešto radi. Trebaju ti instrumenti koji mere umesto tebe:

- **Testovi**, mali automatski programi koji proveravaju da aplikacija radi ono što treba ("kad korisnik unese pogrešnu lozinku, prikaže se greška"). Jedna komanda, jasan rezultat: prošlo ili palo.
- **Lint**, automatski kontrolor stila i čestih grešaka u kodu; hvata probleme pre nego što postanu bagovi.
- **Build**, proba "sklapanja" cele aplikacije u oblik spreman za objavljivanje. Ako build pukne, lansiranja nema.

Zato instrumente tražiš **PRVO, pre prve funkcionalnosti**: bez njih je svaka Claude-ova tvrdnja "gotovo je, radi" samo tvrdnja; sa njima imaš dokaz, princip iz Modula 1 na delu. A autonomni rad iz Modula 7 (`/goal`, `/loop`) bukvalno zavisi od njih: autonomiji daješ uslov tipa "radi dok svi testovi ne prolaze", što je moguće samo ako testovi postoje. Bez instrumenata nema autopilota.

Evo tačnog prompta, iskopiraj ga čim projekat postoji:

```
Pre nego što napravimo bilo koju funkcionalnost, podesi merne instrumente projekta:

1. Testove, okvir za automatske testove i bar jedan primer testa koji prolazi.
2. Lint, automatsku proveru stila i čestih grešaka.
3. Build, proveru da se cela aplikacija uspešno sklapa.

Sve tri provere moraju da se pokreću jednom jednostavnom komandom.
Upiši te komande u CLAUDE.md. Na kraju mi pokaži izlaz sve tri komande
kao dokaz da prolaze, i objasni mi jednostavnim jezikom šta koja proverava.
```

Od tog trenutka tvoj refren posle svake izmene glasi: "pokreni testove, lint i build i pokaži mi rezultat." Zelena tabla = letimo dalje. Crvena lampica = popravljamo pre nego što nastavimo.

### CI: kontrolor koji nikad ne spava

Poslednji temelj je **CI** (continuous integration, "neprekidna provera"): automatika na GitHub-u koja pokreće tvoje instrumente pri svakoj izmeni koja stigne u repozitorijum. Radi se preko **GitHub Actions**, automatizacije vezane za tvoj repozitorijum, koja može npr. da pregleda svaki PR (pull request, formalni predlog izmena koji čeka pregled pre nego što uđe u glavnu verziju koda) ili pokrene sve provere bez tvog angažovanja.

Instrumenti u avionu su tu dok ti letiš; CI je kontrola letenja na zemlji koja proverava svaki let, čak i dok spavaš. Ako neka izmena polomi testove, CI je obeleži crvenim pre nego što se približi produkciji.

```
Podesi GitHub Actions za ovaj repozitorijum tako da se pri svakoj izmeni
automatski pokreću testovi, lint i build. Ako bilo šta padne, izmena mora
biti jasno označena kao neispravna. Objasni mi gde na GitHub-u vidim rezultate.
```

Time je krug zatvoren: git čuva prošlost, `CLAUDE.md` čuva znanje, instrumenti mere sadašnjost, a CI stražari nad budućnošću.

### Vežba

Uradi ovo na projektu iz Modula 2 (ili napravi prazan folder za probu):

1. Otvori Claude Code u folderu projekta i reci: `Postavi git za ovaj projekat i napravi prvi commit. Objasni mi šta si uradio.`
2. Pokreni `/init` da dobiješ početni `CLAUDE.md`, pa dodaj svojim rečima opis proizvoda i bar jednu ključnu odluku (zamoli Claude-a da to upiše).
3. Iskopiraj prompt za merne instrumente iz ovog modula i pošalji ga. Ne prihvataj "gotovo je", traži izlaz sve tri komande kao dokaz.
4. Reci: `Napravi GitHub repozitorijum i pošalji projekat tamo.` (Ako nemaš GitHub nalog, prvo ga napravi besplatno na github.com, obična registracija imejlom. Ako te pri prvom slanju zatraži povezivanje naloga, samo prati uputstva na ekranu.) Otvori link u pregledaču i uveri se da fajlovi stoje u sefu.
5. Za kraj, zatraži podešavanje GitHub Actions promptom iz prethodne sekcije, pa napravi sitnu izmenu i gledaj kako kontrolor radi svoj posao.

### Najčešće greške

1. **Odlaganje commit-a "dok ne bude savršeno".** Onda nešto pukne i nemaš snimak za povratak. Rešenje: commit posle svake celine koja radi, makar bila sitna.
2. **Preskakanje instrumenata jer "prvo hoću da vidim aplikaciju".** Bez instrumenata svaki sledeći korak gradi na nečemu što ne umeš da proveriš. Rešenje: prompt za instrumente ide pre prve funkcionalnosti, bez izuzetka.
3. **CLAUDE.md kao mrtvo slovo.** Generišeš ga jednom i nikad ne pipneš; posle dve nedelje laže. Rešenje: svaku važnu odluku odmah diktiraj u njega, ili je zabeleži porukom koja počinje sa `#`.
4. **Verovanje na reč umesto traženja dokaza.** "Sve provere prolaze" nije dokaz, izlaz komande jeste. Rešenje: uvek traži da ti Claude pokaže rezultat testova, linta i builda.
5. **Mešanje git-a i GitHub-a.** Misliš da je projekat "u oblaku" iako commit-i postoje samo lokalno. Rešenje: posle važnijih commit-a traži i slanje na GitHub ("pošalji izmene na GitHub").

### Kontrolna lista

- [ ] Projekat ima git i bar jedan commit
- [ ] Postoji GitHub repozitorijum i poslednje stanje je poslato u njega
- [ ] `/init` je pokrenut i `CLAUDE.md` postoji
- [ ] U `CLAUDE.md` su opis proizvoda, ključne odluke, konvencije i komande
- [ ] Testovi, lint i build postoje i sve tri provere prolaze (video si izlaz svojim očima)
- [ ] Komande za provere su upisane u `CLAUDE.md`
- [ ] GitHub Actions automatski pokreće provere pri svakoj izmeni
- [ ] Zabeležio si naviku (npr. porukom sa `#`) da se commit predlaže posle svake celine

### Proveri znanje

**1. Claude je upravo polomio funkcionalnost koja je juče radila. Šta tražiš?**
Da vrati projekat na poslednji commit u kom je sve radilo, prirodnim jezikom, npr. "vrati projekat na jučerašnje stanje". Zato commit-uješ često: vremenska mašina vredi onoliko koliko ima snimaka.

**2. Zašto se merni instrumenti podešavaju pre prve funkcionalnosti, a ne posle?**
Jer bez njih nemaš način da proveriš nijednu izmenu, gradio bi sprat po sprat bez ikakvog merenja temelja. Uz to, autonomni rad iz Modula 7 zahteva merljive uslove ("testovi prolaze"), koji bez instrumenata ne postoje.

**3. U čemu je razlika između provera koje pokrećeš u sesiji i CI-ja?**
Provere u sesiji pokrećeš ti (ili Claude na tvoj zahtev), dok radiš. CI (GitHub Actions) ih pokreće automatski pri svakoj izmeni u repozitorijumu, i kad ne gledaš. Prvo je instrument-tabla u kokpitu, drugo kontrola letenja koja proverava svaki let.


---

## Modul 4: Od ideje do specifikacije

Najskuplja greška u pravljenju digitalnog proizvoda nije bag u kodu. Najskuplja greška je savršeno izgraditi pogrešnu stvar. Možeš imati besprekoran kod, prelep dizajn i brz sajt, ako rešava problem koji niko nema, potrošio si mesece ni na šta. Zato pre prvog reda koda dolazi nešto mnogo važnije: razgovor sa samim sobom o tome šta zapravo praviš. A Claude je, kada ga pravilno usmeriš, odličan sagovornik za taj razgovor.

### Šta ćeš naučiti

- Kako da nateraš Claude-a da tvoju ideju napadne, a ne da ti tapše po ramenu
- Kako da definišeš problem, ciljnu grupu i ključnu vrednost u jednoj rečenici
- Šta je MVP i kako da nemilosrdno isečeš sve što nije neophodno za prvu verziju
- Kako da napišeš `docs/spec.md`, dokument koji postaje ustav tvog projekta
- Kako da spec koristiš kao trajnu referencu u svakoj budućoj sesiji

### Zašto moraš da tražiš kritiku (i zašto je nećeš dobiti besplatno)

Claude je sam od sebe uslužan. Ako mu kažeš "imam ideju za aplikaciju koja povezuje vlasnike pasa sa šetačima", on će ti vratiti entuzijastičan odgovor, listu funkcionalnosti i predlog kako da počneš. To prija, i to je zamka. Dobio si navijača, a tebi treba đavolji advokat.

Kritiku moraš eksplicitno da tražiš. Kao kada prijatelja pitaš "kako ti se čini moj poslovni plan?", dobićeš "super zvuči!". Ali ako pitaš "šta je najslabija tačka ovog plana i zašto bi propao?", dobićeš odgovor koji vredi. Isto važi za Claude-a.

Evo prompta koji možeš da iskopiraš i prilagodiš:

```
Imam ideju za proizvod: [opiši ideju u 2-3 rečenice].

Nemoj da me hvališ i nemoj da budeš ljubazan. Ponašaj se kao
iskusan investitor koji je video stotine propalih projekata:

1. Postavi mi 10 najtežih pitanja o ovoj ideji.
2. Reci mi šta je najrizičnije, gde će najverovatnije pući.
3. Reci mi šta bi izbacio iz prve verzije i zašto.
4. Reci mi ko već rešava ovaj problem i zašto bi neko prešao kod mene.

Budi direktan. Više mi vredi neprijatna istina sada nego
propao projekat za šest meseci.
```

Odgovori na tih deset pitanja, pisano, ozbiljno. Ako na tri pitanja nemaš odgovor, nisi spreman da gradiš. To nije poraz; to je jeftino otkriće. Upravo si uštedeo mesece.

Ako koristiš plugin-ove (detaljno u Modulu 12), `product-management` plugin ima skill `brainstorm` koji vodi ovakav razgovor strukturirano. Ali i običan prompt iznad radi posao.

### Tri rečenice koje moraš da znaš napamet

Pre nego što napišeš spec, moraš da umeš da odgovoriš na tri pitanja, svako u jednoj rečenici:

1. **Problem**: Šta tačno boli koga? ("Frilenseri gube sate mesečno na ručno pisanje faktura.")
2. **Ciljna grupa**: Ko je taj kome je dovoljno hitno da plati ili promeni naviku? ("Frilenseri u Srbiji koji izdaju 5-20 faktura mesečno.")
3. **Ključna vrednost**: Zašto baš tvoje rešenje, u jednoj rečenici koju razume tvoja tetka? ("Faktura gotova za 30 sekundi, automatski u skladu sa domaćim propisima.")

Ako ne umeš da ih izgovoriš bez "i još...", "a takođe...", "pa zavisi...", ideja još nije sazrela. Vrati se na brainstorm.

### MVP: prvo skejtbord, ne polu-automobil

MVP (Minimum Viable Product, najmanji upotrebljiv proizvod) je prva verzija koja rešava srž problema, i ništa više. Klasična analogija: ako praviš prevozno sredstvo, MVP nije šasija automobila bez točkova, to je polu-automobil koji ne vozi i nikome ne koristi. MVP je skejtbord: ružan, jednostavan, ali te već danas preveze od tačke A do tačke B. Sledeća verzija je trotinet, pa bicikl, pa tek onda auto. U svakom koraku korisnik dobija nešto što radi.

Za rezanje MVP-a iskoristi Claude-a kao nemilosrdnog urednika:

```
Evo liste svih funkcionalnosti koje zamišljam: [nalepi listu].

Za svaku stavku odgovori: da li korisnik može da dobije osnovnu
vrednost proizvoda BEZ nje? Ako može, predloži da je izbacimo
iz prve verzije. Cilj je da prva verzija ima najviše 3 ključne
funkcionalnosti. Budi brutalan.
```

Pravilo palca: ako prvu verziju ne možeš da opišeš u jednoj rečenici i ne vidiš je gotovu za par nedelja rada, još uvek nisi dovoljno sekao.

### Pisanje `docs/spec.md`: ustav tvog projekta

Sada sve to pretačeš u jedan fajl: `docs/spec.md` (folder `docs` u tvom projektu, fajl u Markdown formatu, običan tekst sa naslovima, isti format kao `CLAUDE.md` iz Modula 3). Ovo je dokument kome se i ti i Claude vraćate kad god se pojavi dilema "a da dodamo i ovo?".

Struktura koja se pokazala dobrom:

```
# Specifikacija: [ime proizvoda]

## Problem
Jedna do tri rečenice: šta boli, koga i koliko.

## Korisnik
Ko je ciljna grupa. Konkretno: "frilenseri u Srbiji koji...",
ne "svi koji žele...".

## Ključna vrednost
Jedna rečenica koju razume laik.

## Funkcionalnosti
### Mora (MVP)
- [funkcionalnost 1, jedna rečenica šta korisnik može da uradi]
- [funkcionalnost 2]
- [funkcionalnost 3]

### Trebalo bi (verzija 2)
- [stvari koje su važne, ali ne za prvi dan]

### Kasnije (možda nikad)
- [ideje koje su zanimljive, ali ih svesno odlažeš]

## Šta NIJE u MVP-u
Eksplicitna lista. Npr: "Nema mobilne aplikacije. Nema više
jezika. Nema timskih naloga."

## Kriterijumi uspeha
Merljivo: "Korisnik kreira prvu fakturu za manje od 60 sekundi."
"10 ljudi koristi proizvod nedeljno mesec dana posle lansiranja."
```

Sekcija "Šta NIJE u MVP-u" je možda i najvrednija. Ona štiti od tebe samog, od trenutka u tri ujutru kad pomisliš "a da ubacim i čet?". Piše crno na belo: ne, ne sada.

Ne moraš spec da pišeš sam. Daj Claude-u beleške sa brainstorma i zatraži da ti sastavi prvi nacrt po ovoj strukturi, pa ga ti doteraj. Ti si urednik i potpisnik, Claude je pisar.

### Spec kao trajna referenca

Setimo se Modula 1: Claude ne pamti ništa između sesija (osim `CLAUDE.md` i memorije). Tvoj spec je način da svaka nova sesija počne sa istim razumevanjem proizvoda. Navika koja se isplati:

```
Pročitaj docs/spec.md pa mi reci kako sledeća funkcionalnost
koju planiramo utiče na ono što tamo piše.
```

Možeš i da zamoliš Claude-a da u `CLAUDE.md` doda napomenu da spec uvek pročita na početku rada, ili jednostavno pošalji poruku koja počinje sa `#`, čime Claude tu napomenu trajno zabeleži.

### Primer dijaloga iz prakse

**Ti:**

```
Imam ideju: aplikacija u koju ubaciš video, ona ga automatski
transkribuje i iseče tišine i poštapalice. Za male kreatore
sadržaja. Postavi mi 10 najtežih pitanja i reci šta bi izbacio
iz prve verzije.
```

**Claude (skraćeno):** "Pitanje 3: CapCut i Descript već rade nešto slično, zašto bi neko prešao kod tebe? Pitanje 7: obrada videa je skupa, ko plaća server dok je proizvod besplatan? Iz prve verzije bih izbacio: izvoz u više formata, timsku saradnju i mobilnu verziju. Zadržao bih samo: upload, transkripciju i automatsko sečenje tišina."

**Ti reaguješ:** Na pitanje 3 imaš odgovor, tvoja aplikacija radi odlično za srpski jezik, što veliki alati ne pokrivaju. To ide u spec pod "Ključna vrednost". Na pitanje 7 nemaš odgovor, beležiš ga kao rizik koji ćeš istražiti pre lansiranja. Predlog rezanja prihvataš i MVP postaje tri funkcionalnosti.

Vidiš mehaniku: Claude izaziva, ti odlučuješ. Ti si direktor (Modul 0), on je oštrouman savetnik.

### Vežba

1. Uzmi svoju ideju (ili izmisli jednu za vežbu, npr. aplikacija za deljenje troškova na putovanjima).
2. Otvori sesiju u Claude Code-u u folderu projekta i nalepi "đavolji advokat" prompt sa početka modula, sa svojom idejom.
3. Pisano odgovori na svih 10 pitanja. Za ona na koja nemaš odgovor, napiši "RIZIK: nemam odgovor", to su ti domaći zadaci.
4. Zatraži MVP rezanje promptom iz ovog modula. Cilj: najviše 3 funkcionalnosti u "Mora".
5. Zatraži od Claude-a: "Na osnovu ovog razgovora napiši nacrt `docs/spec.md` po sledećoj strukturi: problem, korisnik, ključna vrednost, funkcionalnosti (mora / trebalo bi / kasnije), šta NIJE u MVP-u, kriterijumi uspeha."
6. Pročitaj nacrt rečenicu po rečenicu. Sve sa čime se ne slažeš, ispravi ili izbaci. Ovo je tvoj dokument.
7. Sačuvaj fajl i potvrdi da postoji: zatraži od Claude-a da ti prikaže sadržaj `docs/spec.md`.

### Najčešće greške

1. **Tražiš mišljenje, a ne kritiku.** "Šta misliš o ovoj ideji?" donosi pohvale. Rešenje: uvek eksplicitno traži najteža pitanja, rizike i razloge za neuspeh, kao u promptu iz ovog modula.
2. **MVP od deset funkcionalnosti.** "Sve je neophodno" znači da nisi odlučio šta je srž. Rešenje: za svaku stavku pitaj "može li korisnik da dobije osnovnu vrednost bez ovoga?", ako može, seci.
3. **Spec napisan pa zaboravljen.** Posle dve nedelje gradiš nešto čega u spec-u nema. Rešenje: svaku sesiju počni sa "pročitaj `docs/spec.md`", a svaku novu ideju propusti kroz pitanje "da li ovo menja spec?".
4. **Ciljna grupa "svi".** Proizvod za sve je proizvod ni za koga. Rešenje: suzi dok ne zaboli, "frilenseri u Srbiji sa 5-20 faktura mesečno" je dobro; "ljudi koji rade" nije.
5. **Kriterijumi uspeha bez brojeva.** "Korisnici su zadovoljni" se ne može izmeriti. Rešenje: broj, vreme ili procenat, "prva faktura za manje od 60 sekundi" (princip merljivosti iz Modula 1).

### Kontrolna lista

- [ ] Claude mi je postavio 10 teških pitanja i odgovorio sam na svako (ili zabeležio rizik)
- [ ] Problem, ciljnu grupu i ključnu vrednost umem da kažem u po jednoj rečenici
- [ ] MVP ima najviše 3 funkcionalnosti pod "Mora"
- [ ] `docs/spec.md` postoji i sadrži svih šest sekcija, uključujući "Šta NIJE u MVP-u"
- [ ] Kriterijumi uspeha su merljivi (broj, vreme, procenat)
- [ ] Znam da svaku sledeću sesiju počinjem sa "pročitaj `docs/spec.md`"

### Proveri znanje

**1. Zašto moraš eksplicitno da tražiš kritiku od Claude-a?**

Zato što je Claude sam od sebe uslužan i podržavajući, na neutralno pitanje vratiće ohrabrenje, a ne analizu rizika. Kritiku, teška pitanja i razloge za neuspeh dobijaš samo ako ih izričito zatražiš.

**2. Šta znači analogija "prvo skejtbord, ne polu-automobil"?**

Prva verzija proizvoda treba da bude mala ali upotrebljiva, da već danas rešava srž problema (skejtbord vozi), umesto da bude nedovršen komad velike vizije koji nikome ne koristi (polu-automobil ne vozi).

**3. Čemu služi sekcija "Šta NIJE u MVP-u" i kako spec koristiš u budućim sesijama?**

Ta sekcija je pisana brana protiv širenja obima, kada dođe iskušenje da dodaš novu funkcionalnost, dokument te podseća da je svesno odložena. Spec koristiš tako što svaku novu sesiju počneš sa "pročitaj `docs/spec.md`", jer Claude ne pamti prethodne razgovore.


---

## Modul 5: Planiranje i arhitektura: odlučivanje bez tehničkog znanja

Imaš specifikaciju iz Modula 4. Sledeći refleks većine ljudi je: "Hajde, Claude, pravi!" Sačekaj. Pre nego što se zida kuća, arhitekta donese nacrt na sto. Ti ga pogledaš, postaviš pitanja, tražiš izmene, i tek kad ti potpišeš, počinje gradnja. U ovom modulu učiš upravo to: kako da budeš investitor koji pametno odobrava nacrte, iako sam nikad nije držao mistriju.

### Šta ćeš naučiti

- Šta je plan mode i zašto je tvoj najvažniji zaštitni mehanizam
- Formulu za donošenje tehničkih odluka bez tehničkog znanja: 2 opcije + preporuka + razmena
- Četiri zlatna pitanja koja postavljaš pre svake važne odluke
- Kako da kažeš Claude-u za šta optimizuješ, i zašto bez toga on samo pogađa
- Standardni početni tehnološki skup (Next.js + Supabase + Vercel) objašnjen jezikom prodavnice, a ne programera

### Plan mode: nacrt pre zidanja

Plan mode je poseban režim rada u kom Claude **istražuje i predlaže, ali ništa ne menja**. Čita tvoje fajlove, razmišlja, piše plan, i čeka tvoje odobrenje. Tek kad kažeš "može", kreće da menja kod.

Zašto je ovo važno baš tebi, kao netehničkoj osobi? Zato što je čitanje plana na srpskom jeziku nešto što TI umeš da proceniš. Kod možda ne razumeš, ali rečenicu "napravićemo stranicu za prijavu pa tek onda plaćanje", razumeš savršeno. Plan mode premešta odluku na teren gde si ti jak.

Uključuje se prečicom `Shift+Tab` (ona kruži kroz režime rada, pa pritiskaj dok ne vidiš plan mode). A ako prečicu zaboraviš, dovoljno je da napišeš:

```
Prvo napravi plan, ne menjaj ništa dok ne odobrim.
```

Pravilo palca: sve što je veće od sitne ispravke teksta zaslužuje plan. Plan je jeftin, pet minuta čitanja. Pogrešno izgrađen temelj je skup, dani vraćanja unazad.

### Formula odlučivanja: 2 opcije + preporuka + razmena

Tokom planiranja Claude će nailaziti na raskrsnice: koju bazu podataka, koji način prijave korisnika, gde čuvati slike. Ako ga pustiš, odlučiće sam, i to često sasvim dobro. Ali ti si direktor, i direktor odlučuje o stvarima koje koštaju novac i vreme. Zato uvedi kućno pravilo:

```
Za svaku važnu tehničku odluku u ovom projektu:
1. Ponudi mi tačno 2 opcije.
2. Reci koju TI preporučuješ.
3. Objasni razmena (šta dobijam, šta žrtvujem) jezikom za nekoga
   ko nije programer, bez žargona, sa poređenjem iz svakodnevnog života.
```

*Razmena* je razmena: svaki izbor nešto daje i nešto uzima. Jeftiniji lokal je dalje od centra. Brži auto troši više. Ne postoji opcija bez cene, postoji samo cena koju nisi video. Tvoj posao nije da znaš tehnologije; tvoj posao je da tražiš da ti cena bude pokazana.

Dve opcije, ne pet. Sa pet opcija se davi i iskusan inženjer; sa dve opcije i jasnom preporukom, odluka traje dva minuta.

### Četiri zlatna pitanja

Kad ti Claude ponudi opcije, ova četiri pitanja postavljaš uvek, nauči ih napamet, kao pin kod:

```
1. Šta je rizik ovog izbora? Šta najgore može da se desi?
2. Šta je teže promeniti kasnije, opciju A ili opciju B?
3. Koliko me ovo košta mesečno, danas i kad budem imao 1.000 korisnika?
4. Šta bi TI izabrao za ovaj konkretan projekat i zašto?
```

Drugo pitanje je najvrednije. Neke odluke su tapete, promeniš ih za popodne. Druge su nosivi zidovi, menjaš ih rušenjem pola kuće. Boja dugmeta je tapeta. Izbor baze podataka je bliže nosivom zidu. Kad znaš šta je zid, znaš gde da uložiš pažnju, a gde da odlučiš za trideset sekundi i ne osvrćeš se.

### Reci za šta optimizuješ

Ovo je rečenica koju većina početnika nikad ne izgovori, a menja sve. Claude ne zna da li praviš prototip za vikend ili sistem za banku, ako mu ne kažeš, **pogađa**. Isti zadatak ima tri različita dobra odgovora u zavisnosti od cilja:

- **Brzina do prvog korisnika**, najjednostavnije što radi, gotovi servisi, minimalno podešavanja.
- **Skala**, izdrži rast, čak i ako je početak sporiji i skuplji.
- **Trošak**, što bliže nuli mesečno, čak i po cenu ručnog rada.

Zato svaki plan počni ovako:

```
Kontekst: ovo je MVP, optimizujem za brzinu do prvog korisnika.
Budžet je do 20 evra mesečno. Skala me sada ne zanima, ako proizvod
uspe, prepravićemo. Predlaži najjednostavnija rešenja koja rade.
```

❌ "Napravi mi aplikaciju za rezervacije.", Claude pogađa tvoje prioritete.
✅ "Napravi plan za MVP aplikacije za rezervacije. Optimizujem za brzinu lansiranja, budžet 20 €/mesečno, jedan grad, do 50 korisnika u prva tri meseca.", Claude bira ciljano.

### Standardni početni tehnološki skup: izlog, magacin i lokal

*Tehnološki skup* je skup tehnologija od kojih je proizvod sagrađen, kao spisak materijala za kuću. Za prvi proizvod ne moraš da istražuješ: postoji proverena kombinacija koju koristi ogroman broj malih timova, pa je i Claude odlično poznaje.

- **Next.js**, *izlog i unutrašnjost prodavnice*. Ono što korisnik vidi i sa čim klikće: stranice, dugmad, forme.
- **Supabase**, *magacin sa katancem*. Tu žive podaci (korisnici, narudžbine, sadržaj) i sistem za prijavljivanje, ko sme da uđe i šta sme da vidi.
- **Vercel**, *lokal koji iznajmljuješ*. Tvoja prodavnica mora negde fizički da stoji da bi je ljudi posetili; Vercel je adresa na internetu gde tvoja aplikacija živi, sa kirijom koja je za početak nula ili sitna.

Zašto baš ovo? Sve troje ima besplatan početni nivo, međusobno se lepo uklapaju, a za Vercel i Supabase postoje i plugin-ovi za Claude Code (detaljno u Modulu 12; lansiranje na Vercel obrađuje Modul 9). Ako Claude predloži nešto drugo i laički ti obrazloži zašto je za tvoj slučaj bolje, saslušaj ga, zato i postavljaš zlatna pitanja. Ali teret dokazivanja je na alternativi, ne na standardu.

### Odluke upiši u CLAUDE.md: ili ne postoje

Claude između sesija ne pamti ništa osim fajla `CLAUDE.md` (i memorije). Odluka doneta u razgovoru, a nezapisana, sutra je, nepostojeća. Nova sesija će istu raskrsnicu rešiti iznova, možda drugačije, i dobićeš proizvod koji se sam sa sobom svađa.

Zato se svaka usvojena odluka odmah zapisuje. Možeš da zamoliš Claude-a:

```
Usvojili smo odluke: Next.js + Supabase + Vercel, optimizujemo za brzinu
do prvog korisnika, budžet 20 €/mesečno. Upiši ovo u CLAUDE.md u sekciju
"Arhitektonske odluke", sa jednom rečenicom obrazloženja po odluci.
```

Ili iskoristi prečicu: poruka koja počinje sa `#` se trajno beleži u memoriju/CLAUDE.md. O ulozi `CLAUDE.md` kao "radne sveske" projekta detaljno smo pričali u Modulu 1 i Modulu 3.

### Vežba

1. Otvori terminal u folderu svog projekta i pokreni `claude`.
2. Uključi plan mode prečicom `Shift+Tab` (ili napiši: "prvo plan, ništa ne menjaj dok ne odobrim").
3. Nalepi prompt, prilagodi svojoj specifikaciji iz Modula 4:

```
Pročitaj docs/spec.md. Predloži arhitekturu za MVP. Kontekst:
optimizujem za brzinu do prvog korisnika, budžet 20 €/mesečno,
nisam programer. Za svaku važnu odluku daj 2 opcije, svoju
preporuku i razmena objašnjen laički.
```

4. Za svaku raskrsnicu u planu postavi bar dva od četiri zlatna pitanja. Posebno: "Šta je teže promeniti kasnije?"
5. Kad si zadovoljan, odobri plan i traži da se usvojene odluke upišu u `CLAUDE.md`.
6. Pokreni `/clear` pa pitaj: "Koje su arhitektonske odluke ovog projekta?" Ako Claude odgovori tačno, zapisivanje radi.

### Najčešće greške

1. **Preskakanje plana jer "žuri mi se".** Pet minuta čitanja plana štedi dane prepravki. Rešenje: plan mode kao podrazumevani početak za svaku veću izmenu.
2. **Klimanje glavom na plan koji ne razumeš.** Ako ne umeš da prepričaš plan prijatelju, nisi ga odobrio, samo si kliknuo. Rešenje: "Objasni mi tačku 3 kao da imam petnaest godina."
3. **Nisi rekao za šta optimizuješ.** Claude tada pogađa, često ka složenijem rešenju nego što ti treba. Rešenje: rečenica o cilju i budžetu na početku svakog planiranja.
4. **Odluke ostale u razgovoru, ne u `CLAUDE.md`.** Sledeća sesija kreće od nule i odlučuje drugačije. Rešenje: nijedna rasprava se ne završava bez upisa usvojenog zaključka.
5. **Egzotičan tehnološki skup jer je "najnoviji".** Za novu tehnologiju ima manje primera, pa i Claude i ti češće lutate. Rešenje: standardni tehnološki skup dok ne postoji konkretan, laički objašnjen razlog za izuzetak.

### Kontrolna lista

- [ ] Znam da uključim plan mode (`Shift+Tab` ili rečenicom) i kad da ga koristim
- [ ] Svaku važnu odluku tražim kao: 2 opcije + preporuka + razmena laički
- [ ] Četiri zlatna pitanja znam napamet
- [ ] Claude-u sam rekao za šta optimizujem (brzina / skala / trošak) i koliki je budžet
- [ ] Razumem analogiju: Next.js = izlog, Supabase = magacin, Vercel = lokal
- [ ] Usvojene odluke su upisane u `CLAUDE.md` i provereno preživljavaju `/clear`

### Proveri znanje

**1. Šta plan mode radi, a šta ne radi?**
Claude istražuje projekat i predlaže plan, ali ne menja nijedan fajl dok plan ne odobriš. Uključuje se prečicom `Shift+Tab` ili jednostavnim zahtevom u poruci.

**2. Zašto je pitanje "šta je teže promeniti kasnije" vrednije od "šta je bolje"?**
Zato što razdvaja tapete od nosivih zidova: odluke koje se lako menjaju donosi brzo i bez griže savesti, a pažnju i pitanja ulaže u one koje bi kasnije zahtevale rušenje pola proizvoda.

**3. Zašto odluke moraju u `CLAUDE.md`, a ne samo u razgovor?**
Claude između sesija ne pamti razgovore, na početku svake sesije učitava samo `CLAUDE.md` (i memoriju). Nezapisana odluka za sutrašnju sesiju ne postoji, pa bi istu dilemu mogao da reši drugačije i unese nedoslednost u projekat.


---

## Modul 6: Ritam razvoja: funkcionalnost po funkcionalnost

Stigao si do srca cele metodologije. Sve do sada, okruženje, temelji, specifikacija, plan, bila je priprema. Odavde pa do lansiranja, 80% tvog vremena provodi se u jednom istom ciklusu koji se ponavlja za svaku funkcionalnost (jednu zaokruženu stvar koju proizvod radi, npr. "kontakt forma" ili "prijava korisnika"). Kad taj ciklus uđe u ruke, razvoj prestaje da bude haos i postaje zanat: predvidiv, miran, merljiv.

Zamisli ga kao pranje veša. Ne ubacuješ sve odjednom u mašinu, sortiraš, opereš jednu turu, proveriš da li je čisto, složiš, pa tek onda sledeća tura. Jedna funkcionalnost = jedna tura.

### Šta ćeš naučiti

- Ciklus od 7 koraka koji ponavljaš za svaku funkcionalnost, od prazne sesije do potvrde da sve radi
- Zašto svaka funkcionalnost zaslužuje svežu sesiju (`/clear`) i šta se dešava kad to preskočiš
- Kako da tražiš dokaz umesto obećanja, snimak ekrana, test, log
- Formulu savršenog prompta: KONTEKST → ZADATAK → KRITERIJUM PRIHVATANJA → OGRANIČENJA
- Kompletan, stvaran primer jednog ciklusa koji možeš da kopiraš i prilagodiš

### Ciklus od 7 koraka

**Korak 1: `/clear`, sveža sesija za svaku funkcionalnost.** Sesija je jedan razgovor sa Claude-om, a kontekst je njegova radna memorija u tom razgovoru (detaljno u Modulu 1). Kad u istoj sesiji nakupiš tri funkcionalnosti, dve ispravke i jedan eksperiment, ta memorija se zatrpa, Claude počinje da meša stare zahteve sa novima, kao konobar koji pamti porudžbine celog dana umesto samo tvog stola. Zato: nova funkcionalnost, nova sesija. Ne brini za "zaboravljanje", sve trajno važno živi u `CLAUDE.md` i u tvojim fajlovima sa specifikacijom, a oni se učitavaju iznova.

**Korak 2: Plan mode za sve što nije trivijalno.** Plan mode je režim u kom Claude istražuje projekat i predlaže plan, ali ne menja nijedan fajl dok ti plan ne odobriš. Uključuješ ga prečicom `Shift+Tab` ili jednostavno napišeš: "prvo napravi plan, ne menjaj ništa dok ne odobrim". Pravilo palca: ako funkcionalnost dira više od jednog fajla ili uvodi nešto novo (bazu, plaćanje, slanje imejlova), plan mode. Ako je sitnica ("promeni boju dugmeta"), preskoči. Kako da čitaš i izazivaš predloženi plan naučio si u Modulu 5.

**Korak 3: Implementacija.** Odobriš plan i pustiš Claude-a da radi. Tvoj posao nije da razumeš svaki red koda, nego da pratiš da li se drži plana. Ako vidiš da skreće, `Esc` ga prekida usred rada i odmah možeš da ga preusmeriš, to nije nepristojno, to je upravljanje.

**Korak 4: Verifikacija u pregledaču, traži dokaz.** Ovo je korak koji početnici najčešće preskaču, a najviše vredi. Claude ume da pokrene dev server (lokalnu, probnu verziju tvoje aplikacije na tvom računaru), klikće po njoj, popunjava forme i pravi snimke ekrana. Nikad ne prihvataj "implementirano je" kao kraj, to je obećanje, ne dokaz.

```
Pokreni dev server, otvori stranicu /kontakt u pregledaču, popuni formu
probnim podacima i pošalji je. Napravi snimak ekrana forme pre slanja i
snimak ekrana poruke o uspehu posle slanja. Pokaži mi oba.
```

**Korak 5: `/code-review`.** Pre nego što izmene proglasiš gotovim, pusti pregled koda: `/code-review` pregleda trenutne izmene i prijavi probleme. Ima nivoe temeljnosti (low/medium/high/max), za svakodnevni rad srednji nivo je sasvim dovoljan. Šta znače nalazi i kada da posegneš za `/security-review`, detaljno u Modulu 8.

**Korak 6: Commit.** Commit je snimak stanja projekta u git-u, kao "sačuvaj igru" u video igrici: tačka kojoj uvek možeš da se vratiš (osnove git-a su u Modulu 3). Jedna funkcionalnost = jedan commit (ili nekoliko manjih, ali nikad "sve od prošle nedelje odjednom").

```
Napravi commit ovih izmena sa jasnom porukom na srpskom koja opisuje
šta funkcionalnost radi, i pošalji na GitHub.
```

**Korak 7: `/loop` za praćenje CI-ja.** CI (continuous integration) je automatska kontrola kvaliteta na GitHub-u koja posle svakog slanja koda sama pokreće testove (podesio si je u Modulu 3). Umesto da sediš i osvežavaš stranicu, zaduži Claude-a: `/loop 5m proveri status CI provera za poslednji commit; ako je nešto palo, ispravi i pošalji ponovo`. Petlja ponavlja prompt na zadati interval i prekida se sa `Esc`. Više o autonomnom radu i zaštitnim ogradama, Modul 7.

I onda? `/clear` i sledeća funkcionalnost. To je ceo ritam.

### Formula savršenog prompta

Svaki dobar radni prompt ima četiri dela. Zapamti ih kao K-Z-K-O.

**1. KONTEKST, gde Claude treba da gleda.** Ne prepričavaj specifikaciju, uputi ga na nju:

```
Pročitaj docs/spec.md, sekciju "Kontakt forma".
```

**2. ZADATAK, šta se pravi.** Jedna jasna rečenica, jedna funkcionalnost. Ako u zadatku stoji veznik "i" između dve različite stvari, verovatno su to dva ciklusa.

**3. KRITERIJUM PRIHVATANJA, "gotovo je kad…".** Ovo je najmoćniji deo i najčešće izostavljen. Bez njega Claude sam odlučuje šta znači "gotovo", a njegova definicija i tvoja se retko poklapaju. Kriterijum mora biti proverljiv:

❌ `Napravi lepu kontakt formu.` (šta je "lepo"? kad je gotovo?)
✅ `Gotovo je kad: forma na /kontakt prima ime, imejl i poruku; posle slanja poruka se vidi u bazi; korisnik dobije potvrdu na ekranu; npm run build prolazi bez grešaka.`

**4. OGRANIČENJA, šta NE dirati.** Claude je vredan i ponekad "usput" sredi i ono što nisi tražio. Ogradi teren:

```
Ne diraj postojeću stranicu /cenovnik ni navigaciju. Ne uvodi nove
biblioteke bez pitanja. Postojeći testovi moraju i dalje da prolaze.
```

### Kompletan primer: kontakt forma koja čuva poruke u bazu

Prođimo ceo ciklus na stvarnoj funkcionalnosti, prompt po prompt.

**1.** Ukucaj `/clear`. Prazna tabla.

**2.** Plan (Shift+Tab za plan mode, pa):

```
Pročitaj docs/spec.md, sekciju "Kontakt forma". Napravi plan za kontakt
formu na stranici /kontakt: polja ime, imejl i poruka, čuvanje poruka
u našu bazu, potvrda korisniku posle slanja, jasna poruka ako nešto
pođe po zlu. Gotovo je kad poslata poruka postoji u bazi i korisnik
vidi potvrdu. Ne diraj ostale stranice i ne uvodi nove biblioteke bez
pitanja. Objasni mi plan jezikom za nekoga ko ne programira.
```

**3.** Pročitaj plan, postavi pitanja ("šta se desi ako neko pošalje prazan imejl?"), odobri. Claude implementira.

**4.** Dokaz:

```
Pokreni dev server i verifikuj u pregledaču: popuni formu na /kontakt
podacima "Marko Marković, marko@test.com, Probna poruka" i pošalji.
Napravi snimak ekrana potvrde. Zatim mi pokaži da ta poruka stvarno
postoji u bazi. Probaj i slanje prazne forme, snimak ekrana poruke
o grešci.
```

Pogledaj snimke ekrana svojim očima. Ti si poslednja kontrola.

**5.** `/code-review`, pa zamoli Claude-a da ispravi ono što pregled nađe i ponovi verifikaciju iz koraka 4 ako je menjao logiku.

**6.** Commit:

```
Napravi commit sa porukom "Dodaj kontakt formu sa čuvanjem poruka
u bazu" i pošalji na GitHub.
```

**7.** `/loop 5m proveri da li su CI provere za poslednji commit prošle; ako je nešto palo, ispravi uzrok i pošalji ponovo`. Kad CI pozeleni, `Esc`, pa `/clear`, i sledeća tura veša.

### Vežba

1. Otvori svoj `docs/spec.md` (napravio si ga u Modulu 4) i izaberi najmanju nezapočetu funkcionalnost sa liste.
2. Napiši na papiru ili u beležnici njegova četiri dela: kontekst, zadatak, kriterijum prihvatanja, ograničenja. Ne preskači kriterijum!
3. Ukucaj `/clear`, uđi u plan mode (`Shift+Tab`) i pošalji svoj prompt.
4. Prođi svih 7 koraka do kraja, uključujući snimak ekrana kao dokaz i commit.
5. Na kraju zapiši: koji korak ti je bio najneprirodniji? Njega sledeći put radi prvo.

### Najčešće greške

1. **Nastavljanje u istoj sesiji ceo dan.** Simptom: Claude "meša" stare i nove zahteve, vraća izmene koje si već odbacio. Rešenje: `/clear` posle svake završene funkcionalnosti; ako sesija mora da bude duga, `/compact` da sažme razgovor.
2. **Prihvatanje "gotovo je" bez dokaza.** Claude može iskreno da veruje da nešto radi, i da greši. Rešenje: uvek traži snimak ekrana, izlaz testova ili log; korak 4 nije opcioni.
3. **Prompt bez kriterijuma prihvatanja.** Dobiješ nešto, ali ne ono što si hteo, pa kreće prepravljanje u krug. Rešenje: pre slanja prompta dopiši rečenicu koja počinje sa "Gotovo je kad…".
4. **Tri funkcionalnosti u jednom promptu.** Plan postane ogroman, verifikacija nemoguća, a kad nešto pukne ne znaš šta je krivac. Rešenje: jedan ciklus = jedna funkcionalnost; ostalo ide u backlog (listu čekanja, Modul 10).
5. **Commit "kad se nakupi".** Posle nedelju dana imaš planinu izmena i nijednu sigurnu tačku za povratak. Rešenje: commit je korak 6 svakog ciklusa, ne mesečna proslava.

### Kontrolna lista

- [ ] Počeo sam rad na funkcionalnosti sa `/clear`, u svežoj sesiji
- [ ] Za netrivijalnu funkcionalnost koristio sam plan mode i odobrio plan pre izmena
- [ ] Moj prompt ima sva četiri dela: kontekst, zadatak, kriterijum prihvatanja, ograničenja
- [ ] Video sam dokaz da funkcionalnost radi (snimak ekrana, test, log), ne samo tvrdnju
- [ ] Pokrenuo sam `/code-review` i razrešio nalaze
- [ ] Napravio sam commit sa jasnom porukom i poslao na GitHub
- [ ] CI provere su zelene (pratio sam ih kroz `/loop` ili proverio ručno)

### Proveri znanje

**1. Zašto se svaka funkcionalnost radi u svežoj sesiji?**
Zato što se kontekst (radna memorija razgovora) vremenom zatrpa starim zahtevima i eksperimentima, pa Claude počinje da ih meša sa novim zadatkom. `/clear` daje čistu tablu, a trajno znanje ostaje u `CLAUDE.md` i fajlovima projekta.

**2. Koja su četiri dela formule savršenog prompta i koji se najčešće zaboravlja?**
Kontekst (gde da gleda), zadatak (šta se pravi), kriterijum prihvatanja ("gotovo je kad…") i ograničenja (šta ne dirati). Najčešće se zaboravlja kriterijum prihvatanja, a bez njega Claude sam definiše "gotovo".

**3. Šta je prihvatljiv dokaz da funkcionalnost radi, a šta nije?**
Prihvatljivo: snimak ekrana iz pregledača, izlaz testova, zapis u bazi, log. Neprihvatljivo: rečenica "implementirano je", to je obećanje, a ti tražiš dokaz koji možeš da vidiš svojim očima.


---

## Modul 7: Autonomni rad: /goal, /loop i granice poverenja

Do sada si radio sa Claude-om kao sa kolegom za istim stolom: ti kažeš, on uradi, ti pogledaš. U ovom modulu učiš nešto moćnije, kako da mu daš zadatak, odeš na ručak, i vratiš se na završen posao. To je delegiranje u pravom smislu: jasan cilj, jasna pravila, jasne granice. I baš zato što je moćno, ovde su zaštitne ograde važnije nego igde drugde.

### Šta ćeš naučiti

- Kako da sa `/goal` zadaš cilj i pustiš Claude-a da radi sam dok ga ne ispuni
- Kako da napišeš uslov koji se može dokazati, i zašto je to srce cele priče
- Kada koristiti `/loop` za ponavljanje, a `/schedule` za rad kad je računar ugašen
- Četiri zaštitne ograde koje autonoman rad čine bezbednim umesto rizičnim

### Auto mode: preduslov autonomije

Podrazumevano, Claude te pita za odobrenje pre potencijalno opasnih akcija. To je odlično dok sediš pored njega, ali autonoman rad po definiciji znači da te nema da klikneš „odobri", zato je **auto mode** preduslov.

Auto mode, listu unapred dozvoljenih komandi u `.claude/settings.json` i skill `/fewer-permission-prompts` koji tu listu predlaže umesto tebe, sve si upoznao u Modulu 2 (sekcija „Sistem dozvola"). Pre autonomnog rada ih podesi: pokreni skill jednom i imaš temelj.

### /goal: zadaj cilj i skloni se

`/goal` (zahteva Claude Code v2.1.139 ili noviji) radi ovako: ti napišeš uslov, a Claude radi turu za turom, menja kod, pokreće provere, ispravlja greške, potpuno autonomno, dok uslov nije ispunjen. Tura je jedan „krug" rada: Claude nešto uradi, pokaže rezultat, pa kreće sledeći krug.

```
/goal Svi testovi prolaze: `npm test` izlazi sa 0. Pokreni testove
posle svake izmene i pokaži izlaz. Postojeći testovi se ne menjaju
i ne brišu. Ako cilj nije ispunjen posle 20 tura, stani i napiši
šta te blokira.
```

Ko odlučuje da li je cilj ispunjen? Ne Claude koji radi posao, to bi bilo kao da učenik sam sebi ocenjuje kontrolni. Posle svake ture, **mali brzi model (Haiku)** pogleda razgovor i oceni: da li uslov važi, da ili ne? To je nezavisni kontrolor. I tu je kvaka: kontrolor vidi samo ono što Claude pokaže u razgovoru. Ako uslov ne može da se dokaže kroz nešto vidljivo, izlaz komande, log, snimak ekrana, kontrolor nema šta da oceni.

Korisno za upravljanje:

- `/goal` bez ičega, status: koji je uslov, koliko tura je prošlo, koliko vremena i tokena je potrošeno
- `/goal clear`, prekid
- Jedan aktivan goal po sesiji; novi zamenjuje stari
- Goal preživljava `claude --resume`, pa možeš zatvoriti terminal i nastaviti kasnije
- Radi i neinteraktivno: `claude -p "/goal ..."`, pokreneš i pustiš

### Dokaziv uslov: razlika između uspeha i lutanja

Ovo je najvažnija veština ovog modula. Uslov mora biti nešto što kontrolor može da proveri gledajući dokaze, ne utiske.

| Uslov | Ocena | Zašto |
|---|---|---|
| `npm test` izlazi sa 0 i izlaz je prikazan | ✅ | Komanda sa jednoznačnim ishodom, da ili ne, bez tumačenja |
| `npm run build` prolazi bez grešaka, `npm run lint` bez upozorenja | ✅ | Dve konkretne provere, obe vidljive u razgovoru |
| Stranica `/kontakt` postoji i snimak ekrana pokazuje formu sa poljima za ime, imejl i poruku | ✅ | Dokaz je slika, sadržaj je nabrojan stavku po stavku |
| Aplikacija je kvalitetna i spremna za korisnike | ❌ | „Kvalitetna" je utisak, kontrolor nema šta da izmeri |
| Kod je čist i lako se održava | ❌ | Subjektivno; ne postoji komanda koja to dokazuje |
| Sajt radi brzo | ❌ | „Brzo" bez broja i načina merenja je neproverivo |
| Sredi bagove | ❌ | Nije završno stanje, koje bagove? Kako znamo da su sređeni? |

### Četiri sastojka dobrog uslova

Pogledaj ponovo primer iznad, u njemu su sva četiri:

1. **Merljivo završno stanje**, „svi testovi prolaze, `npm test` izlazi sa 0". Cilj, ne pravac.
2. **Način provere**, „pokreni testove posle svake izmene i pokaži izlaz". Kontrolor mora da vidi dokaz.
3. **Ograničenja**, „postojeći testovi se ne menjaju i ne brišu". Ovo je ključno: AI koji juri cilj može pronaći prečicu. Najlakši način da test koji pada „prođe" jeste, da se obriše. To je kao da kažeš nekome „soba mora biti čista", pa on sve gurne u orman. Ograničenje zatvara orman.
4. **Limit tura**, „ili stani posle 20 tura". Osigurač: ako nešto ne ide, bolje da stane i javi nego da se vrti u krug i troši tokene.

### /loop: strpljivi pomoćnik koji proverava umesto tebe

`/goal` juri cilj; `/loop` ponavlja zadatak. Dva režima:

**Fiksni interval**, ti odrediš ritam (jedinice: `s`, `m`, `h`, `d`). Idealno za praćenje CI provera posle push-a (push = slanje commit-ova na GitHub, ono što smo u Modulu 3 zvali „pošalji na GitHub"; CI je automatska provera koda koja se tada pokreće, oba detaljno u Modulu 3):

```
/loop 5m Proveri status CI provera za poslednji push. Ako je nešto
palo, pročitaj log, popravi uzrok i push-uj ispravku. Ako je sve
zeleno, samo kratko javi status.
```

**Dinamički režim**, bez intervala, Claude sam bira pauze (1–60 minuta) prema aktivnosti i može sam da završi petlju kad je posao gotov. Savršeno za „babysitting" deploy-a (deploy = objavljivanje aplikacije na internet, detaljno u Modulu 9):

```
/loop Prati deploy. Proveravaj status; ako padne, pročitaj log
greške i popravi uzrok. Kad deploy uspe i sajt radi, završi petlju.
```

A samo `/loop` bez ičega pokreće podrazumevani prompt za održavanje sesije (nastavi nedovršeno, sredi PR); možeš ga prilagoditi kroz fajl `.claude/loop.md`.

Ograničenja: petlju zaustavlja `Esc`, važi samo dok je sesija otvorena (najviše 7 dana) i **ne radi kad je računar ugašen**. Laptop u rancu = petlja spava.

### /schedule: noćna smena u oblaku

Kad ti treba rad i kad je računar ugašen, tu je `/schedule`, Routines: zakazani agenti koji rade u oblaku, ne na tvojoj mašini. Klasičan primer: dnevni izveštaj o stanju projekta koji te čeka uz jutarnju kafu. Za automatizaciju vezanu za repozitorijum (npr. pregled svakog PR-a) postoji i GitHub Actions. Više o rutinama posle lansiranja u Modulu 10.

### Koji alat kada

| Situacija | Alat |
|---|---|
| Jasan cilj sa proverivim krajem („svi testovi prolaze") | `/goal` |
| Ponavljanje iste provere dok čekaš (CI, deploy) | `/loop` |
| Redovan posao i kad je računar ugašen (dnevni izveštaj) | `/schedule` |
| Automatizacija vezana za repozitorijum (pregled svakog PR-a) | GitHub Actions |

### Zaštitne ograde kao sistem

Autonomija bez ograda nije hrabrost, nego kockanje. Četiri ograde rade zajedno:

1. **Git, dugme za poništavanje.** Commit pre svakog autonomnog rada znači da se svaka izmena može vratiti (Modul 3). Najgori scenario prestaje da bude katastrofa.
2. **Testovi, kompas.** Bez testova, kontrolor nema šta da meri, a Claude nema čime da se orijentiše. Autonoman rad bez testova je vožnja noću bez farova.
3. **Limiti, osigurač.** Limit tura u uslovu radi isto što i osigurač u struji: kad nešto pođe naopako, prekine pre štete.
4. **Ograničenja u uslovu, integritet.** „Postojeći testovi se ne menjaju" čuva smisao cilja: sprečava da se cilj „ispuni" slabljenjem provera.

### Vežba

1. Otvori projekat u terminalu i pokreni `claude`.
2. Zamoli Claude-a: `Napravi commit trenutnog stanja sa porukom "pre autonomnog rada"`, to ti je sigurnosna kopija.
3. Izaberi mali, jasan zadatak (npr. nekoliko testova koji padaju, ili lint upozorenja). Ako je kod tebe sve zeleno, pripremi vežbu sam: zamoli Claude-a, `Ubaci u kod 5 namernih stilskih grešaka koje će lint prijaviti, pa napravi commit sa porukom "vežba za /goal"`. Zatim pokreni goal iz koraka 4 i gledaj kako ih sam ispravlja.
4. Napiši goal sa sva četiri sastojka:

```
/goal `npm run lint` prolazi bez ijednog upozorenja. Pokreći lint
posle svake izmene i pokaži izlaz. Ne isključuj lint pravila i ne
dodavaj izuzetke, ispravi sam kod. Stani posle 15 tura ako cilj
nije ispunjen.
```

5. Pusti ga da radi. Povremeno ukucaj `/goal` da vidiš status.
6. Kad završi, zamoli: `Pokaži mi git diff i objasni svaku izmenu jednostavnim jezikom.`
7. Ako ti se nešto ne sviđa, git ti čuva leđa: sve se može vratiti.

### Najčešće greške

1. **Neproveriv uslov.** „Neka aplikacija bude bolja", kontrolor nema šta da izmeri, pa goal luta. *Rešenje:* uvek komanda + očekivani ishod („`npm test` izlazi sa 0").
2. **Bez ograničenja.** Claude „ispuni" cilj tako što oslabi proveru (obriše test, isključi lint pravilo). *Rešenje:* eksplicitno zabrani: „postojeći testovi se ne menjaju i ne brišu".
3. **Bez limita tura.** Goal se vrti satima na nemogućem zadatku i troši tokene. *Rešenje:* „stani posle 20 tura i napiši šta te blokira".
4. **`/loop` preko noći na laptopu koji ode na spavanje.** Petlja radi samo dok je sesija otvorena i računar budan. *Rešenje:* za rad van sesije koristi `/schedule`.
5. **Autonoman rad bez prethodnog commit-a.** Ako rezultat ne valja, nemaš čistu tačku za povratak. *Rešenje:* commit pre svakog `/goal`, uvek.

### Kontrolna lista

- [ ] Auto mode i lista dozvoljenih komandi su podešeni (`/fewer-permission-prompts`)
- [ ] Napravljen je commit pre pokretanja autonomnog rada
- [ ] Uslov ima merljivo završno stanje i način provere
- [ ] Uslov ima ograničenja („postojeći testovi se ne menjaju")
- [ ] Uslov ima limit tura
- [ ] Znam da proverim status (`/goal`) i prekinem (`/goal clear`, `Esc` za `/loop`)
- [ ] Posle završetka sam pregledao izmene kroz `git diff`

### Proveri znanje

**1. Ko ocenjuje da li je `/goal` uslov ispunjen i šta iz toga sledi za pisanje uslova?**

Mali brzi model (Haiku) posle svake ture ocenjuje da li uslov važi, ali vidi samo ono što Claude pokaže u razgovoru. Zato uslov mora biti dokaziv: izlaz komande, log ili snimak ekrana, ne utisak.

**2. Zašto u uslov pišemo „postojeći testovi se ne menjaju"?**

Jer AI koji juri cilj može pronaći prečicu: najlakši način da test „prođe" je da se obriše ili oslabi. Ograničenje čuva integritet cilja, uspeh mora doći od popravke koda, ne od slabljenja provere.

**3. Računar ti je ugašen preko noći, a hoćeš jutarnji izveštaj o projektu. Koji alat biraš i zašto ne ostale?**

`/schedule`, zakazani agenti u oblaku rade i kad je tvoj računar ugašen. `/goal` i `/loop` žive unutar otvorene sesije na tvojoj mašini, pa sa ugašenim računarom ne rade.


---

## Modul 8: Kvalitet i bezbednost: poverenje se gradi proverom

Tvoj proizvod sada radi. Funkcionalnosti se ređaju, demo izgleda dobro, i prirodno je da poželiš da odmah lansiraš. Ali između "radi kod mene" i "spremno za prave korisnike" stoji jedan korak koji profesionalci nikad ne preskaču: nezavisna provera. Dobra vest, ne moraš da budeš programer da bi je sproveo. Claude Code ima ugrađene alate za pregled koda, a tvoj posao je isti kao posao dobrog direktora: da postavljaš prava pitanja i tražiš dokaze.

Zamisli to ovako: kad kupuješ stan, ne veruješ prodavcu na reč da su instalacije ispravne, dovedeš svog majstora da pregleda. `/code-review`, `/security-review` i `/simplify` su tvoji majstori za pregled. Razlika je u tome što su uvek dostupni i pregled traje minute, ne dane.

### Šta ćeš naučiti

- Kako da pokreneš `/code-review` i izabereš pravi nivo temeljnosti za situaciju
- Kada je `/security-review` obavezan, a ne opcioni
- Kako da čitaš nalaze pregleda iako ne razumeš kod, formula od tri pitanja
- Kako da "napadneš" sopstvenu aplikaciju pre nego što to uradi neko drugi
- Koje crvene zastavice u Claude-ovim odgovorima zahtevaju da odmah staneš

### /code-review: drugi par očiju za tvoj kod

Komanda `/code-review` pregleda izmene koje su trenutno u toku i traži greške: stvari koje će se pokvariti, ivične slučajeve koji nisu pokriveni, logiku koja ne radi ono što misliš da radi. To je kao lektor za kod, ne piše tekst umesto tebe, nego hvata ono što je autoru promaklo.

Postoje nivoi temeljnosti: `low`, `medium`, `high` i `max`. Niži nivoi su brži i fokusirani na najvažnije; viši nivoi pregledaju temeljnije. Praktično pravilo:

- **low/medium**, svakodnevni ritam, posle svake završene funkcionalnosti (vidi Modul 6). Brzo, hvata očigledne propuste.
- **high/max**, pre spajanja veće celine, posle autonomnog rada iz Modula 7, ili kad menjaš nešto osetljivo.
- **`/code-review ultra`**, za najvažnije prekretnice: pred lansiranje, posle velikog refaktorisanja (krupnog unutrašnjeg sređivanja koda koje ne menja ono što korisnik vidi, detaljno u Modulu 10). Ovo je multi-agent pregled celog brancha u oblaku, više nezavisnih pregledača radi paralelno, pa je najtemeljniji. Dodatno se naplaćuje i pokrećeš ga ti, svesno, ne usput.

```
/code-review high
```

Nemoj da pregledaš sve odjednom jednom mesečno. Mali, česti pregledi su kao pranje sudova posle svakog obroka, deset minuta dnevno umesto traume vikendom.

### /security-review: brava na vratima

`/code-review` traži greške; `/security-review` traži rupe kroz koje neko zlonameran može da uđe. Pregleda bezbednosne propuste u izmenama na trenutnom branchu (branch = paralelna verzija projekta na kojoj se izmene prave pre spajanja u glavnu, vidi rečnik u Dodatku C).

Dva trenutka kad je ova komanda **obavezna**, bez izuzetka:

1. **Pred lansiranje**, uvek, kao tehnički pregled pre registracije auta.
2. **Posle svake izmene koja dodiruje prijavu korisnika, plaćanja ili lične podatke.** Imejl adrese, lozinke, brojevi kartica, istorija korišćenja, sve su to podaci za koje si odgovoran i pravno i moralno.

```
/security-review
```

Trošak: nekoliko minuta. Trošak propusta: poverenje korisnika koje se ne vraća lako.

### /simplify: generalno spremanje

Kod vremenom raste i zapliće se, kao fioka u koju mesecima ubacuješ stvari "samo na trenutak". `/simplify` pojednostavljuje i čisti izmenjeni kod, uklanja dupliranje, skraćuje zaobilazne puteve. Važno: on **ne traži bagove**, za to je `/code-review`. Pokreći ga periodično, recimo posle svake zaokružene celine, čistiji kod znači da će svaka sledeća izmena biti brža i jeftinija.

### Kako čitaš nalaze kad nisi programer

Pregled će ti vratiti listu nalaza punu tehničkih izraza. Ne treba da ih razumeš na nivou koda, treba da doneseš odluku, a za odluku ti treba prevod. Za **svaki** nalaz traži tri stvari:

```
Za nalaz broj 2 iz pregleda:
1. Objasni mi prostim jezikom, bez žargona, šta je problem, kao da pričaš
   sa nekim ko nikad nije programirao.
2. Koliko je ozbiljno na skali 1-10? Šta je najgore što može da se desi
   ako ovo ne popravimo?
3. Predloži ispravku i reci koliko bi posla bilo. Ne menjaj ništa dok ne odobrim.
```

Sa ova tri odgovora odlučuješ kao direktor: ozbiljnost 8+ se rešava odmah, 4-7 ide u backlog (spisak budućih zadataka, vidi Modul 10), 1-3 možda nikad. Ti određuješ prioritete, Claude ti daje informacije za odluku.

### Igraj napadača pre napadača

Najbolji bezbednosni test koji možeš da uradiš besplatno: zamoli Claude-a da razmišlja kao neko ko želi da te ošteti.

```
Ponašaj se kao zlonameran korisnik moje aplikacije. Šta sve mogu da
zloupotrebim? Probaj da pristupiš tuđim podacima, da promeniš tuđe
sadržaje, da zaobiđeš prijavu, da pošalješ besmislene ili ogromne
podatke u forme. Za svaki uspešan "napad" pokaži mi tačno šta si
uradio i koji je dokaz da je uspeo.
```

Claude može da pokrene dev server i proveri ovo u pregledaču, da klikće, popunjava forme i pravi snimke ekrana. Ako "napad" uspe, imaćeš snimak ekrana ili log kao dokaz, a onda i jasan zadatak za ispravku.

### Princip dokaza i crvene zastavice

Iz Modula 1 znaš pravilo: **tvrdnja bez dokaza se ne računa.** "Popravio sam" ne znači ništa bez test rezultata, snimka ekrana ili loga. U kontekstu kvaliteta, ovo su tri crvene zastavice na koje reaguješ odmah:

❌ **"Gotovo je" bez dokaza.** Odgovor: "Pokaži mi rezultat testova / snimak ekrana ekrana / log koji to potvrđuje."

❌ **Test "popravljen" tako što je obrisan ili oslabljen.** Ako test ne prolazi, problem je u kodu, ne u testu. Ovo je kao da požarni alarm utišaš vađenjem baterije. Reci unapred:

```
Postojeće testove ne smeš da brišeš niti menjaš da bi prošli.
Ako test pada, popravi kod. Ako misliš da je sam test pogrešan,
stani i objasni mi zašto pre nego što ga diraš.
```

❌ **Upozorenja koja se ignorišu.** Kad build ili lint izbaci upozorenje (warning), a Claude kaže "to nije bitno, nastavljam", pitaj: "Objasni mi to upozorenje prostim jezikom i šta rizikujemo ako ga ostavimo."

✅ Zdrav obrazac izgleda ovako: izmena → testovi prolaze (vidiš rezultat) → `/code-review` → nalazi prevedeni i odlučeni → dokaz da ispravke rade.

### Vežba

1. Otvori terminal u folderu projekta i pokreni `claude`.
2. Pokreni `/code-review medium` nad trenutnim izmenama (ako nemaš sveže izmene, zamoli Claude-a da pregleda poslednju završenu funkcionalnost).
3. Izaberi jedan nalaz i postavi tri pitanja iz formule: prost jezik, ozbiljnost 1-10 + najgori scenario, predlog ispravke.
4. Odluči: popraviti odmah, backlog, ili ignorisati. Zapiši odluku i razlog.
5. Pokreni `/security-review`. Ako vrati nalaze, ponovi korak 3 za najozbiljniji.
6. Kopiraj prompt "zlonamernog korisnika" iz ovog modula i pusti Claude-a da napadne tvoju aplikaciju. Traži dokaz za svaki nalaz.
7. Za jednu odobrenu ispravku traži dokaz da radi: test rezultat ili snimak ekrana.

### Najčešće greške

1. **Pregled samo pred lansiranje.** Tada je nalaza previše i nastaje panika. *Rešenje:* mali pregled posle svake funkcionalnosti, `ultra` samo za prekretnice.
2. **Slepo odobravanje svih ispravki odjednom.** Ne znaš šta si odobrio ni zašto. *Rešenje:* nalaz po nalaz, tri pitanja, pa odluka.
3. **Ignorisanje nalaza jer "aplikacija radi".** To što vrata nisu obijena ne znači da brava valja. *Rešenje:* ozbiljnost 7+ rešavaš pre lansiranja, uvek.
4. **Prihvatanje "popravio sam testove" bez gledanja.** Možda su obrisani. *Rešenje:* traži da ti pokaže šta je tačno promenjeno i rezultat testova pre i posle.
5. **Preskakanje `/security-review` posle "male" izmene prijave ili plaćanja.** Male izmene prave velike rupe. *Rešenje:* pravilo je mehaničko, dira login/pare/lične podatke → pregled, bez razmišljanja.

### Kontrolna lista

- [ ] Posle svake završene funkcionalnosti pokrećem `/code-review` (low/medium)
- [ ] Pred veliku prekretnicu razmatram `/code-review ultra` (svestan da se dodatno naplaćuje)
- [ ] `/security-review` pokrećem pred lansiranje i posle svake izmene prijave, plaćanja ili ličnih podataka
- [ ] Za svaki nalaz tražim: prost jezik, ozbiljnost 1-10 + najgori scenario, predlog ispravke
- [ ] Ispravke odobravam pojedinačno, ne paušalno
- [ ] Bar jednom pred lansiranje pustio sam prompt "zlonamernog korisnika"
- [ ] Periodično pokrećem `/simplify` za čišćenje koda
- [ ] Ne prihvatam "gotovo je" bez test rezultata, snimka ekrana ili loga
- [ ] Proveravam da testovi nisu obrisani ili oslabljeni da bi "prošli"

### Proveri znanje

**1. Kada koristiš `/code-review medium`, a kada `/code-review ultra`?**

Medium za svakodnevni ritam posle svake funkcionalnosti, brz, fokusiran na najvažnije. Ultra za najvažnije prekretnice (pred lansiranje, posle velikog refaktorisanja), multi-agent pregled celog brancha u oblaku, najtemeljniji, dodatno se naplaćuje i pokrećeš ga ti.

**2. Koja tri pitanja postavljaš za svaki nalaz pregleda?**

(1) Objasni prostim jezikom šta je problem. (2) Koliko je ozbiljno na skali 1-10 i šta je najgore što može da se desi? (3) Koji je predlog ispravke? Tek onda odobravaš, ili šalješ u backlog.

**3. Claude kaže da je popravio bag i da sada svi testovi prolaze. Šta tražiš pre nego što prihvatiš?**

Dokaz: rezultat testova i pregled šta je tačno izmenjeno. Posebno proveravaš da nijedan test nije obrisan ili oslabljen, tvrdnja bez dokaza se ne računa.


---

## Modul 9: Lansiranje: od tvog računara do interneta

Do sada je tvoj proizvod živeo samo na tvom računaru: radio je, prošao preglede kvaliteta iz Modula 8, ali niko osim tebe ne može da ga vidi. U ovom modulu izlazi na internet: prvo na probnu adresu koju vidiš samo ti, zatim na pravu, javnu adresu sa tvojim domenom.

### Šta ćeš naučiti

- Šta znači deploy i zašto se uvek radi u dva koraka: prvo proba, pa javnost
- Kako da povežeš projekat sa Vercel-om i objaviš ga uz pomoć Claude-a
- Šta su env varijable i zašto API ključevi nikad ne smeju u kod
- Zašto ti trebaju odvojene baze za testiranje i produkciju
- Pre-lansiranje checklist i strategiju mekog lansiranja

### Šta je deploy: otvaranje radnje

Zamisli da si nedeljama pravio nameštaj u svojoj radionici, ali radionica je zaključana i mušterije ne mogu da uđu. **Deploy** (izgovara se „diploj") je trenutak kad otvoriš radnju na glavnoj ulici: kopiraš aplikaciju sa svog računara na servere koji su stalno upaljeni i dostupni svima na internetu.

Tvoj računar nije dobar server: gasiš ga, nosiš ga na put, internet ti varira. Zato u ovom kursu koristimo **Vercel**, servis koji uzme tvoj kod sa GitHub-a (postavili smo ga u Modulu 3), sagradi aplikaciju i drži je dostupnom 24/7, a uz to odlično sarađuje sa Claude Code-om kroz vercel plugin.

### Pre nego što počneš

Dva preduslova. Prvo, besplatan nalog na vercel.com, obična registracija klikovima, kao na bilo kom servisu. Drugo, vercel plugin u Claude Code-u; zamoli Claude-a:

```
Hoću da dodam vercel plugin u ovaj projekat, provedi me kroz
instalaciju korak po korak.
```

Detaljna priča o plugin-ovima čeka te u Modulu 12; za sada je dovoljno da je instaliran, bez njega komande iz ovog modula ne postoje u tvojoj sesiji.

### Korak 1: Povezivanje: `/vercel:bootstrap`

Projekat zatim povezuješ sa Vercel nalogom komandom:

```
/vercel:bootstrap
```

Ona pokreće vođeni proces: proveri da li je sve spremno, poveže tvoj repozitorijum sa Vercel projektom i sredi env varijable (o njima za koji pasus). Ako te negde zaglavi, opiši Claude-u šta vidiš:

```
Pokrenuo sam /vercel:bootstrap i dobio poruku o grešci koju ne razumem.
Evo šta piše na ekranu: [nalepi poruku]. Objasni mi šta znači i provedi
me kroz rešenje korak po korak, kao nekoga ko ovo radi prvi put.
```

### Korak 2: Preview deploy: proba pre javnosti

Ovde dolazi najvažnija navika ovog modula: **nikad ne ideš direktno u produkciju**. Prvo praviš preview deploy, probnu verziju na privatnom linku koji znaš samo ti. To je generalna proba u pozorištu: sve je kao na premijeri, samo publika još nije ušla.

```
/vercel:deploy
```

Bez dodatnih argumenata, ova komanda pravi upravo preview deploy. Kad se završi, otvori dobijeni link i prođi kroz aplikaciju kao prvi korisnik: registruj se, klikni svako dugme, probaj glavni tok od početka do kraja. Na svom računaru si testirao hiljadu puta, ali server je drugačije okruženje, i baš tu isplivaju greške tipa „kod mene radi".

### Korak 3: Produkcija

Tek kad preview verzija radi besprekorno, šalješ u produkciju:

```
/vercel:deploy prod
```

To je premijera, aplikacija je na javnoj adresi, dostupna svakome. Vercel automatski daje adresu oblika `tvoj-projekat.vercel.app`, sasvim dovoljnu za početak.

### Env varijable: ključevi od stana se ne lepe na vrata

Tvoja aplikacija koristi tajne: API ključ za OpenAI, lozinku za bazu, slično. **API ključ** je kao ključ od stana, ko ga ima, ulazi i troši o tvom trošku. Ako ključ završi u kodu, a kod ode na GitHub, to je kao da si ga zalepio na ulazna vrata sa ceduljom „izvolite". Botovi non-stop pretražuju GitHub baš tražeći ovakve procurele ključeve, zloupotreba stiže za par minuta.

Rešenje su **env varijable** (environment variables, „promenljive okruženja"): tajne se čuvaju van koda, u posebnom sefu, lokalno u fajlu `.env.local` koji nikad ne ide na git, a na Vercel-u u podešavanjima projekta. Kod onda kaže samo „uzmi ključ iz sefa", bez ključa u sebi.

Dobra vest: ovo ne radiš ručno, zamoli Claude-a:

```
Proveri ceo projekat: da li je neki API ključ, lozinka ili tajna upisana
direktno u kod? Ako jeste, prebaci je u env varijablu, dodaj je u
.env.local, i proveri da je .env.local naveden u .gitignore fajlu
(da nikad ne ode na GitHub). Zatim mi izlistaj sve env varijable koje
moram da unesem u Vercel za produkciju, sa objašnjenjem čemu svaka služi.
```

Komanda `/security-review` iz Modula 8 takođe hvata procurele tajne pre nego što odu na GitHub, još jedan razlog da je pokrećeš redovno.

### Tvoj domen: adresa radnje

`tvoj-projekat.vercel.app` radi, ali deluje privremeno. Sopstveni domen (`tvojproizvod.com` ili `.rs`) je adresa tvoje radnje i deo brenda: kupuješ ga kod registra (Namecheap, GoDaddy, za .rs domene domaći registri), pa ga povežeš sa Vercel projektom kroz DNS podešavanja, internet imenik koji ukucanu adresu vodi na pravi server. U praksi je to unošenje dve-tri vrednosti koje ti Vercel prikaže. Zamoli Claude-a da te provede:

```
Kupio sam domen mojproizvod.rs kod [ime registra]. Provedi me korak po
korak kroz povezivanje tog domena sa mojim Vercel projektom: šta tačno
da unesem u DNS podešavanja kod registra i kako da proverim da je uspelo.
```

### Dve baze: nikad ne testiraš na pravim podacima

Ako tvoj proizvod koristi bazu podataka (preko supabase plugin-a iz Modula 5), od lansiranja važi gvozdeno pravilo: **odvojena baza za razvoj, odvojena za produkciju**.

Zašto? Zamisli da posle lansiranja kažeš Claude-u „obriši sve test naloge", a povezan si na produkcijsku bazu, upravo si obrisao prave korisnike. Sa dve baze takva greška košta te nula: razvojnu slobodno puniš, brišeš i lomiš, produkcijska ostaje netaknuta.

```
Hoću odvojene Supabase baze za razvoj i produkciju. Postavi projekat tako
da lokalni razvoj koristi razvojnu bazu, a Vercel produkcija produkcijsku,
preko env varijabli. Na kraju mi pokaži kako da u svakom trenutku proverim
na koju bazu sam trenutno povezan.
```

### Pre-lansiranje checklist i probno lansiranje

Pre nego što adresu podeliš sa svetom, prođi listu na kraju modula. Dve stavke zaslužuju dodatnu reč:

**Pravne stranice.** Uslovi korišćenja i politika privatnosti nisu ukras, ako prikupljaš bilo kakve podatke korisnika (čak i samo imejl), zakonski su obavezne. Claude ti može sastaviti solidan nacrt prilagođen tvom proizvodu; za ozbiljan biznis daj ga pravniku na pregled.

**Praćenje grešaka.** Kad korisniku nešto pukne, najčešće ti neće javiti, samo će otići. Zato zamoli Claude-a da u aplikaciju uveže servis za praćenje grešaka (npr. Sentry), koji ti javi čim se greška pojavi. Više o tome u Modulu 10.

I na kraju, **probno lansiranje** („meko lansiranje"). Ne objavljuj proizvod odmah svima: prvo ga pošalji grupi od 5–15 poznanika i zamoli ih da ga koriste nedelju dana. Oni će naći probleme na koje ne bi pomislio, a oprostiće ti ih, nepoznata publika neće, ona se ne vraća. Tek kad prva grupa prođe bez ozbiljnih problema, ideš javno.

### Vežba

0. Ako već nisi: nalog na vercel.com i vercel plugin (prompt iz odeljka „Pre nego što počneš").
1. Pokreni Claude Code u folderu projekta i izvrši `/vercel:bootstrap`. Ako zapne, nalepi Claude-u poruku o grešci i traži objašnjenje.
2. Pokreni prompt za proveru tajni iz odeljka o env varijablama. Uveri se da nijedan ključ nije u kodu i da je `.env.local` u `.gitignore`.
3. Napravi preview deploy: `/vercel:deploy`. Otvori dobijeni link i prođi glavni tok kao novi korisnik. Zapiši svaki problem.
4. Ako si našao probleme, reši ih sa Claude-om (ritam iz Modula 6), pa ponovi preview.
5. Pokreni `/security-review`, a zatim zamoli Claude-a: „Pokreni sve testove i pokaži mi izlaz", oba moraju biti čista.
6. Tek tada: `/vercel:deploy prod`. Otvori javnu adresu sa telefona, ne sa svog računara, i čestitaj sebi.
7. Pošalji link trojici poznanika sa molbom da probaju i jave šta ih je zbunilo.

### Najčešće greške

1. **Prvi deploy ide pravo u produkciju.** „Radi kod mene" ne znači „radi na serveru". Rešenje: uvek prvo `/vercel:deploy` (preview), klikći kroz aplikaciju na privatnom linku, pa tek onda `prod`.
2. **API ključ završi na GitHub-u.** Najskuplja greška ovog modula, botovi je nalaze za par minuta. Rešenje: prompt za proveru tajni pre svakog deploy-a; procureli ključ odmah poništi kod izdavaoca (OpenAI, Supabase…) i napravi novi, brisanje iz koda nije dovoljno, git pamti istoriju.
3. **Jedna baza za sve.** Testiranjem nove funkcije obrišeš ili iskvariš prave podatke korisnika. Rešenje: odvojena razvojna i produkcijska baza od prvog dana, povezane preko env varijabli.
4. **Aplikacija radi na preview linku, ali ne u produkciji.** Najčešći uzrok: env varijable unete za preview, ali ne i za produkciju. Rešenje: zamoli Claude-a da uporedi okruženja i izlista šta nedostaje.
5. **Veliko lansiranje bez probne publike.** Sve karte na javnu objavu prvog dana, pa prvi utisak pokvari bag koji bi poznanik našao za sat. Rešenje: probno lansiranje, mala grupa prvo, javnost posle.

### Kontrolna lista

- [ ] `/vercel:bootstrap` izvršen, projekat povezan sa Vercel-om
- [ ] Nijedna tajna nije u kodu; sve su u env varijablama, `.env.local` je u `.gitignore`
- [ ] Env varijable unete u Vercel i za preview i za produkcijsko okruženje
- [ ] Preview deploy pregledan klik-po-klik, glavni tok radi
- [ ] Svi testovi zeleni, `/security-review` bez kritičnih nalaza
- [ ] Odvojene baze za razvoj i produkciju; backup produkcijske baze uključen
- [ ] Praćenje grešaka (npr. Sentry) uvezano i proveren da prijavljuje
- [ ] Stranice za uslove korišćenja i privatnost objavljene
- [ ] Sopstveni domen povezan i radi (proveri sa drugog uređaja)
- [ ] Soft lansiranje: 5–15 poznanika koristilo proizvod pre javne objave

### Proveri znanje

**Zašto se nikad ne ide direktno u produkciju, nego prvo na preview deploy?**
Server je drugačije okruženje od tvog računara, greške koje lokalno ne vidiš isplivaju tek tamo. Preview je generalna proba na privatnom linku: greške hvataš pre korisnika.

**Šta su env varijable i šta uraditi ako API ključ ipak završi na GitHub-u?**
Tajne (ključevi, lozinke) koje se čuvaju van koda, lokalno u `.env.local`, na Vercel-u u podešavanjima projekta. Procureli ključ odmah poništi kod izdavaoca i napravi novi; brisanje iz koda ne pomaže, git pamti istoriju.

**Zašto su potrebne dve odvojene baze podataka?**
Da razvoj nikad ne dira prave podatke korisnika: razvojnu bazu smeš da lomiš bez posledica, produkcijska ostaje netaknuta, a koju kod koristi određuju env varijable po okruženju.


---

## Modul 10: Život posle lansiranja

Otvorio si vrata radnje, prvi kupci ulaze, i sada počinje pravi posao. Lansiranje iz Modula 9 nije cilj, nego startna linija: proizvod tek sada počinje da živi, da se kvari, da raste i da ti šalje signale. U ovom modulu učiš kako da ga slušaš i neguješ, a da te to ne pojede pola dana.

### Šta ćeš naučiti

- Kako da pratiš zdravlje proizvoda kroz logove i greške, bez ijednog tehničkog alata koji sam moraš da čitaš
- Kako da uz `/loop` nadgledaš deploy dok je sesija otvorena, a uz `/schedule` praviš rutine koje rade i kad je računar ugašen
- Kako da povratne informacije korisnika pretvoriš u `docs/backlog.md` i prioritizuješ ih sa Claude-om
- Zašto svaka nova funkcionalnost i posle lansiranja prolazi isti disciplinovani ciklus iz Modula 6
- Kako da prepoznaš trenutak za refaktorisanje, i zašto je to sređivanje magacina, ne gubljenje vremena

### Proizvod je živ organizam

Posle lansiranja ljudi koriste proizvod na načine koje nisi predvideo, stari telefoni, spor internet, podaci kakve nisi ni zamislio, i neke od tih situacija proizvešće **greške**. To je normalno: razlika između proizvoda koji raste i onog koji umire nije u tome da li grešaka ima, nego da li ih neko primećuje i popravlja.

Tvoja nova uloga ima tri dela: **posmatraj** (da li sve radi?), **slušaj** (šta korisnici žele?), **iteriraj** (popravljaj i dograđuj istim ritmom kao i do sada).

### Posmatraj: logovi su puls tvog proizvoda

**Log** je dnevnik koji aplikacija sama vodi, svaki zahtev, svaka greška, svaki neuspeli pokušaj ostavlja zapis, kao knjiga žalbi koja se piše sama. Dobra vest: ne moraš da naučiš da je čitaš. Claude ume, a ti samo postavljaš pitanja na srpskom.

Otvori sesiju u folderu projekta i pitaj:

```
Pregledaj logove naše produkcije od juče. Ima li grešaka koje se
ponavljaju? Ako ima, grupiši ih po tipu, reci mi koliko korisnika je
pogođeno i koja je najhitnija, objasni mi to rečima, bez žargona.
```

Claude će povući logove (kroz hosting alate o kojima smo pričali u Modulu 9 i Modulu 12), pročitati ih umesto tebe i prevesti na ljudski: „Tri korisnika su pokušala da otpreme fajl veći od dozvoljenog i dobila nerazumljivu poruku." Na osnovu toga ti, kao direktor, odlučuješ šta je prioritet.

Navika koja te spasava: ovakvu proveru radi posle svakog deploy-a i bar jednom nedeljno, čak i kad „sve izgleda u redu".

### `/loop`: dežurni stražar dok je sesija otvorena

Upravo si pustio novu verziju u produkciju i želiš da neko motri prvih sat vremena? Umesto da svakih pet minuta osvežavaš ekran, zaduži Claude-a:

```
/loop 10m Proveri da li je produkcija dostupna i pregledaj sveže logove.
Ako se pojavi nova greška koja se ponavlja, opiši mi je i predloži uzrok.
Ako je sve u redu, samo kratko javi "sve čisto".
```

`/loop 10m` znači: ponavljaj ovaj zadatak na svakih 10 minuta. Za ovaj modul je bitno jedno ograničenje: petlja živi samo dok je sesija otvorena i **ne radi kad je računar ugašen**, zato je idealna za „dežurstvo" posle deploy-a, a za trajne provere postoji `/schedule`. Kako `/loop` radi u detalje (intervali, dinamički režim, prekid, ograničenja), u Modulu 7.

### `/schedule`: rutine koje rade i dok spavaš

`/schedule` pravi **Routines**, zakazane agente koji rade u oblaku (na tuđim serverima, ne na tvom računaru), pa funkcionišu i kad je tvoj laptop u rancu. To je kao da si zaposlio noćnog čuvara.

Dve rutine koje preporučujem svakom proizvodu od prvog dana:

✅ Dnevni izveštaj o greškama:

```
/schedule Svakog jutra u 8h: pregledaj produkcijske logove za poslednja
24 sata. Napravi kratak izveštaj: broj grešaka, ima li novih tipova
grešaka u odnosu na juče, i jedna rečenica preporuke. Piši jednostavno,
za netehničku osobu.
```

✅ Nedeljna provera zastarelih zavisnosti (**zavisnosti** su tuđi delovi koda koje tvoj projekat koristi, kao sastojci u receptu; vremenom izlaze novije, bezbednije verzije):

```
/schedule Svakog ponedeljka u 9h: proveri da li projekat koristi
zastarele zavisnosti, posebno one sa poznatim bezbednosnim problemima.
Napravi listu: šta je zastarelo, koliko je rizično, i šta predlažeš
da ažuriramo prvo. Ništa ne menjaj, samo izvesti.
```

Primeti obrazac u oba prompta: jasno **šta** se proverava, **kada**, u **kom obliku** stiže izveštaj, i ograničenje „ne menjaj ništa". Rutina izveštava, ti odlučuješ.

### Slušaj: backlog kao spisak želja

Korisnici će ti pisati: imejlom, porukom, usmeno na kafi. Svaka takva poruka je zlato, ali zlato koje se lako zaturi. Zato uvedi jedno mesto za sve: `docs/backlog.md`. **Backlog** je spisak svega što bi proizvod jednog dana mogao da dobije, spisak želja, ne spisak obaveza.

Kad stigne povratna informacija, ne trči da je odmah implementiraš. Samo je zabeleži:

```
Dodaj u docs/backlog.md: korisnica Mira kaže da bi volela da može da
preuzme izveštaj kao PDF. Drugi korisnik ovo pominje ove nedelje.
Zapiši datum i ko je tražio.
```

Onda, recimo jednom u dve nedelje, sedneš sa Claude-om na „sastanak o prioritetima":

```
Pročitaj docs/backlog.md i pomozi mi da rangiram stavke po odnosu
vrednost/trud. Za svaku proceni: koliko korisnika dobija korist (malo/
srednje/mnogo) i koliko je posla za implementaciju (sati/dani/nedelje).
Predloži top 3 za sledeću iteraciju i obrazloži. Konačnu odluku donosim ja.
```

Odnos vrednost/trud je tvoj kompas: funkcionalnost koja usreći mnogo korisnika a traži dan posla pobeđuje funkcionalnost koja usreći jednog a traži mesec. Claude procenjuje trud bolje od tebe (vidi kod iznutra), ti procenjuješ vrednost bolje od njega (poznaješ korisnike). Zajedno ste kompletan tim.

### Iteriraj: disciplina se ne opušta

Najveća zamka posle lansiranja: „pa sad samo brzo da dodam ovo sitno, ne treba mi ceo ciklus". Treba ti. Baš zato što sada postoje pravi korisnici, cena greške je veća nego ikad, pre lansiranja bag je nervirao tebe, sada nervira ljude koji ti veruju.

Svaka nova funkcionalnost, ma koliko sitna, prolazi isti ciklus iz Modula 6: plan mode pre koda, mali koraci, dokaz da radi (test, snimak ekrana, log, princip iz Modula 1), pa `/code-review` i `/security-review` pre objavljivanja (Modul 8). Razlika: na kraju ciklusa sada stoji deploy u produkciju, i `/loop` dežurstvo posle njega.

### Refaktorisanje: sređivanje magacina

Kako proizvod raste, kod se prirodno zapetljava, kao magacin u koji mesecima samo ubacuješ robu. Jednog dana ni ti ni Claude više ništa ne nalazite brzo, a svaka nova funkcionalnost traje duplo duže.

**Refaktorisanje** je sređivanje tog magacina: kod se reorganizuje da bude pregledniji i lakši za dalji rad, a proizvod spolja radi potpuno isto. Korisnici ne vide razliku, ali svaka sledeća funkcionalnost stiže brže.

Ti nećeš znati da prepoznaš zapetljan kod, i ne moraš. Claude će ti sam reći („ovaj deo je postao težak za održavanje, predlažem da ga sredimo"), ili ga ti povremeno pitaj:

```
Pogledaj naš kod iz ptičje perspektive. Ima li delova koji su se
zapetljali toliko da usporavaju dalji razvoj? Ako ima, predloži plan
sređivanja: šta, zašto, koliko posla, i kako proveravamo da se
ponašanje proizvoda nije promenilo. Ne menjaj ništa dok ne odobrim.
```

Refaktorisanje je svoja iteracija, sa svojim testovima i review-om, nikad „usput", a `/simplify` ti je saveznik za čišćenje izmenjenog koda (Modul 8).

### Vežba

1. Otvori sesiju u folderu svog projekta i zatraži: `Pregledaj logove produkcije od juče, ima li grešaka koje se ponavljaju? Objasni mi nalaze bez žargona.`
2. Napravi fajl spiska želja: `Napravi docs/backlog.md sa sekcijama "Novo", "Rangirano" i "Urađeno", i ubaci tri ideje koje ti sad izdiktiram.` Izdiktiraj tri stvarne želje (svoje ili korisnika).
3. Zatraži rangiranje: `Rangiraj stavke iz docs/backlog.md po odnosu vrednost/trud i predloži šta prvo da radimo.` Pročitaj predlog i sam donesi konačnu odluku.
4. Postavi jednu trajnu rutinu: `/schedule Svakog jutra u 8h pregledaj produkcijske logove i pošalji mi kratak izveštaj o greškama, pisan za netehničku osobu.`
5. Sledeći put kad radiš deploy, odmah posle njega pokreni: `/loop 10m Proveri produkciju i sveže logove; javi ako se pojavi nova greška.` Posle sat vremena prekini petlju sa `Esc`.

### Najčešće greške

1. **„Lansirao sam, gotovo je", pa ne pogledaš logove nedeljama.** Greške se gomilaju u tišini, korisnici tiho odlaze. Rešenje: `/schedule` dnevni izveštaj o greškama od prvog dana, pa makar svaki dan pisalo „sve čisto".
2. **Oslanjanje na `/loop` za noćno nadgledanje.** `/loop` radi samo dok je sesija otvorena i računar upaljen, ako poklopiš laptop, stražar je otišao kući. Rešenje: `/loop` za dežurstvo posle deploy-a, `/schedule` za sve što mora da radi non-stop.
3. **Implementiranje svake želje čim stigne.** Najglasniji korisnik nije uvek najvažniji, a skakanje sa zadatka na zadatak ubija fokus. Rešenje: sve u `docs/backlog.md`, prioritizacija po vrednost/trud jednom u dve nedelje.
4. **„Sitna izmena" direktno u produkciju, bez ciklusa.** Upravo sitne izmene bez plana i provere najčešće obore proizvod, jer ih niko ozbiljno ne pogleda. Rešenje: i jedna rečenica izmene prolazi ciklus iz Modula 6, plan, dokaz, review, deploy.
5. **Odlaganje refaktorisanja dok ne postane kriza.** Kad svaka nova funkcionalnost traje duplo duže, magacin je već zatrpan do plafona. Rešenje: jednom mesečno pitaj Claude-a da li se neki deo koda zapetljao i tretiraj sređivanje kao ravnopravnu stavku backloga.

### Kontrolna lista

- [ ] Posle svakog deploy-a tražim od Claude-a pregled svežih logova (ili pokrenem `/loop` dežurstvo)
- [ ] Postavljena je `/schedule` rutina: dnevni izveštaj o greškama, pisan za netehničku osobu
- [ ] Postavljena je `/schedule` rutina: nedeljna provera zastarelih zavisnosti (samo izveštava, ništa ne menja)
- [ ] Postoji `docs/backlog.md` i svaka povratna informacija korisnika završi u njemu istog dana
- [ ] Backlog rangiram sa Claude-om po odnosu vrednost/trud bar jednom u dve nedelje
- [ ] Svaka nova funkcionalnost prolazi pun ciklus iz Modula 6, bez prečica „jer je sitno"
- [ ] Povremeno pitam Claude-a da li je vreme za refaktorisanje, i sređivanje odobravam kao posebnu iteraciju

### Proveri znanje

1. **U čemu je ključna razlika između `/loop` i `/schedule` rutina?**
2. **Stiglo ti je pet predloga korisnika u jednoj nedelji. Šta radiš s njima i kako biraš koji ide prvi?**
3. **Šta je refaktorisanje i ko odlučuje da se uradi?**

Odgovori:

1. `/loop` ponavlja zadatak unutar otvorene sesije, radi samo dok je sesija živa i računar upaljen. `/schedule` pravi rutine koje rade u oblaku, po rasporedu, i kad je tvoj računar ugašen. Dežurstvo posle deploy-a = `/loop`; trajne provere = `/schedule`.
2. Ništa ne implementiram odmah: sve zapisujem u `docs/backlog.md` (sa datumom i ko je tražio), pa sa Claude-om rangiram po odnosu vrednost/trud. Claude predlaže redosled, ja donosim konačnu odluku.
3. Refaktorisanje je reorganizacija koda da bude pregledniji i lakši za dalji razvoj, dok proizvod spolja radi isto. Claude predlaže kad se kod zapetlja (ili ga ja pitam), a ja odobravam i tretiram to kao posebnu iteraciju sa proverama.


---

## Modul 11: Majstorstvo promptovanja: 10 pravila

Do sada si naučio ceo proces: od ideje, preko plana, do lansiranja. Ovaj modul je tvoja brusilica, deset pravila koja razdvajaju prompt koji "nekako prođe" od prompta koji iz prve da tačno ono što si zamislio. Nijedno pravilo nije teorija; svako je nastalo iz situacije u kojoj je neko izgubio sat vremena jer je rekao premalo, previše ili pogrešnim redom. Formulu savršenog prompta upoznao si u Modulu 6, ovde je razlažemo na zanatske detalje.

### Šta ćeš naučiti

- Kako da svaki zadatak definišeš tako da Claude tačno zna kada je "gotovo"
- Kako da ograničenjima i referencama sprečiš da Claude radi više (ili manje) nego što treba
- Kada da tražiš plan, a kada da ideš direktno
- Kako da od Claude-a dobiješ dokaz umesto uveravanja
- Kako da ispravke pretvoriš u trajna pravila, da iste stvari ne objašnjavaš dvaput

### Pravilo 1: Kriterijum prihvatanja u svakom zadatku

Claude radi dok ne ispuni ono što je tražio, ali ako ne kažeš kako izgleda "gotovo", on sam odlučuje gde da stane. Kriterijum prihvatanja je kao spisak primopredaje sa majstorom: bez njega, "renovirano kupatilo" znači šta god majstor misli da znači.

❌ Loš prompt:

```
Sredi formu za prijavu na bilten.
```

✅ Dobar prompt:

```
Sredi formu za prijavu na bilten. Gotovo je kada:
1. Prazno polje za imejl prikazuje poruku "Unesi imejl adresu" na srpskom
2. Neispravan imejl (bez @) prikazuje "Imejl adresa nije ispravna"
3. Posle uspešne prijave forma se zameni porukom "Hvala, na listi si!"
4. `npm test` prolazi bez grešaka
```

Razlika: prvi prompt prepušta Claude-u da pogađa šta "sredi" znači, a drugi mu daje merljivu liniju cilja koju i ti i on možete da proverite.

### Pravilo 2: Reci za šta optimizuješ

Svaka odluka u kodu je kompromis, brzina ili čitljivost, jednostavnost ili fleksibilnost. Ako ne kažeš šta ti je prioritet, Claude bira sam, često "za svaki slučaj" gradeći više nego što ti treba.

❌ Loš prompt:

```
Dodaj upload profilne slike.
```

✅ Dobar prompt:

```
Dodaj upload profilne slike. Optimizuj za jednostavnost, ovo je MVP
sa najviše 100 korisnika. Najprostije rešenje koje radi; ne dodavaj
keširanje, obradu slika ni biblioteke koje nisam tražio.
```

Razlika: rečenica "optimizuj za jednostavnost" pretvorila je otvoren zadatak u zadatak sa jasnim kompasom, pa nema prebukiranih rešenja koja kasnije moraš da održavaš.

### Pravilo 3: Eksplicitna ograničenja

Claude je vredan, ponekad previše. Ako ne kažeš šta NE sme da dira, može usput da "popravi" i stvari koje su radile. Ograničenja su kao traka kojom moler oblepi prozore: definišu gde se posao završava.

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

Sesija je jedan razgovor, a kontekst razgovora se puni kao radni sto, što više nepovezanih stvari na njemu, veća šansa da se nešto pomeša. Tri zadatka u jednom promptu znače da Claude deli pažnju, a tebi je teže da proveriš svaki posebno.

❌ Loš prompt:

```
Popravi bag sa prijavom, dodaj tamnu temu i napiši mi tekst za
prodajnu stranicu.
```

✅ Dobar prompt:

```
Samo jedan zadatak: popravi bag gde se aplikacija zamrzne kada
korisnik tri puta unese pogrešnu lozinku. Gotovo je kada mogu pet
puta da unesem pogrešnu lozinku i svaki put dobijem poruku o grešci.
```

…a zatim `/clear` pa sledeći zadatak u svežoj sesiji.

Razlika: jedan zadatak znači punu pažnju, čistu proveru i čist commit, a `/clear` između zadataka drži radni sto prazan.

### Pravilo 6: Plan za veliko: direktno za malo

Za sitnice je plan gubljenje vremena; za velike stvari je preskakanje plana kockanje. Plan mode (uključuje se prečicom Shift+Tab, koja kruži kroz režime rada) tera Claude-a da prvo istraži i predloži plan, bez menjanja fajlova dok ne odobriš, detaljno u Modulu 5.

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

Čim vidiš da je Claude krenuo pogrešnim smerom, pritisni `Esc`, to ga prekida usred rada i odmah možeš da ga preusmeriš. Čekanje da završi pa ispravljanje je kao da pustiš taksistu da te odveze do pogrešne adrese jer ti je neprijatno da ga prekineš.

❌ Loš pristup (deset minuta ćutanja, pa):

```
Sve ovo što si napravio je pogrešno. Nisam hteo novu stranicu.
Obriši sve i počni ispočetka.
```

✅ Dobar pristup (`Esc` posle prvih redova, pa):

```
Stani, pogrešan smer. Ne treba mi nova stranica za podešavanja,
nego izmena postojeće na /podesavanja. Dodaj sekciju "Notifikacije"
na dno te stranice.
```

Razlika: rani prekid je sačuvao i vreme i kontekst, Claude još pamti zadatak i samo ga preusmeravaš, umesto da čistiš pogrešno urađen posao.

### Pravilo 8: Za odluke traži opcije + preporuku

Kad pitaš "šta je najbolje?", dobiješ jedan odgovor koji ne umeš da preispitaš. Kad tražiš opcije sa preporukom, dobiješ i odluku i razloge, pa kao direktor odlučuješ informisano, bez tehničkog znanja.

❌ Loš prompt:

```
Koja baza podataka je najbolja?
```

✅ Dobar prompt:

```
Treba mi baza za listu čekanja: čuvam imejl adrese i datum prijave,
očekujem do 10.000 unosa. Daj mi 2-3 opcije sa prednostima i manama
ZA MOJ SLUČAJ, pa preporuči jednu i obrazloži u dve rečenice.
Optimizuj za jednostavnost održavanja, radim sam.
```

Razlika: kontekst + zahtev za opcijama pretvorili su generičan odgovor "zavisi" u odluku skrojenu za tvoju situaciju, koju razumeš i možeš da braniš.

### Pravilo 9: Traži dokaz, a ne tvrdnju

"Trebalo bi da radi" nije dokaz, to je nada. Claude može da pokrene testove, podigne dev server, klikće po aplikaciji u pregledaču i napravi snimak ekrana. Traži to, kao što od majstora tražiš da pred tobom odvrne slavinu pre nego što platiš.

❌ Loš prompt:

```
Jesi li siguran da forma sada radi?
```

✅ Dobar prompt:

```
Dokaži da forma radi: pokreni `npm test` i pokaži mi izlaz. Zatim
pokreni aplikaciju, popuni formu ispravnim podacima i napravi
snimak ekrana poruke o uspehu. Pa probaj i sa neispravnim imejlom i
pokaži snimak ekrana poruke o grešci.
```

Razlika: umesto uveravanja dobio si test izlaz i snimke ekrana, dokaze koje i sam možeš da pogledaš, bez ijednog reda koda (princip dokaza iz Modula 1).

### Pravilo 10: Svaku ponovljenu ispravku upiši u CLAUDE.md

Claude ne pamti ništa između sesija, osim fajla `CLAUDE.md` i memorije. Ako istu ispravku kucaš drugi put, to nije poruka za razgovor, to je pravilo za `CLAUDE.md`. Najbrži način: počni poruku znakom `#` i Claude napomenu trajno zabeleži.

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

Ako tvoj projekat nema stranicu sa cenama, primeni isti postupak na bilo koju svoju stranicu, zameni "stranicu sa cenama" onom koju imaš.

1. Otvori projekat i pokreni `claude` (ili desktop aplikaciju).
2. Prepiši prompt tako da ima kriterijum prihvatanja (Pravilo 1): šta tačno znači "bolja"? Npr. "tri paketa jedan pored drugog, srednji istaknut".
3. Dodaj za šta optimizuješ (Pravilo 2), npr. "optimizuj za jasnoću, posetilac za 5 sekundi mora da vidi razliku između paketa".
4. Dodaj ograničenja (Pravilo 3), šta ne sme da se menja (cene, tekstovi, ostale stranice).
5. Dodaj referencu (Pravilo 4), "stil kartica kao na početnoj stranici".
6. Pošalji prompt. Dok Claude radi, drži prst na `Esc`, ako krene pogrešno, prekini i preusmeri (Pravilo 7).
7. Na kraju traži dokaz (Pravilo 9): snimak ekrana stranice na desktopu i na telefonu.
8. Ako si Claude-a morao nešto da ispravljaš, a slutiš da će se ponoviti, upiši pravilo porukom koja počinje sa `#` (Pravilo 10).

Uporedi rezultat sa onim što bi dobio od prvobitnog prompta. Razlika je tvoj napredak.

### Najčešće greške

1. **Roman umesto prompta.** Deset pasusa konteksta u kojima se zadatak izgubi. Rešenje: struktura, jedan red šta, kriterijum gotovog, ograničenja, referenca. Sve preko toga je šum.
2. **Prompt-pregovaranje posle lošeg rezultata.** Pet poruka "ne, mislio sam…" u istoj sesiji puni kontekst pogrešnim pokušajima. Rešenje: posle dva neuspela kruga, `/clear` i nov, bolji prompt iz početka, sa onim što si naučio iz neuspeha.
3. **Kriterijum koji se ne može proveriti.** "Da bude profesionalno" niko ne može da izmeri, ni ti ni Claude. Rešenje: prevedi utisak u nešto vidljivo, "isti razmaci kao na početnoj", "test prolazi", "snimak ekrana pokazuje X".
4. **Pitanje koje već sadrži odgovor.** "Je l' da da je ovo dobro rešenje?", Claude će se rado složiti. Rešenje: pitaj neutralno, "koje su mane ovog rešenja?" ili traži opcije + preporuku (Pravilo 8).
5. **Ispravljanje umesto zapisivanja.** Istu stilsku primedbu kucaš svake sesije ispočetka. Rešenje: drugi put kad nešto ispravljaš, to je signal za `#` poruku i `CLAUDE.md` (Pravilo 10).

### Kontrolna lista

Pre nego što pošalješ važan prompt, proveri:

- [ ] Postoji kriterijum prihvatanja, znam tačno kako izgleda "gotovo"
- [ ] Rekao sam za šta optimizujem (brzina, jednostavnost, izgled…)
- [ ] Naveo sam šta NE sme da se menja
- [ ] Gde postoji dobar primer u projektu, pokazao sam na njega umesto da opisujem
- [ ] U prompt sam stavio jedan zadatak, ne tri
- [ ] Za velik zadatak tražim plan pre koda; za sitnicu idem direktno
- [ ] Spreman sam da pritisnem `Esc` čim vidim pogrešan smer
- [ ] Za odluke tražim opcije sa preporukom, ne "šta je najbolje"
- [ ] Tražim dokaz (test izlaz, snimak ekrana, log), ne tvrdnju
- [ ] Ponovljene ispravke upisujem u `CLAUDE.md` porukom sa `#`

### Proveri znanje

**1. Zašto je "Gotovo je kada `npm test` prolazi i snimak ekrana pokazuje poruku o uspehu" bolji kriterijum od "da sve radi kako treba"?**

Zato što je proverljiv: i ti i Claude možete objektivno da utvrdite da li je ispunjen. "Radi kako treba" je utisak, a utisak ne može da se izmeri, pa svako od vas dvoje može da ga tumači drugačije.

**2. Claude je krenuo da pravi novu stranicu, a ti si hteo izmenu postojeće. Šta radiš i zašto baš tada?**

Pritisneš `Esc` odmah, čim primetiš pogrešan smer, i u sledećoj poruci ga preusmeriš. Što ranije prekineš, manje pogrešnog posla ima da se čisti, a Claude još drži ceo zadatak u kontekstu pa je preusmeravanje trenutno.

**3. Treći put ove nedelje ispravljaš Claude-a da dugmad piše malim slovima. Šta je pravi potez?**

Pošalješ poruku koja počinje znakom `#` (npr. `# Tekst na dugmadima uvek malim slovima`), Claude to trajno zabeleži, pa pravilo važi u svim budućim sesijama i više ga ne objašnjavaš.


---

## Modul 12: Ekosistem: plugin-ovi, skill-ovi i MCP konektori

Do sada si radio sa Claude-om kao sjajnim generalistom: zna da planira, piše kod, testira, popravlja. Ali zamisli da svom timu možeš da dodaš specijaliste, dizajnera koji ne pravi generične sajtove, stručnjaka za hosting koji zna svaki detalj objavljivanja, bibliotekara koji uvek ima najnoviju dokumentaciju pri ruci. Upravo to rade plugin-ovi, skill-ovi i MCP konektori: ne menjaju Claude-a, nego mu daju nova znanja i nove veze sa svetom. Ti ostaješ direktor, samo sada biraš i koga ćeš "zaposliti".

### Šta ćeš naučiti

- Razliku između plugin-a, skill-a i MCP konektora, i analogiju koja sve troje drži na okupu
- Koji su preporučeni plugin-ovi i kada ti koji treba (laičkim jezikom, bez tehničke magle)
- Zašto je `context7` posebno važan i šta znači "zastarelo znanje o bibliotekama"
- Kako MCP konektori povezuju Claude sa servisima koje već koristiš (Figma, Slack, Notion)
- Princip minimalnog izbora i bezbednosno pravilo koje ne smeš da preskočiš

### Tri pojma, jedna analogija

Zamisli da vodiš firmu i zapošljavaš ljude.

**Plugin** je kao da zaposliš celog specijalistu, paket veština i alata koji se instalira u Claude Code. Kad dodaš `vercel` plugin, Claude odjednom "zna" sve o objavljivanju sajtova na Vercel platformi: dobio si stručnjaka za hosting u timu.

**Skill** je konkretna veština tog specijaliste, nešto što pozivaš komandom koja počinje kosom crtom, na primer `/vercel:deploy`. Ako je plugin zaposleni, skill je stavka u njegovom opisu posla: tačno definisan zadatak koji ume da odradi od početka do kraja. Jedan skill si već sreo: `brainstorm` iz Modula 4 dolazi iz `product-management` plugin-a; isti plugin donosi i `write-spec`, njegov par za pisanje specifikacije.

**MCP konektor** je nešto drugačiji, to nije veština, nego most ka spoljnom servisu. MCP (Model Context Protocol) je standard koji omogućava Claude-u da "vidi" i koristi tvoje druge alate: Figma dizajne, Slack poruke, Notion stranice. Ako je plugin zaposleni, MCP konektor je službeni telefon kojim taj zaposleni zove druge firme i razmenjuje podatke sa njima.

Kratko: plugin = paket veština, skill = konkretna veština koju pozivaš sa `/imenom`, MCP konektor = most ka spoljnom servisu.

### Preporučeni plugin-ovi: ko ti treba i kada

Evo tima specijalista koji se najčešće isplati, sa opisom posla za svakog:

**`vercel`**, tvoj stručnjak za hosting i objavljivanje. Donosi skill-ove poput `/vercel:bootstrap` (priprema projekta za objavljivanje) i `/vercel:deploy` (samo objavljivanje), plus rad sa env varijablama, tajnim podešavanjima poput API ključeva. Treba ti čim hoćeš da tvoj proizvod bude dostupan na internetu, a ne samo na tvom računaru. Detaljno smo ga koristili u Modulu 9.

**`supabase`**, stručnjak za bazu podataka i prijavu korisnika (auth). Baza podataka je mesto gde tvoja aplikacija trajno čuva podatke, korisnike, narudžbine, sadržaj. Auth je sistem "ko si ti i šta smeš da vidiš". Treba ti čim tvoj proizvod mora da pamti bilo šta između dve posete ili da ima korisničke naloge.

**`shadcn`**, majstor za gotove, lepe UI komponente: dugmad, forme, tabele, dijaloge koji izgledaju profesionalno odmah. Umesto da Claude svaki ekran crta od nule, poseže za proverenim, uglađenim delovima. Treba ti praktično u svakom web projektu sa korisničkim interfejsom.

**`context7`**, bibliotekar sa uvek svežom dokumentacijom. Ovaj zaslužuje poseban pasus.

**`feature-dev`**, vodič kroz razvoj funkcionalnosti: umesto da Claude odmah jurne u kod, prvo razume kodnu bazu i arhitekturu, pa te vodi kroz izgradnju korak po korak. Treba ti kad gradiš veću funkcionalnost i hoćeš disciplinovan proces, ne improvizaciju.

**`frontend-design`**, dizajner koji ne pravi generične sajtove. Ako ti se čini da sve AI-generisane stranice liče jedna na drugu, ovaj plugin postoji baš zbog toga: gura dizajn ka prepoznatljivom, autorskom izgledu. Treba ti kad izgled proizvoda nije sporedna stvar nego deo brenda.

**`product-management`**, produkt menadžer u timu, sa skill-ovima `brainstorm` (razrada ideje koja te izaziva pitanjima) i `write-spec` (pisanje specifikacije). `brainstorm` si već upoznao u Modulu 4; `write-spec` je njegov par za sledeći korak, ovde samo da znaš odakle te veštine dolaze.

Kako instalirati? Postupak zavisi od tvoje verzije Claude Code-a, pa je najlakše da pitaš samog Claude-a:

```
Hoću da dodam vercel i shadcn plugin u ovaj projekat.
Proveri šta mi je već instalirano i provedi me kroz dodavanje, korak po korak.
```

### Zašto je `context7` toliko važan

Claude je učio iz ogromne količine tekstova, ali do određenog datuma. Biblioteke (gotovi paketi koda koje tvoj projekat koristi, npr. Next.js ili Tailwind) se u međuvremenu menjaju: izlaze nove verzije, stare komande prestaju da rade, pravila se menjaju. To znači da Claude ponekad piše kod po uputstvu koje je važilo pre godinu dana, kao kuvar koji kuva po starom izdanju kuvara, a recept je u međuvremenu promenjen.

`context7` rešava baš to: daje Claude-u uvek svežu, aktuelnu dokumentaciju biblioteka. Kad Claude treba da upotrebi neku biblioteku, umesto da se osloni na sećanje, pogleda najnovije uputstvo. Rezultat: manje misterioznih grešaka tipa "ovo je radilo juče svima, zašto ne radi meni".

```
Koristimo Next.js u ovom projektu. Pre nego što napišeš kod za novu stranicu,
proveri u aktuelnoj dokumentaciji da li je tvoj pristup i dalje preporučen
za verziju koju imamo u projektu.
```

### MCP konektori: Claude upoznaje tvoje alate

MCP konektori povezuju Claude sa servisima u kojima već živi tvoj posao:

- **Figma**, Claude može da vidi tvoj dizajn i pretvori ga u kod, umesto da mu opisuješ rečima "dugme je plavo i malo zaobljeno".
- **Slack**, Claude može da radi sa porukama tvog tima, npr. da iz razgovora izvuče dogovorene zadatke.
- **Notion**, Claude može da čita i dopunjava tvoje beleške, specifikacije i baze znanja.

Postoje konektori i za Linear, Gmail i mnoge druge servise. Princip je uvek isti: umesto da ti ručno prepisuješ sadržaj iz alata u razgovor, Claude dobija direktan, kontrolisan pristup.

```
Povezao sam Notion. U bazi "Backlog proizvoda" pronađi sve stavke označene
kao "sledeći sprint" i predloži mi redosled implementacije sa obrazloženjem.
```

### Princip izbora: kreni minimalno

Ovde laici često upadnu u zamku "više je bolje", instaliraju deset plugin-ova i povežu sve servise "za svaki slučaj". Nemoj. Više alata znači više buke: Claude ima više opcija da odmeri, ti imaš više stvari da razumeš, a većinu nikad ne upotrebiš.

Pravilo: **kreni sa nulom, dodaj kad osetiš konkretnu potrebu.** Treba ti objavljivanje na internet? Dodaj `vercel`. Proizvod mora da pamti korisnike? Dodaj `supabase`. Tek kad te zaboli, kupuješ lek, ne pre.

### Bezbednosna napomena koju ne preskačeš

Svaki MCP konektor znači da Claude, i alat koji stoji iza konektora, dobija pristup tvojim podacima u tom servisu. Konektor za Gmail vidi tvoju poštu. Konektor za Slack vidi prepiske tima. Zato važi isto pravilo kao kad nekome daješ ključ od kancelarije: **povezuj samo ono što stvarno koristiš**, a kad konektor više ne koristiš, ukloni ga. O bezbednosti tvog koda detaljnije smo pričali u Modulu 8, ovo je njen rođak sa strane podataka.

### Vežba

1. Otvori svoj projekat i pokreni Claude Code.
2. Pitaj Claude-a šta već imaš: `Koji plugin-ovi i skill-ovi su mi trenutno dostupni u ovom projektu? Izlistaj ih sa kratkim opisom svakog.`
3. Pogledaj listu i za svaku stavku se zapitaj: "Da li sam ovo upotrebio u poslednjih mesec dana?" Zapiši šta je višak.
4. Izaberi JEDAN plugin sa spiska preporučenih koji rešava tvoj stvarni, trenutni problem (npr. `shadcn` ako ti UI izgleda sirovo).
5. Zamoli Claude-a da te provede kroz instalaciju tog jednog plugin-a, pa odmah isprobaj jedan njegov skill na malom zadatku.
6. U `CLAUDE.md` zabeleži (poruka koja počinje sa `#`) koji plugin si dodao i zašto, da svaka sledeća sesija zna kontekst.

### Najčešće greške

1. **Instaliranje svega "za svaki slučaj".** Deset plugin-ova koje ne koristiš samo prave buku i konfuziju. → Rešenje: kreni sa nulom; dodaj plugin tek kad imaš konkretan problem koji on rešava.
2. **Povezivanje svih servisa preko MCP-a odjednom.** Svaki konektor je pristup tvojim podacima. → Rešenje: poveži samo servis koji ti treba za tekući zadatak; ostale dodaj kad zatrebaju, a nekorišćene ukloni.
3. **Oslanjanje na Claude-ovo "sećanje" o bibliotekama.** Kod izgleda uverljivo, ali je pisan po zastarelom uputstvu i puca. → Rešenje: koristi `context7` ili izričito traži da Claude proveri aktuelnu dokumentaciju pre pisanja koda.
4. **Mešanje pojmova: "instalirao sam skill".** Pa onda tražiš pogrešnu stvar na pogrešnom mestu. → Rešenje: zapamti hijerarhiju, instaliraš plugin, on donosi skill-ove, skill pozivaš sa `/imenom`.
5. **Očekivanje da plugin radi posao umesto tebe.** Plugin je specijalista, ali ti si i dalje direktor: bez jasnog zadatka i provere rezultata (Modul 1: princip dokaza), ni najbolji specijalista ne vredi. → Rešenje: i sa plugin-ovima traži dokaz da je posao urađen.

### Kontrolna lista

- [ ] Umem da objasnim razliku između plugin-a, skill-a i MCP konektora jednom rečenicom za svaki
- [ ] Znam koja tri-četiri preporučena plugin-a pokrivaju moje stvarne potrebe, i zašto baš ti
- [ ] Razumem zašto `context7` smanjuje greške sa bibliotekama
- [ ] Pregledao sam šta mi je instalirano i uklonio (ili odlučio da ne dodajem) višak
- [ ] Svaki MCP konektor koji imam povezan mogu da opravdam konkretnom upotrebom
- [ ] Zabeležio sam u `CLAUDE.md` koje plugin-ove projekat koristi i čemu služe

### Proveri znanje

**1. Koja je razlika između plugin-a i skill-a?**

Plugin je paket, "zaposleni specijalista" koji se instalira u Claude Code i donosi više veština i alata. Skill je jedna konkretna veština iz tog paketa, koju pozivaš komandom sa kosom crtom, npr. `/vercel:deploy`.

**2. Zašto ti treba `context7` ako Claude "već zna" biblioteke poput Next.js-a?**

Zato što je Claude-ovo znanje zamrznuto u trenutku treniranja, a biblioteke se stalno menjaju. `context7` daje Claude-u pristup uvek svežoj dokumentaciji, pa kod piše po aktuelnim pravilima umesto po zastarelom sećanju.

**3. Koje bezbednosno pravilo važi za MCP konektore?**

Svaki konektor znači pristup tvojim podacima u tom servisu (pošta, prepiske, dokumenti). Zato povezuješ samo ono što stvarno koristiš, a konektore koje više ne koristiš, uklanjaš.


---

## Modul 13: Kada stvari krenu naopako

Pre nego što kreneš dalje, jedna rečenica koju vredi zapamtiti: **skoro ništa nije nepovratno.** Ako si pratio Modul 3 i radiš sa git-om, sistemom koji čuva snimak projekta posle svake zaokružene celine (commit), tvoj projekat ima "tačka čuvanja" kao u video igrici. Najgore što se obično desi jeste da izgubiš sat vremena, ne projekat. Ovo poglavlje je tvoj kućni priručnik prve pomoći: za svaki problem prvo prepoznaš simptom, zatim razumeš dijagnozu, pa primeniš lek.

### Šta ćeš naučiti

- Kako da prepoznaš sedam najčešćih problema u radu sa Claude Code-om
- Kada da pritisneš `Esc` i preusmeriš Claude-a, a kada da kreneš iz čistog konteksta sa `/clear`
- Kako da od Claude-a uvek tražiš dokaz umesto da veruješ na reč
- Kako da git iskoristiš kao vremeplov kada nešto što je radilo prestane da radi
- Kada je problem prevelik za tebe i Claude-a, i kako da pripremiš pitanje za stručnjaka

### Scenario 1: Claude ide u pogrešnom smeru

**SIMPTOM:** Gledaš kako Claude radi i vidiš da pravi nešto što nisi tražio, drugi ekran, pogrešnu funkcionalnost, izmene u delu aplikacije koji nisi ni pomenuo.

**DIJAGNOZA:** Tvoj prompt je bio dvosmislen ili je Claude pogrešno protumačio cilj. Što duže radi u pogrešnom smeru, više posla kasnije čistiš.

**LEK:** Pritisni `Esc` ODMAH. Ne čekaj "da završi pa ćemo videti", `Esc` prekida Claude-a usred rada i odmah možeš da ga preusmeriš. To nije nepristojno, to je tvoj posao kao direktora (Modul 0).

```
Stani. Krenuo si da menjaš stranicu za prijavu, a ja sam tražio izmenu
na stranici sa podešavanjima. Vrati izmene koje si do sada napravio,
pa mi prvo ukratko opiši šta planiraš, ne menjaj ništa dok ne odobrim.
```

### Scenario 2: Vrti se u krug sa istom greškom

**SIMPTOM:** Claude treći put "popravlja" isti bag, svaki put kaže "sada bi trebalo da radi", i svaki put iskoči ista greška.

**DIJAGNOZA:** Claude je zaglavljen u jednom pristupu i pokušava varijacije istog rešenja. Razgovor pun neuspelih pokušaja ga dodatno vuče ka istim idejama.

**LEK:** Zaustavi ga i nateraj da promeni perspektivu:

```
Stani sa popravkama. Objasni mi prostim jezikom, bez žargona:
šta je tačno problem i zašto dosadašnji pokušaji nisu uspeli?
Zatim predloži 3 SUŠTINSKI različita pristupa rešenju, sa
prednostima i manama svakog. Ne piši kod dok ne izaberem.
```

Ako ni to ne pomogne, ukucaj `/clear` (briše kontekst i počinje svežu sesiju) i opiši problem iz početka, kratko, fokusirano, bez istorije neuspeha. Svež početak često reši ono što deset zakrpa nije.

### Scenario 3: Kaže "gotovo je", a ne radi

**SIMPTOM:** Claude tvrdi da je funkcionalnost završena. Otvoriš aplikaciju, dugme ne radi, forma se ne šalje, stranica je prazna.

**DIJAGNOZA:** Claude je napisao kod koji *izgleda* ispravno, ali ga nije proverio u stvarnim uslovima. Tvrdnja nije dokaz, to je princip iz Modula 1.

**LEK:** Nikad ne prihvataj "gotovo" bez dokaza. Claude može da pokrene dev server i verifikuje izmene u pregledaču: da klikće, popunjava forme i pravi snimke ekrana.

```
Ne verujem dok ne vidim. Pokreni aplikaciju, otvori stranicu za
registraciju u pregledaču, popuni formu test podacima i pošalji je.
Napravi snimak ekrana rezultata i pokaži mi log, tek onda je gotovo.
```

### Scenario 4: Nešto što je radilo sada je pokvareno

**SIMPTOM:** Prijava korisnika je radila prošle nedelje. Danas, posle nekoliko novihfunkcionalnosti, više ne radi.

**DIJAGNOZA:** Neka od novijih izmena je usput polomila staru funkcionalnost (programeri to zovu "regresija"). Dešava se i najboljima, zato postoje commit-i.

**LEK:** Git je tvoj vremeplov. Ne moraš da znaš nijednu git komandu, samo reci Claude-u šta hoćeš:

```
Prijava korisnika je radila ranije, a sada ne radi. Pregledaj
istoriju commit-a i pronađi poslednji commit u kom je prijava
radila. Uporedi taj kod sa sadašnjim, reci mi koja izmena je
polomila prijavu, i predloži: da li da popravimo unapred ili
da vratimo projekat na taj commit. Ne menjaj ništa bez odobrenja.
```

Ovo je razlog zašto u Modulu 6 insistiramo na malim, čestim commit-ima: što su tačke čuvanja gušći, manje posla gubiš vraćanjem.

### Scenario 5: Sesija predugačka, odgovori sve lošiji

**SIMPTOM:** Radite satima u istom razgovoru. Claude počinje da zaboravlja ranije dogovore, meša imena fajlova, odgovara sporije i konfuznije.

**DIJAGNOZA:** Kontekst (radna memorija razgovora) je pretrpan. Zamisli radni sto zatrpan papirima, u nekom trenutku više ne pomaže što je "sve tu", jer se ništa ne nalazi.

**LEK:** `/clear` za svež početak, ili `/compact` ako želiš da sažmeš razgovor a zadržiš suštinu. Ne plaši se da ćeš izgubiti "sve što Claude zna o projektu", kontinuitet ne čuva razgovor, nego fajlovi: `CLAUDE.md` se učitava na početku svake sesije, a `docs/spec.md` (Modul 4) čuva šta gradiš i zašto. Posle `/clear` samo usmeri Claude-a:

```
Pročitaj docs/spec.md. Radimo na funkcionalnosti izvoza u PDF,
prethodni korak je završen i commit-ovan. Sledeći korak: dugme
za izvoz na stranici izveštaja. Prvo plan, pa implementacija.
```

### Scenario 6: Tvrdnja o spoljnoj biblioteci deluje netačno

**SIMPTOM:** Claude tvrdi da neka biblioteka (tuđi gotov kod koji tvoj projekat koristi, npr. za plaćanja ili slanje imejlova) radi na određeni način, ali kod puca, ili tvrdnja deluje zastarelo.

**DIJAGNOZA:** Claude-ovo znanje ima datum preseka, a biblioteke se menjaju često. Ono što je važilo za prošlogodišnju verziju možda više ne važi.

**LEK:** Traži da proveri svežu dokumentaciju umesto da se oslanja na pamćenje. U promptu ispod pominje se `package.json`, to je fajl u kom projekat vodi spisak biblioteka koje koristi i njihovih verzija, pa Claude tamo proverava koju verziju imaš. Ako imaš instaliran `context7` plugin (Modul 12), on služi baš tome, uvek sveža dokumentacija biblioteka.

```
Pre nego što nastaviš: proveri aktuelnu dokumentaciju za verziju
biblioteke koju koristimo u projektu (pogledaj package.json).
Uporedi ono što si predložio sa zvaničnom dokumentacijom i reci
mi da li se nešto promenilo.
```

### Scenario 7: Vreme je za ljudsku pomoć

**SIMPTOM:** Sumnjaš da su ti procureli podaci korisnika ili pristupni ključevi; dobio si pravno pitanje (GDPR, ugovori, odgovornost); izgubio si podatke iz produkcione baze; u pitanju je novac korisnika.

**DIJAGNOZA:** Ovo više nije tehnički problem koji se rešava boljim promptom. Bezbednosni incidenti, pravna pitanja i gubitak tuđih podataka nose stvarne posledice, tu treba čovek sa iskustvom i, po potrebi, licencom.

**LEK:** Ne guraj sam. Ali Claude ti i ovde pomaže, da pripremiš kvalitetno pitanje, jer stručnjakov sat je skup, a precizno pitanje ga skraćuje:

```
Sumnjam na bezbednosni incident i zvaću stručnjaka. Pomozi mi da
pripremim sažetak: (1) šta se tačno desilo i kada, (2) koji podaci
su potencijalno ugroženi, (3) šta sam već preduzeo, (4) koja pitanja
da postavim. Piši činjenično, bez nagađanja, na jednoj stranici.
```

U međuvremenu: promeni lozinke i pristupne ključeve, ne briši ništa (tragovi pomažu dijagnozi) i zapisuj vremena događaja.

### Vežba

Provežbaj oporavak dok ništa nije na kocki, tako će te pravi problem zateći spremnog:

1. Otvori svoj vežbovni projekat i zamoli Claude-a: `Napravi commit trenutnog stanja sa porukom "stabilna tačka pre vežbe oporavka".`
2. Zatraži namernu izmenu: `Promeni naslov na početnoj stranici u "POKVARENO" i sačuvaj.`
3. Proveri u pregledaču da je izmena tu (princip dokaza!).
4. Sada glumi krizu: `Naslov je pokvaren. Vrati projekat na poslednji commit gde je naslov bio ispravan i pokaži mi dokaz da je vraćeno.`
5. Proveri u pregledaču da je sve po starom. Čestitam, upravo si izveo svoj prvi oporavak i uverio se da commit zaista čuva.

### Najčešće greške

1. **Čekaš da Claude "završi pa ćemo ispraviti".** Pogrešan smer se ne ispravlja sam, produbljuje se. Rešenje: `Esc` čim primetiš skretanje, pa preusmeri.
2. **Posle pete neuspele popravke tražiš šestu na isti način.** Rešenje: prekini obrazac, traži objašnjenje prostim jezikom i tri različita pristupa, ili `/clear` pa svež opis.
3. **Prihvataš "gotovo je" bez dokaza.** Rešenje: standardno traži snimak ekrana, test rezultat ili log. Ako uđe u naviku, ovaj scenario skoro nestaje.
4. **Radiš satima bez ijednog commit-a.** Bez tačke čuvanja, vremeplov iz Scenarija 4 nema kuda da te vrati. Rešenje: commit posle svake zaokružene celine (Modul 6).
5. **U panici brišeš fajlove ili "resetuješ sve".** Brisanje je jedna od retkih stvarno nepovratnih radnji. Rešenje: prvo duboko udahni, pa pitaj Claude-a da proceni štetu, pre bilo kakve akcije.

### Kontrolna lista

- [ ] Znam da `Esc` prekida Claude-a usred rada i koristim ga čim vidim pogrešan smer
- [ ] Kada se Claude vrti u krug, tražim objašnjenje prostim jezikom + 3 različita pristupa
- [ ] Ne prihvatam "gotovo je" bez dokaza (snimak ekrana, test, log)
- [ ] Redovno commit-ujem, pa uvek imam tačku za povratak
- [ ] Znam da `/clear` ne briše znanje o projektu, `CLAUDE.md` i `docs/spec.md` čuvaju kontinuitet
- [ ] Tvrdnje o spoljnim bibliotekama proveravam kroz svežu dokumentaciju
- [ ] Znam tri situacije u kojima zovem stručnjaka i kako da pripremim pitanje

### Proveri znanje

**1. Claude pravi funkcionalnost koju nisi tražio. Šta radiš, odmah ili kad završi?**
Odmah: pritisni `Esc`, prekini ga i preusmeri. Svaki minut rada u pogrešnom smeru je minut čišćenja kasnije.

**2. Zašto `/clear` nije opasan za projekat, iako briše ceo razgovor?**
Jer kontinuitet ne živi u razgovoru nego u fajlovima: kod i commit-i su na disku, `CLAUDE.md` se učitava na početku svake sesije, a specifikacija u `docs/spec.md` čuva šta gradiš i zašto.

**3. Koje tri vrste problema NE rešavaš sam sa Claude-om, nego zoveš stručnjaka?**
Bezbednosni incident (curenje podataka ili ključeva), pravna pitanja i gubitak produkcionih podataka, svuda gde greška nosi stvarne posledice po korisnike, novac ili zakon.


---

## Dodaci

Ovo poglavlje je drugačije od ostalih: nema lekcija, nema vežbi, nema pitanja. Ovo je tvoj priručnik za svaki dan, mesto na koje se vraćaš kad ti zatreba komanda koje ne možeš da se setiš, šablon prompta koji ne želiš da pišeš iz nule, ili pojam koji ti je promakao. Slobodno ga odštampaj, zalepi pored monitora ili drži otvoren u drugom prozoru dok radiš.

---

## Dodatak A: Cheat-tabela komandi

Sve komande na jednom mestu. Komande koje počinju sa `claude` kucaš u terminal (program za kucanje komandi, detaljno u Modulu 2). Komande koje počinju kosom crtom (`/`) kucaš unutar razgovora sa Claude-om.

### Instalacija i pokretanje

| Komanda | Šta radi | Kada je koristiš |
|---|---|---|
| `npm install -g @anthropic-ai/claude-code` | Instalira Claude Code CLI verziju (zahteva Node.js); alternativa je desktop aplikacija | Jednom, pri postavljanju računara (Modul 2) |
| `claude` | Pokreće Claude Code iz foldera projekta | Svaki put kad počinješ rad na projektu |
| `claude --resume` / `claude --continue` | Nastavak ranije sesije | Kad si juče stao na pola posla i hoćeš da nastaviš tu gde si stao |
| `claude -p "..."` | Neinteraktivno pokretanje: jedan zadatak, bez interaktivnog razgovora | Za brze, jednokratne zadatke ili automatizaciju |

### Rad u sesiji

| Komanda | Šta radi | Kada je koristiš |
|---|---|---|
| `/init` | Generiše `CLAUDE.md` sa opisom projekta, komandama i konvencijama | Jednom po projektu, na samom početku (Modul 3) |
| Poruka koja počinje sa `#` | Claude tu napomenu trajno beleži (memorija / `CLAUDE.md`) | Kad otkriješ pravilo koje Claude treba da pamti zauvek, npr. `# uvek piši poruke commit-a na srpskom` |
| `/clear` | Briše kontekst i počinje svežu sesiju | Kad prelaziš na potpuno novi zadatak ili je razgovor postao konfuzan |
| `/compact` | Sažima dugačak razgovor da oslobodi prostor | Kad je sesija duga, a želiš da nastaviš isti posao bez gubljenja niti |
| `Shift+Tab` | Kruži kroz režime rada, uključujući plan mode (Claude istražuje i predlaže plan, ne menja fajlove dok ne odobriš) | Pre svake veće izmene, prvo plan, pa rad (Modul 5) |
| `Esc` | Prekida Claude-a usred rada; odmah možeš da ga preusmeriš | Kad vidiš da je krenuo u pogrešnom pravcu, ne čekaj da završi |
| `/fewer-permission-prompts` | Analizira tvoj rad i predlaže listu bezbednih komandi za unapred odobrenje (čuva se u `.claude/settings.json`) | Kad te Claude prečesto pita za dozvole za iste, bezopasne stvari |

### Autonomni rad (detaljno u Modulu 7)

| Komanda | Šta radi | Kada je koristiš |
|---|---|---|
| `/goal <uslov>` | Claude radi turu za turom autonomno dok uslov nije ispunjen; posle svake ture mali brzi model (Haiku) ocenjuje da li uslov važi | Za zadatke sa jasnim, dokazivim ciljem, npr. „svi testovi prolaze" |
| `/goal` | Prikazuje status: uslov, broj tura, vreme, potrošnju tokena | Kad hoćeš da proveriš dokle je stigao |
| `/goal clear` | Prekida aktivni goal | Kad odustaješ ili menjaš cilj (novi goal i sam zamenjuje stari) |
| `/loop 5m <prompt>` | Ponavlja prompt na fiksni interval (jedinice: `s`, `m`, `h`, `d`) | Za periodične provere dok radiš nešto drugo |
| `/loop <prompt>` | Dinamički režim: Claude sam bira pauze (1–60 min) prema aktivnosti i može sam da završi petlju kad je posao gotov | Kad ne znaš tačan ritam, ali hoćeš da Claude prati posao |
| `/loop` | Podrazumevani prompt za održavanje sesije (nastavi nedovršeno, sredi PR); prilagođava se kroz `.claude/loop.md` | Kad hoćeš da Claude „dežura" nad projektom dok je sesija otvorena |
| `/schedule` | Routines: zakazani agenti u oblaku koji rade i kad je tvoj računar ugašen | Za redovne zadatke van sesije, npr. dnevni izveštaj (Modul 10) |

Napomena: `/loop` važi samo dok je sesija otvorena (najviše 7 dana) i ne radi kad je računar ugašen, za to postoji `/schedule`. `/goal` radi i neinteraktivno: `claude -p "/goal ..."`.

### Kvalitet i bezbednost (detaljno u Modulu 8)

| Komanda | Šta radi | Kada je koristiš |
|---|---|---|
| `/code-review` | Pregled trenutnih izmena koda; nivoi temeljnosti `low`/`medium`/`high`/`max` | Posle svake završene funkcionalnosti, pre spajanja izmena |
| `/code-review ultra` | Multi-agent pregled celog brancha u oblaku, najtemeljniji, dodatno se naplaćuje | Pred lansiranje ili pred veliku, rizičnu izmenu |
| `/security-review` | Bezbednosni pregled izmena na trenutnom branchu | Pre lansiranja i posle svake izmene koja dira lozinke, plaćanja ili podatke korisnika |
| `/simplify` | Pojednostavljuje i čisti izmenjeni kod (ne traži bagove) | Kad funkcionalnost radi, a hoćeš da kod ostane uredan i održiv |

### Ekosistem (detaljno u Modulu 12)

| Komanda | Šta radi | Kada je koristiš |
|---|---|---|
| `/vercel:bootstrap` | Postavlja projekat za rad sa Vercel-om (hosting, env varijable), deo vercel plugin-a | Jednom, kad povezuješ projekat sa hostingom (Modul 9) |
| `/vercel:deploy` | Pravi preview deploy, probnu verziju na privatnom linku | Pre svakog objavljivanja: prvo proveriš na privatnom linku (Modul 9) |
| `/vercel:deploy prod` | Objavljuje u produkciju | Tek kad preview verzija radi besprekorno, nikad direktno u produkciju (Modul 9) |

### Korisni fajlovi koje vredi znati

| Fajl | Čemu služi |
|---|---|
| `CLAUDE.md` | Claude-ovo „dugoročno pamćenje" o projektu, učitava se na početku svake sesije |
| `.claude/settings.json` | Lista unapred dozvoljenih komandi (dozvole) |
| `.claude/loop.md` | Prilagođeni podrazumevani prompt za `/loop` |
| `docs/spec.md` | Tvoja specifikacija proizvoda (Modul 4) |

---

## Dodatak B: Šabloni promptova

Osam šablona za situacije koje se najčešće ponavljaju. Kopiraj, zameni sve što je u uglastim zagradama `[OVAKO]` svojim sadržajem, i pošalji. Logika iza svakog šablona objašnjena je u modulima na koje se odnose; ovde je samo „gotova jela".

### Šablon 1: Inicijalizacija novog projekta sa mernim instrumentima

Koristiš na samom početku, posle Modula 3. Posle ovog prompta ukucaj i `/init` da nastane `CLAUDE.md`.

```
Pravim novi projekat: [KRATAK OPIS PROIZVODA, npr. "veb aplikacija za zakazivanje termina u frizerskom salonu"].

Postavi temelje:
1. Inicijalizuj git repozitorijum i napravi prvi commit.
2. Postavi projekat koristeći [TEHNOLOGIJA, ili napiši: "predloži mi standardan, dobro podržan izbor tehnologija za ovakav proizvod i objasni ga laičkim jezikom pre nego što kreneš"].
3. Podesi tri merna instrumenta: testove, lint i build.
4. Pokreni sve tri komande i pokaži mi njihov izlaz kao dokaz da prolaze.

Ja nisam programer, kad god doneseš tehničku odluku, objasni mi je u jednoj rečenici.
```

### Šablon 2: Brainstorm koji te izaziva

Koristiš pre nego što napišeš i jedan red specifikacije (Modul 4). Poenta je da Claude bude kritičar, ne navijač.

```
Imam ideju za proizvod: [OPIS IDEJE U 2-3 REČENICE].

Budi mi kritičan sagovornik, ne navijač:
1. Postavi mi 10 najtežih pitanja na koja moram da imam odgovor pre nego što počnem.
2. Navedi 3 najverovatnija razloga zašto ova ideja može da propadne.
3. Predloži 2 alternativna ugla na isti problem koje možda nisam razmotrio.
4. Reci mi šta je NAJMANJA verzija ove ideje koja i dalje rešava stvarni problem.

Ne piši nikakav kod i ne menjaj nijedan fajl, ovo je samo razgovor. Pitanja mi postavljaj jedno po jedno i sačekaj moj odgovor.
```

### Šablon 3: Pisanje spec-a

Koristiš posle brainstorma, kad je ideja prečišćena (Modul 4).

```
Na osnovu našeg dosadašnjeg razgovora napiši specifikaciju proizvoda u fajl docs/spec.md.

Proizvod: [IME + JEDNA REČENICA ŠTA RADI]
Za koga je: [CILJNA GRUPA]
Glavni problem koji rešava: [PROBLEM]

Struktura dokumenta:
1. Problem i za koga ga rešavamo
2. MVP funkcionalnosti, najviše [BROJ, npr. 5], svaka opisana iz ugla korisnika ("korisnik može da...")
3. Šta svesno NIJE u MVP-u (i zašto)
4. Merljivi kriterijumi uspeha za svaku funkcionalnost

Pravila: piši jednostavnim srpskim jezikom, bez tehničkog žargona. Sve što ti je nejasno, pitaj me PRE pisanja, nemoj da pretpostavljaš.
```

### Šablon 4: Arhitektonska odluka (2 opcije + preporuka)

Koristiš kad treba doneti tehničku odluku, a nemaš tehničko znanje (Modul 5). Najbolje radi u plan mode-u.

```
Treba da odlučimo: [ODLUKA, npr. "gde i kako čuvamo podatke korisnika"].

Predstavi mi tačno 2 realne opcije. Za svaku:
- objasni je u jednom pasusu, kao da objašnjavaš nekome ko nikad nije programirao
- navedi najviše 3 prednosti i 3 mane
- reci šta znači za troškove (sada i kad poraste broj korisnika) i za održavanje

Na kraju daj svoju preporuku i JEDAN ključni razlog za nju.
Ne menjaj nijedan fajl dok ti ne kažem koju opciju biramo.
```

### Šablon 5: Funkcionalnost ciklus (kontekst → zadatak → kriterijum → ograničenja)

Tvoj svakodnevni radni prompt (Modul 6). Ovo je formula koju ćeš koristiti najčešće.

```
KONTEKST: Radimo na projektu [IME]. Trenutno stanje: [ŠTA VEĆ POSTOJI I RADI, npr. "korisnik može da se registruje i prijavi"].

ZADATAK: Dodaj [FUNKCIONALNOST OPISANA IZ UGLA KORISNIKA, šta korisnik vidi i šta može da uradi].

KRITERIJUM USPEHA: Gotovo je tek kada [MERLJIV USLOV, npr. "korisnik može da rezerviše termin, dobije potvrdu na ekranu, i svi testovi prolaze"].

OGRANIČENJA:
- Ne diraj [DELOVI KOJE NE TREBA MENJATI, npr. "postojeću prijavu korisnika"].
- Postojeći testovi moraju i dalje da prolaze.
- Napiši testove i za novu funkcionalnost.
- Ako ti bilo šta nije jasno, pitaj me pre nego što kreneš.

Na kraju mi pokaži dokaz: izlaz testova i kratak opis šta si promenio.
```

### Šablon 6: /goal uslov

Koristiš za autonoman rad (Modul 7). Zapamti pravilo: uslov mora biti dokaziv kroz ono što Claude pokaže u razgovoru, „aplikacija je kvalitetna" kontrolor ne može da izmeri, „testovi prolaze" može.

```
/goal [MERLJIVO ZAVRŠNO STANJE, npr. "funkcionalnost rezervacije termina je implementirana"]. Provera: komanda `[TEST KOMANDA, npr. npm test]` izlazi bez ijedne greške i `[BUILD KOMANDA, npr. npm run build]` prolazi. Ograničenja: postojeći testovi se ne menjaju i ne brišu. Ako uslov nije ispunjen posle [BROJ, npr. 20] tura, stani i napiši šta te blokira.
```

### Šablon 7: Verifikacija sa dokazom

Koristiš kad Claude tvrdi da je nešto gotovo, a ti hoćeš dokaz, ne obećanje (princip iz Modula 1).

```
Tvrdiš da je [FUNKCIONALNOST] gotova. Dokaži mi to:

1. Pokreni sve testove i pokaži mi kompletan izlaz.
2. Pokreni aplikaciju i prođi kroz ovaj scenario kao korisnik: [KORACI, npr. "otvori početnu stranu, prijavi se kao test korisnik, rezerviši termin za sutra u 14h"]. Napravi snimak ekrana svakog koraka.
3. Proveri i šta se dešava kad korisnik pogreši: [LOŠ SCENARIO, npr. "pokuša da rezerviše već zauzet termin"], i to mi pokaži.

Ako bilo šta ne radi, nemoj da mi objašnjavaš zašto, popravi, pa ponovi ceo dokaz ispočetka. Ne prihvatam "trebalo bi da radi": samo izlaz komandi i snimke ekrana.
```

### Šablon 8: Priprema za lansiranje

Koristiš pred objavljivanje (Modul 9). Posle ovog prompta sam pokreni i `/security-review` i `/code-review`, to su tvoje nezavisne kontrole.

```
Pripremamo [IME PROJEKTA] za lansiranje. Prođi kroz ovu listu i za SVAKU stavku mi pokaži dokaz (izlaz komande, snimak ekrana ili sadržaj fajla):

1. Build prolazi bez grešaka i upozorenja.
2. Svi testovi prolaze.
3. Nijedna tajna (lozinka, API ključ) nije upisana direktno u kod, sve je u env varijablama, a fajl sa tajnama je isključen iz git-a.
4. Aplikacija razumno reaguje na greške: [KLJUČNI LOŠI SCENARIO, npr. "pad veze sa bazom"] ne ruši ceo sajt nego prikazuje poruku.
5. Probaj aplikaciju na ekranu veličine telefona i pokaži mi snimak ekrana.

Za svaku stavku koja NE prolazi: prvo mi reci šta si našao, predloži popravku, i sačekaj moje odobrenje pre menjanja.
```

---

## Dodatak C: Rečnik pojmova

Trideset pojmova koje ćeš sretati svakodnevno, objašnjenih bez žargona. Ako te neki pojam zanima dublje, pored njega stoji modul u kom se detaljno obrađuje.

**API**, način na koji programi pričaju jedni s drugima, kao konobar između tebe i kuhinje: ti naručiš, on prenese, kuhinja vrati jelo. Kad tvoja aplikacija „povlači podatke" od nekog servisa, radi to preko API-ja.

**auth (autentifikacija)**, sve oko provere ko je korisnik: registracija, prijava, lozinke, nalozi. Deo aplikacije koji odgovara na pitanje „ko si ti i šta smeš da vidiš".

**backend**, deo aplikacije koji korisnik ne vidi: radi na serveru, obrađuje podatke i logiku. Kuhinja restorana, gosti je ne vide, ali bez nje nema jela.

**backlog**, uredna lista svega što čeka da bude urađeno, poređana po važnosti. Tvoj „spisak želja" za proizvod (Modul 10).

**baza podataka**, organizovano skladište podataka tvoje aplikacije: korisnici, narudžbine, poruke. Zamisli digitalni arhivski ormar u kom svaka fioka ima svoje mesto i etiketu.

**branch (grana)**, paralelna kopija koda u git-u na kojoj možeš da eksperimentišeš bez diranja glavne verzije. Kad si zadovoljan, izmene se spajaju nazad.

**build**, proces „sklapanja" izvornog koda u verziju spremnu za rad. Ako build pukne, znaš da nešto fundamentalno ne valja, zato je jedan od tvoja tri merna instrumenta (Modul 3).

**CI (continuous integration)**, robot na GitHub-u koji automatski pokreće testove i provere pri svakoj izmeni koda. Tvoj kontrolor kvaliteta koji nikad ne spava (Modul 3).

**commit**, sačuvana „fotografija" stanja celog projekta u git-u, sa opisom šta je promenjeno. Tačka u istoriji na koju uvek možeš da se vratiš ako nešto krene naopako.

**deploy**, objavljivanje aplikacije na internet, da bude dostupna stvarnim korisnicima. Trenutak kad jelo izlazi iz kuhinje u salu (Modul 9).

**env varijabla**, podešavanje ili tajna (API ključ, lozinka za bazu) koja se čuva van koda, u posebnom fajlu ili na hosting servisu. Tajne nikad ne idu u kod, jer kod ide na GitHub.

**feature**, jedna funkcionalnost proizvoda iz ugla korisnika: „korisnik može da rezerviše termin". Osnovna jedinica posla u ritmu razvoja (Modul 6).

**frontend**, deo aplikacije koji korisnik vidi i koristi: ekrani, dugmad, forme, boje. Sala restorana, u kojoj gost provodi vreme.

**git**, program koji pamti kompletnu istoriju svih izmena koda. Vremenska mašina tvog projekta: u svakom trenutku znaš šta je promenjeno, kada, i možeš da se vratiš (Modul 3).

**kontekst**, sve što Claude „drži u glavi" tokom jedne sesije: razgovor, fajlove koje je pročitao, ono što je uradio. Ograničen je, zato postoje `/clear` i `/compact` (Modul 1).

**lint**, automatski lektor za kod: pronalazi stilske greške, nedoslednosti i sumnjiva mesta pre nego što postanu problemi. Drugi od tri merna instrumenta.

**log**, dnevnik onoga što se dešava u aplikaciji dok radi: ko se prijavio, šta je puklo i zašto. Prvo mesto na kom se traži uzrok problema (Modul 13).

**MVP (minimum viable product)**, najmanja verzija proizvoda koja rešava stvarni problem stvarnom korisniku. Sve preko toga je ukras koji čeka svoj red (Modul 4).

**plan mode**, režim rada u kom Claude istražuje i predlaže plan, ali ne menja nijedan fajl dok plan ne odobriš. Tvoja sigurnosna kočnica pre velikih izmena (Modul 5).

**PR (pull request)**, formalni predlog: „ove izmene želim da ubacim u glavnu verziju koda". Mesto gde se izmene pregledaju pre nego što budu prihvaćene.

**preview**, probna verzija sajta na privremenoj internet adresi, da izmene vidiš i isprobaš pre nego što odu u produkciju. Generalna proba pred premijeru.

**produkcija**, „prava" verzija aplikacije, ona koju koriste stvarni korisnici. Sve što dotiče produkciju zaslužuje dodatnu pažnju i dokaz da radi.

**prompt**, poruka, uputstvo ili zahtev koji daješ Claude-u. Kvalitet prompta direktno određuje kvalitet rezultata (Modul 11).

**refaktorisanje**, sređivanje koda iznutra bez promene onoga što korisnik vidi. Kao generalno raspremanje kuhinje: meni ostaje isti, ali se posle kuva brže i bezbednije.

**repozitorijum (repo)**, folder projekta pod nadzorom git-a; na GitHub-u dobija i svoju onlajn kopiju. Kad neko kaže „pogledaj repozitorijum", misli na ceo projekat sa istorijom.

**sesija**, jedan razgovor sa Claude Code-om. Između sesija Claude ne pamti ništa, osim fajla `CLAUDE.md` i memorije, zato je `CLAUDE.md` toliko važan (Modul 1).

**tehnološki skup (stack)**, skup tehnologija od kojih je proizvod sagrađen: jezik, okvir, baza, hosting. Kao spisak materijala od kojih je sagrađena kuća.

**test**, automatska provera da određeni deo aplikacije radi kako treba. Sigurnosna mreža: kad Claude nešto menja, testovi javljaju ako je usput nešto pokvario. Najvažniji od tri merna instrumenta.

**token**, jedinica teksta (otprilike deo reči) kojom se meri koliko Claude čita i piše, pa i koliko rad košta. Zato `/goal` status prikazuje potrošnju tokena.

**UI (user interface)**, korisnički interfejs: sve vizuelno preko čega korisnik komunicira sa aplikacijom, dugmad, forme, raspored, boje.

---

Toliko od priručnika. Ako si stigao dovde čitajući redom, čestitam: prošao si ceo put od ideje do proizvoda na produkciji. Sada se vraćaj ovde po potrebi, a kada nešto krene naopako, Modul 13 te čeka. Srećno graditeljstvo.


---

## Za predavače: kako iz ovog dokumenta izvesti kurs

Ovaj dokument je pisan da se čita samostalno, ali najbolje rezultate daje kad ga neko provede kroz njega uživo. Ako si predavač, mentor ili interni trener koji želi da od ovih petnaest poglavlja napravi kurs za ne-tehničke polaznike, ovo poglavlje je za tebe. Nije još jedan modul gradiva; ovo je plan časa.

Jedno pravilo iznad svih: **polaznici ne uče slušajući tebe, uče radeći pored tebe.** Svaka odluka u ovom planu, trajanje, redosled, struktura radionice, proizilazi iz tog pravila.

### Format kursa

- **6 radionica po 2 do 2,5 sata**, jednom nedeljno. Nedeljni razmak nije slučajan: polaznicima treba vreme između radionica da rade na završnom projektu i da se sapletu, jer se na sapletanju uči.
- **Uživo ili onlajn**, oba formata rade. Online zahteva da svaki polaznik deli ekran kad zapne; uživo zahteva da ti hodaš po sali i gledaš ekrane. U oba slučaja, predavač mora da vidi šta polaznik radi, ne samo da čuje šta kaže.
- **Završni projekat projekat** se proteže kroz ceo kurs: svaki polaznik bira svoj mali proizvod na drugoj radionici i lansira ga do šeste. Kurs bez kapstona je predavanje; kurs sa kapstonom je transformacija.
- Maksimalno **8–10 polaznika** po predavaču. Više od toga i nećeš stići da odglaviš svakoga ko zapne u samostalnom delu.

### Mapa radionica

| Radionica | Moduli | Cilj sa kojim svako odlazi kući |
|---|---|---|
| R1 | Moduli 0–2 | Mindset „ti si direktor" + postavka: **svi polaznici odu sa instaliranim i pokrenutim Claude Code-om** i prvim obavljenim razgovorom |
| R2 | Moduli 3–4 | Temelji (git, GitHub, `/init`) + specifikacija: **svako napiše `docs/spec.md` svoje ideje za završni projekat** |
| R3 | Moduli 5–6 | Plan mode + ritam razvoja: **svako izgradi prvu funkcionalnost uživo**, kroz ciklus plan → izvršenje → dokaz → commit |
| R4 | Moduli 7–8 | Autonomni rad (`/goal`, `/loop`) + kvalitet (`/code-review`, `/security-review`): svako pusti prvi autonomni zadatak sa zaštitnim ogradama |
| R5 | Moduli 9–10 | Lansiranje + život posle: **svako lansira preview verziju svog proizvoda** na javnu adresu |
| R6 | Moduli 11–13 | Majstorstvo promptovanja, ekosistem, dijagnostika problema + **prezentacije završnih projekata** |

Redosled ne menjaj. R1 mora da se završi instalacijom kod svih, polaznik koji ode kući bez radnog okruženja na drugoj radionici sedi i gleda, a posle treće odustaje. Zato u R1 planiraj duži samostalni blok i dođi spreman na uobičajene zastoje (Node.js verzije, prijava na nalog, antivirus koji blokira terminal).

### Struktura svake radionice

Svaka radionica prati isti ritam od četiri bloka:

1. **Demo uživo (20 min)**, ti radiš, oni gledaju. Ne slajdove: pravi projekat, pravi terminal, pravi promptovi. Razmišljaj naglas: „Sad ću tražiti plan pre izmena, jer ne želim da menja fajlove dok ne vidim kuda ide."
2. **Vežba zajedno (40 min)**, svi rade isti zadatak istovremeno, ti diktiraš tempo korak po korak. Niko ne ide dalje dok svi nisu prošli kontrolnu tačku („svi vidite zeleni test? idemo dalje").
3. **Samostalni zadatak (40 min)**, svako radi na svom završnom projektu, primenjujući ono iz vežbe. Ti kružiš i odglavljuješ. Ovde se gradivo pretvara u veštinu.
4. **Diskusija grešaka (20 min)**, svako podeli jednu stvar koja mu nije radila i kako ju je (ili nije) rešio.

Zašto je diskusija grešaka najvredniji deo? Iz tri razloga. Prvo, **greške su gradivo koje ne možeš isplanirati**, svaki polaznik udari u drugačiji zid, pa grupa za 20 minuta vidi osam različitih problema i osam oporavaka, što je više dijagnostičkog iskustva nego što bi sam skupio za mesec dana. Drugo, **normalizuje neuspeh**: ne-tehnički polaznici greške doživljavaju kao dokaz da „ovo nije za njih", kad čuju da je i najbolji u grupi zaglavio, taj strah nestaje, a baš taj strah je razlog broj jedan zašto ljudi odustanu. Treće, vežbaš ih u **jeziku dijagnoze** iz Modula 13: simptom → dijagnoza → lek. Insistiraj na formatu: „Šta si očekivao? Šta se desilo? Šta je bio dokaz? Šta si pokušao?", to je tačno onaj refleks koji im treba kad kurs prođe a tebe više nema pored.

### Završni projekat projekat

Svaki polaznik na R2 bira **mali, stvarni proizvod**: jedan problem, jedna ciljna grupa, jedna stvar koju aplikacija radi. Ne „platforma za fitnes" nego „stranica gde moji klijenti zakazuju termin i dobiju potvrdu imejlom". Pravilo iz Modula 4 ovde sprovedi nemilosrdno: ako spec ne staje na jednu stranu, projekat je prevelik za šest nedelja.

Tvoja najvažnija intervencija na R2 je rezanje obima. Polaznici će se opirati, svaki misli da je baš njegova treća funkcionalnost neophodna. Pomozi sebi promptom koji svi zajedno pokrenu nad svojim spec-om:

```
Pročitaj docs/spec.md. Ja imam 4 nedelje i radim sa Claude Code-om
po 3-4 sata nedeljno. Predloži šta da izbacim iz prve verzije da
proizvod ostane koristan, a obim realan. Budi nemilosrdan, za
svaku stavku koju zadržiš objasni zašto je nezamenljiva.
```

Stvarni proizvod znači: na kraju kursa postoji javna adresa, i bar jedna osoba koja nije polaznik ga je upotrebila. To je cilj prezentacija na R6, ne „pogledajte moj kod", nego „evo šta sam lansirao i evo šta je prvi korisnik rekao".

### Merljivi kriterijumi uspeha polaznika

Primeni princip iz Modula 1 na sopstveni kurs: uspeh se dokazuje, ne tvrdi. Polaznik je uspešno završio kurs ako:

- [ ] Ima projekat na GitHub-u sa istorijom commit-ova kroz sve nedelje kursa (ne jedan džinovski commit poslednje večeri)
- [ ] Projekat ima `CLAUDE.md` i `docs/spec.md` koje je sam pisao i menjao
- [ ] Bar jedna funkcionalnost je izgrađena kroz ciklus: plan mode → odobrenje → implementacija → dokaz (test ili snimak ekrana) → commit
- [ ] Pokrenuo je `/code-review` i `/security-review` i rešio bar jedan nalaz
- [ ] Proizvod je lansiran na javnu adresu (preview je dovoljan) i bar jedna spoljna osoba ga je koristila
- [ ] Na prezentaciji ume da odgovori: „šta bi sledeće dodao i kako bi to tražio od Claude-a", to pokazuje da je proces postao njegov

Primeti šta ovde nema: ni jedan kriterijum ne meri kvalitet koda. Polaznici nisu programeri i neće to postati za šest nedelja, mere se proces, dokazi i lansiran proizvod.

### Saveti za predavača

**Tri tačke zbunjenosti, i kako ih demonstrirati.** Iskustvo kaže da ne-tehnički polaznici zapinju na ista tri mesta:

1. **Terminal.** Crni prozor sa trepćućim kursorom je za mnoge prvi susret sa računarom bez ikona. Demistifikuj ga analogijom: terminal je šalter, umesto da hodaš po zgradi i tražiš pravu kancelariju (klikćeš po menijima), priđeš šalteru i kažeš tačno šta hoćeš. Demonstriraj sa tri bezopasne komande (`pwd`, gde sam, `ls`, šta je ovde, `cd`, idem tamo) i odmah pređi na poentu: čim pokrenu `claude`, dalje pričaju normalnim jezikom. Terminal je samo predvorje.
2. **Git.** Apstraktan je dok ga ne vide kao vremeplov. Demonstriraj uživo: napravi izmenu, commit-uj je, pa namerno „upropasti" fajl i vrati se na prethodno stanje. Taj jedan minut, „vidite, ništa nije izgubljeno", vredi više od pola sata teorije o granama. Poruka koju nosiš kroz ceo kurs: commit posle svakog koraka koji radi, jer je commit tačka na koju uvek možeš da se vratiš (detaljno u Modulu 3).
3. **Dozvole.** Kad Claude prvi put pita „da li smem da pokrenem ovu komandu?", polaznici se uplaše da su nešto pokvarili. Objasni unapred: to je sigurnosna provera, kao kad ti novi saradnik kaže „hoću da pošaljem ovaj imejl klijentu, jesi saglasan?", znak da sistem radi, ne da je nešto pošlo naopako. Pokaži kako odobravanje izgleda, šta znači lista dozvoljenih komandi u `.claude/settings.json`, i pomeni da skill `/fewer-permission-prompts` ume da predloži bezbednu listu (detaljno u Modulu 7).

**Namerno izazovi grešku uživo.** Ovo je najjači trik u tvom arsenalu. Negde u demou, najbolje na R3, namerno traži nešto dvosmisleno ili pusti da build pukne, pa pred svima prođi kroz oporavak: pročitaj poruku o grešci naglas, prevedi je na običan jezik, nalepi je Claude-u i traži dijagnozu, pritisni `Esc` ako je krenuo pogrešnim putem i preusmeri ga. Polaznici koji su videli predavača kako mirno izlazi iz greške ne paniče kad se njima desi, a desiće se iste večeri. Ako greška neće da se desi sama, izazovi je: traži funkcionalnost bez ikakvog konteksta („dodaj plaćanje") i pokaži zašto je rezultat loš, pa isti zahtev formuliši po formuli iz Modula 6 i pokaži razliku.

**Koristi šablone iz Dodatka B kao radne listove.** Ne teraj polaznike da promptove smišljaju iz glave dok su početnici, podeli šablone iz Dodatka B (odštampane ili kao fajl) i neka u samostalnom delu radionice popunjavaju praznine svojim projektom. Šablon za spec na R2, šablon za funkcionalnost na R3, šablon za `/goal` uslov na R4, kontrolna lista pre lansiranja na R5. Vremenom će šablone odbaciti sami, ali u prvim nedeljama, popunjavanje praznina pretvara paralizu pred praznim ekranom u rutinu.

I poslednji savet: vodi sopstveni završni projekat paralelno sa polaznicima. Predavač koji svake nedelje pokaže svoj napredak, svoje greške i svoje commit-ove nije autoritet koji priča o plivanju sa obale, on je u vodi, pored njih. To je ton celog ovog dokumenta, i ton koji kurs čini uspešnim.
