   const show_drop_down_button = document.getElementById('showDropdown');
   const drop_down = document.getElementById('dropdown');
   
    show_drop_down_button.addEventListener('click', function() {
    drop_down.style.display = (drop_down.style.display === 'block') ? 'none' : 'block';
   });

   const option1 = document.getElementById('option1');
   option1.addEventListener('click', function(event) {
       event.stopPropagation();
       window.location.href = '/graph';
   });
