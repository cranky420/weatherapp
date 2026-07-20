const searchButton = document.getElementById("search-btn");

searchButton.addEventListener("click", async () => {
  const city = document.getElementById("city-input").value.trim();

  if (!city) {
    alert("Please enter a city.");
    return;
  }

  try {
    const response = await fetch(
      `/api/weather?city=${encodeURIComponent(city)}`,
    );

    if (!response.ok) {
      throw new Error("Unable to fetch weather.");
    }

    const data = await response.json();

    document.getElementById("temperature").textContent =
      `${data.temperature} °C`;
    document.getElementById("humidity").textContent = `${data.humidity}%`;
    document.getElementById("wind").textContent = `${data.wind} km/h`;
    document.getElementById("condition").textContent = data.condition;
  } catch (err) {
    console.error(err);
    alert(err.message || "Failed to fetch weather data.");
  }
});
