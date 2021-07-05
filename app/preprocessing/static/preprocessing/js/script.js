const fileZone = document.getElementById('file-zone');
const fileInput = document.getElementById('id_upload_file');
const reader = new FileReader();
const input = document.getElementById("id_wl_corr");

fileZone.addEventListener('dragover', (event) => {
    event.preventDefault();
    fileInput.parentNode.style.background = '#756C91';
    fileInput.parentNode.style.color = '#ffffff';
});

fileZone.addEventListener('dragleave', (event) => {
    event.preventDefault();
    fileInput.parentNode.style.background = '#ffffff';
    fileInput.parentNode.style.color = '#756C91';
})

fileZone.addEventListener('drop', (event) => {
    event.preventDefault();
    const files = event.dataTransfer.files;
    fileInput.files = files;
    const file = fileInput.files[0];
    reader.readAsText(file);
    fileInput.parentNode.style.background = '#756C91';
    fileInput.parentNode.style.color = '#ffffff';
})

fileInput.addEventListener('change', (event) => {
    const file = event.target.files[0];
    reader.readAsText(file);
    fileInput.parentNode.style.background = '#756C91';
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
    const alertWavelength = document.getElementById('wl_corr_alert');

    if (event.target.value < startPoint || event.target.value > endPoint) {
        event.preventDefault();
        alertWavelength.innerHTML = `指定できる波長範囲は${startPoint} nm ~ ${endPoint} nm です。`;
        alertWavelength.style.color = 'red'
    } else {
        alertWavelength.innerHTML = '';
    }
})

const formElement = document.querySelector('form');

formElement.addEventListener('submit', (event) => {
    if (input.value < startPoint || input.value > endPoint) {
        event.preventDefault();
        alert(`ゼロに補正する波長で指定できる波長範囲は${startPoint} nm ~ ${endPoint} nm です。`);
    }
})