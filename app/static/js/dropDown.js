 const showDropdownButton = document.getElementById('showDropdown');
 const dropdown = document.getElementById('dropdown');
 
 showDropdownButton.addEventListener('click', function() {
    dropdown.style.display = (dropdown.style.display === 'block') ? 'none' : 'block';
 });

 const option1 = document.getElementById('option1');
 option1.addEventListener('click', function(event) {
    event.stopPropagation();
    window.location.href = '/temp-graph';
 });