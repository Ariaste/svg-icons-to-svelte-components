# SVG Icons to Svelte Components - Generator

The SVGs provided in ```example_of_generated_icons/lib/icons/utils/icons.json/``` are mostly zondicons. [Here](https://www.zondicons.com/icons.html) you find an overview about all zondicons. They are provided under [MIT license](https://github.com/dukestreetstudio/zondicons/blob/master/LICENSE).

## Creating components with iconGen.py
Take a look at the script ```iconGen.py```above. With this, you can create Svelte components out of ```.svg```files.

### Syntax:  
```console
python iconGen.py <svg directory> <destination directory> <"append" (optional)>
```

Example for creating a whole new directory of icon components:
```console
python iconGen.py "C:\Downloads\icons" "C:\Users\UserName\Documents\rezepte\src"
```

Example for inserting additional icons into an existing directory:
```console
python iconGen.py "C:\Downloads\zusatz-icons" "C:\Users\UserName\Documents\rezepte\src" "append"
```

The destination path will normally be the ```src``` directory of your Svelte project. This creates the following structure:
```console
lib
|---components  //contains Svelte components
|---utils
    |---Icon.svelte
    |---icons.json
```

The Svelte components in ```lib/icons/components```  are wrappers for ```lib/icons/utils/Icon.svelte```. The component ```Icon.svelte``` displays all icons provided in ```lib/icons/util/icons.json```. The main advantage of this approach is the flexibililty: all changes in ```Icon.svelte``` are affecting the wrapper components without building them again.
  
## Configuration of Svelte
In ```lib/icons/components``` the generated icon components are found. All js imports are realised with the alias variable ```$lib```. If this alias is not already established in your project, you can add it by editing your ```svelte.config.js``` as follows:
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
## Using the generated Svelte components

### All generated components share the following properties:
+ size: icon size in rem (default: 1)
+ direction: icon direction in degree (default: 0)
+ className: css classes to apply (default: "")
+ color: icon css color (default: black)
+ hover: css color by mouse hovering (default: "")
+ rotationSpeed: in degrees per second, positive value clockwise, negative value counterclockwise (default: 0)
+ backgroundColor: icon  css background color (default: inherit)

### Example of use
```svelte
<AddOutline 
	size=2 
	direction=45 
	className="my-css-class" 
	color=blue 
	hover=green 
	rotationSpeed=10 
	backgroundColor=grey  
/>
```

## License
This code is provided under [MIT license](LICENSE). 