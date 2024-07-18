#!/bin/bash

# Eliminar informe.pdf si existe
rm -f informe.pdf

# Declarar array con los nombres de los capítulos
capitulos=("1_ejercicio.md" "2_ejercicio.md" "3_ejercicio.md" "4_ejercicio.md" "5_ejercicio.md" "6_ejercicio.md" "7_ejercicio.md" "8_ejercicio.md" "9_ejercicio.md" 10_ejercicio.md "11_ejercicio.md" "12_ejercicio.md" "13_ejercicio.md" "14_ejercicio.md" "15_ejercicio.md")
margen="2cm"

# Convertir cada archivo markdown a PDF
for capitulo in "${capitulos[@]}"; do
    echo "Creando PDF de $capitulo"
    pandoc "$capitulo" -o "${capitulo%.md}.pdf" --variable classoption=oneside --variable fontsize=12pt --variable linkcolor=blue --variable urlcolor=blue --variable geometry:margin="$margen" --include-in-header config.tex
done

# Crear el PDF del informe completo
echo "Creando PDF de todo el informe"
#pdftk 1_ejercicio.pdf 2_ejercicio.pdf 3_ejercicio.pdf cat output informe.pdf
pdftk 1_ejercicio.pdf 2_ejercicio.pdf 3_ejercicio.pdf 4_ejercicio.pdf 5_ejercicio.pdf 6_ejercicio.pdf 7_ejercicio.pdf 8_ejercicio.pdf 9_ejercicio.pdf 10_ejercicio.pdf 11_ejercicio.pdf 12_ejercicio.pdf 13_ejercicio.pdf 14_ejercicio.pdf 15_ejercicio.pdf cat output informe.pdf

# Eliminar PDFs temporales
for capitulo in "${capitulos[@]}"; do
    rm "${capitulo%.md}.pdf"
done

# Concatenar los archivos markdown en README.md
> README.md
for capitulo in "${capitulos[@]}"; do
    cat "$capitulo" >> README.md
done

echo "Informe creado en informe.pdf"

# ejecutar con bash generar-pdf.sh
