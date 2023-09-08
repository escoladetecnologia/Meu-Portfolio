let score1 = 0;
let score2 = 0;

// Lista de times com seus nomes e caminhos de imagens
const times = [
  {
    name: 'América-MG',
    imageSrc: './image/america-mg-logo.png',
  },
  {
    name: 'Athletico-PR',
    imageSrc: './image/athletico-pr-logo.png',
  },
  {
    name: 'Atlético-MG',
    imageSrc: './image/atletico-mg-logo.png',
  },
  {
    name: 'Bahia',
    imageSrc: './image/bahia-logo.png',
  },
  {
    name: 'Botafogo',
    imageSrc: './image/botafogo-logo.png',
  },
  {
    name: 'Corinthians',
    imageSrc: './image/corinthians-logo.png',
  },
  {
    name: 'Coritiba',
    imageSrc: './image/coritiba-logo.png',
  },
  {
    name: 'Cruzeiro',
    imageSrc: './image/cruzeiro-logo.png',
  },
  {
    name: 'Cuiabá',
    imageSrc: './image/cuiaba-logo.png',
  },
  {
    name: 'Flamengo',
    imageSrc: './image/flamengo-logo.png',
  },
  {
    name: 'Fluminense',
    imageSrc: './image/fluminense-logo.png',
  },
  {
    name: 'Fortaleza',
    imageSrc: './image/fortaleza-logo.png',
  },
  {
    name: 'Goiás',
    imageSrc: './image/goias-logo.png',
  },
  {
    name: 'Grêmio',
    imageSrc: './image/gremio-logo.png',
  },
  {
    name: 'Internacional',
    imageSrc: './image/internacional-logo.png',
  },
  {
    name: 'Palmeiras',
    imageSrc: './image/palmeiras-logo.png',
  },
  {
    name: 'Bragantino',
    imageSrc: './image/bragantino-logo.png',
  },
  {
    name: 'Santos',
    imageSrc: './image/santos-logo.png',
  },
  {
    name: 'São Paulo',
    imageSrc: './image/sao-paulo-logo.png',
  },
  {
    name: 'Vasco da Gama',
    imageSrc: './image/vasco-logo.png',
  },
];


let currentTeamIndex1 = 0;
let currentTeamIndex2 = 1;

function incrementScore(team) {
  if (team === 1) {
    score1++;
    document.getElementById('score1').textContent = score1;
  } else if (team === 2) {
    score2++;
    document.getElementById('score2').textContent = score2;
  }
}

function decrementScore(team) {
  if (team === 1 && score1 > 0) {
    score1--;
    document.getElementById('score1').textContent = score1;
  } else if (team === 2 && score2 > 0) {
    score2--;
    document.getElementById('score2').textContent = score2;
  }
}

function resetScores() {
  score1 = 0;
  score2 = 0;
  document.getElementById('score1').textContent = score1;
  document.getElementById('score2').textContent = score2;
}

/**
 * Função changeTeam: Altera o time exibido na interface com base na direção.
 *
 * @param {number} direction - A direção da mudança (1 para avançar, -1 para retroceder).
 * @param {string} team - O time a ser alterado ('team1' ou 'team2').
 */
function changeTeam(direction, team) {
  let currentIndex; // Índice do time atual
  // Verifica o time selecionado e atribui o índice correspondente
  if (team === 'team1') {
    currentIndex = currentTeamIndex1;
  } else if (team === 'team2') {
    currentIndex = currentTeamIndex2;
  }

  // Atualiza o índice com base na direção
  currentIndex += direction;

  // Garante que o índice permaneça dentro dos limites da lista de times (loop)
  if (currentIndex < 0) {
    currentIndex = times.length - 1;
  } else if (currentIndex >= times.length) {
    currentIndex = 0;
  }

  // Atualiza o índice do time atual e a interface com o novo time selecionado
  if (team === 'team1') {
    currentTeamIndex1 = currentIndex;
    document.getElementById('team1Name').textContent = times[currentIndex].name;
    document.getElementById('team1Image').src = times[currentIndex].imageSrc;
  } else if (team === 'team2') {
    currentTeamIndex2 = currentIndex;
    document.getElementById('team2Name').textContent = times[currentIndex].name;
    document.getElementById('team2Image').src = times[currentIndex].imageSrc;
  }
}