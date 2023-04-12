from playwright.sync_api import playwright, Page, sync_playwright, expect
import pytest

def test_if_new_look_price_is_discounted(page):
    page.goto("https://www.sewessential.co.uk/sewing-patterns/shop-sewing-patterns-by-brand/new-look-sewing-patterns/new-look-womens-sewing-patterns/new-look-dresses-sewing-patterns")
    page.get_by_role("listitem").filter(has_text="Quickview Misses Two-Piece Dresses New Look Sewing Pattern 6741. Size 6-18. Rati").get_by_role("link").first.click()
    #expect(page.getByText("Availability: In stock")).toBeVisible()
    
    price_locator = page.locator("div.product-info-price span.price")
    price = float(price_locator.inner_text().strip().replace('£', ''))
    assert price > 7.0
    

