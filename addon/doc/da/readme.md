# Udvidet Aria #

* Forfatter: Jose Manuel Delicado
* Legacy add-on: NVDA 2019.3 and later can read articles on the web
* NVDA-kompatibilitet: 2017.4 til 2019.2
* Download [stabil version][1]

Denne tilføjelse giver dig mulighed for at tilpasse hvilke ARIA-landmærker,
der rapporteres af NVDA, når du surfer på internettet.

Dens funktionalitet er meget enkel. Når tilføjelsen er installeret, skal du
åbne din webbrowser og besøge internettet som normalt. De standard
ARIA-landmærker, der rapporteres af Firefox og Chrome, vil også være synlige
i Internet Explorer, så du vil være i stand til at trykke på tasterne for
bogstavnavigation for at springe mellem dem og liste dem ved at trykke på
NVDA+f7 i alle browsere. Læs NVDA Brugervejledning for yderligere
information.

Tilføjelsen tilføjer et ekstra landmærke, der ikke er medtaget som standard
i NVDA, artikel (forkortet som art på punkt).

## Indstillingsdialogen

Du kan aktivere eller deaktivere landmærker ved at gå til
NVDA-menuen>Opsætning>Enhanced ARIA Settings eller fra den relevante
kategori i NVDA-indstillingsdialogboksen. Dialogboksen har et
afkrydsningsfelt for hvert landmærke. Hvis du deaktiverer et landmærke, kan
du ikke hoppe til det ved at trykke på d-tasten, når du surfer på en
webside, og NVDA vil ikke rapportere det.

## Kontaktinfo

Denne tilføjelse er udviklet af Jose Manuel Delicado. Hvis du ønsker at
kontakte mig, send en e-mail til jm.delicado@nvda.es, eller åbn et issue på
GitHub https://github.com/jmdaweb/enhancedAria

## Ændringslog

### Version 2.8

* Nye og opdaterede oversættelser.
* Updated NVDA compatibility flags.

### Version 2.7

* Opdaterede kompatibilitetsflag til nyere NVDA-versioner.
* Nye og opdaterede oversættelser.

### Version 2.6

* Opdaterede kompatibilitetsflag til nyere NVDA-versioner. Denne version er
  kun kompatibel med NVDA 2017.4 og nyere.
* Nye og opdaterede oversættelser.
* Nu anvendes konfigurationen automatisk efter skift af NVDA-profiler og
  gendannelse af indstillinger til fabriksindstillingerne.

### Version 2.5

* Opdaterede kompatibilitetsflag til nyere NVDA-versioner.

### Version 2.4

* Nu bliver indstillingerne kun fjernet, når tilføjelsen er
  afinstalleret. Konfigurationen nulstilles ikke længere ved opgradering.
* Nye og opdaterede oversættelser.

### Version 2.3

* Tilføjede kompatibilitet for seneste NVDA-versioner.
* Nye oversættelser.

### Version 2.2

* Rettede en fatal fejl, når et punktdisplay blev brugt, og rollen "article"
  blev konfigureret til at blive rapporteret.

### Version 2.1

* Stabilitetsforbedringer

### Version 2.0

* understøtter nu indstillingsdialog med listen af flere kategorier,
  tilgængelig i NVDA 2018.2 og nyere
* Gjorde tilføjelsen kompatibel med Python 3
* Modulet GuiHelper bruges nu til at skabe brugergrænsefladen for
  tilføjelsespakken

### Version 1.3

* Tilføjede configobj-specifikation for tilføjesesindstillinger

### Version 1.2

* Fejl rettede

### Version 1.1

* Rettede problemer, der forhindrede at åbne dialogboksen til
  tilføjelsesindstillinger, når du vendte tilbage til NVDA-gemt
  konfiguration

[[!tag dev stable legacy]]

[1]: https://addons.nvda-project.org/files/get.php?file=earia
