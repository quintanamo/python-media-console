function playMusicFile(item) {
    var audio = document.getElementById("audio");
    document.getElementById("song-info").innerHTML = item.getAttribute('songref');
    audio.src = item.getAttribute('songref');
    audio.play();
}