import { defineConfig } from 'vite'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  root: '.',
  build: {
    outDir: 'static/dist',
    emptyOutDir: true,
    rollupOptions: {
      input: 'frontend/js/main.js',
      output: {
        entryFileNames: 'js/main.js',
        chunkFileNames: 'js/chunk.js',
        assetFileNames: ({ name }) => {
          if (name && name.endsWith('.css')) {
            return 'css/style.css';
          }
          if (name && name.endsWith('.js')) {
            return 'js/[name].js';
          }
          return 'assets/[name][extname]';
        }
      }
    }
  },
  plugins: [
    tailwindcss(),
  ],
})