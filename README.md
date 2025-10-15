# Earlybird Strategies™ Website

A professional, single-page website for Earlybird Strategies™ - Advanced IT Infrastructure & Cybersecurity Solutions.

## Features

### Design & Layout
- **Static Header**: Fixed navigation bar with smooth scrolling to sections
- **Responsive Design**: Fully responsive layout that works on all devices
- **Professional Styling**: Modern, clean design with professional color scheme
- **Single Page Layout**: All content organized in logical sections on one page

### Sections Included
1. **Hero Section** - Company introduction with key statistics
2. **Services Overview** - Grid layout of main services
3. **Detailed Services** - In-depth service descriptions with process steps
4. **Certifications** - Licensed, Insured, Background-Checked credentials
5. **About Us** - Company story and values
6. **Why Choose Us** - Statistics and testimonials
7. **Contact Information** - Phone, service area, and business hours
8. **Quote Request Form** - Professional contact form with validation

### Interactive Features
- **Mobile Navigation** - Responsive hamburger menu for mobile devices
- **Smooth Scrolling** - Navigation links smoothly scroll to sections
- **Form Validation** - Client-side validation for quote requests
- **Notification System** - User feedback for form submissions
- **Scroll Progress** - Visual progress bar showing scroll position
- **Fade-in Animations** - Elements animate into view as user scrolls

### Technical Features
- **Accessibility** - WCAG compliant with proper ARIA labels and focus states
- **Performance** - Optimized CSS with minimal external dependencies
- **SEO Ready** - Proper meta tags and semantic HTML structure
- **Cross-browser** - Compatible with modern browsers

## File Structure

```
earlybird-strategies/
├── index.html          # Main HTML file
├── css/
│   └── style.css       # Main stylesheet
├── js/
│   └── script.js       # Interactive functionality
├── images/             # Image assets (placeholder folder)
└── README.md           # This file
```

## Getting Started

### Option 1: Simple File Opening
Open `index.html` directly in any modern web browser.

### Option 2: Local Server (Recommended)
For full functionality, serve the files through a local web server:

```bash
# Using Python 3
cd earlybird-strategies
python3 -m http.server 8080

# Using Node.js (if you have it installed)
npx serve .

# Using PHP (if you have it installed)
php -S localhost:8080
```

Then visit `http://localhost:8080` in your browser.

## Customization

### Colors
The website uses CSS custom properties (variables) for easy color customization. Edit the `:root` section in `css/style.css`:

```css
:root {
    --primary-color: #1a365d;      /* Main brand color */
    --secondary-color: #2b77a3;    /* Secondary brand color */
    --accent-color: #3182ce;       /* Accent/link color */
    /* ... other colors */
}
```

### Content
All content can be edited directly in `index.html`. The structure is semantic and well-commented.

### Images
Add your company images to the `images/` folder and update the `src` attributes in the HTML.

## Form Handling

The quote request form currently shows a success message and logs data to the browser console. To connect it to a real backend:

1. Update the form submission handler in `js/script.js`
2. Replace the `setTimeout` simulation with an actual API call
3. Configure your server endpoint to handle form submissions

## Browser Support

- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

## Performance Notes

- Uses system fonts with web font fallbacks
- Minimal external dependencies (only Font Awesome for icons)
- Optimized CSS with efficient selectors
- Lazy loading support for images
- Smooth scrolling with reduced motion support

## Accessibility Features

- Semantic HTML structure
- Proper heading hierarchy
- ARIA labels for interactive elements
- High contrast color ratios
- Focus indicators for keyboard navigation
- Screen reader friendly

## Contact Information

**Phone**: (915) 221-8820  
**Service Area**: Dallas-Based with National Reach  
**Business Hours**: Monday - Friday, 8:00 AM - 6:00 PM

---

*Built with modern web standards for optimal performance and user experience.*