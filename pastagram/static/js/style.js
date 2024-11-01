
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


/* 이미지 url 전송 */
// function submitImages() {
//     var selectedImageUrls = $('input[name="selectedImages"]:checked').map(function() {
//         return $(this).val();
//     }).get();

// }
// function submitImages() {
    // var selectedImageUrls = $('input[name="selectedImages"]:checked').map(function() {
    //     return $(this).val();
    // }).get();
    // alert("알림 메시지입니다.");

    // $.ajax({
    //     url: url,
    //     method: 'POST',
    //     data: { selectedImageUrls: selectedImageUrls },
    //     success: function(response) {
    //         // 성공적으로 서버로 데이터를 전송한 후 실행되는 코드
    //         alert("성공.");

    //         console.log('이미지 전송이 완료되었습니다.');
    //     },
    //     error: function(xhr, status, error) {
    //         // 서버로 데이터 전송이 실패한 경우 실행되는 코드
    //         console.error('이미지 전송 중 오류가 발생했습니다:', error);
    //     }
    // });

    // 서버로 데이터를 전송하는 POST 요청을 보냅니다.
    // axios.post(url, {
    //     selectedImageUrls: selectedImageUrls,

    // })
    // .then(function(response) {
    //     console.log(selectedImageUrls);

        
    //     // 성공적으로 서버로부터 응답을 받았을 때 실행될 코드를 여기에 작성합니다.
    //     console.log(response);
    // })
    // .catch(function(error) {
    //     // 오류가 발생했을 때 실행될 코드를 여기에 작성합니다.
    //     console.error(error);
    // });
// }

// post_add textarea 자동 높이 조절
var textarea = document.querySelector('.post-text-content');

function adjustHeight() {
    textarea.style.height = '7rem'; 
    textarea.style.height = textarea.scrollHeight * 0.1 + 'rem'; 
}

textarea.addEventListener('input', adjustHeight);
adjustHeight();