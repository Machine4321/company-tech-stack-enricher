"""Technology stack detection signatures and analyzer for B2B websites."""

from typing import Dict, List, Any
import re

# Comprehensive signatures covering CMS, Frontend, Analytics, CRM, Payments, Hosting
TECH_SIGNATURES = [
    # --- CMS & E-commerce ---
    {
        "name": "Shopify",
        "category": "E-Commerce",
        "patterns": [r"cdn\.shopify\.com", r"Shopify\.theme", r"myshopify\.com", r"shopify-buy"]
    },
    {
        "name": "WooCommerce",
        "category": "E-Commerce",
        "patterns": [r"woocommerce", r"wc-ajax", r"woocommerce-layout-css"]
    },
    {
        "name": "Magento",
        "category": "E-Commerce",
        "patterns": [r"Mage\.Cookies", r"/static/frontend/", r"mage/cookies\.js"]
    },
    {
        "name": "BigCommerce",
        "category": "E-Commerce",
        "patterns": [r"cdn11\.bigcommerce\.com", r"stencil-"]
    },
    {
        "name": "PrestaShop",
        "category": "E-Commerce",
        "patterns": [r"prestashop", r"generator=[\"']PrestaShop"]
    },
    {
        "name": "WordPress",
        "category": "CMS",
        "patterns": [r"/wp-content/", r"/wp-includes/", r"generator=[\"']WordPress"]
    },
    {
        "name": "Webflow",
        "category": "CMS & Site Builder",
        "patterns": [r"assets\.website-files\.com", r"data-wf-page", r"wf-site-id", r"webflow\.js"]
    },
    {
        "name": "Wix",
        "category": "CMS & Site Builder",
        "patterns": [r"static\.wixstatic\.com", r"wix-code", r"parastorage\.com", r"_wix_"]
    },
    {
        "name": "Squarespace",
        "category": "CMS & Site Builder",
        "patterns": [r"static1\.squarespace\.com", r"squarespace\.com"]
    },
    {
        "name": "Ghost",
        "category": "CMS",
        "patterns": [r"ghost-search", r"generator=[\"']Ghost"]
    },
    {
        "name": "Drupal",
        "category": "CMS",
        "patterns": [r"drupal\.js", r"Drupal\.settings", r"sites/all/modules/"]
    },

    # --- Frontend Frameworks & Libraries ---
    {
        "name": "Next.js",
        "category": "Frontend Framework",
        "patterns": [r"/_next/static/", r"__NEXT_DATA__"]
    },
    {
        "name": "Nuxt.js",
        "category": "Frontend Framework",
        "patterns": [r"/_nuxt/", r"__NUXT__"]
    },
    {
        "name": "React",
        "category": "JavaScript Library",
        "patterns": [r"react\.production\.min\.js", r"data-reactroot", r"_reactListening"]
    },
    {
        "name": "Vue.js",
        "category": "Frontend Framework",
        "patterns": [r"vue\.runtime", r"vue\.min\.js", r"data-v-[0-9a-fA-F]+", r"__vue__"]
    },
    {
        "name": "Angular",
        "category": "Frontend Framework",
        "patterns": [r"ng-version=", r"ng-app=", r"angular\.min\.js"]
    },
    {
        "name": "Svelte",
        "category": "Frontend Framework",
        "patterns": [r"svelte-[a-zA-Z0-9]+", r"__svelte__"]
    },
    {
        "name": "Astro",
        "category": "Frontend Framework",
        "patterns": [r"astro-island", r"data-astro-"]
    },
    {
        "name": "Remix",
        "category": "Frontend Framework",
        "patterns": [r"__remixContext", r"/__remix_"]
    },
    {
        "name": "Tailwind CSS",
        "category": "CSS Framework",
        "patterns": [r"tailwind", r"data-tailwind"]
    },
    {
        "name": "Bootstrap",
        "category": "CSS Framework",
        "patterns": [r"bootstrap(?:\.bundle)?(?:\.min)?\.(?:js|css)"]
    },
    {
        "name": "jQuery",
        "category": "JavaScript Library",
        "patterns": [r"jquery(?:\.min)?\.js", r"window\.jQuery"]
    },

    # --- Analytics & Tracking ---
    {
        "name": "Google Analytics 4 (GA4)",
        "category": "Analytics",
        "patterns": [r"googletagmanager\.com/gtag/js\?id=G-", r"gtag\([\"']config[\"'],\s*[\"']G-"]
    },
    {
        "name": "Google Tag Manager",
        "category": "Tag Management",
        "patterns": [r"googletagmanager\.com/gtm\.js", r"gtm\.start"]
    },
    {
        "name": "Microsoft Clarity",
        "category": "Analytics",
        "patterns": [r"clarity\.ms/tag/", r"window\.clarity"]
    },
    {
        "name": "Hotjar",
        "category": "Analytics",
        "patterns": [r"static\.hotjar\.com", r"_hjSettings"]
    },
    {
        "name": "Mixpanel",
        "category": "Analytics",
        "patterns": [r"cdn\.mxpnl\.com", r"mixpanel\.init"]
    },
    {
        "name": "Segment",
        "category": "Customer Data Platform",
        "patterns": [r"cdn\.segment\.com/analytics\.js"]
    },
    {
        "name": "PostHog",
        "category": "Analytics",
        "patterns": [r"posthog\.com", r"posthog\.init"]
    },
    {
        "name": "Amplitude",
        "category": "Analytics",
        "patterns": [r"cdn\.amplitude\.com", r"amplitude\.getInstance"]
    },
    {
        "name": "Meta (Facebook) Pixel",
        "category": "Advertising Tracking",
        "patterns": [r"connect\.facebook\.net/[a-zA-Z_]+/fbevents\.js", r"fbq\([\"']init[\"']"]
    },
    {
        "name": "LinkedIn Insight Tag",
        "category": "Advertising Tracking",
        "patterns": [r"snap\.licdn\.com/li\.lms-analytics/insight\.min\.js"]
    },

    # --- CRM, Marketing & Chat ---
    {
        "name": "HubSpot",
        "category": "CRM & Marketing",
        "patterns": [r"js\.hs-scripts\.com", r"js\.hsforms\.net", r"hubspot\.com"]
    },
    {
        "name": "Salesforce / Pardot",
        "category": "CRM & Marketing",
        "patterns": [r"pi\.pardot\.com", r"salesforce\.com/embeddedservice"]
    },
    {
        "name": "Intercom",
        "category": "Live Chat & Support",
        "patterns": [r"widget\.intercom\.io", r"Intercom\([\"']boot[\"']"]
    },
    {
        "name": "Zendesk",
        "category": "Customer Support",
        "patterns": [r"static\.zdassets\.com", r"zE\([\"']webWidget[\"']"]
    },
    {
        "name": "Crisp Chat",
        "category": "Live Chat",
        "patterns": [r"client\.crisp\.chat"]
    },
    {
        "name": "Drift",
        "category": "Live Chat",
        "patterns": [r"js\.driftt\.com"]
    },
    {
        "name": "Klaviyo",
        "category": "Email Marketing",
        "patterns": [r"static\.klaviyo\.com", r"klaviyo\.js"]
    },
    {
        "name": "Mailchimp",
        "category": "Email Marketing",
        "patterns": [r"chimpstatic\.com", r"list-manage\.com"]
    },

    # --- Payments ---
    {
        "name": "Stripe",
        "category": "Payment Gateway",
        "patterns": [r"js\.stripe\.com/v[23]", r"checkout\.stripe\.com"]
    },
    {
        "name": "PayPal",
        "category": "Payment Gateway",
        "patterns": [r"paypal\.com/sdk/js", r"paypalobjects\.com"]
    },
    {
        "name": "Klarna",
        "category": "Payment Gateway",
        "patterns": [r"klarna\.com", r"klarna-placement"]
    },
    {
        "name": "Adyen",
        "category": "Payment Gateway",
        "patterns": [r"checkoutshopper-(?:test|live)\.adyen\.com"]
    },
    {
        "name": "Lemon Squeezy",
        "category": "Payment Gateway",
        "patterns": [r"assets\.lemonsqueezy\.com"]
    },

    # --- Cloud & Hosting ---
    {
        "name": "Cloudflare",
        "category": "CDN & Security",
        "patterns": [r"cloudflare", r"__cf_bm", r"cf-ray"]
    },
    {
        "name": "Vercel",
        "category": "Cloud Hosting",
        "patterns": [r"/_vercel/", r"x-vercel-id"]
    },
    {
        "name": "Netlify",
        "category": "Cloud Hosting",
        "patterns": [r"netlify", r"x-nf-request-id"]
    },
    {
        "name": "Amazon Web Services (AWS)",
        "category": "Cloud Hosting",
        "patterns": [r"amazonaws\.com", r"cloudfront\.net"]
    },
    {
        "name": "Fastly",
        "category": "CDN & Edge",
        "patterns": [r"fastly", r"x-fastly"]
    }
]

# Precompile regex patterns for high-speed matching
COMPILED_SIGNATURES = [
    {
        "name": sig["name"],
        "category": sig["category"],
        "regexes": [re.compile(p, re.IGNORECASE) for p in sig["patterns"]]
    }
    for sig in TECH_SIGNATURES
]


def detect_tech_stack(html_text: str, headers: Dict[str, str] = None) -> List[Dict[str, str]]:
    """Detect technologies in HTML text and optional response headers."""
    if not html_text:
        return []

    combined_text = html_text
    if headers:
        headers_str = " ".join(f"{k}: {v}" for k, v in headers.items())
        combined_text = f"{headers_str}\n{html_text}"

    detected = []
    seen_names = set()

    for item in COMPILED_SIGNATURES:
        name = item["name"]
        category = item["category"]

        for regex in item["regexes"]:
            if regex.search(combined_text):
                if name not in seen_names:
                    seen_names.add(name)
                    detected.append({
                        "name": name,
                        "category": category
                    })
                break

    return detected
