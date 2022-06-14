(function () {

    const btnDelet = document.querySelectorAll(".btnDelet");

    btnDelet.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirmation = confirm('Are you sure you want to remove this item?');
            if (!confirmation) {
                e.preventDefault();
            }
        });
    });
    
})();
