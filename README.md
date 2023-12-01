# Final-Software

## Pregunta número 3

### En las clases:
Clase Cuenta:  
  - Agregaría un nuevo atributo a la clase Cuenta para rastrear el total de dinero transferido en el día actual.  
  - También modificaría el método pagar para verificar si la transferencia excede el límite diario.

### Casos de prueba
  - Una para verificar que no se puede transferir más de 200 soles en un solo día.  
  - Una para verificar que después de un día, el límite se restablece y se pueden hacer más transferencias.

### Riesgo
  - El riesgo de romper la funcionalidad existente es relativamente bajo, ya que los cambios que propuse funcionan independientemente a la funcionalidad existente y no deberían afectar a las operaciones de pago ya existentes, pues solo agregariamos un condicional más al momento de pagar y no afectaria a nada. Pero de la misma forma es importante realizar más test después de hacer los cambios.
