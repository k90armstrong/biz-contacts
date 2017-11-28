document.addEventListener("DOMContentLoaded", function (event) {
    console.log('hi')

    // global variables
    var rightMenu = {state: 'close'};
    var newContactModal = {
        state: 'close', 
        el: document.getElementById('new-contact-modal')
    };

    // functions
    function openRightMenu() {
        document.getElementById('right-menu-dropdown').className = "dropdown is-active";
        rightMenu.state = 'open';
    }

    function closeRightMenu() {
        document.getElementById('right-menu-dropdown').className = "dropdown";
        rightMenu.state = 'close';
    }

    function openModal(modal) {
        console.log(modal);
        modal.el.className = 'modal is-active';
        modal.state = 'open';
    }

    function closeModal(modal) {
        console.log(modal);
        modal.el.className = 'modal';
        modal.state = 'close';
    }

    // handlers
    function rightMenuHandler(event) {
        event.stopPropagation();
        openRightMenu();
    }

    function documentClickHandler(event) {
        if (rightMenu.state === 'open') {
            closeRightMenu();
        }
        if (newContactModal.state === 'open') {
            closeModal(newContactModal);
            console.log(event);
        }
    }

    function addNewContactHandler(event) {
        event.stopPropagation();  
        openModal(newContactModal);
        getNewContactForm();
    }

    function modalClickHandler(event) {
        event.stopPropagation();
    }

    function keyUpOnSearchHandler(event) {
        var searchTerm = document.getElementById('search_input').value;
        var url = 'search/';
        url += '?q=' + searchTerm;
        $.ajax({
            url: url,
            type: 'get',
            dataType: 'json',
            success: function (data) {
                $('#contact_cards').html(data.html);
                console.log('did it work?')
            }
        });

    }

    // ajax calls
    function getNewContactForm() {
        console.log('start of ajax');
        $.ajax({
            url: 'newcontact/',
            type: 'get',
            dataType: 'json',
            success: function (data) {
                console.log('form stuff')
              $("#contact-info-form").html(data.html_form);
            }
        });
    }

    // add event listener to the join and login
    document.getElementById('right-menu').addEventListener('click', rightMenuHandler);
    document.addEventListener('click', documentClickHandler);
    document.getElementById('new-contact-button').addEventListener('click', addNewContactHandler);
    document.getElementById('search_input').addEventListener('keyup', keyUpOnSearchHandler);
    $('.modal-content').on('click', modalClickHandler);

});