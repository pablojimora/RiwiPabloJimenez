for nota in notas:
        if nota > calificacionmayor:
            valor_mayor_a.append(nota)
            contador+=1
        print(f"Hay un total de {contador_mayor} notas mayores, las cuales serian {valor_mayor_a}")
else:
    print("No se requiere comparacion")