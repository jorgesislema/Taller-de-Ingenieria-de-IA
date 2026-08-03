# Estado del Proyecto: Vibe Check IA

## Información General

| Campo | Valor |
|-------|-------|
| **Nombre** | Vibe Check IA |
| **Versión** | 1.0.0 |
| **Fecha** | 2024 |
| **Estado** | En desarrollo |
| **Última actualización** | Laboratorio 2 |

---

## Estado Actual

### ✅ Completado
- [x] Diseño de lógica del sistema
- [x] Definición de arquitectura por capas
- [x] Creación de estructura de carpetas (src/, tests/, data/)
- [x] Archivo CSV con 15 tweets de ejemplo
- [x] Documentación básica (context, arquitectura)

### 🔄 En Progreso
- [ ] Implementación de src/analizador.py
- [ ] Implementación de src/datos.py
- [ ] Implementación de src/graficos.py
- [ ] Implementación de app.py
- [ ] Configuración de tests

### ⏳ Pendiente
- [ ] Pruebas automatizadas con 90% cobertura
- [ ] Optimización de rendimiento
- [ ] Despliegue en la nube
- [ ] Documentación de usuario final

---

## Funcionalidades Implementadas

| Funcionalidad | Estado | Notas |
|---------------|--------|-------|
| Lectura de CSV | ⏳ Pendiente | Usa pandas en src/datos.py |
| Clasificación con IA | ⏳ Pendiente | Google Gemini en src/analizador.py |
| Gráfico de pastel | ⏳ Pendiente | Plotly en src/graficos.py |
| Gráfico de barras | ⏳ Pendiente | Plotly en src/graficos.py |
| Gráfico de línea | ⏳ Pendiente | Plotly en src/graficos.py |
| Filtros por sentimiento | ⏳ Pendiente | Sidebar en app.py |
| Tests automáticos | ⏳ Pendiente | Pytest + Mocks |

---

## Métricas de Calidad

| Métrica | Meta | Actual |
|---------|------|--------|
| Cobertura de código | ≥ 90% | - |
| Tests aprobados | ≥ 90% | - |
| Tiempo de respuesta | < 5s | - |
| Documentación | 100% | - |

---

## Próximos Pasos

### Corto Plazo (Laboratorio 2)
1. Implementar src/analizador.py con IA
2. Crear src/datos.py para leer CSV
3. Crear src/graficos.py con 3 gráficos
4. Crear app.py con Streamlit
5. Escribir tests automatizados
6. Verificar 90% de cobertura

### Mediano Plazo
7. Agregar filtros avanzados
8. Crear gráfico de dispersión
9. Agregar exportación de datos
10. Mejorar diseño responsive

### Largo Plazo
11. Crear versión web en la nube
12. Agregar autenticación
13. Soporte para múltiples influencers
14. Análisis de tendencias en el tiempo

---

## Dependencias

| Librería | Versión | Propósito |
|----------|---------|-----------|
| streamlit | ≥ 1.28.0 | Dashboard web |
| plotly | ≥ 5.18.0 | Gráficos interactivos |
| google-generativeai | ≥ 0.3.0 | API de IA |
| pandas | ≥ 2.1.0 | Manipulación de datos |
| python-dotenv | ≥ 1.0.0 | Variables de entorno |
| pytest | ≥ 7.4.0 | Tests automatizados |
| pytest-cov | ≥ 4.1.0 | Cobertura de código |

---

## Conocimiento Técnico

### Lo que el estudiante aprende:
- Conversar con IA de forma estructurada
- Definir lógica ANTES de programar
- Organizar proyectos de software profesionalmente
- Crear dashboards interactivos
- Generar gráficos profesionales
- Escribir tests automáticos

### Herramientas que usa:
- **VS Code**: Editor de código
- **Python**: Lenguaje de programación
- **Git**: Control de versiones
- **IA**: Compañero de diseño

---

## Limitaciones Conocidas

1. **API Key requerida**: Necesita cuenta de Google AI Studio
2. **Conexión a internet**: La IA requiere conexión
3. **Límites de API**: Google Gemini tiene límites de uso gratuito
4. **Datos ficticios**: El CSV es solo de ejemplo

---

## Contacto y Soporte

- **Instructor**: Jorge Sislema
- **Repositorio**: GitHub del curso
- **Dudas**: Preguntar en clase o usar IA como asistente
