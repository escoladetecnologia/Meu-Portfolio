let contador = 0;
const valueElement = document.getElementById("value");

// Função para atualizar o valor exibido
function atualizarValor() {
  valueElement.textContent = contador;
}

// Função para diminuir o contador
function decrementar() {
  contador--;
  atualizarValor();
}

// Função para resetar o contador
function resetar() {
  contador = 0;
  atualizarValor();
}

// Função para aumentar o contador
function incrementar() {
  contador++;
  atualizarValor();
}

// Chamar a função para exibir o valor inicial
atualizarValor();
