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
