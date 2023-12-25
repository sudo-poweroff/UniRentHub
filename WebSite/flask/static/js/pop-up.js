        $(document).ready(() => {
	$('form header a').each((idx, item) => {
		$(item).click(function() {
			$(this).siblings().removeClass('active');
			$(this).addClass('active');

			const idx = $(this).index();
			$('form section').css('display', 'none');
			$(`form section#section-${idx + 1}`).css('display', 'block');

			if(idx === 1) {
				$('form footer').css('display', 'none');
			} else {
				$('form footer').css('display', 'block');
			}
		});
	});
});