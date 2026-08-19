const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ headless: "new" });
  const page = await browser.newPage();
  
  page.on('console', msg => console.log('BROWSER CONSOLE:', msg.text()));
  page.on('pageerror', err => console.log('BROWSER ERROR:', err.message));
  
  await page.goto('http://localhost:5173', { waitUntil: 'networkidle2' }).catch(e => console.log("GOTO ERROR:", e));
  
  const stExists = await page.evaluate(() => typeof window.St);
  console.log("window.St type:", stExists);
  
  if (stExists === 'object') {
      const pageFlipExists = await page.evaluate(() => typeof window.St.PageFlip);
      console.log("window.St.PageFlip type:", pageFlipExists);
  }
  
  const pageFlipGlobal = await page.evaluate(() => typeof window.PageFlip);
  console.log("window.PageFlip type:", pageFlipGlobal);
  
  await browser.close();
})();
