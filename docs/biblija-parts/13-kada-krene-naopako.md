## Modul 13: Kada stvari krenu naopako

Pre nego što kreneš dalje, jedna rečenica koju vredi zapamtiti: **skoro ništa nije nepovratno.** Ako si pratio Modul 3 i radiš sa git-om — sistemom koji čuva snimak projekta posle svake zaokružene celine (commit) — tvoj projekat ima "save point" kao u video igrici. Najgore što se obično desi jeste da izgubiš sat vremena, ne projekat. Ovo poglavlje je tvoj kućni priručnik prve pomoći: za svaki problem prvo prepoznaš simptom, zatim razumeš dijagnozu, pa primeniš lek.

### Šta ćeš naučiti

- Kako da prepoznaš sedam najčešćih problema u radu sa Claude Code-om
- Kada da pritisneš `Esc` i preusmeriš Claude-a, a kada da kreneš iz čistog konteksta sa `/clear`
- Kako da od Claude-a uvek tražiš dokaz umesto da veruješ na reč
- Kako da git iskoristiš kao vremeplov kada nešto što je radilo prestane da radi
- Kada je problem prevelik za tebe i Claude-a — i kako da pripremiš pitanje za stručnjaka

### Scenario 1: Claude ide u pogrešnom smeru

**SIMPTOM:** Gledaš kako Claude radi i vidiš da pravi nešto što nisi tražio — drugi ekran, pogrešnu funkcionalnost, izmene u delu aplikacije koji nisi ni pomenuo.

**DIJAGNOZA:** Tvoj prompt je bio dvosmislen ili je Claude pogrešno protumačio cilj. Što duže radi u pogrešnom smeru, više posla kasnije čistiš.

**LEK:** Pritisni `Esc` ODMAH. Ne čekaj "da završi pa ćemo videti" — `Esc` prekida Claude-a usred rada i odmah možeš da ga preusmeriš. To nije nepristojno, to je tvoj posao kao direktora (Modul 0).

```
Stani. Krenuo si da menjaš stranicu za prijavu, a ja sam tražio izmenu
na stranici sa podešavanjima. Vrati izmene koje si do sada napravio,
pa mi prvo ukratko opiši šta planiraš — ne menjaj ništa dok ne odobrim.
```

### Scenario 2: Vrti se u krug sa istom greškom

**SIMPTOM:** Claude treći put "popravlja" isti bag, svaki put kaže "sada bi trebalo da radi" — i svaki put iskoči ista greška.

**DIJAGNOZA:** Claude je zaglavljen u jednom pristupu i pokušava varijacije istog rešenja. Razgovor pun neuspelih pokušaja ga dodatno vuče ka istim idejama.

**LEK:** Zaustavi ga i nateraj da promeni perspektivu:

```
Stani sa popravkama. Objasni mi prostim jezikom, bez žargona:
šta je tačno problem i zašto dosadašnji pokušaji nisu uspeli?
Zatim predloži 3 SUŠTINSKI različita pristupa rešenju, sa
prednostima i manama svakog. Ne piši kod dok ne izaberem.
```

Ako ni to ne pomogne, ukucaj `/clear` (briše kontekst i počinje svežu sesiju) i opiši problem iz početka — kratko, fokusirano, bez istorije neuspeha. Svež početak često reši ono što deset zakrpa nije.

### Scenario 3: Kaže "gotovo je", a ne radi

**SIMPTOM:** Claude tvrdi da je funkcionalnost završena. Otvoriš aplikaciju — dugme ne radi, forma se ne šalje, stranica je prazna.

**DIJAGNOZA:** Claude je napisao kod koji *izgleda* ispravno, ali ga nije proverio u stvarnim uslovima. Tvrdnja nije dokaz — to je princip iz Modula 1.

**LEK:** Nikad ne prihvataj "gotovo" bez dokaza. Claude može da pokrene dev server i verifikuje izmene u browseru: da klikće, popunjava forme i pravi screenshotove.

```
Ne verujem dok ne vidim. Pokreni aplikaciju, otvori stranicu za
registraciju u browseru, popuni formu test podacima i pošalji je.
Napravi screenshot rezultata i pokaži mi log — tek onda je gotovo.
```

