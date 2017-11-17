document.addEventListener("DOMContentLoaded", function (event) {
    console.log('hi')

    function openModal(modal) {
        console.log(modal);
        modal.className = 'modal is-active';
    }

    function closeModal(modal) {
        console.log(modal);
        modal.className = 'modal';
    }


    // handler functions
    function joinClickHandler(event) {
        openModal(document.getElementById('signup-modal'))
    }

    function loginClickHandler(event) {
        openModal(document.getElementById('login-modal'));
    }

    function submitLoginHandler(event) {

    }

    function cancelButtonHandler(event) {
        closeModal(document.getElementById('signup-modal'));
        closeModal(document.getElementById('login-modal'));

    }

    // add event listener to the join and login
    document.getElementById('join-button').addEventListener('click', joinClickHandler);
    document.getElementById('login-button').addEventListener('click', loginClickHandler);
    document.getElementById('submit-login-button').addEventListener('click', submitLoginHandler);
    document.getElementById('submit-login-button').addEventListener('click', submitLoginHandler);
    document.getElementById('cancel-signup-button').addEventListener('click', cancelButtonHandler);
    document.getElementById('cancel-login-button').addEventListener('click', cancelButtonHandler);


});