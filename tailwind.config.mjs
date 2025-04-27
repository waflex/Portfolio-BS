export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  safelist: [
    'bg-base-200/30',
    'bg-base-200/50'
  ],
  theme: {
    extend: {
      colors: {
        'neon-pink': '#ff2d55',
        'neon-blue': '#0ff',
        'neon-purple': '#b026ff',
        'cyber-black': '#0a0a0f',
        'cyber-dark': '#1a1a2e'
      },
      boxShadow: {
        'neon-glow': '0 0 5px rgb(0 255 255), 0 0 20px rgb(0 255 255)',
        'neon-pink-glow': '0 0 5px rgb(255 45 85), 0 0 20px rgb(255 45 85)',
        'neon-purple-glow': '0 0 5px rgb(176 38 255), 0 0 20px rgb(176 38 255)'
      },
      keyframes: {
        typing: {
          "0%": {
            width: "0%",
            visibility: "hidden"
          },
          "100%": {
            width: "100%"
          }  
        },
        blink: {
          "50%": {
            borderColor: "transparent"
          },
          "100%": {
            borderColor: "white"
          }  
        }
      },
      animation: {
        typing: "typing 2s steps(20) infinite alternate, blink 1s infinite"
      }
    },
  },
  plugins: [require("@tailwindcss/typography"), require("daisyui")],
  daisyui: {
    themes: [
      {
        cyberpunk: {
          "primary": "#ff2d55",
          "secondary": "#0ff",
          "accent": "#b026ff",
          "neutral": "#1a1a2e",
          "base-100": "#0a0a0f",
          "base-200": "#1a1a2e",
          "info": "#0ff",
          "success": "#00ff9f",
          "warning": "#ffb300",
          "error": "#ff2d55",
        },
      },
      "dark"
    ],
  }
}