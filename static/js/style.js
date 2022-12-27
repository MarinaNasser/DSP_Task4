var saveImage1 = document.getElementById("saveImage1");

var blob = null;

saveImage1.addEventListener("change", ()=>{
    
    const fileReader = new FileReader();

    fileReader.readAsDataURL(saveImage1.files[0]);

    fileReader.addEventListener('load', () =>{
        const url = fileReader.result;
        console.log(url);

        fetch(url)
    .then(res => res.blob())
    .then(blob => handler(blob))
    console.log(blob)
        save(blob);
    })
});
let save = imageBlob => {
    let formdata = new FormData();
    formdata.append("ImageFile", imageBlob, "image.jpg");
    $.ajax({
        type: "POST",
        url: 'http://127.0.0.1:5000/image1',
        data: formdata,
        contentType: false,
        cache: false,
        processData: false,

        success: function (res) {
            $('#output').text(res.output).show();
            

        },
    });
    // event.preventDefault();

};