### Scenario 4: Nešto što je radilo sada je pokvareno

**SIMPTOM:** Prijava korisnika je radila prošle nedelje. Danas, posle nekoliko novih feature-a, više ne radi.

**DIJAGNOZA:** Neka od novijih izmena je usput polomila staru funkcionalnost (programeri to zovu "regresija"). Dešava se i najboljima — zato postoje commit-i.

**LEK:** Git je tvoj vremeplov. Ne moraš da znaš nijednu git komandu — samo reci Claude-u šta hoćeš:

```
Prijava korisnika je radila ranije, a sada ne radi. Pregledaj
istoriju commit-a i pronađi poslednji commit u kom je prijava
radila. Uporedi taj kod sa sadašnjim, reci mi koja izmena je
polomila prijavu, i predloži: da li da popravimo unapred ili
da vratimo projekat na taj commit. Ne menjaj ništa bez odobrenja.
```

Ovo je razlog zašto u Modulu 6 insistiramo na malim, čestim commit-ima: što su save point-ovi gušći, manje posla gubiš vraćanjem.

### Scenario 5: Sesija predugačka, odgovori sve lošiji

**SIMPTOM:** Radite satima u istom razgovoru. Claude počinje da zaboravlja ranije dogovore, meša imena fajlova, odgovara sporije i konfuznije.

**DIJAGNOZA:** Kontekst (radna memorija razgovora) je pretrpan. Zamisli radni sto zatrpan papirima — u nekom trenutku više ne pomaže što je "sve tu", jer se ništa ne nalazi.

**LEK:** `/clear` za svež početak, ili `/compact` ako želiš da sažmeš razgovor a zadržiš suštinu. Ne plaši se da ćeš izgubiti "sve što Claude zna o projektu" — kontinuitet ne čuva razgovor, nego fajlovi: `CLAUDE.md` se učitava na početku svake sesije, a `docs/spec.md` (Modul 4) čuva šta gradiš i zašto. Posle `/clear` samo usmeri Claude-a:

```
Pročitaj docs/spec.md. Radimo na funkcionalnosti izvoza u PDF —
prethodni korak je završen i commit-ovan. Sledeći korak: dugme
za izvoz na stranici izveštaja. Prvo plan, pa implementacija.
```

### Scenario 6: Tvrdnja o spoljnoj biblioteci deluje netačno

**SIMPTOM:** Claude tvrdi da neka biblioteka (tuđi gotov kod koji tvoj projekat koristi, npr. za plaćanja ili slanje mejlova) radi na određeni način — ali kod puca, ili tvrdnja deluje zastarelo.

**DIJAGNOZA:** Claude-ovo znanje ima datum preseka, a biblioteke se menjaju često. Ono što je važilo za prošlogodišnju verziju možda više ne važi.

**LEK:** Traži da proveri svežu dokumentaciju umesto da se oslanja na pamćenje. U promptu ispod pominje se `package.json` — to je fajl u kom projekat vodi spisak biblioteka koje koristi i njihovih verzija, pa Claude tamo proverava koju verziju imaš. Ako imaš instaliran `context7` plugin (Modul 12), on služi baš tome — uvek sveža dokumentacija biblioteka.

```
Pre nego što nastaviš: proveri aktuelnu dokumentaciju za verziju
biblioteke koju koristimo u projektu (pogledaj package.json).
Uporedi ono što si predložio sa zvaničnom dokumentacijom i reci
mi da li se nešto promenilo.
```

### Scenario 7: Vreme je za ljudsku pomoć

**SIMPTOM:** Sumnjaš da su ti procureli podaci korisnika ili pristupni ključevi; dobio si pravno pitanje (GDPR, ugovori, odgovornost); izgubio si podatke iz produkcione baze; u pitanju je novac korisnika.

**DIJAGNOZA:** Ovo više nije tehnički problem koji se rešava boljim promptom. Bezbednosni incidenti, pravna pitanja i gubitak tuđih podataka nose stvarne posledice — tu treba čovek sa iskustvom i, po potrebi, licencom.

**LEK:** Ne guraj sam. Ali Claude ti i ovde pomaže — da pripremiš kvalitetno pitanje, jer stručnjakov sat je skup, a precizno pitanje ga skraćuje:

