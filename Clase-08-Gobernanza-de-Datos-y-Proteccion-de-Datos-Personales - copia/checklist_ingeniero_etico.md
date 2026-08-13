# Checklist del Ingeniero Ético — Protección de Datos en Proyectos de IA

Usa este checklist antes de iniciar cualquier proyecto de IA que involucre datos personales.

---

## Fase 1: Planificación (antes de escribir código)

### Identificación de datos
- [ ] He identificado **todos** los datos que necesito
- [ ] He clasificado cada dato como personal / sensible / no personal
- [ ] He eliminado los datos que **no son estrictamente necesarios**
- [ ] He verificado que los datos son **correctos y están actualizados**

### Base legal
- [ ] He identificado la **base legal** para cada tratamiento
- [ ] He obtenido **consentimiento informado** cuando es necesario
- [ ] He informado claramente la **finalidad** del tratamiento
- [ ] He verificado que el tratamiento es **proporcional** al fin

### Documentación
- [ ] He creado un **registro de tratamientos**
- [ ] He redactado una **política de privacidad**
- [ ] He documentado las **medidas de seguridad** implementadas
- [ ] He definido el **período de retención** de datos

---

## Fase 2: Diseño (antes de implementar)

### Arquitectura de seguridad
- [ ] Los datos sensibles están **cifrados** en reposo
- [ ] Los datos sensibles están **cifrados** en tránsito
- [ ] He implementado **control de acceso** basado en roles
- [ ] He configurado **logs de auditoría** para accesos a datos
- [ ] He implementado **copias de seguridad** cifradas

### Privacidad por diseño
- [ ] He implementado **anonimización** cuando sea posible
- [ ] He implementado **pseudonimización** cuando la anonimización no es viable
- [ ] He minimizado los datos que se almacenan
- [ ] He configurado la **eliminación automática** después del período de retención

### Derechos de los titulares
- [ ] He implementado mecanismos para ejercer el **derecho de acceso**
- [ ] He implementado mecanismos para ejercer el **derecho de rectificación**
- [ ] He implementado mecanismos para ejercer el **derecho de eliminación**
- [ ] He implementado mecanismos para ejercer el **derecho de oposición**

---

## Fase 3: Implementación (durante el desarrollo)

### Código seguro
- [ ] No almaceno **credenciales** en el código fuente
- [ ] No registro **datos personales** en logs de aplicación
- [ ] Implemento **validación de entrada** para evitar inyecciones
- [ ] Implemento **rate limiting** para abusos

### Modelos de IA
- [ ] Verifico que los datos de entrenamiento **no contengan datos personales innecesarios**
- [ ] Implemento **técnicas de ofuscación** en los datos de entrenamiento
- [ ] Verifico que el modelo **no memorice** datos personales específicos
- [ ] Implemento **mecanismos de explicabilidad** para decisiones automatizadas

### Pruebas
- [ ] He realizado **pruebas de penetración** del sistema
- [ ] He verificado que no hay **filtraciones de datos** en los logs
- [ ] He verificado que los **controles de acceso** funcionan correctamente
- [ ] He probado los **mecanismos de ejercicio de derechos**

---

## Fase 4: Operación (después de implementar)

### Monitoreo
- [ ] He configurado **alertas** de accesos no autorizados
- [ ] He configurado **alertas** de incidentes de seguridad
- [ ] Realizo **auditorías periódicas** de acceso a datos
- [ ] Reviso **logs de auditoría** regularmente

### Mantenimiento
- [ ] Actualizo los **datos personales** cuando me informan de cambios
- [ ] Elimino datos **después del período de retención**
- [ ] Actualizo las **medidas de seguridad** según nuevas amenazas
- [ ] Capacito al **personal** en protección de datos

### Incidentes
- [ ] Tengo un **plan de respuesta a incidentes** documentado
- [ ] Tengo **contactos de emergencia** actualizados
- [ ] Sé a quién **notificar** en caso de filtración
- [ ] Sé cómo **informar** a los titulares afectados

---

## Fase 5: Cierre (cuando el proyecto termina)

### Eliminación de datos
- [ ] He eliminado todos los **datos personales** según la política de retención
- [ ] He verificado que la eliminación es **irreversible**
- [ ] He documentado la **eliminación** en el registro de tratamientos
- [ ] He notificado a los **titulares** si es necesario

### Documentación final
- [ ] He actualizado el **registro de tratamientos** con el cierre
- [ ] He archivado la **documentación** según la política de retención
- [ ] He eliminado **accesos** de personas que ya no necesitan acceso
- [ ] He documentado **lecciones aprendidas**

---

## Preguntas de Reflexión

Antes de finalizar cada fase, preguntate:

1. **¿Lo haría con mis propios datos?** Si no querrías que hicieran contigo lo que estás haciendo con los datos de otros, no lo hagas.

2. **¿Puedo explicarlo a alguien que no sabe de tecnología?** Si no puedes explicarle a tu abuela qué haces con sus datos, es que algo no está claro.

3. **¿Qué pasa si hay un incidente?** Si no tienes un plan para cuando algo salga mal, estás construyendo sobre arena.

4. **¿Estoy respetando los derechos de las personas?** No es solo cumplir la ley; es respetar la dignidad humana.

---

## Errores Comunes a Evitar

1. **"Es solo un proyecto pequeño, no necesita protección de datos"** — Todos los proyectos con datos personales necesitan protección.

2. **"Ya tengo el consentimiento, puedo hacer lo que quiera"** — El consentimiento es para una finalidad específica, no un cheque en blanco.

3. **"Los datos están anonimizados, no hay problema"** — Verifica que realmente sea imposible reidentificar.

4. **"Si no tengo intención de hacer daño, no importa"** — La ley se basa en el tratamiento, no en la intención.

5. **"La protección de datos es cosa del área legal"** — Es responsabilidad de todo el equipo técnico.

---

## Referencias

- LOPDP del Ecuador: [https://www.finanzaspublicas.gob.ec/LOPDP.pdf](https://www.finanzaspublicas.gob.ec/LOPDP.pdf)
- Guías de la SUPERCOM: [https://www.supercom.gov.ec/](https://www.supercom.gov.ec/)
- Guías de la AEPD: [https://www.aepd.es/](https://www.aepd.es/)