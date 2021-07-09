function recupera() {
    fetch("https://mindicador.cl/api/dolar")
        .then(
            function(response) {
                if (response.status != 200) {
                    alert("Actualmente los servicios no estan disponibles");
                    return;
                }
                response.json().then(function(data) {
                    console.log(data)
                    var dolar = data.serie[0].valor;
                    alert('El valor del dolar actual es de: ' + dolar + ' CLP');
                })
            }
        )
}