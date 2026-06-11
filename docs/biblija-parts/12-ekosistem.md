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
