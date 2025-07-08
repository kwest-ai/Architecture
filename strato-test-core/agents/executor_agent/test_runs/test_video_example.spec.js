import { test, expect } from '@playwright/test';
test.use({ video: 'on' });
test('Wikipedia Title', async ({ page }) => {
  await page.goto('https://en.wikipedia.org/wiki/Playwright');
  await expect(page).toHaveTitle(/Playwright - Wikipedia/);
});