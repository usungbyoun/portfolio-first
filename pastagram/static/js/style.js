
/* 이미지 파일 선택하면 이름 띄우기 */
function displayFileName(input) {
    var fileInputs = input.files;
    var fileNameDisplay = document.querySelector('.local-file-name');
    var errorMessage = document.querySelector('.none-image-error');
    if (fileInputs.length > 0) {
        var fileNames = Array.from(fileInputs).map(function(file) {
            return file.name;
        });
        
        fileNameDisplay.textContent = fileNames.join(', ');
        if (errorMessage) {
            errorMessage.style.display = 'none';
        }


    }
}


// post_add textarea 자동 높이 조절
var textarea = document.querySelector('.post-text-content');

function adjustHeight() {
    textarea.style.height = '7rem'; 
    textarea.style.height = textarea.scrollHeight * 0.1 + 'rem'; 
}

textarea.addEventListener('input', adjustHeight);
adjustHeight();