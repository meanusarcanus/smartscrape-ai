# 🐝 SmartScrape AI Web Data Extractor Actor

Extract structured JSON (title, price, specs, stock) from any web page URL using AI—no complex CSS selectors or BeautifulSoup code required!

## 🚀 Usage & Input Parameters

| Field | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `url` | string | Target web page URL | `https://example.com/product/123` |
| `extraction_targets` | array | JSON fields to extract | `["product_name", "price", "stock_status"]` |

## 📤 Output Format

```json
{
  "status": "success",
  "url": "https://example.com/product/123",
  "extracted_data": {
    "product_name": "UltraComfort Headphones",
    "price": "$49.99",
    "stock_status": "In Stock"
  }
}
```
