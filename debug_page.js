const puppeteer = require('puppeteer');
const http = require('http');
const fs = require('fs');
const path = require('path');

const server = http.createServer((req, res) => {
    let p = '.' + req.url.split('?')[0];
    if (p.endsWith('/')) p += 'index.html';
    const ext = path.extname(p);
    let ctype = 'text/html';
    if (ext === '.css') ctype = 'text/css';
    if (ext === '.js') ctype = 'text/javascript';
    
    fs.readFile(p, (err, data) => {
        if (err) { res.writeHead(404); res.end(); return; }
        res.writeHead(200, {'Content-Type': ctype});
        res.end(data);
    });
});

server.listen(8080, async () => {
    try {
        const browser = await puppeteer.launch({args: ['--no-sandbox']});
        const page = await browser.newPage();
        page.on('console', msg => console.log('PAGE LOG:', msg.text()));
        page.on('pageerror', err => console.log('PAGE ERROR:', err.toString()));
        await page.goto('http://localhost:8080/dental-implants/', {waitUntil: 'networkidle0'});
        await browser.close();
    } catch (e) {
        console.error(e);
    }
    server.close();
});
