# dolphin.css

`dolphin.css` was something that came out of [water.css](https://watercss.kognise.dev/) 
which is a very nice drop-in collection of CSS styles.

Here is a [demo of dolphin.css](https://diversen.github.io/dolphin.css/)

Main difference: 

* All styles in a single file and two theme files (light and dark)
* No build system
* Removed some of the styles
* If you need to develop on the water repository, then your `node_modules` will take 968 MB of space. 
* This takes up 44 KB

# Usage:

Clone the repository. 

Copy a theme file, `light.css` or `dark.css`, and link it in your HTML file.
Then copy the `dolphin.css` file and link it in your HTML file just below the theme file.

Something like this will do it: 

```html
<link id="theme-select" rel="stylesheet" href="/css/dark.css">
<link rel="stylesheet" href="/css/dolphin.css">
```

If you want to use a theme-shifter, then take a look at the index.html file and the script.js

Live reload while developing: 

    npm install browser-reload -g
    browser-reload 

# License

MIT © [Dennis Iversen](https://github.com/diversen)