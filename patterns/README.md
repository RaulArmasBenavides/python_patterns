# Python Design Patterns

Una colección de ejemplos prácticos de **patrones de diseño** implementados en Python. Este proyecto es ideal para aprender y comprender cómo aplicar patrones de diseño en aplicaciones reales.

## 📚 Patrones Incluidos

### Patrones Creacionales
Patrones enfocados en la creación flexible de objetos.

| Patrón | Descripción | Ubicación |
|--------|-------------|-----------|
| **Singleton** | Garantiza que una clase tenga una única instancia en toda la aplicación | `singleton/` |
| **Factory Method** | Crea objetos sin especificar sus clases concretas | `factorymethod/` |
| **Builder** | Construye objetos complejos paso a paso | `builder/` |
| **Prototype** | Crea nuevos objetos clonando un prototipo existente | `prototype/` |
| **Borg** | Comparte el estado entre múltiples instancias | `borg/` |

### Patrones Estructurales
Patrones que manejan la composición y relaciones entre clases.

| Patrón | Descripción | Ubicación |
|--------|-------------|-----------|
| **Adapter** | Convierte la interfaz de una clase en otra esperada por el cliente | `adaptador/` |
| **Facade** | Proporciona una interfaz simplificada a un subsistema complejo | `facade/` |
| **Proxy** | Controla el acceso a otro objeto mediante un sustituto | `proxy/` |
| **Bridge** | Desvincula la abstracción de su implementación | `bridge/` |

### Patrones de Comportamiento
Patrones que definen la comunicación entre objetos y la distribución de responsabilidades.

| Patrón | Descripción | Ubicación |
|--------|-------------|-----------|
| **Observer** | Notifica a múltiples observadores sobre cambios de estado | `observer/` |
| **State** | Cambia el comportamiento de un objeto según su estado interno | `state/` |
| **Iterator** | Accede secuencialmente a los elementos de una colección | `iterator/` |
| **Mediator** | Centraliza la comunicación entre objetos relacionados | `mediator/` |

## 🚀 Cómo Usar

### Ejecutar un ejemplo específico

Cada patrón tiene un archivo `main.py` que demuestra su uso:

```bash
# Ejecutar el patrón Singleton
python singleton/main.py

# Ejecutar el patrón Observer
python observer/main.py

# Ejecutar el patrón Factory Method
python factorymethod/main.py
```

### Explorar el código

Cada directorio contiene:
- **main.py**: Implementación del patrón con ejemplo práctico
- **Documentación inline**: Docstrings explicativos en las clases
- **Ejecución directa**: Ejemplos que se ejecutan al correr el script

## 📋 Requisitos

- Python 3.6 o superior
- Ninguna dependencia externa

## 🎯 Estructura del Proyecto

```
patterns/
├── adaptador/          # Adapter pattern
├── borg/               # Borg pattern
├── bridge/             # Bridge pattern
├── builder/            # Builder pattern
├── facade/             # Facade pattern
├── factorymethod/      # Factory Method pattern
├── iterator/           # Iterator pattern
├── mediator/           # Mediator pattern
├── observer/           # Observer pattern
├── prototype/          # Prototype pattern
├── proxy/              # Proxy pattern
├── singleton/          # Singleton pattern
├── state/              # State pattern
└── README.md           # Este archivo
```

## 💡 Ejemplo Rápido

### Patrón Singleton
```python
from singleton.main import Singleton

# Ambas referencias apuntan al mismo objeto
instance1 = Singleton()
instance2 = Singleton()
print(instance1 is instance2)  # True
```

### Patrón Observer
```python
from observer.main import Subject, Observer

subject = Subject()
observer = Observer()
subject.attach(observer)
subject.notify()  # El observer es notificado
```

## 🎓 Cuándo Usar Cada Patrón

| Situación | Patrón Recomendado |
|-----------|-------------------|
| Necesitas una única instancia global | Singleton |
| Tienes muchas subclases para crear objetos | Factory Method |
| Construyes objetos complejos paso a paso | Builder |
| Necesitas una interfaz simple para un subsistema complejo | Facade |
| Múltiples objetos necesitan reaccionar a cambios | Observer |
| El comportamiento cambia según el estado | State |
| Necesitas iterar sobre colecciones sin conocer su estructura | Iterator |
| Los objetos necesitan comunicarse de forma compleja | Mediator |

## 📖 Para Aprender Más

Estos ejemplos siguen los principios del libro **"Design Patterns: Elements of Reusable Object-Oriented Software"** de Gang of Four (GoF). Cada patrón está diseñado para ser educativo y fácil de entender.

## 🤝 Contribuciones

Si deseas agregar más patrones o mejorar los ejemplos existentes, ¡adelante!

---

**Última actualización:** 2026-06-11
