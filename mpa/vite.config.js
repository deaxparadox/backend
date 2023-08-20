import { resolve } from 'path'
import { defineConfig } from 'vite'

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, './index.html'),
        polls: resolve(__dirname, './pages/polls/index.html'),
        linux: resolve(__dirname, './pages/linux/index.html'),
        python: resolve(__dirname, './pages/python/index.html'),
        python_introduction: resolve(__dirname, './pages/python/introduction.html'),
        python_numeric_types: resolve(__dirname, './pages/python/numeric_types.html'),
      },
    },
  },
})