```
Sumnjam na bezbednosni incident i zvaću stručnjaka. Pomozi mi da
pripremim sažetak: (1) šta se tačno desilo i kada, (2) koji podaci
su potencijalno ugroženi, (3) šta sam već preduzeo, (4) koja pitanja
da postavim. Piši činjenično, bez nagađanja, na jednoj stranici.
```

U međuvremenu: promeni lozinke i pristupne ključeve, ne briši ništa (tragovi pomažu dijagnozi) i zapisuj vremena događaja.

### Vežba

Provežbaj oporavak dok ništa nije na kocki — tako će te pravi problem zateći spremnog:

1. Otvori svoj vežbovni projekat i zamoli Claude-a: `Napravi commit trenutnog stanja sa porukom "stabilna tačka pre vežbe oporavka".`
2. Zatraži namernu izmenu: `Promeni naslov na početnoj stranici u "POKVARENO" i sačuvaj.`
3. Proveri u browseru da je izmena tu (princip dokaza!).
4. Sada glumi krizu: `Naslov je pokvaren. Vrati projekat na poslednji commit gde je naslov bio ispravan i pokaži mi dokaz da je vraćeno.`
5. Proveri u browseru da je sve po starom. Čestitam — upravo si izveo svoj prvi oporavak i uverio se da commit zaista čuva.

### Najčešće greške

1. **Čekaš da Claude "završi pa ćemo ispraviti".** Pogrešan smer se ne ispravlja sam — produbljuje se. Rešenje: `Esc` čim primetiš skretanje, pa preusmeri.
2. **Posle pete neuspele popravke tražiš šestu na isti način.** Rešenje: prekini obrazac — traži objašnjenje prostim jezikom i tri različita pristupa, ili `/clear` pa svež opis.
3. **Prihvataš "gotovo je" bez dokaza.** Rešenje: standardno traži screenshot, test output ili log. Ako uđe u naviku, ovaj scenario skoro nestaje.
4. **Radiš satima bez ijednog commit-a.** Bez save point-a, vremeplov iz Scenarija 4 nema kuda da te vrati. Rešenje: commit posle svake zaokružene celine (Modul 6).
5. **U panici brišeš fajlove ili "resetuješ sve".** Brisanje je jedna od retkih stvarno nepovratnih radnji. Rešenje: prvo duboko udahni, pa pitaj Claude-a da proceni štetu — pre bilo kakve akcije.

### Kontrolna lista

- [ ] Znam da `Esc` prekida Claude-a usred rada i koristim ga čim vidim pogrešan smer
- [ ] Kada se Claude vrti u krug, tražim objašnjenje prostim jezikom + 3 različita pristupa
- [ ] Ne prihvatam "gotovo je" bez dokaza (screenshot, test, log)
- [ ] Redovno commit-ujem, pa uvek imam tačku za povratak
- [ ] Znam da `/clear` ne briše znanje o projektu — `CLAUDE.md` i `docs/spec.md` čuvaju kontinuitet
- [ ] Tvrdnje o spoljnim bibliotekama proveravam kroz svežu dokumentaciju
- [ ] Znam tri situacije u kojima zovem stručnjaka i kako da pripremim pitanje

### Proveri znanje

**1. Claude pravi funkcionalnost koju nisi tražio. Šta radiš — odmah ili kad završi?**
Odmah: pritisni `Esc`, prekini ga i preusmeri. Svaki minut rada u pogrešnom smeru je minut čišćenja kasnije.

**2. Zašto `/clear` nije opasan za projekat, iako briše ceo razgovor?**
Jer kontinuitet ne živi u razgovoru nego u fajlovima: kod i commit-i su na disku, `CLAUDE.md` se učitava na početku svake sesije, a specifikacija u `docs/spec.md` čuva šta gradiš i zašto.

**3. Koje tri vrste problema NE rešavaš sam sa Claude-om, nego zoveš stručnjaka?**
Bezbednosni incident (curenje podataka ili ključeva), pravna pitanja i gubitak produkcionih podataka — svuda gde greška nosi stvarne posledice po korisnike, novac ili zakon.
