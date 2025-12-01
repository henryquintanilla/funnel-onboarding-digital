# 🚀 Optimización de Onboarding Digital: Análisis de Fricción & A/B Testing

## 📌 Contexto del Negocio
El banco detectó una caída significativa en la conversión de usuarios móviles durante el flujo de alta digital. El objetivo de este proyecto fue analizar el embudo de conversión, identificar puntos de fricción técnicos y evaluar la efectividad de un nuevo flujo simplificado (Variante B) mediante experimentación rigurosa.

## 🔍 Hallazgos Clave

### 1. La Variante B es indiscutiblemente superior
El Test A/B demostró un **Lift (incremento) del 11.6%** en la tasa de conversión global respecto al grupo de control.
* **Validación Estadística:** Chi-Square Test con un *p-value* de `0.00000002`, confirmando que el resultado no es aleatorio (Significancia > 99%).

### 2. Hallazgo Crítico en Android (Fricción Técnica)
Se identificó una degradación de experiencia severa en dispositivos Android:
* **Latencia:** Los usuarios de Android tardan **17.95s** en promedio para escanear su DNI, comparado con **11.84s** en iOS (+51% más lento).
* **Impacto:** Esta fricción correlaciona con un "Drop-off rate" masivo del **~30%** en la transición hacia el escaneo del DNI.
* **Validación:** T-Test confirmado con *p-value* `0.00000000`.

## 🛠️ Stack Tecnológico
* **Python:** Generación de datos sintéticos y lógica de negocio.
* **Pandas:** Limpieza de datos, ingeniería de variables y análisis de embudo (Funnel Analysis).
* **Scipy:** Pruebas de hipótesis estadísticas (Chi-Square & T-Test).

## 📂 Estructura del Proyecto
* `src/data_gen.py`: Script de generación de datos que simula 10,000 usuarios con patrones de comportamiento y sesgos técnicos.
* `notebooks/`: Análisis exploratorio (EDA) y validación estadística detallada.

## 🚀 Recomendación Estratégica
1.  **Roll-out:** Desplegar la Variante B al 100% de la base de usuarios inmediatamente.
2.  **Ingeniería:** Abrir ticket prioritario para optimizar la librería de visión por computador en la versión Android (objetivo: reducir latencia a <12s).
3.  **Marketing:** Pausar temporalmente la inversión de pauta pagada (Ads) dirigida a dispositivos Android hasta corregir el bug para evitar desperdicio de presupuesto (CAC ineficiente).