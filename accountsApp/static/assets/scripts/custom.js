$(document).ready(function(){
    $(document).on('click', '.menu-btn', function(e){
        let el = $('.navigation ul');
        let ov = $('#overlay');
        
        if (el.css("right") == '0'){
            el.animate({right: '-100%'});
        }else{
            el.animate({right: '0'});
            ov.fadeIn(100);
        }
    });

    $(document).on('click', '#overlay', function(e){
        $(this).fadeOut(100);
        $('.navigation ul').animate({right: '-100%'});
    });

    //accordion menu
    $(".accordion .item").click(function(e){
        let icon = $(this).find(".icon i");
        let isOpen = icon.hasClass("fa-plus") ? false : true;
        $(this).children(".hide").slideToggle();

        if (isOpen){
            icon.removeClass("fa-minus");
            icon.addClass("fa-plus");
        }else{
            icon.removeClass("fa-plus");
            icon.addClass("fa-minus");
        }
    });
});