| **\*ODOO 18 COMMUNITY EDITION** **\*Documento de Requisitos de Desarrollo** **\*FDD / TDD — Odoo** **\*Employee Performance** |
| ----------------------------------------------------------------------------------------------------------------------------- |

| **\*Modulo / Proyecto**       | **\*Employee Performance**        |
| ----------------------------- | --------------------------------- |
| **\*Cliente / Departamento**  | **\*Binhex Cloud Solutions S.L.** |
| **\*Autor**                   | **\*Nelson Vera Cabrera**         |
| **\*Fecha de Creación**       | **\*24/04/2026**                  |
| **\*Versión de Odoo Destino** | **\*Odoo 18 CE**                  |

**_Binhex Systems Solutions S.L. · Consultor y Desarrollador: \[Nombre\]_**

**\*Confidencial — Uso Interno**

# **\*Control de Versiones**

| **\*Versión** | **\*Fecha**      | **\*Autor**               | **\*Cambios Realizados**             |
| ------------- | ---------------- | ------------------------- | ------------------------------------ |
| **\*1.0**     | **\*28/04/2026** | **\*Nelson Vera Cabrera** | **\*Creación del documento inicial** |
|               |                  |                           |                                      |

# **\*1. Información General**

| **\*Modulo / Proyecto**       | **\*employee_performance**        |
| ----------------------------- | --------------------------------- |
| **\*Cliente / Departamento**  | **\*Binhex Cloud Solutions S.L.** |
| **\*Autor**                   | **\*Nelson Vera Cabrera**         |
| **\*Fecha de Creación**       | **\*28/04/2026**                  |
| **\*Versión de Odoo Destino** | **\*Odoo 18 CE**                  |

# **\*2. Objetivo y Contexto**

## **\*2.1. Propósito**

**\*La funcionalidad de este módulo es introducir un nuevo menú en Tablero para mostrar
gráficas de ventas, CRM, Gastos, etc... por empleado, con el fin de tener un análisis
más centralizado y de manera más accesible.**

## **\*2.2. Proceso Actual (As-Is)**

| Actualmente no se cuenta con gráficas de datos por empleado, además para ver las actuales gráficas tenemos que dirigirnos al respectivo módulo e ir a Informes. |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## **\*2.3. Proceso Propuesto (To-Be)**

| **\*Tendremos un acceso rápido a distintas estadísticas de empleados desde el módulo Tablero, donde se podrán contrastar datos de distintos meses.** |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- |

# **\*3. Alcance**

## **\*3.1. Incluido en el desarrollo**

| **\*✓** | **\*Acceso desde la barra superior de menú en el módulo Tablero** |
| ------- | ----------------------------------------------------------------- |
| **\*✓** | **\*Gráficas de ventas asignadas por empleado**                   |
| **\*✓** | **\*Gráficas de oportunidades asignados por empleado**            |
| **\*✓** | **\*Gráficas de gastos por empleado**                             |

## **\*3.2. Excluido del desarrollo (Fuera de alcance)**

| **\*✗** | **\*\[Funcionalidad excluida 1\]** |
| ------- | ---------------------------------- |
| **\*✗** | **\*\[Funcionalidad excluida 2\]** |

# **\*4. Requisitos Funcionales (Perspectiva del Usuario)**

## **\*4.1. Casos de Uso**

| **\*\#**    | **\*Caso de Uso**                | **\*Descripción**                                                     |
| ----------- | -------------------------------- | --------------------------------------------------------------------- |
| **\*CU-01** | **\*\[Nombre del caso de uso\]** | **\*\[Descripción detallada del caso de uso y su flujo principal.\]** |
| **\*CU-02** | **\*\[Nombre del caso de uso\]** | **\*\[Descripción detallada del caso de uso y su flujo principal.\]** |
| **\*CU-03** | **\*\[Nombre del caso de uso\]** | **\*\[Descripción detallada del caso de uso y su flujo principal.\]** |

## **\*4.2. Reglas de Negocio**

| **\*\[Regla de negocio n. 1: Describir la restricción o regla que debe aplicarse.\]** |
| ------------------------------------------------------------------------------------- |

# **\*5. Diseño de Interfaz y Mockups (UI/UX)**

## **\*Pantalla 1 — \[Nombre de la pantalla\]**

**_\[Descripción de la pantalla: donde se ubica el nuevo campo o elemento, condiciones
de visibilidad, comportamiento esperado al interactuar.\]_**

| **_\[ Figura 1: Captura o mockup de la Pantalla 1 \]_** **_Insertar imagen o captura de pantalla aqui_** |
| -------------------------------------------------------------------------------------------------------- |

## **\*Pantalla 2 — \[Nombre de la pantalla\]**

**_\[Descripción de la pantalla: como se visualiza el resultado en esta vista, que
cambia respecto al comportamiento actual.\]_**

| **_\[ Figura 2: Captura o mockup de la Pantalla 2 \]_** **_Insertar imagen o captura de pantalla aqui_** |
| -------------------------------------------------------------------------------------------------------- |

# **\*6. Requisitos Técnicos (Perspectiva Odoo)**

## **\*6.1. Modelos de Datos (Models & Fields)**

**_\[Indicar el modelo Odoo al que pertenece el campo o modelo nuevo. Ej: account.tax,
sale.order, etc.\]_**

