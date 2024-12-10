document.getElementById('uploadButton').addEventListener('click', () => {
    const imageInput = document.getElementById('imageInput');
    if (imageInput.files.length === 0) {
      alert("Veuillez choisir une image !");
      return;
    }
  
    const file = imageInput.files[0];
    const formData = new FormData();
    formData.append("image", file);
  
    // Simulation d'envoi vers un backend
    fetch('https://api.fake-recipes.com/upload', {
      method: 'POST',
      body: formData,
    })
      .then(response => response.json())
      .then(data => {
        const resultsSection = document.getElementById('results');
        const recipeList = document.getElementById('recipeList');
  
        recipeList.innerHTML = ''; // Vider les anciens résultats
        data.recipes.forEach(recipe => {
          const li = document.createElement('li');
          li.textContent = recipe.name;
          recipeList.appendChild(li);
        });
  
        resultsSection.style.display = 'block';
      })
      .catch(err => {
        alert("Erreur lors de l'envoi de l'image !");
        console.error(err);
      });
  });
  