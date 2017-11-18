document.addEventListener("DOMContentLoaded", function (event) {
    console.log('hi')

    // global variables
    var rightMenu = {state: 'close'};

    // functions
    function openRightMenu() {
        document.getElementById('right-menu-dropdown').className = "dropdown is-active";
        rightMenu.state = 'open';
    }

    function closeRightMenu() {
        document.getElementById('right-menu-dropdown').className = "dropdown";
        rightMenu.state = 'close';
    }

    // handlers
    function rightMenuHandler(event) {
        event.stopPropagation();
        openRightMenu();
    }

    function documentClickHandler(event) {
        if (rightMenu.state == 'open') {
            console.log('close');
            closeRightMenu();
        }
    }

    // add event listener to the join and login
    document.getElementById('right-menu').addEventListener('click', rightMenuHandler);
    document.addEventListener('click', documentClickHandler);


});