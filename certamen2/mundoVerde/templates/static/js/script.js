document.addEventListener("DOMContentLoaded", function() {
    const tipoResiduos = document.getElementById("tipo-residuo");
    const subcategorias = document.getElementById("subcategoria");

    const opcionesSubcategorias = {
        "Plástico": ["Botellas", "Envases", "Bolsas"],
        "Papel": ["Periódicos", "Cartón", "Papel de oficina"],
        "Vidrio": ["Botellas", "Frascos", "Cristalería"],
        "Metales": ["Latas", "Cables", "Electrodomésticos pequeños"],
        "Electrónicos": ["Teléfonos móviles", "Baterías", "Componentes de computadoras"]
    };

    tipoResiduos.addEventListener("change", function() {
        const selectedTipo = this.value;
        subcategorias.innerHTML = "";
        if (selectedTipo) {
            const subcategoriasOptions = opcionesSubcategorias[selectedTipo];
            subcategoriasOptions.forEach(subcat => {
                const option = document.createElement("option");
                option.value = subcat;
                option.textContent = subcat;
                subcategorias.appendChild(option);
            });
        }
    });
});
