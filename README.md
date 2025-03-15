# Pure-Fabrication-e-indirection
Ejemplo: Sistema de Pedidos en un Restaurante
Queremos un sistema donde un Cliente haga un pedido y este llegue al Cocinero a través de un Mesero. Además, usaremos un Calculador de Cuenta para calcular el total del pedido.
Paso 2: Aplicamos Indirection (Capa Intermedia: Mesero)
El Mesero actúa como intermediario entre el Cliente y el Cocinero, lo que reduce el acoplamiento directo.
Paso 3: Aplicamos Pure Fabrication (Clase que no existe en la vida real)
Creamos un CalculadorDeCuenta para separar la lógica de cálculo del pedido.


¿Qué principios puede violar este diseño?

Principio de Alta Cohesión 🛑

Si agregamos demasiadas capas de indirección o clases de fabricación pura sin necesidad, podemos hacer que el sistema sea difícil de seguir.

Solución: Solo agregar clases intermedias cuando realmente se necesiten.

Principio de Encapsulación 🛑

Si CalculadorDeCuenta accediera directamente a los atributos internos de Pedido, se rompería la encapsulación.

Solución: Usar métodos públicos para acceder a los datos en lugar de acceder directamente a los atributos privados.

Principio de Diseño Basado en el Dominio (DDD) 🛑

CalculadorDeCuenta no es un objeto real en un restaurante, lo que se aleja del modelo del negocio.
Solución: Justificar su existencia asegurándonos de que realmente ayuda a la organización del código.


Conclusión

✔ Usamos Indirection con Mesero para reducir acoplamiento.
✔ Usamos Pure Fabrication con CalculadorDeCuenta para organizar la lógica.
✔ Si abusamos de estas técnicas, podemos hacer el código innecesariamente complicado.

💡 Clave: Siempre buscar un equilibrio entre separación de responsabilidades y simplicidad. 🚀
