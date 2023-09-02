import { resolve } from 'path'
import { defineConfig } from 'vite'

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        add: resolve(__dirname, ".pages/add/add.html")
      },
    },
  },
})