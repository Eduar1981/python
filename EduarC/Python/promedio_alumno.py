"""Un alumno desea saber cual será su promedio general en las tres materias mas difíciles que cursa y cual será el promedio que obtendrá en cada una de ellas. Estas materias se evalúan como se muestra a continuación"""
"""La calificación de Matemáticas se obtiene de la sig. manera:
Examen 90%
Promedio de tareas 10%
En esta materia se pidió un total de tres tareas.
La calificación de Física se obtiene de la sig. manera:
Examen 80%
Promedio de tareas 20%
En esta materia se pidió un total de dos tareas.
La calificación de Química se obtiene de la sig. manera:
Examen 85%
Promedio de tareas 15%
En esta materia se pidió un promedio de tres tareas."""
Exam_matemt=float(input("Ingrese la nota del examen de matematicas:"))
Prom_tar_matemt1=float(input("Ingrese la nota de la tarea #1 de matematicas:"))
Prom_tar_matemt2=float(input("Ingrese la nota de la tarea #2 de matematicas:"))
Prom_tar_matemt3=float(input("Ingrese la nota de la tarea #3 de matematicas:"))
Total_Prom_tareas_matemt=(Prom_tar_matemt1+Prom_tar_matemt2+Prom_tar_matemt3)/3
Prom_matemt=(Exam_matemt*0.90)+(Total_Prom_tareas_matemt*0.10)


Exam_fisic=float(input("Ingrese la nota del examen de fisica:"))
Prom_tar_fisic1=float(input("Ingrese la nota de la tarea #1 de fisica:"))
Prom_tar_fisic2=float(input("Ingrese la nota de la tarea #2 de fisica:"))
Total_Prom_tareas_fisic=(Prom_tar_fisic1+Prom_tar_fisic2)/2
Prom_fisic=(Exam_fisic*0.80)+(Total_Prom_tareas_fisic*0.20)

Exam_quimc=float(input("Ingrese la nota del examen de quimica:"))
Prom_tar_quimic1=float(input("Ingrese la nota de la tarea #1 de quimica:"))
Prom_tar_quimic2=float(input("Ingrese la nota de la tarea #2 de quimica:"))
Prom_tar_quimic3=float(input("Ingrese la nota de la tarea #3 de quimica:"))
Total_Prom_tareas_quimic=(Prom_tar_quimic1+Prom_tar_quimic2+Prom_tar_quimic3)/3
Prom_quimic=(Exam_quimc*0.85)+(Total_Prom_tareas_quimic*0.15)
Prom_genl=(Prom_matemt+Prom_fisic+Prom_quimic)/3

print("El promedio de matematicas es:",Prom_matemt)
print("El promedio de fisica es:",Prom_fisic)
print("El promedio de quimica es:",Prom_quimic)


print("El promedio general de las tres materias es:",Prom_genl)