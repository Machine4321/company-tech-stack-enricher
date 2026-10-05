# 🏢 B2B Company & Tech Stack Enricher (AI & MCP Ready)

Turn any domain or company website into structured B2B intelligence in seconds. Detect website tech stacks (CMS, eCommerce, frontend frameworks, analytics, CRM, payments, hosting), public contact emails, phone numbers, and official social media profiles.

Designed specifically for **AI Agents**, **Model Context Protocol (MCP)** workflows, **n8n / Make.com** automations, and **sales prospecting teams**.

---

## ⚡ Why Use B2B Company & Tech Stack Enricher?

- **Blazing Fast**: Lightweight HTTP-level analysis runs in **1 to 2 seconds** per domain—no heavy browser bloat.
- **50+ Tech Signatures**: Accurately recognizes Shopify, WordPress, Next.js, React, Vue, Stripe, HubSpot, Google Analytics 4, Intercom, Cloudflare, AWS, and more.
- **Lead Contact Discovery**: Automatically extracts public business emails, `tel:` phone numbers, and company metadata.
- **Social Media Presence**: Discovers official LinkedIn company pages, Twitter/X, GitHub, Facebook, Instagram, and YouTube channels.
- **AI & MCP Compatible**: Works seamlessly with Apify's MCP server (`mcp.apify.com`), Claude Desktop, Cursor, ChatGPT, and LangChain.

---

## 🔍 What Data Is Extracted?

For each website domain, the Actor extracts:

| Field | Description | Example |
| :--- | :--- | :--- |
| `domain` | Normalized website domain | `apify.com` |
| `companyName` | Clean company / site title | `Apify` |
| `description` | Meta or OpenGraph description | `Apify is the cloud platform for web scraping...` |
| `techStack` | List of detected technologies with category | `[{"name": "Next.js", "category": "Frontend Framework"}, ...]` |
| `techCount` | Total technologies discovered | `8` |
| `contacts.emails` | Validated public email addresses | `["support@apify.com", "sales@apify.com"]` |
| `contacts.phones` | Formatted contact phone numbers | `["+1 (888) 555-0199"]` |
| `socialProfiles` | Direct links to social pages | `{"linkedin": "https://linkedin.com/company/apify", ...}` |
| `meta` | Title, language, favicon, OG image | `{"title": "...", "language": "en"}` |

---

## 🤖 MCP (Model Context Protocol) Integration

You can call this Actor directly as an AI tool inside **Claude Desktop**, **Cursor**, or custom LLM agents using Apify MCP:

### Claude Desktop Configuration (`claude_desktop_config.json`)
```json
{
  "mcpServers": {
    "apify": {
      "command": "npx",
      "args": [
        "-y",
        "@apify/mcp-server",
        "--actors",
        "knobby_wallpaper/company-tech-stack-enricher"
      ],
      "env": {
        "APIFY_TOKEN": "YOUR_APIFY_API_TOKEN"
      }
    }
  }
}
```

Now Claude can naturally enrich leads:  
> *"Enrich stripe.com and tell me what analytics and CRM tools they use."*

---

## 📥 Input Parameters

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `startUrls` | Array | Yes | `[{"url": "https://apify.com"}]` | List of website URLs or domains to analyze. |
| `extractTechStack` | Boolean | No | `true` | Detect CMS, frameworks, tracking, and payments. |
| `extractContacts` | Boolean | No | `true` | Extract public contact emails and phone numbers. |
| `extractSocials` | Boolean | No | `true` | Extract LinkedIn, Twitter/X, GitHub, and social links. |
| `maxRequestsPerCrawl` | Integer | No | `10` | Maximum number of domains to process. |
| `proxyConfiguration` | Object | No | `{ "useApifyProxy": true }` | Apify Proxy settings for reliable global requests. |

### Example Input
```json
{
  "startUrls": [
    { "url": "https://apify.com" },
    { "url": "https://stripe.com" }
  ],
  "extractTechStack": true,
  "extractContacts": true,
  "extractSocials": true,
  "maxRequestsPerCrawl": 10
}
```

---

## 📤 Example Output

```json
{
  "url": "https://apify.com",
  "domain": "apify.com",
  "companyName": "Apify",
  "description": "Apify is the cloud platform for web scraping, data extraction, and web automation.",
  "techCount": 6,
  "techStack": [
    { "name": "Next.js", "category": "Frontend Framework" },
    { "name": "React", "category": "JavaScript Library" },
    { "name": "Google Analytics 4 (GA4)", "category": "Analytics" },
    { "name": "Google Tag Manager", "category": "Tag Management" },
    { "name": "Stripe", "category": "Payment Gateway" },
    { "name": "Cloudflare", "category": "CDN & Security" }
  ],
  "contacts": {
    "emails": ["support@apify.com", "press@apify.com"],
    "phones": []
  },
  "socialProfiles": {
    "linkedin": "https://www.linkedin.com/company/apifytech",
    "twitter": "https://twitter.com/apify",
    "github": "https://github.com/apify"
  },
  "meta": {
    "title": "Apify: Full-stack web scraping and data extraction platform",
    "language": "en",
    "favicon": "https://apify.com/favicon.ico",
    "ogImage": "https://apify.com/og-image.png"
  },
  "scrapedAt": "2026-10-05T07:25:00.000Z"
}
```

---

## 💡 Top Use Cases

1. **AI Sales Agents & Cold Outreach**: Automatically qualify prospects before reaching out. If they use Shopify, pitch your Shopify app; if they use WordPress, offer migration services.
2. **Lead Enrichment in n8n / Make**: Pipe incoming webhook leads from Google Sheets, HubSpot, or Airtable and enrich them in real-time.
3. **Market & Competitor Intelligence**: Monitor what technologies your competitors are adopting over time.
4. **Recruitment Intelligence**: Discover companies building with modern stacks like React, Next.js, or AWS to target top candidates.

---

## 💬 Support & Customization

Developed and maintained by **Apex Data Solutions**. For feedback, custom integrations, or additional technology signatures, reach out via the Apify Console or open an issue on GitHub.
