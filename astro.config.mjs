// @ts-check
import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  outDir: './dist',
  base: '/',
  output: 'static',
  image: {
    service: { entrypoint: 'astro/assets/services/sharp' },
    domains: ['avatars.githubusercontent.com'],
  },
  vite: {
    define: {
      'import.meta.env.PUBLIC_WEB3FORMS_KEY': JSON.stringify(process.env.Web3Forms_KEY)
    },
    build: {
      assetsDir: 'assets',
    },
    server: {
      proxy: {
        '/api': { target: 'http://localhost:8000', changeOrigin: true },
      },
    },
  },
  integrations: [tailwind()],  
});
