document.addEventListener("DOMContentLoaded", function() {
  // Seleziona il banner di consenso ai cookie
  const cookieBanner = document.querySelector('.cookie-consent-banner');

  // Funzione per controllare se il cookie è già presente
  function checkCookie() {
    const cookieName = 'ilmiocookie'; // Nome del cookie

    // Ottieni tutti i cookie
    const cookies = document.cookie.split(';');

    // Cicla attraverso i cookie per controllare se il cookie desiderato è presente
    for (let i = 0; i < cookies.length; i++) {
      let cookie = cookies[i].trim();

      // Verifica se il cookie desiderato è presente
      if (cookie.startsWith(`${cookieName}=`)) {
        // Se il cookie è presente, nascondi il banner di consenso ai cookie
        cookieBanner.style.display = 'none';
        return; // Esci dalla funzione se trovi il cookie
      }
    }

    // Se il cookie non è stato trovato, mostra il banner di consenso ai cookie
    cookieBanner.classList.add('show');
  }

  // Chiama la funzione per controllare se il cookie è presente al caricamento della pagina
  checkCookie();

  // Aggiungi un gestore per il click sul pulsante "Accetta"
  const acceptButton = document.querySelector('.cookie-consent-banner__cta');
  acceptButton.addEventListener('click', function() {
    const cookieName = 'ilmiocookie'; // Nome del cookie
    const cookieValue = 'valorecookie'; // Valore del cookie
    const cookieDays = 30; // Durata del cookie in giorni

    // Ottieni la data corrente
    const currentDate = new Date();
    // Imposta la scadenza del cookie
    currentDate.setTime(currentDate.getTime() + (cookieDays * 24 * 60 * 60 * 1000));
    const expires = "expires=" + currentDate.toUTCString();

    // Crea il cookie
    document.cookie = `${cookieName}=${cookieValue}; ${expires}; path=/`;

    // Nascondi il banner di consenso ai cookie dopo aver accettato
    cookieBanner.style.display = 'none';
  });
});
