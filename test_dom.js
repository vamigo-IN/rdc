const fs = require('fs');
const jsdom = require('jsdom');
const { JSDOM } = jsdom;

const html = fs.readFileSync('dental-implants/index.html', 'utf8');
const script = fs.readFileSync('assets/js/main.js', 'utf8');

const dom = new JSDOM(html, { runScripts: "dangerously" });
try {
    dom.window.eval(script);
    console.log("Script executed without throwing.");
} catch (e) {
    console.error("Error executing script:", e);
}
