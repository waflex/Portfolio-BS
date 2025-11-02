// @ts-check
import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  integrations: [tailwind()],
  vite: {
    define: {
      'import.meta.env.PUBLIC_WEB3FORMS_KEY': JSON.stringify(process.env.Web3Forms_KEY)
    }
  }
});
