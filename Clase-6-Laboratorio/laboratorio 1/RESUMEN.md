# 📋 Resumen Ejecutivo - Clase 6

## Para el Profesor
| Archivo | Uso |
|---------|-----|
| `NOTAS_PROFESOR.md` | Guía completa con cronograma, puntos clave y extensiones |
| `INSTRUCCIONES.md` | Dar a los alumnos paso a paso |
| `PROMPTS.md` | Prompts listos para que los alumnos copien y usen |
| `GUIA_RAPIDA.md` | Referencia de comandos y conceptos |
| `EVALUACION.md` | Plantilla de autoevaluación |

---

## Para el Alumno
| Archivo | Cuándo usarlo |
|---------|---------------|
| `INSTRUCCIONES.md` | Seguir paso a paso durante el laboratorio |
| `PROMPTS.md` | Copiar y pegar en la IA cuando necesites ayuda |
| `GUIA_RAPIDA.md` | Consultar si olvidas un comando o concepto |
| `EVALUACION.md` | Al finalizar para autoevaluarte |

---

## 🐛 El Error Clave de la Clase

**Archivo:** `deepseek_chatbot.py`  
**Línea:** 23  
**Error:** `os.getenv("GEMINI_API_KEY")`  
**Corrección:** `os.getenv("DEEPSEEK_API_KEY")`

**Explicación para alumnos:**  
Es como usar la llave de tu casa para intentar entrar a la casa de tu amigo. Cada servicio (Gemini, DeepSeek) tiene su propia llave (API key).

---

## ⏱️ Tiempo Total: 80 minutos

| Fase | Tiempo | Actividad |
|------|--------|-----------|
| 1 | 5 min | Preparación |
| 2 | 5 min | Clonar repositorio |
| 3 | 15 min | Reconocer archivos |
| 4 | 15 min | Analizar con IA |
| 5 | 15 min | Encontrar error |
| 6 | 10 min | Corregir error |
| 7 | 10 min | Reflexión |

---

## ✅ Checklist del Profesor

Antes de la clase:
- [ ] Verificar que Git funciona
- [ ] Verificar que Python funciona
- [ ] Tener una IA abierta para demostrar
- [ ] Probar el laboratorio completo

Durante la clase:
- [ ] Dar tiempo suficiente para cada fase
- [ ] Rotar entre alumnos ofreciendo ayuda
- [ ] Hacer preguntas de verificación
- [ ] Guiar sin dar respuestas directas

Después de la clase:
- [ ] Recoger evaluaciones
- [ ] Identificar alumnos que necesitan refuerzo
- [ ] Preparar material para la siguiente clase
