/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    content: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        '../templates/**/*.html',

        /*
         * Main templates directory of the project (BASE_DIR/templates).
         * Adjust the following line to match your project structure.
         */
        '../../templates/**/*.html',

        /*
         * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
         * Adjust the following line to match your project structure.
         */
        '../../**/templates/**/*.html',
        '../../**/templates/**/*.css',

        /**
         * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
         * patterns match your project structure.
         */
        /* JS 1: Ignore any JavaScript in node_modules folder. */
        // '!../../**/node_modules',
        /* JS 2: Process all JavaScript files in the project. */
        // '../../**/*.js',

        /**
         * Python: If you use Tailwind CSS classes in Python, uncomment the following line
         * and make sure the pattern below matches your project structure.
         */
        // '../../**/*.py'
    ],
    theme: {
        extend: {
            // colors: {
            //     primary: {
            //     50: '#f0f9ff',
            //     100: '#e0f2ff',
            //     200: '#cce5ff',
            //     300: '#b2d7ff',
            //     400: '#87cefa',  // Your blue - slightly adjusted for the scale
            //     500: '#38bdf8', // Your blue
            //     600: '#0ea5e9',
            //     700: '#0369a1',
            //     800: '#075985',
            //     900: '#0c4a6e',
            //     950: '#111827',
            //     },
            //     secondary: {  // Gray scale
            //     50: '#f9fafb',
            //     100: '#f3f4f6',
            //     200: '#e5e7eb',
            //     300: '#d1d5db',
            //     400: '#9ca3af',
            //     500: '#6b7280',
            //     600: '#4b5563',
            //     700: '#374151',
            //     800: '#1f2937',
            //     900: '#111827',
            //     },
            //     background: '#f0f0f0', // Light gray background
            //     whiteish: '#f8f8f8',
            //     // goofy: '#1e900f',
            // }
        },
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
        require("daisyui"),
    ],
    // daisyui: {
    //   themes: ["light", "dark", "cupcake", "aqua"],
    // },
    daisyui: {
        themes: ["light", "dark", "cupcake", "aqua",
          {
            mytheme: {
                "primary": "#6686b9",
                // "primary-content": "#000000",
                "secondary": "#2b4881",
                // "secondary-content": "#2b4881",
                "accent": "#39c1f0",
                // "accent-content": "#39c1f0",
                "neutral": "#39c1f0",
                // "neutral-content": "#39c1f0",
                "base-100": "#f1eff0",
                "base-200": "#d2d0d1",
                "base-300": "#b3b1b2",
                "base-content": "#141414",
                "info": "#7fbed9",
                // "info-content": "#7fbed9",
                "success": "#46b480",
                // "success-content": "#46b480",
                "warning": "#c4a448",
                // "warning-content": "#c4a448",
                "error": "#f44336",
                // "error-content": "#f44336",
                "unknown": "#999999",
                "unknown2": "#677AAF",
                "goofy": "#FF10F0",
              },
            },
    ],
    },
}

// To add $ npm i -D daisyui@latest