window.addEventListener("load", function (e) {
    const row = document.querySelector(".result_row");
    const artist = document.querySelector(".artist");
    const title = document.querySelector(".title");
    const genre = document.querySelector(".genre");

    row.addEventListener("click", function () {
        localStorage.setItem("title", title.value);
        localStorage.setItem("artist", artist.value);
        localStorage.setItem("genre", genre.value);
    });
})