import puppeteer from "puppeteer";
import Jimp from "jimp";
// Custom timeout function for delays
function wait(ms) {
    return new Promise((resolve)=>setTimeout(resolve, ms));
}
// Função para tentar fechar banners
async function closeBanners(page) {
    const selectors = [
        'button[aria-label="close"]',
        'button[class*="close"]',
        'div[class*="cookie"] button',
        'div[class*="banner"] button'
    ];
    for (const selector of selectors){
        const buttons = await page.$$(selector);
        for (const button of buttons){
            console.log(`Tentando fechar banner usando o seletor: ${selector}`);
            await button.click().catch((e)=>console.error(`Erro ao clicar no botão: ${e.message}`));
            await wait(1000); // Esperar para a ação ser processada
        }
    }
}
// Função para ocultar banners usando CSS e remover fundos escuros
async function hideBanners(page) {
    await page.addStyleTag({
        content: `
             div[class*="cookie"],  div[class*="popup"], 
            div[class*="overlay"], div[class*="backdrop"] {
                display: none !important;
            }
            body.modal-open, body.scroll-locked {
                overflow: auto !important;
                position: static !important;
            }
        ` // Adicione mais regras CSS conforme necessário
    });
}
async function captureScreenshots(page, scrollInterval, outputPath) {
    let scrollHeight = 0;
    let lastScrollHeight = await page.evaluate(()=>document.body.scrollHeight);
    let screenshots = [];
    while(scrollHeight < lastScrollHeight){
        await page.evaluate((scrollHeight)=>window.scrollTo(0, scrollHeight), scrollHeight);
        await wait(200); // Wait for any lazy-loaded content
        // Take a screenshot at this scroll position
        const screenshot = await page.screenshot();
        screenshots.push(screenshot);
        // Update scroll height and calculate next position
        scrollHeight += scrollInterval;
        let newScrollHeight = await page.evaluate(()=>document.body.scrollHeight);
        // Check if the new scroll height has reached the end or remains the same
        if (newScrollHeight === lastScrollHeight && scrollHeight >= lastScrollHeight) {
            break; // Break if no new content is loaded and we are at the end
        } else if (lastScrollHeight - scrollHeight < scrollInterval / 2) break;
        lastScrollHeight = newScrollHeight;
    }
    const images = await Promise.all(screenshots.map((s)=>Jimp.read(s)));
    let totalHeight = images.reduce((acc, img)=>acc + img.getHeight(), 0);
    let maxWidth = Math.max(...images.map((img)=>img.getWidth()));
    const finalImage = new Jimp(maxWidth, totalHeight);
    let y = 0;
    for (let img of images){
        finalImage.blit(img, 0, y);
        y += img.getHeight();
    }
    await finalImage.writeAsync(outputPath);
}
async function takeScreenshot(url, outputPath) {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto(url, {
        waitUntil: 'networkidle2'
    });
    await page.setViewport({
        width: 1344,
        height: 336
    }); // Set the viewport size
    closeBanners(page);
    hideBanners(page);
    await captureScreenshots(page, 800, outputPath); // Adjust scrollInterval based on viewport height
    console.log(`Screenshot saved: ${outputPath}`);
    await browser.close();
}
takeScreenshot('https://uol.com.br/', 'complete-screenshot.png').catch(console.error);
