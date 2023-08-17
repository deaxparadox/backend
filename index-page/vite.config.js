import { resolve } from 'path'
import { defineConfig } from 'vite'

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, './index.html'),
        linux: resolve(__dirname, './pages/linux.html'),
        python: resolve(__dirname, './pages/python.html'),
        python_introduction: resolve(__dirname, './pages/introduction.html'),
        python_numeric_types: resolve(__dirname, './pages/numeric_types.html'),
      },
    },
  },
})