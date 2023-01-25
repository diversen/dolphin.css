# dolphin.css

`dolphin.css` was something that came out of [water.css](https://watercss.kognise.dev/) 
which is a very nice drop-in collection of CSS styles.

Main difference: 

* All styles in a single file (is this a feature?)
* No build system (is this a feature?)
* Removed some of the styles
* If you need to develop on a clone of the water repository, then your `node_modules` will take 968 MB of space. 
* I am a simple man. I like simple thing. This just takes up 44 KB

## Usage:

Clone the repository. 

copy the `light.css` or `dark.css` and link it in your HTML file.
Then copy the `dolphin.css` file and link it in your HTML file below.

Something like this: 

```html
<link id="theme-select" rel="stylesheet" href="dark.css">
<link rel="stylesheet" href="dolphin.css">
```

If you want to use a theme-shifter, then take a look at the index.html file and the script.js

# License

MIT © [Dennis Iversen](https://github.com/diversen)