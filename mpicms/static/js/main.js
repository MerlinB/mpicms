document.addEventListener('DOMContentLoaded', function () {

    // Dropdowns
    var $dropdowns = getAll('.dropdown:not(.is-hoverable), .has-dropdown:not(.is-hoverable)');

    if ($dropdowns.length > 0) {
        $dropdowns.forEach(function ($el) {
            $el.addEventListener('click', function (event) {
                event.stopPropagation();
                $el.classList.toggle('is-active');
            });
        });

        document.addEventListener('click', function (event) {
            closeDropdowns();
        });
    }

    function closeDropdowns() {
        $dropdowns.forEach(function ($el) {
            $el.classList.remove('is-active');
        });
    }

    // Close dropdowns if ESC pressed
    document.addEventListener('keydown', function (event) {
        var e = event || window.event;
        if (e.keyCode === 27) {
            closeDropdowns();
        }
    });

    // Navbar
    const $navbarBurgers = getAll('.navbar-burger');

    if ($navbarBurgers.length > 0) {
      $navbarBurgers.forEach( el => {
        el.addEventListener('click', () => {
          const target = el.dataset.target;
          const $target = document.getElementById(target);
          el.classList.toggle('is-active');
          $target.classList.toggle('is-active');

        });
      });
    }

    document.querySelectorAll('.navbar-link').forEach(function(navbarLink){
        navbarLink.addEventListener('click', function(){
          navbarLink.nextElementSibling.classList.toggle('is-hidden-touch');
        })
      });

    // Functions
    function getAll(selector) {
        return Array.prototype.slice.call(document.querySelectorAll(selector), 0);
    }

    //Modals
    document.querySelectorAll(['.richtext-image', '.modal-image']).forEach(function(el, index) {
        document.body.insertAdjacentHTML('afterbegin', 
            `<div id="modal-${index}" class="modal">
                <div class="modal-background"></div>
                <div class="modal-content">
                    <p class="image has-ratio">
                        <img src="${el.getAttribute('src')}" width="${el.getAttribute('width')}" height="${el.getAttribute('height')}" alt="${el.getAttribute('alt')}">
                    </p>
                </div>
                <button class="modal-close is-large" aria-label="close"></button>
            </div>`
        );
        el.addEventListener('click', function(event) {
            event.preventDefault();
            var modal = document.getElementById(`modal-${index}`);
            modal.classList.add('is-active');
        
            modal.querySelectorAll(['.modal-background', '.modal-close']).forEach(function(el){
                el.addEventListener('click', function(e) {
                    e.preventDefault();
                    modal.classList.remove('is-active');
                });
            });
        });
    });

});