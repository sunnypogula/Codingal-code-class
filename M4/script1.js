function validate(e) {
    e.preventDefault();
    const email = document.getElementById('email').value;
    const pass = document.getElementById('password').value;
    const age = document.getElementById('age').value;
    const msgBox = document.getElementById('message');
    let message ='';
    if (email === '') {
        message = 'please enter an email.'
        msgBox.style.color = 'red ' ;
    } else if (pass === '') {
        message = 'Password must de at least 8 characters.';
        msgBox.style.color ='red';
    } else if ( age === '') {
        message = ' age must be between 12 and 50.';
        msgBox.style.color='red'
    } else {
        message = 'login successfil';
        msgBox.style.color = 'green';
    }
    msgbox.inerText=message;
}