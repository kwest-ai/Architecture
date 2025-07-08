import { test, expect } from '@playwright/test';

import fs from 'fs';
import path from 'path';
test.afterEach(async ({ page }, testInfo) => {
  const html = await page.content();
  fs.writeFileSync(path.resolve('/Users/krkaushikkumar/Desktop/kwest-ai/strato-test-core/agents/executor_agent/test_runs/test_broken_selector.spec.html'), html);
});

test.use({ video: 'on' });
test('Broken Selector', async ({ page }) => {
  await page.goto('https://en.wikipedia.org/wiki/Playwright');
  await expect(page.locator('h1')).toHaveText('Playwright');
});