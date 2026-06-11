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
