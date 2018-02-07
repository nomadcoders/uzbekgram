var heart = $('#heart');
heart.on('click', function () {
    el = $(this)
    el.toggleClass('far fa clicked-heart')
})