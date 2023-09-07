
let score1 = 0;
let score2 = 0;

  function incrementScore(team) {
    if (team === 1) {
      score1++;
      document.getElementById("score1").textContent = score1;
    } else if (team === 2) {
      score2++;
      document.getElementById("score2").textContent = score2;
    }
  }

  function resetScores() {
    score1 = 0;
    score2 = 0;
    document.getElementById("score1").textContent = score1;
    document.getElementById("score2").textContent = score2;
  }

