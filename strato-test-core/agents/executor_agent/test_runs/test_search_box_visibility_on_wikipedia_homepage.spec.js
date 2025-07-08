import { test, expect } from '@playwright/test';

import fs from 'fs';
import path from 'path';
test.afterEach(async ({ page }, testInfo) => {
  const html = await page.content();
  fs.writeFileSync(path.resolve('/Users/krkaushikkumar/Desktop/kwest-ai/strato-test-core/agents/executor_agent/test_runs/test_search_box_visibility_on_wikipedia_homepage.spec.html'), html);
});

test('Search box visibility on Wikipedia homepage', async ({ page }) => {
  await page.goto('https://en.wikipedia.org');
  const searchBox = await page.locator('input[id="searchInput"]');
  expect(searchBox).toBeVisible();
});