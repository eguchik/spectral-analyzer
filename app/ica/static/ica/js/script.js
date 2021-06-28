const fileZone = document.getElementById('file-zone');
const fileInput = document.getElementById('id_upload_file');
const reader = new FileReader();
const inputComponents = document.getElementById('id_n_components');
const inputWlRangeStart = document.getElementById('id_wl_range_start');
const inputWlRangeEnd = document.getElementById('id_wl_range_end');

/* Enter keyによるフォーム送信のキャンセル */
inputComponents.onkeypress = (event) => {
    const key = event.keyCode || event.charCode || 0;
    if (key == 13) {
        event.preventDefault();
    }
}

inputWlRangeStart.onkeypress = (event) => {
    const key = event.keyCode || event.charCode || 0;
    if (key == 13) {
        event.preventDefault();
    }
}

inputWlRangeEnd.onkeypress = (event) => {
    const key = event.keyCode || event.charCode || 0;
    if (key == 13) {
        event.preventDefault();
    }
}

inputComponents.addEventListener("input", (event) => {
    const alertComponents = document.getElementById('alertComponents');

    if (event.target.value <= 0 || event.target.value > n_samples) {
        event.preventDefault();
        alertComponents.innerHTML = `指定できるコンポーネント数は${n_samples}以下です。`;
        alertComponents.style.color = 'red';
    } else {
        alertComponents.innerHTML = '';
    }
})

inputWlRangeStart.addEventListener("input", (event) => {
    const alertWavelengthStart = document.getElementById('alertWavelengthStart');

    if (event.target.value < startPoint || event.target.value > endPoint) {
        event.preventDefault();
        alertWavelengthStart.innerHTML = `指定できる波長範囲は${startPoint} nm ~ ${endPoint} nm です。`;
        alertWavelengthStart.style.color = 'red';
    } else {
        alertWavelengthStart.innerHTML = '';
    }
})

inputWlRangeEnd.addEventListener("input", (event) => {
    const alertWavelengthEnd = document.getElementById('alertWavelengthEnd');

    if (event.target.value < startPoint || event.target.value > endPoint) {
        event.preventDefault();
        alertWavelengthEnd.innerHTML = `指定できる波長範囲は${startPoint} nm ~ ${endPoint} nm です。`;
        alertWavelengthEnd.style.color = 'red';
    } else {
        alertWavelengthEnd.innerHTML = '';
    }
})


fileZone.addEventListener('dragover', (event) => {
    event.preventDefault();
    fileInput.parentNode.style.background = '#ff8c00';
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
    fileInput.parentNode.style.background = '#ff8c00';
    fileInput.parentNode.style.color = '#ffffff';
})

fileInput.addEventListener('change', (event) => {
    const file = event.target.files[0];
    reader.readAsText(file);
    fileInput.parentNode.style.background = '#ff8c00';
    fileInput.parentNode.style.color = '#ffffff';
})

reader.addEventListener('load', () => {
    const row_arr = reader.result.split('\n');
    n_samples = row_arr[0].split(',').length - 1;
    startPoint = row_arr[1].split(',')[0];
    endPoint = row_arr[row_arr.length - 2].split(',')[0];
})

const formElement = document.querySelector('form');

formElement.addEventListener('submit', (event) => {
    if (inputComponents.value <= 0 || inputComponents.value > n_samples) {
        event.preventDefault();
        alert(`指定できるコンポーネント数は${n_samples}以下です。`);
    }
})