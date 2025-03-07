/** @type {import('tailwindcss').Config} */
export default {
    content: [
      "./templates/**/*.html",      // Main templates folder
      "./**/templates/**/*.html",   // Django apps' templates
      "./static/**/*.js",           // Any JavaScript files in static
      "./**/*.py",                  // Django views (optional for class names in strings)
    ],
}
  