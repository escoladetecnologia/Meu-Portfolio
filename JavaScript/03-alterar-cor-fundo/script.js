const button = document.querySelector('button');


function resetColor() {
    if (document.body.style.backgroundColor === 'blue') {
        document.body.style.backgroundColor = '';
    } else {
        document.body.style.backgroundColor = 'blue';
    }
}

button.addEventListener('click', resetColor);
 

