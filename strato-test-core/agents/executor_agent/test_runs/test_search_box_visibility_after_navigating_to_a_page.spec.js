import { test, expect } from '@playwright/test';

import fs from 'fs';
import path from 'path';
test.afterEach(async ({ page }, testInfo) => {
  const html = await page.content();
  fs.writeFileSync(path.resolve('/Users/krkaushikkumar/Desktop/kwest-ai/strato-test-core/agents/executor_agent/test_runs/test_search_box_visibility_after_navigating_to_a_page.spec.html'), html);
});

test('Search box visibility after navigating to a page', async ({ page }) => {
  await page.goto('https://en.wikipedia.org/wiki/Main_Page');
  const searchBox = await page.locator('input[name="search"]');
  expect(searchBox).toBeVisible();
});