document.addEventListener('DOMContentLoaded', () => {
  const loginForm = document.getElementById('login-form');
  const loginLink = document.getElementById('login-link');
  const token = getCookie('token');

  // Si hay token, ocultamos el botón de login (en index.html)
  if (token && loginLink) {
    loginLink.style.display = 'none';
  }

  // FUNCIONALIDAD DE LOGIN
  if (loginForm) {
    loginForm.addEventListener('submit', async (event) => {
      event.preventDefault();

      const email = document.getElementById('email').value;
      const password = document.getElementById('password').value;
      const errorMessage = document.getElementById('error-message');

      try {
        const response = await fetch('http://127.0.0.1:5000/api/v1/auth/login', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ email, password })
        });

        if (response.ok) {
          const data = await response.json();
          document.cookie = `token=${data.access_token}; path=/`;
          window.location.href = 'index.html';
        } else {
          const errorData = await response.json();
          errorMessage.textContent = errorData.error || 'Login failed';
          errorMessage.style.display = 'block';
        }
      } catch (error) {
        errorMessage.textContent = 'Could not connect to the server';
        errorMessage.style.display = 'block';
      }
    });
  }

  // FUNCIONALIDAD DE INDEX: Fetch de lugares
  const placesList = document.getElementById('places-list');
  const priceFilter = document.getElementById('price-filter');

  if (placesList && token) {
    fetchPlaces(token);
  }

  async function fetchPlaces(token) {
    try {
      const response = await fetch('http://127.0.0.1:5000/api/v1/places', {
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        }
      });

      if (!response.ok) throw new Error("Error loading places");

      const places = await response.json();
      displayPlaces(places);
    } catch (error) {
      console.error("Error loading places:", error);
      placesList.innerHTML = '<p style="color: red;">Error loading places</p>';
    }
  }

  function displayPlaces(places) {
    placesList.innerHTML = '';

    places.forEach(place => {
      const card = document.createElement('div');
      card.className = 'place-card';
      card.dataset.price = place.price || place.price_per_night;

      card.innerHTML = `
        <h2>${place.name}</h2>
        <p>Price: $${place.price || place.price_per_night}/night</p>
        <button class="details-button" onclick="location.href='place.html?id=${place.id}'">View Details</button>
      `;

      placesList.appendChild(card);
    });
  }

  // FILTRO DE PRECIO
  if (priceFilter) {
    priceFilter.addEventListener('change', () => {
      const maxPrice = priceFilter.value;
      const cards = document.querySelectorAll('.place-card');

      cards.forEach(card => {
        const price = parseFloat(card.dataset.price);
        if (maxPrice === 'all' || price <= parseFloat(maxPrice)) {
          card.style.display = 'block';
        } else {
          card.style.display = 'none';
        }
      });
    });
  }

  // UTILIDAD: Leer cookie
  function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
  }
});
