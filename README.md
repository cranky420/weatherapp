# Weather App

A responsive weather application for checking current conditions, searching cities, and viewing short-term and multi-day forecasts.

## Overview

This project is a front-end weather dashboard that lets users:
- search for weather by city name
- view current temperature, humidity, wind speed, and weather description
- display hourly and daily forecast data
- switch between metric and imperial units
- use browser geolocation for local weather
- view a clean, mobile-friendly UI

The app typically connects to a public weather API such as OpenWeatherMap or WeatherAPI and renders the returned data in a user-friendly interface.

## Features

- Search weather by location
- Current weather card with conditions and temperature
- Hourly forecast display
- Daily forecast panel
- Temperature unit conversion
- Loading and error states
- Responsive layout for desktop and mobile
- Optional location-based weather lookup

## Tech Stack

- Frontend: React, Next.js, or plain JavaScript
- Build tool: Vite or Webpack
- Styling: CSS Modules, Tailwind CSS, SCSS, or styled-components
- State management: React Context, Redux, Zustand, or local state
- Weather API: OpenWeatherMap, WeatherAPI, or similar
- Linting: ESLint
- Formatting: Prettier
- Testing: Vitest, Jest, or Cypress

## Project Structure

```text
weatherapp/
├── public/
│   ├── favicon.ico
│   ├── icons/
│   ├── images/
│   └── manifest.json
├── src/
│   ├── components/
│   │   ├── Header/
│   │   ├── SearchBar/
│   │   ├── WeatherCard/
│   │   ├── Forecast/
│   │   └── ErrorState/
│   ├── context/
│   │   └── WeatherContext.jsx
│   ├── hooks/
│   │   ├── useWeatherData.js
│   │   └── useLocation.js
│   ├── pages/
│   │   ├── Home.jsx
│   │   └── Details.jsx
│   ├── services/
│   │   └── weatherApi.js
│   ├── utils/
│   │   ├── formatDate.js
│   │   ├── convertUnits.js
│   │   └── weatherIcons.js
│   ├── App.jsx
│   ├── main.jsx
│   └── index.css
├── .env.example
├── .gitignore
├── package.json
├── vite.config.js
├── README.md
└── LICENSE
```

## Folder Explanations

### public/
This folder stores static assets such as icons, favicons, images, and other files served directly by the browser.

### src/
This is the main source directory for the app logic and UI.

### src/components/
Reusable UI blocks like:
- search bar
- weather cards
- forecast list
- error/loading displays
- header/navigation

### src/context/
Stores app-wide state such as:
- selected city
- current weather data
- preferred temperature unit
- loading/error flags

### src/hooks/
Custom hooks that handle:
- API calls
- geolocation access
- derived data processing
- reusable app logic

### src/services/
The API layer responsible for:
- building request URLs
- sending requests to the weather provider
- parsing responses
- handling failures and status errors

### src/utils/
Helper functions such as:
- date formatting
- unit conversion
- weather code mapping to icons
- small reusable utility logic

### src/pages/
Page-level components or route screens, for example:
- home page
- forecast page
- location details page

## Installation

Install dependencies:

```bash
npm install
```

## Environment Variables

Create a `.env` file in the project root:

```env
VITE_WEATHER_API_KEY=your_api_key_here
```

If the project uses a Next.js configuration instead, the environment variable may look like:

```env
NEXT_PUBLIC_WEATHER_API_KEY=your_api_key_here
```

Important:
- never commit real API keys to version control
- add `.env` to `.gitignore`

## Running the App

Start the development server:

```bash
npm run dev
```

Build the app for production:

```bash
npm run build
```

Preview the production build:

```bash
npm run preview
```

## Typical App Flow

The app usually follows this flow:

```text
User enters city or allows location access
    -> app validates input
    -> weather API request is sent
    -> loading state shows while fetching
    -> response is parsed and normalized
    -> weather data is rendered in the UI
```

A typical service call could look like:

```js
async function fetchWeather(city) {
  const response = await fetch(
    `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${import.meta.env.VITE_WEATHER_API_KEY}&units=metric`
  );

  if (!response.ok) {
    throw new Error("Weather data could not be fetched");
  }

  return response.json();
}
```

## Data Displayed

The app often displays:
- current temperature
- weather condition text
- humidity
- wind speed
- sunrise and sunset
- hourly forecast
- daily forecast
- min/max temperature
- precipitation chance

## Styling

The UI is usually designed with:
- clean card layouts
- dark/light themes
- weather-specific colors
- responsive mobile-first design
- icon-driven status indicators

## Testing

Run the test suite:

```bash
npm test
```

Common test cases include:
- invalid city search
- loading spinner behavior
- successful weather fetch
- failed API response handling
- temperature conversion logic
- forecast rendering

## Deployment

This project can be deployed to:
- Vercel
- Netlify
- GitHub Pages
- Firebase
- AWS Amplify

Example Vercel deployment:

```bash
npm install -g vercel
vercel
```

## Troubleshooting

### API key issues
- check `.env` values
- confirm the key is valid
- verify the request URL is correct

### Blank page
- inspect browser console errors
- confirm the app is rendering without runtime exceptions
- check network requests in dev tools

### Forecast not updating
- verify state updates after city change
- inspect API response parsing
- ensure the app is not caching old data

## License

This project is licensed under the MIT license. See `LICENSE` for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and lint checks
5. Open a pull request
