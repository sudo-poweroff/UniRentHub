
    // Funzione per pulire il contenuto delle caselle di testo
    function clearTextBoxes() {
    document.getElementById('email').value = '';
    document.getElementById('nome').value = '';
    document.getElementById('cognome').value = '';
    document.getElementById('password').value = '';
}

    // Esegui la funzione quando la pagina è completamente caricata
    window.onload = function() {
    clearTextBoxes(); // Chiamata alla funzione per pulire le caselle di testo al caricamento della pagina
}
