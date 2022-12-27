const image1 = document.getElementById("image1");
const cropbtn1 = document.getElementById("cropImageBtn1");
const image2 = document.getElementById("image2");
const cropbtn2 = document.getElementById("cropImageBtn2");

const cropper = new Cropper(image1,{
    aspectRatio: 0,
    viewMode: 0,
});

cropbtn1.addEventListener('click', function(){
var croppedImage = cropper.getCroppedCanvas().toDataURL('image1/png');

document.getElementById('output1').src = croppedImage;

});


const cropper2 = new Cropper(image2,{
    aspectRatio: 0,
    viewMode: 0,
});

cropbtn2.addEventListener('click', function(){
var croppedImage = cropper2.getCroppedCanvas().toDataURL('image2/png');

document.getElementById('output2').src = croppedImage;

});
