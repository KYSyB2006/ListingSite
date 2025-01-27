/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
   './templates/**/*.html',         // Templates HTML globaux
    './authentication/templates/**/*.html', // App authentication
    './listing/templates/**/*.html', // App listing
    './static/**/*.js',
    './node_modules/flyonui/dist/js/*.js',
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('flyonui'),
    require('flyonui/plugin'),
  ],
}

