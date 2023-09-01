var total = 0;
document.getElementById("form").addEventListener("submit", function(event){
    event.preventDefault()
    var nome = document.getElementById("nome").value;
    var preco = document.getElementById("preco").value;
    preco = preco.replace(/[^0-9,]/g, "");
    var table = document.getElementById("lista");
    var row = table.insertRow(-1);
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    var cell3 = row.insertCell(2);
    cell1.innerHTML = nome;
    cell2.innerHTML = preco;
    cell3.innerHTML = "<button>X</button>";
    cell3.firstChild.addEventListener("click", function(){
        row.remove();
        total -= parseFloat(preco.replace(",", "."));
        document.getElementById("total").innerHTML = total.toFixed(2).replace(".", ",");
    });
    document.getElementById("nome").value = "";
    document.getElementById("preco").value = "";
    total += parseFloat(preco.replace(",", "."));
    document.getElementById("total").innerHTML = total.toFixed(2).replace(".", ",");
});
