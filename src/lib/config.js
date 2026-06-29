/**
 * Configuración central del portafolio
 *
 * Uso: import { API_BASE } from "../../lib/config";
 *
 * Para desarrollo local:  PUBLIC_API_BASE=http://localhost:8000
 * Para producción:        PUBLIC_API_BASE=https://internal.jrtdev.cl
 * Valor por defecto:      http://localhost:8000
 */
export const API_BASE = import.meta.env.PUBLIC_API_BASE || "";
