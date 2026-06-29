/**
 * Configuración central del portafolio
 *
 * API_BASE      — URL pública para peticiones desde el navegador (cliente)
 *                 Default vacío = misma origen (Nginx proxy /api → backend)
 * SERVER_API    — URL interna para fetch en build-time (Astro frontmatter)
 *                 Default http://localhost:8000 (backend en Docker)
 *
 * Uso cliente:  import { API_BASE } from "../../lib/config";
 * Uso servidor: import { SERVER_API } from "../../lib/config";
 */
export const API_BASE = import.meta.env.PUBLIC_API_BASE || "";
export const SERVER_API = "http://localhost:8000";
