# Guia de Licencias de Software para Ingenieros de IA

## Para que sirve esta carpeta?

Esta carpeta contiene **ejemplos reales** de los archivos de licencia mas comunes en el mundo del software y la IA. Puedes usarlos como referencia para:

1. **Reconocer** que tipo de licencia tiene un proyecto que vas a usar
2. **Copiar y adaptar** la licencia para tu propio proyecto
3. **Entender** que puedes y que no puedes hacer con cada una

## Archivos incluidos

### Licencias de Software (para codigo)

| Archivo | Tipo | Nivel de Permisividad | Ejemplo de uso |
|---------|------|----------------------|----------------|
| `LICENSE_MIT.txt` | MIT | 🟢 Muy permisiva | React, TensorFlow, Python |
| `LICENSE_APACHE.txt` | Apache 2.0 | 🟢 Permisiva + Patentes | Android, TensorFlow |
| `LICENSE_BSD_2CLAUSE.txt` | BSD 2-Clause | 🟢 Permisiva simple | Proyectos academicos |
| `LICENSE_BSD_3CLAUSE.txt` | BSD 3-Clause | 🟢 Permisiva + Sin endoso | Proyectos academicos |
| `LICENSE_GPL_v3.txt` | GPL v3 | 🟡 Copyleft (viral) | Linux, WordPress |
| `LICENSE_LGPL_v3.txt` | LGPL v3 | 🟡 Copyleft suave | Librerias compartidas |
| `LICENSE_MPL_2.txt` | MPL 2.0 | 🟡 Copyleft por archivo | Firefox |
| `LICENSE_PROPETARIA_EJEMPLO.txt` | Propietaria | 🔒 Control total | Software comercial |

### Licencias de Contenido (para fotos, textos, datos)

| Archivo | Tipo | Nivel de Permisividad | Ejemplo de uso |
|---------|------|----------------------|----------------|
| `LICENSE_CREATIVE_COMMONS_BY.txt` | CC BY 4.0 | 🟢 Muy permisiva | Fotos, blog posts |
| `LICENSE_CREATIVE_COMMONS_NC.txt` | CC BY-NC 4.0 | 🟡 No comercial | Investigacion |
| `LICENSE_CREATIVE_COMMONS_DOMINIO_PUBLICO.txt` | CC0 | 🟢 Dominio publico | Datos abiertos |

## Como usar estos archivos

### Para tu proyecto

1. Copia el archivo de licencia que necesites
2. Renombralo a `LICENSE` (sin extension) o `LICENSE.txt`
3. Pega el contenido completo en el archivo
4. Cambia "[Tu Nombre o Empresa]" por tu nombre real
5. Cambia el ano por el ano actual
6. Guarda el archivo en la **raiz** de tu proyecto

### Para reconocer la licencia de un proyecto ajeno

1. Busca el archivo `LICENSE`, `LICENSE.txt` o `COPYING` en la carpeta raiz
2. Abre el archivo y lee las primeras 3 lineas
3. Busca las palabras clave:
   - "MIT License" → MIT
   - "Apache License" → Apache
   - "GNU GENERAL PUBLIC" → GPL
   - "BSD" → BSD
   - "Mozilla Public" → MPL
   - "Creative Commons" → CC
   - "PROPRIETARY" o "CONFIDENTIAL" → Propietaria

## Regla de Oro

> **Si no sabes que licencia tiene un proyecto, NO lo uses hasta averiguarlo.**
> Un ingeniero de IA siempre verifica las licencias antes de usar codigo o datos de terceros.
