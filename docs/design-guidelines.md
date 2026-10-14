# Sygnity design guidelines

Source: [sygnity.pl](https://www.sygnity.pl/), which redirected to the English homepage at `https://www.sygnity.pl/en/sygnity-en/`. The values below were inspected in the visible Playwright browser on 2026-10-14. Values described as normalized are a practical scale derived from the observed page, not literal site variables.

## Assets

| Asset | File | Notes |
|---|---|---|
| Full homepage capture | [homepage.png](../assets/homepage.png) | Full page, captured after dismissing the cookie banner with Reject |
| Primary wordmark | [logo.svg](../assets/logo.svg) | Original SVG from the site header |
| Favicon | [favicon.png](../assets/favicon.png) | Same-origin PNG referenced by the page |
| Design tokens | [design-tokens.json](../assets/design-tokens.json) | Structured palette and component reference |
| Extraction observations | [design-observations.json](../assets/design-observations.json) | Computed styles and visible asset metadata |
| Dashicons font | [dashicons.ttf](../assets/fonts/dashicons/dashicons.ttf) | Site-provided icon font |
| Elementor icons font | [eicons.woff2](../assets/fonts/eicons/eicons.woff2) | Site-provided icon font |
| Font Awesome Brands | [fa-brands-400.woff2](../assets/fonts/font-awesome-5-brands/fa-brands-400.woff2) | Site-provided icon font |
| Font Awesome Regular | [fa-regular-400.woff2](../assets/fonts/font-awesome-5-free/fa-regular-400.woff2) | Site-provided icon font |
| Font Awesome Solid | [fa-solid-900.woff2](../assets/fonts/font-awesome-5-free/fa-solid-900.woff2) | Site-provided icon font |
| Font Awesome legacy | [fontawesome-webfont.woff2](../assets/fonts/fontawesome/fontawesome-webfont.woff2) | Site-provided icon font |
| GeneratePress icons | [generatepress.woff2](../assets/fonts/generatepress/generatepress.woff2) | Site-provided icon font |
| Glyphicons Halflings | [glyphicons-halflings-regular.woff2](../assets/fonts/glyphicons-halflings/glyphicons-halflings-regular.woff2) | Site-provided icon font |
| LightGallery icons | [lg.woff2](../assets/fonts/lg/lg.woff2) | Site-provided icon font |

## Colors

| Token | Value | Use |
|---|---|---|
| Brand primary | `#00AEEF` | Main buttons, active navigation, section accents and links |
| Logo cyan | `#009DDE` | Supplied SVG wordmark fill |
| Accent blue | `#1E73BE` | Standard text links |
| Text primary | `#3A3A3A` | Body copy and general text |
| Text secondary | `#666666` | Supporting copy and labels |
| Text muted | `#69727D` | Low emphasis metadata |
| Background default | `#FFFFFF` | Header, cards, form surfaces |
| Background light | `#F9F9F9` | Alternating section backgrounds |
| Background section | `#F1F1F1` | Light gray section panels |
| On dark | `#FFFFFF` | Text placed over dark imagery |
| Error fallback | `#D32F2F` | Conventional fallback; not observed in the captured page |
| Success fallback | `#2E7D32` | Conventional fallback; not observed in the captured page |

## Typography

- **Primary and display:** Montserrat, sans-serif. The page reports `Montserrat, sans-serif` for body and sampled headings.
- The page did not expose a self-hosted Montserrat `@font-face`; Montserrat appears to be externally served. No Montserrat files were downloaded.
- Observed heading sample: 32px, weight 500, line height 1.2. Body sample: 16px, weight 400, 24px line height. Button sample: 14px, weight 400.
- Normalized weights: 400 regular, 500 medium, 600 semibold, 700 bold. Normalized sizes: 12px, 16px, 18px, 24px and 32px.
- Site-provided icon fonts were downloaded for reference: `assets/fonts/dashicons/dashicons.ttf`, `assets/fonts/eicons/eicons.woff2`, `assets/fonts/font-awesome-5-brands/fa-brands-400.woff2`, `assets/fonts/font-awesome-5-free/fa-regular-400.woff2`, `assets/fonts/font-awesome-5-free/fa-solid-900.woff2`, `assets/fonts/fontawesome/fontawesome-webfont.woff2`, `assets/fonts/generatepress/generatepress.woff2`, `assets/fonts/glyphicons-halflings/glyphicons-halflings-regular.woff2`, and `assets/fonts/lg/lg.woff2`.
- Verify the licenses for the downloaded wordmark and icon fonts before using or redistributing them.

## Spacing

Use a normalized 4px base unit: 4, 8, 12, 16, 20, 24, 28 and 32px. The page uses generous section separation; 48px is a useful normalized section gap. These values are a practical scale, not all directly measured CSS tokens.

## Border radius

- 0px for square edges and form controls where appropriate.
- 2px for primary CTA buttons (directly observed).
- 3px for modest card rounding (observed among visible elements).
- 5px for larger image/card rounding (observed among visible elements).
- 50% for circular carousel indicators.

## Components

- **Header:** White, compact horizontal header with a cyan wordmark, small navigation links, language selector, share-price detail and social icons. Sampled text uses `#3A3A3A`; active language uses the primary cyan.
- **Navigation:** Small, regular-weight Montserrat labels; use cyan for active/selected items. Desktop labels are compact and arranged in a single row.
- **Primary button:** Cyan `#00AEEF`, white text, 14px, 6px 12px padding, 2px corner radius. Keep labels short and direct.
- **Inputs:** White surfaces with thin light-gray borders and small corner radii. Contact form fields are vertically stacked with clear labels and generous spacing.
- **Cards:** White panels with restrained shadows, small radii, and image-led content. Use cyan for small labels and calls to action.
- **Sections:** Alternate white and very light gray backgrounds. Center section titles and use a short horizontal rule beneath them.
- **Hero:** Large photographic banner with a darkened image area, left-aligned white heading and a small cyan action button.

## Logo usage

Use `assets/logo.svg` in the header on white or light backgrounds at its original wide aspect ratio. The supplied mark is cyan (`#009DDE`). No inverted logo variant was found in the captured page; do not recolor it for dark backgrounds without an approved brand asset. The logo may be licensed; verify usage rights before using or redistributing it.

## Visual style summary

Sygnity’s page presents an established enterprise technology brand with a restrained, clean layout. Cyan accents add energy to a mostly white and soft-gray interface. Montserrat typography, compact navigation and generous whitespace keep dense corporate information readable. Large technology and industry photography carries the visual weight, while cards and buttons use subtle shadows and modest corner rounding.
