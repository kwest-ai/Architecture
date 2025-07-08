import { test, expect } from '@playwright/test';
test('GitHub Homepage', async ({ page }) => {
  await page.goto('https://github.com');
  await expect(page.locator('h1')).toContainText('Let’s build from here');
});