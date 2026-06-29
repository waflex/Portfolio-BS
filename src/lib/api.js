/**
 * Utilidad para cargar datos desde la API con fallback a datos estáticos.
 * Se usa en el frontmatter de componentes Astro (build-time).
 *
 * En producción (servidor), el backend corre en localhost:8000 antes del build.
 * En desarrollo, si no hay backend, se cae al fallback importado.
 */

import { SERVER_API } from "./config";

export async function fetchFromAPI(endpoint, fallback) {
  try {
    const url = SERVER_API + endpoint;
    const res = await fetch(url, { signal: AbortSignal.timeout(3000) });
    if (!res.ok) throw new Error("HTTP " + res.status);
    return await res.json();
  } catch (err) {
    console.warn("[api] No se pudo conectar con " + endpoint + " — usando fallback");
    return fallback;
  }
}
