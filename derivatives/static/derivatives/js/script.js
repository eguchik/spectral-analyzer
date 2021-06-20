const fileZone = document.getElementById('file-zone');
const fileInput = document.getElementById('id_upload_file');
const reader = new FileReader();
const input = document.getElementById("id_window_length");

fileZone.addEventListener('dragover', (event) => {
    event.preventDefault();
    fileInput.parentNode.style.background = '#0080C0';
    fileInput.parentNode.style.color = '#ffffff';
});

fileZone.addEventListener('dragleave', (event) => {
    event.preventDefault();
    fileInput.parentNode.style.background = '#ffffff';
    fileInput.parentNode.style.color = '#4E4449';
})

fileZone.addEventListener('drop', (event) => {
    event.preventDefault();
    const files = event.dataTransfer.files;
    fileInput.files = files;
    const file = fileInput.files[0];
    reader.readAsText(file);
    fileInput.parentNode.style.background = '#0080C0';
    fileInput.parentNode.style.color = '#ffffff';
})

fileInput.addEventListener('change', (event) => {
    const file = event.target.files[0];
    reader.readAsText(file);
    fileInput.parentNode.style.background = '#0080C0';
    fileInput.parentNode.style.color = '#ffffff';
})

reader.addEventListener('load', () => {
    const row_arr = reader.result.split('\n');
    startPoint = row_arr[1].split(',')[0];
    endPoint = row_arr[row_arr.length - 2].split(',')[0];

    document.getElementById('id_wl_corr').value = endPoint;
})


/* Enter keyによるフォーム送信のキャンセル */
input.onkeypress = (event) => {
    const key = event.keyCode || event.charCode || 0;
    if (key == 13) {
        event.preventDefault();
    }
}

input.addEventListener("input", (event) => {
    const alertWindowLength = document.getElementById('window_length_alert');

    if (event.target.value % 2 == 0 && event.target.value != 0) {
        event.preventDefault();
        alertWindowLength.innerHTML = 'ウィンドウ幅は奇数です。';
        alertWindowLength.style.color = 'red';
    } else {
        alertWindowLength.innerHTML = '';
    }
})

const formElement = document.querySelector('form');

formElement.addEventListener('submit', (event) => {
    if (input.value % 2 == 0 && input.value != 0) {
        event.preventDefault();
        alert('ウィンドウ幅は奇数です。');
    }
})