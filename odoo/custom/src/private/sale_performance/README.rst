========================================
Employee Sale Performance for Board
========================================

Este módulo proporciona una herramienta de análisis visual para medir el rendimiento de
ventas de los empleados directamente desde el módulo de Tableros (Dashboards).

Funcionalidades
===============

* **Gráfica de Ventas (Sales)**: Visualiza el número de ventas realizadas por cada
  empleado en tiempo real.
* **Gráfica de Leads**: Analiza las oportunidades del CRM (``crm.lead``) asignadas a cada
  empleado.
* **Vista Pivot**: Analiza los datos en formato de tabla dinámica para comparativas
  mensuales y anuales.
* **Filtros Dinámicos**:
    * **Este Mes** (Activado por defecto).
    * **Mes Pasado** (Comparativa rápida).
    * **Últimos 90 Días** (Tendencia trimestral).
* **Integración**: Se integra como un menú dedicado dentro de la aplicación
  **Tableros**, con submenús para **Sales** y **Leads**.

¿Cómo obtiene los datos?
========================

El módulo utiliza una **Vista SQL (``_auto = False``)**. Esto optimiza el rendimiento al
no duplicar datos, consultando directamente la información de ventas confirmadas.

Lógica Técnica de Extracción
----------------------------

1. **Origen**: Tabla de pedidos de venta (``sale.order``).
2. **Estado**: Filtra únicamente pedidos en estado **"Pedido de venta"** (``sale``) o
   **"Hecho"** (``done``).
3. **Vinculación**: Cruza los datos con la tabla de empleados (``hr.employee``) a través
   del **Usuario Relacionado**.
4. **Agrupación**: Procesa los datos por empleado y fecha de pedido para su explotación
   estadística.

Configuración Requerida
=======================

Para que los datos se muestren correctamente, es necesario:

1. **Configurar el Empleado**: En la ficha de cada empleado (``hr.employee``), el campo
   **"Usuario relacionado"** debe estar relleno.
2. **Registro de Ventas**: Las ventas deben tener asignado a ese mismo usuario como
   **Comercial** en el pedido.

Estructura Técnica
==================

* **Modelo Técnico**: ``sale.performance.report``
* **Vistas Disponibles**: Graph (Gráfico), Pivot (Tabla Dinámica), List (Listado).
* **Dependencias**: ``base``, ``board``, ``hr``, ``sale``.
* **Compatibilidad**: Odoo 18.0 (Usa etiquetas ``<list>`` en lugar de ``<tree>``).
