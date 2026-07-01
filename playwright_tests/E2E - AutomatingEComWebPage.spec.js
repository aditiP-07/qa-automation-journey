const { test, expect } = require('@playwright/test');

test('Automating ECommerce Web Page', async ({ page }) => {
    await page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    await page.locator("#userEmail").fill("prasad.aditi.4900@gmail.com")
    await page.locator("#userPassword").fill("t$7K9A5D!VG4RkJ")
    await page.locator("#login").click()

    await page.waitForLoadState('networkidle')

    await page.locator(".card-body button").nth(1).click()
    await page.locator('ul button').nth(2).click() //for clicking on cart
    await page.locator("button:has-text('Checkout')").click() //await page.locator('ul button').nth(2).click() (not writing this because it would confuse you later on)
    await page.locator('input').nth(2).fill("666")
    await page.locator('input').nth(3).fill("Aditi Prasad")
    await page.getByPlaceholder("Select Country").pressSequentially("ind", {delay:150}) //sometimes it fails because the application server is slow, dealy:!50 ms gives it sufficent time to respond
    const dropdown = page.locator(".ta-results")
    await dropdown.waitFor()
    const optionsCount = await dropdown.locator("button").count()
    for (let i = 0; i < optionsCount; ++i){
        const text = await dropdown.locator("button").nth(i).textContent()
        if (text === " India"){
            await dropdown.locator("button").nth(i).click()
            break
        }
    }
    await page.locator('a.btnn.action__submit').click()

    await expect(page.locator(".hero-primary")).toHaveText(" Thankyou for the order. ")
    const orderID = await page.locator(".em-spacer-1 .ng-star-inserted").textContent()
    console.log("Order ID:", orderID)

    await page.locator('ul button').nth(1).click() //for clicking on Orders
    const rows = await page.locator("tbody tr")
    for (let i = 0; i < await rows.count(); ++i){
        const rowOrderID = await rows.nth(i).locator("th").textContent()
        if (orderID.includes(rowOrderID)){
            await rows.nth(i).getByRole('button', { name: 'View' }).click();
            await page.locator(".col-text.-main").waitFor();
            break
        }
    }
    await page.pause()
});