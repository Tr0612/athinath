const imgs = document.querySelectorAll('.img-select a');
const imgBtns = [...imgs];
let imgId = 1;

imgBtns.forEach((imgItem) => {
    imgItem.addEventListener('click', (event) => {
        event.preventDefault();
        imgId = imgItem.dataset.id;
        slideImage();
    });
});

function slideImage(){
    const displayWidth = document.querySelector('.img-showcase img:first-child').clientWidth;

    document.querySelector('.img-showcase').style.transform = `translateX(${- (imgId - 1) * displayWidth}px)`;
}



window.addEventListener('resize', slideImage);
$(document).ready(function(){
    $('#img-showcase img').each(function(){
        var maxWidth = 900;
        var ratio = 0;
        var img = $(this);

        if(img.width() > maxWidth){
            ratio = img.height()/img.width();
            img.css("height",(maxWidth*ratio));
            img.css("width",maxWidth);
        }
    });

    $('#img-showcase img').load(function(){
        var maxWidth = 900;
        var ratio = 0;
        var img = $(this);

        if(img.width() > maxWidth){
            ratio = img.height()/img.width();
            img.css("height",(maxWidth*ratio));
            img.css("width",maxWidth);
        }
    });
});