// questi sono  endpoint delle api
const url_cocktail  = 'https://www.thecocktaildb.com/api/json/v1/1/search.php?s=' ;

// questi sono elementi della pagina html
const sezioneCards = document.querySelector("#cards-drinks")
//creo variabili per barra ricerca
const inputCocktail = document.querySelector('#input-cocktail')
const btnSearch = document.querySelector('#btn-search')
//creo variabilr del cockatail cercato
let cocktailSearched = '';



//gestione eventi


btnSearch.addEventListener('click', function() {
    console.log('btn search cliccato');
    
    
    cocktailSearched = inputCocktail.value;
    console.log(cocktailSearched);

    //creo nuova variabile nuova url da chiamare
    const urlSearched = url_cocktail + cocktailSearched;

    //pulisco la oagina con la funzione
    cleanCard();
    //faccio la fetch
    callAPI(urlSearched);

});

// chiamo la funzione che comprende la logica dell'applicazione 
callAPI(url_cocktail);

// qui metto eventuali funzioni e metodi

//creo la funzione callAPI

    function callAPI(url){

        // Questo è la logica dell' applicazione, qui faccio il fetch 
fetch(url)
    .then(res => res.json())
    .then(data => {
        

        // cosa voglio estarre?
        //     strDrink
        //     strAlcoholic
        //     strCategory
        //     strDrinkThumb
        //     strGlass
        //     strInstructions

    //1. ciclare l'array che contiene i drinks
    for(d of data.drinks){
            
        //2. per ogni drink: genera questa card

        sezioneCards.innerHTML += `
        <!-- colonna 1 card -->
      <div class="col-lg-3 mb-4">

        <!-- singola card 1 -->
        <div class="card" style="width:100%">
          <img class="card-img-top" src="${d.strDrinkThumb}">
          <div class="card-body">
            <h4 class="card-title">${d.strDrink}
            <span>(${d.strAlcoholic}</span></h4>
            
            <p class="card-text"> <b>Category : </b>${d.strCategory}.</p>
            <button class="btn btn-info" data-bs-toggle="collapse" data-bs-target="#D${d.idDrink}">Collapsible</button>
            
            <!-- per fare collassare solo 1 elemento per volta 
            l'id deve essere univoco e deve iniziare con qualsiasi carattere e NON per numero-->
            
            <div id="D${d.idDrink}" class="collapse">
              <p>${d.strInstructions}</p>
              </div>
          </div>
        </div>        
      </div>  
        `  
    
        }        
    });
    }


//creo la funzione per svuotare la pagina
function cleanCard() {
    // ripulire le card visualizzate
    sezioneCards.innerHTML = '';
    //per ripulire l'input cercato dall'utente
    inputCocktail.value = ''
}
    