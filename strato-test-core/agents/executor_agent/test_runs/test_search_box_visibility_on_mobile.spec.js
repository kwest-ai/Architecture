import { test, expect } from '@playwright/test';

import fs from 'fs';
import path from 'path';
test.afterEach(async ({ page }, testInfo) => {
  const html = await page.content();
  fs.writeFileSync(path.resolve('/Users/krkaushikkumar/Desktop/kwest-ai/strato-test-core/agents/executor_agent/test_runs/test_search_box_visibility_on_mobile.spec.html'), html);
});

test('Search box visibility on mobile', async ({ page }) => {
  await page.goto('https://en.wikipedia.org');
  await page.setViewport({ width: 375, height: 812 });
  const searchBox = await page.locator('#searchInput');
  expect(searchBox).toBeVisible();
});