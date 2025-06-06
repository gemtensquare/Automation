import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'


// https://vite.dev/config/
export default defineConfig({
  plugins: [
    react(),
    tailwindcss(),
  ],
  server: {
    host: '0.0.0.0',
    watch: {
      usePolling: true,
    },
    port: 5173,
    allowedHosts: ['a155-103-131-145-159.ngrok-free.app'],
    strictPort: true,
  }
})