| **\*Nombre Técnico** | **\*\[nombre_tecnico_campo\]**                      |
| -------------------- | --------------------------------------------------- |
| **\*Tipo**           | **\*\[Many2one / Char / Boolean / Selection ...\]** |
| **\*Etiqueta**       | **\*\[Etiqueta visible para el usuario\]**          |
| **\*required**       | **\*False / True**                                  |
| **\*readonly**       | **\*False / True**                                  |
| **\*store**          | **\*True**                                          |
| **\*copy**           | **\*True / False**                                  |
| **\*domain**         | **\*\[('campo', '=', valor)\]**                     |

## **\*6.2. Vistas e Interfaz de Usuario (Views)**

| **\*Vista a modificar**  | **\*\[Herencia / Nueva vista\]**                        |
| ------------------------ | ------------------------------------------------------- |
| **\*ID Externo**         | **\*\[modulo.id_externo_vista\]**                       |
| **\*Posición del campo** | **\*\[Después de / Antes de / Dentro de ...\]**         |
| **\*Comportamiento**     | **\*\[Desplegable / Campo de texto / Checkbox / ...\]** |

## **\*6.3. Lógica de Negocio (Python Methods)**

### **\*Campos Calculados (@api.depends)**

| **\*\[No aplica / Descripción del campo compute y sus dependencias.\]** |
| ----------------------------------------------------------------------- |

### **\*Eventos Onchange (@api.onchange)**

| **\*\[No aplica / Descripción del evento onchange y su comportamiento dinámico.\]** |
| ----------------------------------------------------------------------------------- |

### **\*Sobreescritura / Herencia de Métodos (super())**

| **\*Modelo**         | **\*Método**              | **\*Descripción del cambio**                                                    |
| -------------------- | ------------------------- | ------------------------------------------------------------------------------- |
| **\*\[model.name\]** | **\*\[nombre_metodo()\]** | **\*\[Descripción de que hace actualmente y que lógica se añade o modifica.\]** |

## **\*6.4. Seguridad y Permisos (Access Rights & Record Rules)**

| **\*Elemento**            | **\*Acción requerida**                  | **\*Justificación**     |
| ------------------------- | --------------------------------------- | ----------------------- |
| **\*ir.model.access.csv** | **\*\[Sin cambios / Añadir entrada\]**  | **\*\[Justificación\]** |
| **\*Record Rules**        | **\*\[Sin cambios / Modificar regla\]** | **\*\[Justificación\]** |

# **\*7. Dependencias y Datos**

| **\*Tipo**                   | **\*Detalle**                                    |
| ---------------------------- | ------------------------------------------------ |
| **\*Módulos Dependientes**   | **\*\[account, l10n_es, sale, purchase ...\]**   |
| **\*Datos de Demostración**  | **\*\[Si / No necesario\]**                      |
| **\*Datos de Configuracion** | **\*\[Si / No necesario — detallar si aplica\]** |

# **\*8. Criterios de Aceptación (Testing)**

| **\*\[Indicar si se definen criterios de aceptación o justificar por que no aplican.\]** |
| ---------------------------------------------------------------------------------------- |

| **\*✓** | **\*\[Criterio de aceptación 1: descripción del comportamiento esperado.\]** |
| ------- | ---------------------------------------------------------------------------- |
| **\*✓** | **\*\[Criterio de aceptación 2: descripción del comportamiento esperado.\]** |
| **\*✓** | **\*\[Criterio de aceptación 3: descripción del comportamiento esperado.\]** |

# **\*9. Estimación de Tiempos y Presupuesto**

**\*Desglose del esfuerzo estimado en horas para la ejecución de este desarrollo.**

| **\*\#** | **\*Fase / Componente**  | **\*Descripción de la Tarea**                                            | **\*Horas Est.** | **\*Notas** |
| -------- | ------------------------ | ------------------------------------------------------------------------ | ---------------- | ----------- |
| **\*1**  | **\*Análisis y Diseño**  | **\*Toma de requerimientos, mockups y redacción de este documento.**     | **\*\[Xh\]**     |             |
| **\*2**  | **\*Modelos de Datos**   | **\*Creación de nuevos modelos, campos, herencias y relaciones (.py).**  | **\*\[Xh\]**     |             |
| **\*3**  | **\*Vistas e Interfaz**  | **\*Creación/modificación de archivos XML (Form, Tree, Kanban, Menus).** | **\*\[Xh\]**     |             |
| **\*4**  | **\*Lógica de Negocio**  | **\*Programación de métodos Python (computes, onchanges, overrides).**   | **\*\[Xh\]**     |             |
| **\*5**  | **\*Seguridad y Datos**  | **\*Archivos CSV de acceso, Record Rules y datos de configuracion.**     | **\*\[Xh\]**     |             |
| **\*6**  | **\*Pruebas y QA**       | **\*Pruebas funcionales, depuración y corrección de errores.**           | **\*\[Xh\]**     |             |
| **\*7**  | **\*Despliegue e Impl.** | **\*Subida a producción, configuración inicial y/o breve capacitación.** | **\*\[Xh\]**     |             |
|          | **\*TOTAL ESTIMADO**     |                                                                          | **\*\[XXh\]**    |             |
