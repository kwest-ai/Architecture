import { test, expect } from '@playwright/test';
test.use({ video: 'on' });
test('Wikipedia Deep Navigation', async ({ page }) => {
  await page.goto('https://en.wikipedia.org/wiki/Main_Page');
  await page.fill('input[name="search"]', 'Selenium (software)');
  await page.keyboard.press('Enter');
  await page.waitForSelector('h1');
  await expect(page.locator('h1')).toHaveText('Selenium (software)');
  
  // Reduce unnecessary waits
  await page.locator('span#History').scrollIntoViewIfNeeded();
  await expect(page.locator('span#History')).toBeVisible(); 

  // Remove redundant waits at the beginning and end
});