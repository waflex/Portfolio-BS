export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  safelist: [
    'bg-base-200/30',
    'bg-base-200/50'
  ],
  theme: {
    extend: {
      colors: {
        'accent': '#00e5a0',
        'accent-hover': '#00c988',
        'border-subtle': 'rgba(255, 255, 255, 0.08)',
        'border-icon': 'rgba(255, 255, 255, 0.15)',
        'blob': 'rgba(0, 229, 160, 0.20)'
      },
      fontFamily: {
        'display': ['Bebas Neue', 'sans-serif'],
        'body': ['Poppins', 'sans-serif']
      },
      boxShadow: {
        'glow': '0 0 20px rgba(0, 229, 160, 0.4)',
        'card': '0 8px 32px rgba(0, 0, 0, 0.4)'
      }
    },
  },
  plugins: [require("@tailwindcss/typography"), require("daisyui")],
  daisyui: {
    themes: [
      {
        'dark-portfolio': {
          "primary": "#00e5a0",
          "secondary": "#00c988",
          "accent": "#00e5a0",
          "neutral": "#111111",
          "base-100": "#0a0a0a",
          "base-200": "#1a1a1a",
          "base-content": "#ffffff",
          "info": "#00e5a0",
          "success": "#00e5a0",
          "warning": "#ffb300",
          "error": "#ff2d55",
        },
      },
      "dark"
    ],
  }
}