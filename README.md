# SVG Icons to Svelte Components - Generator
Die in ```src/lib/icons/utils/icons.json/``` gespeicherten svgs sind größtenteils Zondicons. Eine Übersicht der verfügbaren Zondicons findet sich [hier](https://www.zondicons.com/icons.html). Zondicons sind frei nutzbar im Rahmen der [MIT-Lizenz](https://github.com/dukestreetstudio/zondicons/blob/master/LICENSE).

## Erzeugung von Komponenten mit iconGen.py
Oben findet sich das Skript ```iconGen.py```. Damit lassen sich aus einem Verzeichnis mit ```.svg```-Dateien Svelte Komponenten erzeugen.
Benutzung:  
```console
python iconGen.py <svg directory> <destination directory> <"append" (optional)>
```
Beipspiel zum Erzeugen komplett neuer Icons samt Verzeichnis:
```console
python iconGen.py "C:\Downloads\icons" "C:\Users\UserName\Documents\rezepte\src"
```
Beispiel zum Einfügen zusätzlicher Icons in ein bestehendes Verzeichnis:
```console
python iconGen.py "C:\Downloads\zusatz-icons" "C:\Users\UserName\Documents\rezepte\src" "append"
```
Das Zielverzeichnis ist in der Regel der ```src```-Ordner des Svelte-Projekts.  
Dies erzeugt am Ziel folgende Struktur:
```console
lib
|---components  # enthält Svelte-Komponenten
|---utils
    |---Icon.svelte
    |---icons.json
```
Die Komponenten in ```components``` sind Wrapper für ```Icon.svelte```. Die Komponente ```Icon.svelte``` erzeugt alle Icons mithilfe der ```icons.json```, die die Pfade der SVGs enthält. Vorteil davon ist, dass Veränderungen, die an ```Icon.svelte``` vorgenommen werden, sich direkt auf alle Icon-Komponenten auswirken, ohne, dass ein neuer Build erforderlich wäre.   
  
## Konfiguration von Svelte
In ```lib/icons/components``` finden Sich die generierten Svelte-Komponenten. Alle Importe innerhalb der Komponenten werden mit der alias-Variable ```$lib``` realisiert. Sollte diese noch nicht gesetzt worden sein (eigentlich passsiert das beim Erstellen eines Svelte-Projektes automatisch), so muss nur folgendes in ```svelte.config.js``` eingefügt werden:
```js
/** @type {import('@sveltejs/kit').Config} */
const config = {
	// Consult https://github.com/sveltejs/svelte-preprocess
	// for more information about preprocessors
	preprocess: preprocess(
		{
			postcss: true,
		}
	),

	kit: {
		adapter: adapter(),
        //###############################
        //this block needs to be inserted
		alias: {                   
			'$lib': 'src/lib',
			'$lib/*': 'src/lib/*'
		}
        //###############################
	}
};

export default config;
```