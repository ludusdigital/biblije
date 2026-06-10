## Modul 9: Lansiranje — od tvog računara do interneta

Do sada je tvoj proizvod živeo samo na tvom računaru: radio je, prošao preglede kvaliteta iz Modula 8 — ali niko osim tebe ne može da ga vidi. U ovom modulu izlazi na internet: prvo na probnu adresu koju vidiš samo ti, zatim na pravu, javnu adresu sa tvojim domenom.

### Šta ćeš naučiti

- Šta znači deploy i zašto se uvek radi u dva koraka: prvo proba, pa javnost
- Kako da povežeš projekat sa Vercel-om i objaviš ga uz pomoć Claude-a
- Šta su env varijable i zašto API ključevi nikad ne smeju u kod
- Zašto ti trebaju odvojene baze za testiranje i produkciju
- Pre-launch checklist i strategiju mekog lansiranja

### Šta je deploy: otvaranje radnje

Zamisli da si nedeljama pravio nameštaj u svojoj radionici — ali radionica je zaključana i mušterije ne mogu da uđu. **Deploy** (izgovara se „diploj") je trenutak kad otvoriš radnju na glavnoj ulici: kopiraš aplikaciju sa svog računara na servere koji su stalno upaljeni i dostupni svima na internetu.

Tvoj računar nije dobar server: gasiš ga, nosiš ga na put, internet ti varira. Zato u ovom kursu koristimo **Vercel** — servis koji uzme tvoj kod sa GitHub-a (postavili smo ga u Modulu 3), sagradi aplikaciju i drži je dostupnom 24/7, a uz to odlično sarađuje sa Claude Code-om kroz vercel plugin.

### Pre nego što počneš

Dva preduslova. Prvo, besplatan nalog na vercel.com — obična registracija klikovima, kao na bilo kom servisu. Drugo, vercel plugin u Claude Code-u; zamoli Claude-a:

```
Hoću da dodam vercel plugin u ovaj projekat, provedi me kroz
instalaciju korak po korak.
```

Detaljna priča o plugin-ovima čeka te u Modulu 12; za sada je dovoljno da je instaliran — bez njega komande iz ovog modula ne postoje u tvojoj sesiji.

### Korak 1: Povezivanje — `/vercel:bootstrap`

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

### Korak 2: Preview deploy — proba pre javnosti

Ovde dolazi najvažnija navika ovog modula: **nikad ne ideš direktno u produkciju**. Prvo praviš preview deploy — probnu verziju na privatnom linku koji znaš samo ti. To je generalna proba u pozorištu: sve je kao na premijeri, samo publika još nije ušla.

```
/vercel:deploy
```

Bez dodatnih argumenata, ova komanda pravi upravo preview deploy. Kad se završi, otvori dobijeni link i prođi kroz aplikaciju kao prvi korisnik: registruj se, klikni svako dugme, probaj glavni tok od početka do kraja. Na svom računaru si testirao hiljadu puta — ali server je drugačije okruženje, i baš tu isplivaju greške tipa „kod mene radi".

### Korak 3: Produkcija

Tek kad preview verzija radi besprekorno, šalješ u produkciju:

```
/vercel:deploy prod
```

To je premijera — aplikacija je na javnoj adresi, dostupna svakome. Vercel automatski daje adresu oblika `tvoj-projekat.vercel.app`, sasvim dovoljnu za početak.

### Env varijable: ključevi od stana se ne lepe na vrata

Tvoja aplikacija koristi tajne: API ključ za OpenAI, lozinku za bazu, slično. **API ključ** je kao ključ od stana — ko ga ima, ulazi i troši o tvom trošku. Ako ključ završi u kodu, a kod ode na GitHub, to je kao da si ga zalepio na ulazna vrata sa ceduljom „izvolite". Botovi non-stop pretražuju GitHub baš tražeći ovakve procurele ključeve — zloupotreba stiže za par minuta.

Rešenje su **env varijable** (environment variables, „promenljive okruženja"): tajne se čuvaju van koda, u posebnom sefu — lokalno u fajlu `.env.local` koji nikad ne ide na git, a na Vercel-u u podešavanjima projekta. Kod onda kaže samo „uzmi ključ iz sefa", bez ključa u sebi.

Dobra vest: ovo ne radiš ručno — zamoli Claude-a:

```
Proveri ceo projekat: da li je neki API ključ, lozinka ili tajna upisana
direktno u kod? Ako jeste, prebaci je u env varijablu, dodaj je u
.env.local, i proveri da je .env.local naveden u .gitignore fajlu
(da nikad ne ode na GitHub). Zatim mi izlistaj sve env varijable koje
moram da unesem u Vercel za produkciju, sa objašnjenjem čemu svaka služi.
```

Komanda `/security-review` iz Modula 8 takođe hvata procurele tajne pre nego što odu na GitHub — još jedan razlog da je pokrećeš redovno.

### Tvoj domen: adresa radnje

`tvoj-projekat.vercel.app` radi, ali deluje privremeno. Sopstveni domen (`tvojproizvod.com` ili `.rs`) je adresa tvoje radnje i deo brenda: kupuješ ga kod registra (Namecheap, GoDaddy, za .rs domene domaći registri), pa ga povežeš sa Vercel projektom kroz DNS podešavanja — internet imenik koji ukucanu adresu vodi na pravi server. U praksi je to unošenje dve-tri vrednosti koje ti Vercel prikaže. Zamoli Claude-a da te provede:

```
Kupio sam domen mojproizvod.rs kod [ime registra]. Provedi me korak po
korak kroz povezivanje tog domena sa mojim Vercel projektom: šta tačno
da unesem u DNS podešavanja kod registra i kako da proverim da je uspelo.
```

### Dve baze: nikad ne testiraš na pravim podacima

Ako tvoj proizvod koristi bazu podataka (preko supabase plugin-a iz Modula 5), od lansiranja važi gvozdeno pravilo: **odvojena baza za razvoj, odvojena za produkciju**.

Zašto? Zamisli da posle lansiranja kažeš Claude-u „obriši sve test naloge", a povezan si na produkcijsku bazu — upravo si obrisao prave korisnike. Sa dve baze takva greška košta te nula: razvojnu slobodno puniš, brišeš i lomiš, produkcijska ostaje netaknuta.

```
Hoću odvojene Supabase baze za razvoj i produkciju. Postavi projekat tako
da lokalni razvoj koristi razvojnu bazu, a Vercel produkcija produkcijsku,
preko env varijabli. Na kraju mi pokaži kako da u svakom trenutku proverim
na koju bazu sam trenutno povezan.
```

### Pre-launch checklist i soft launch

Pre nego što adresu podeliš sa svetom, prođi listu na kraju modula. Dve stavke zaslužuju dodatnu reč:

**Pravne stranice.** Uslovi korišćenja i politika privatnosti nisu ukras — ako prikupljaš bilo kakve podatke korisnika (čak i samo email), zakonski su obavezne. Claude ti može sastaviti solidan nacrt prilagođen tvom proizvodu; za ozbiljan biznis daj ga pravniku na pregled.

**Praćenje grešaka.** Kad korisniku nešto pukne, najčešće ti neće javiti — samo će otići. Zato zamoli Claude-a da u aplikaciju uveže servis za praćenje grešaka (npr. Sentry), koji ti javi čim se greška pojavi. Više o tome u Modulu 10.

I na kraju — **soft launch** („meko lansiranje"). Ne objavljuj proizvod odmah svima: prvo ga pošalji grupi od 5–15 poznanika i zamoli ih da ga koriste nedelju dana. Oni će naći probleme na koje ne bi pomislio, a oprostiće ti ih — nepoznata publika neće, ona se ne vraća. Tek kad prva grupa prođe bez ozbiljnih problema, ideš javno.

### Vežba

0. Ako već nisi: nalog na vercel.com i vercel plugin (prompt iz odeljka „Pre nego što počneš").
1. Pokreni Claude Code u folderu projekta i izvrši `/vercel:bootstrap`. Ako zapne, nalepi Claude-u poruku o grešci i traži objašnjenje.
2. Pokreni prompt za proveru tajni iz odeljka o env varijablama. Uveri se da nijedan ključ nije u kodu i da je `.env.local` u `.gitignore`.
3. Napravi preview deploy: `/vercel:deploy`. Otvori dobijeni link i prođi glavni tok kao novi korisnik. Zapiši svaki problem.
4. Ako si našao probleme, reši ih sa Claude-om (ritam iz Modula 6), pa ponovi preview.
5. Pokreni `/security-review`, a zatim zamoli Claude-a: „Pokreni sve testove i pokaži mi izlaz" — oba moraju biti čista.
6. Tek tada: `/vercel:deploy prod`. Otvori javnu adresu sa telefona, ne sa svog računara — i čestitaj sebi.
7. Pošalji link trojici poznanika sa molbom da probaju i jave šta ih je zbunilo.

### Najčešće greške

1. **Prvi deploy ide pravo u produkciju.** „Radi kod mene" ne znači „radi na serveru". Rešenje: uvek prvo `/vercel:deploy` (preview), klikći kroz aplikaciju na privatnom linku, pa tek onda `prod`.
2. **API ključ završi na GitHub-u.** Najskuplja greška ovog modula — botovi je nalaze za par minuta. Rešenje: prompt za proveru tajni pre svakog deploy-a; procureli ključ odmah poništi kod izdavaoca (OpenAI, Supabase…) i napravi novi — brisanje iz koda nije dovoljno, git pamti istoriju.
3. **Jedna baza za sve.** Testiranjem nove funkcije obrišeš ili iskvariš prave podatke korisnika. Rešenje: odvojena razvojna i produkcijska baza od prvog dana, povezane preko env varijabli.
4. **Aplikacija radi na preview linku, ali ne u produkciji.** Najčešći uzrok: env varijable unete za preview, ali ne i za produkciju. Rešenje: zamoli Claude-a da uporedi okruženja i izlista šta nedostaje.
5. **Veliko lansiranje bez probne publike.** Sve karte na javnu objavu prvog dana, pa prvi utisak pokvari bag koji bi poznanik našao za sat. Rešenje: soft launch — mala grupa prvo, javnost posle.

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
- [ ] Soft launch: 5–15 poznanika koristilo proizvod pre javne objave

### Proveri znanje

**Zašto se nikad ne ide direktno u produkciju, nego prvo na preview deploy?**
Server je drugačije okruženje od tvog računara — greške koje lokalno ne vidiš isplivaju tek tamo. Preview je generalna proba na privatnom linku: greške hvataš pre korisnika.

**Šta su env varijable i šta uraditi ako API ključ ipak završi na GitHub-u?**
Tajne (ključevi, lozinke) koje se čuvaju van koda — lokalno u `.env.local`, na Vercel-u u podešavanjima projekta. Procureli ključ odmah poništi kod izdavaoca i napravi novi; brisanje iz koda ne pomaže, git pamti istoriju.

**Zašto su potrebne dve odvojene baze podataka?**
Da razvoj nikad ne dira prave podatke korisnika: razvojnu bazu smeš da lomiš bez posledica, produkcijska ostaje netaknuta, a koju kod koristi određuju env varijable po okruženju.
