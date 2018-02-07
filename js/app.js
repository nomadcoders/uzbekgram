
var heart = $('#heart');


heart.on('click', function () {
    $(this).removeClass('far');
    $(this).addClass('fa clicked-heart');
})

