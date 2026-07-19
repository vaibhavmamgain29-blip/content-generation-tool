import { defineConfig } from "vite";

// In development the Vite dev server proxies /api to the FastAPI backend on
// :8000. In production the built assets are served by nginx, which also
// proxies /api/* to the backend service.
export default defineConfig({
  root: "src",
  publicDir: "../public",
  server: {
    port: 5173,
    proxy: {
      "/api": {
        target: "http://localhost:8000",
        changeOrigin: true,
      },
    },
  },
  build: {
    outDir: "../dist",
    emptyOutDir: true,
  },
});
