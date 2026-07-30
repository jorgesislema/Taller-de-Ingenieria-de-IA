# Notas de Seguridad — Llaves API

## Que es una API Key?

**Analogia:** Una API key es como una llave de tu casa. Si alguien la tiene, puede entrar. Tu llave abre TU puerta, no la de tu vecino.

**En palabras simples:** Es una cadena de texto larga (como `sk-abc123xyz456...`) que le dice al servicio de IA: "Soy fulano, y tengo permiso para usar este servicio". Sin ella, el servicio no te deja pasar.

## Reglas de Seguridad (NO NEGOCIABLES)

### 1. NUNCA subas tu `.env` a GitHub

Si subes tu `.env` a GitHub, **cualquiera en el mundo** puede ver tus llaves y usarlas. Te pueden dejar sin credito en tu tarjeta en minutos.

**Como evitarlo:**
- Siempre ten un `.gitignore` que incluya `.env`
- Antes de hacer `git push`, verifica con `git status` que `.env` NO aparezca
- Si lo subiste por accidente, cambia la llave inmediatamente

### 2. NUNCA compartas tus llaves por chat o correo

No las envies por WhatsApp, correo electronico, ni las pegues en un documento compartido.

### 3. NUNCA pongas las llaves directamente en el codigo

```python
# MAL — NUNCA hagas esto
api_key = "sk-abc123xyz456..."

# BIEN — Lee la llave desde .env
import os
api_key = os.getenv("GOOGLE_API_KEY")
```

### 4. Si una llave se filtra, ELIMINALA inmediatamente

Cada proveedor (Google, OpenAI, etc.) te permite eliminar una llave y crear una nueva. Si sospechas que alguien la vio, cambiala ya.

### 5. Usa llaves diferentes por proyecto

No uses la misma llave de Google para tu proyecto de la universidad y para tu negocio. Si una se compromete, la otra queda segura.

## Que pasa si no protejo mis llaves?

| Consecuencia | Ejemplo |
|-------------|---------|
| Te gastan tu credito | Alguien usa tu llave de OpenAI y te deja sin saldo |
| Te roban datos | Si la IA tiene acceso a tus archivos, pueden leerlos |
| Te demandan | Si tu llave genera contenido ilegal, la responsabilidad es tuya |
| Te bloquean | Los proveedores detectan uso anomalo y cancelan tu cuenta |

## Checkpoint de Seguridad

Antes de ejecutar cualquier script, verifica:

- [ ] Tengo un archivo `.env` (no `.env.example`)
- [ ] Mi `.env` NO esta en GitHub
- [ ] Mi `.gitignore` incluye `.env`
- [ ] Mis llaves estan en el `.env`, NO en el codigo
- [ ] Entiendo que cada llamada a la IA cuesta dinero (aunque sea poco)
