const CookieModal = new bootstrap.Modal(document.getElementById('CookieModal'));
const SuggestModal = new bootstrap.Modal(document.getElementById('writeSuggestModal'));

let results = document.cookie.match(/name=(.+?)(;|$)/);


function saveName() {
    document.cookie = "username=" + document.getElementById("helloInput").value + "; max-age=2678400";
    results = document.cookie.match(/name=(.+?)(;|$)/);
    cookieModalStart()
}

function cookieModalStart() {
    const userName = results;

    if (userName !== null) {
        const userName = results[0].slice(5)
        document.getElementById("hello").innerHTML = "Здравствуйте, " + userName;
        document.getElementById("helloInput").style.visibility = "hidden";
        document.getElementById("save").style.visibility = "hidden";
    } else {
        document.getElementById("hello").innerHTML = "Здравствуйте, вы зашли на этот сайт впервые, представтесь.";
        document.getElementById("helloInput").style.visibility = "visible";
        document.getElementById("save").style.visibility = "visible";
    }
    CookieModal.show()

}

function clearCookies() {
    document.cookie = "username=" + document.getElementById("helloInput").value + "; max-age=-1";
}

function suggestModalStart() {
    SuggestModal.show()
}

cookieModalStart()
