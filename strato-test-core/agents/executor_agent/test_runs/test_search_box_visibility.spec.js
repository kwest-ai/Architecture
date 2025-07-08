import { test, expect } from '@playwright/test';

import fs from 'fs';
import path from 'path';
test.afterEach(async ({ page }, testInfo) => {
  const html = await page.content();
  fs.writeFileSync(path.resolve('/Users/krkaushikkumar/Desktop/kwest-ai/strato-test-core/agents/executor_agent/test_runs/test_search_box_visibility.spec.html'), html);
});

test('Search box visibility', async ({ page }) => { await page.goto('https://www.wikipedia.org'); const searchBox = await page.locator('input[name="search"]'); expect(await searchBox.isVisible()).toBeTruthy(); });