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
