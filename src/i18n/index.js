/**
 * Utilidad de internacionalización.
 *
 * Uso en componente Astro:
 *   ---
 *   import { useTranslation } from "../i18n";
 *   const { lang = "es" } = Astro.props;
 *   const t = useTranslation(lang);
 *   ---
 *   <p>{t("hero.label")}</p>
 *
 * Uso en JavaScript cliente:
 *   import { useTranslation } from "../i18n";
 *   const t = useTranslation(localStorage.getItem("lang") || "es");
 */

import es from "./es.json";
import en from "./en.json";

const messages = { es, en };

/**
 * Retorna una función `t(key)` que busca la traducción en el idioma dado.
 * Si no encuentra la clave, retorna la clave misma como fallback.
 */
export function useTranslation(lang = "es") {
  const dict = messages[lang] || messages.es;

  /**
   * @param {string} key — clave con notación de puntos, ej: "hero.title"
   * @returns {string}
   */
  return function t(key) {
    const parts = key.split(".");
    let value = dict;
    for (const part of parts) {
      if (value && typeof value === "object" && part in value) {
        value = value[part];
      } else {
        console.warn(`[i18n] Falta traducción para "${key}" en idioma "${lang}"`);
        return key;
      }
    }
    if (typeof value === "string") return value;
    console.warn(`[i18n] La clave "${key}" no es un string en "${lang}"`);
    return key;
  };
}
