
        // JavaScript per spostare il separatore più in basso ogni volta che una nuova card viene aggiunta
        function spostaSeparatore() {
            var separator = document.getElementById('separator');
            var marginTop = window.getComputedStyle(separator).marginTop;
            var newMarginTop = parseInt(marginTop) + 40; // Aggiungi un margine di 40px
            separator.style.marginTop = newMarginTop + 'px';
        }

        // Chiamare questa funzione ogni volta che viene aggiunta una nuova card
        spostaSeparatore();
