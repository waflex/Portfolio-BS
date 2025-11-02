// @ts-check
import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  outDir: './dist',
  base: '/',
  output: 'static',
  vite: {
    define: {
      'import.meta.env.PUBLIC_WEB3FORMS_KEY': JSON.stringify(process.env.Web3Forms_KEY)
    },
    build: {
      assetsDir: 'assets', // Asegura que las rutas sean coherentes
    },
  },
  integrations: [tailwind()],  
});
