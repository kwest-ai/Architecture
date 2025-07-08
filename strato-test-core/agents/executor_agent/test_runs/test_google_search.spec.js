import { test, expect } from '@playwright/test';
test('Google Search', async ({ page }) => {
  await page.goto('https://www.google.com');
  await page.fill('input[name="q"]', 'Playwright');
  await page.keyboard.press('Enter');
  await page.waitForSelector('text=playwright.dev');
  const title = await page.title();
  expect(title).toContain('Playwright');
});