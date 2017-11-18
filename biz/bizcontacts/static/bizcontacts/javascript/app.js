document.addEventListener("DOMContentLoaded", function (event) {
    console.log('hi')

    // functions
    function openRightMenu() {
        document.getElementById('right-menu-dropdown').className = "dropdown is-active";
    }

    function closeRightMenu() {
        document.getElementById('right-menu-dropdown').className = "dropdown";
    }

    // handlers
    function rightMenuHandler(event) {
        openRightMenu();
    }

    // add event listener to the join and login
    document.getElementById('right-menu').addEventListener('click', rightMenuHandler);


});