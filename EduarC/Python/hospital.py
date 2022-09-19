"""En un hospital existen tres áreas: Ginecología, Pediatría, Traumatologia. El presupuesto anual del hospital se reparte conforme a la sig. tabla:
Área Porcentaje del presupuesto
Ginecología 40%
Traumatologia 30%
Pediatría 30%
Obtener la cantidad de dinero que recibirá cada área, para cualquier monto presupuestal."""
budget=float(input("Ingrese el monto del presupuesto anual:"))
print("El presupuesto este año para el area de ginecologia es de $",budget*.40)
print("El presupuesto este año para el area de pediatria es de $",budget*.30)
print("El presupuesto este año para el area de traumatologia es de $",budget*.30)