/* function openTab(evt, saidName) {
    // Declare all variables
    var i, tabcontent, tablinks;

    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(saidName).style.display = "block";
    evt.currentTarget.className += " active";
} */
/* original */

function openTab(evt, saidName) {
    // Declare all variables
    var i, tabcontent, tablinks;

    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(saidName).style.display = "block";
    evt.currentTarget.className += " active";
}
function openPage(evt, saidName) {
    // Declare all variables
    var i, tabpage, innertab;

    // Get all elements with class="tabpage" and hide them
    tabpage = document.getElementsByClassName("tabpage");
    for (i = 0; i < tabpage.length; i++) {
        tabpage[i].style.display = "none";
    }

    // Get all elements with class="innertab" and remove the class "active"
    innertab = document.getElementsByClassName("innertab");
    for (i = 0; i < innertab.length; i++) {
        innertab[i].className = innertab[i].className.replace(" active", "");
    }

    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(saidName).style.display = "block";
    evt.currentTarget.className += " active";
}