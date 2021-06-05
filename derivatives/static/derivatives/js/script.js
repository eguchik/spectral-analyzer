var dropZone = document.getElementById('drop-zone');
var preview = document.getElementById('preview');
var fileInput = document.getElementById('id_upload_file');


dropZone.addEventListener('dragover', function(e) {
    e.stopPropagation();
    e.preventDefault();
    this.style.background = '#ced1d3';
}, false);


dropZone.addEventListener('dragleave', function(e) {
    e.stopPropagation();
    e.preventDefault();
    this.style.background = '#ffffff'
}, false);


fileInput.addEventListener('change', function() {
    previewFile(this.files[0]);
});


dropZone.addEventListener('drop', function(e) {
    e.stopPropagation();
    e.preventDefault();
    this.style.background = '#ffffff' //背景色を白に戻す
    var files = e.dataTransfer.files; //ドロップしたファイルを取得
    if (files.length > 1) return alert('アップロードできるファイルは1つだけです。');
    fileInput.files = files; //inputのvalueをドラッグしたファイルに置き換える。
    previewFile(files[0]);
}, false);


function previewFile(file) {
    /* FileReaderで読み込み、プレビュー画面を表示。 */
    var fr = new FileReader();
    fr.onload = function() {
        var img = document.createElement('img');
        img.setAttribute('src', fr.result);
        previewFile.innerHTML = '';
        previewFile.appendChild(img);
    };
}


