# Pakistan Cities and Sub Areas Geocoding

## Overview

This project provides a comprehensive and **publicly available location dataset for Pakistan**, including cities, sub-areas, and addresses with their corresponding geolocation coordinates. The main goal is to offer a **free alternative** to expensive Google Maps API calls, making it ideal for Pakistani applications like OLX, restaurant delivery apps, real estate platforms, and other location-based services.

By making this data public and open-source, it supports startups, indie developers, and companies who need reliable geocoding data without ongoing costs or access restrictions.

## Project Structure and Workflow

```bash
location_info/
├── city/                          # City data collection
│   ├── scraper.py                 # Web scraper for city names
│   └── cities.json                # Raw city data
│
├── city_area/                     # Area data collection
│   ├── area_scraper.py            # Scraper for areas within cities
│   └── city_areas.json            # Raw area data per city
│
├── country/                       # Country-wide data
│   └── merged_data.json           # Combined city and area data
│
├── geocoding/                     # Geocoding implementation
│   ├── photon_search.py           # Photon 0.7.0 OpenSearch integration
│   ├── geocoding_service.py       # Geocoding service implementation
│   └── coordinates.json           # Generated coordinates
│
├── final/                         # Final data processing
│   ├── data_merger.py             # Merges all data into final format
│   └── pakistan_locations.json    # Final structured location data
│
├── lib/                           # Dart implementation
│   ├── models/                    # Dart models for location data
│   │   ├── location.dart          # Base location model
│   │   ├── city.dart              # City model
│   │   └── area.dart              # Area model
│   ├── services/                  # Location-related services
│   └── utils/                     # Utility functions
│
└── README.md                      # Project documentation
```

## Detailed Folder Explanations

### 1. City Folder

- **Purpose**: Initial data collection for Pakistani cities
- **Components**:
  - `scraper.py`: Web scraper that collects city names from reliable sources
  - `cities.json`: Stores the raw list of cities
- **Process**: Uses web scraping to gather an initial list of all major cities in Pakistan.

### 2. City Area Folder

- **Purpose**: Collection of area data for each city
- **Components**:
  - `area_scraper.py`: Scrapes area names for each city
  - `city_areas.json`: Stores area data organized by city
- **Process**: Iterates through cities and collects their respective areas.

### 3. Country Folder

- **Purpose**: Data consolidation
- **Components**:
  - `merged_data.json`: Combines city and area data into a single structure
- **Process**: Merges the collected city and area data into a unified format.

### 4. Geocoding Folder

- **Purpose**: Coordinate generation for locations
- **Components**:
  - `photon_search.py`: Implements Photon 0.7.0 OpenSearch
  - `geocoding_service.py`: Handles coordinate generation
  - `coordinates.json`: Stores generated coordinates
- **Process**:
  1. Uses Photon OpenSearch for bulk geocoding.
  2. Falls back to Google Maps API (limited to 100 requests) for missing coordinates.
  3. Manual coordinate entry for cities not found through automated methods.

### 5. Final Folder

- **Purpose**: Final data processing and structuring
- **Components**:
  - `data_merger.py`: Combines all data into the final format
  - `pakistan_locations.json`: Final structured location dataset
- **Process**: Merges all collected data into a well-structured JSON format.

### 6. Lib Folder (Dart Implementation)

- **Purpose**: Provides easy-to-use Dart models and services
- **Components**:
  - `models/`: Contains Dart classes for location data
  - `services/`: Implements location-related functionality
  - `utils/`: Helper functions and utilities

## Data Flow

1. City data collection (`city/` folder)
2. Area data collection (`city_area/` folder)
3. Initial data merging (`country/` folder)
4. Geocoding process (`geocoding/` folder)
5. Final data structuring (`final/` folder)
6. Dart implementation (`lib/` folder)

## Usage Example

```dart
import 'package:location_info/models/location.dart';

// Initialize the location service
final locationService = LocationService();

// Load all locations
final locations = await locationService.loadLocations();

// Find a specific city
final karachi = await locationService.findCity('Karachi');

// Find areas in a city
final areas = await locationService.findAreasInCity('Karachi');

// Search for a specific area
final clifton = await locationService.findArea('Clifton');
```

## Benefits

- **Cost-Effective**: Eliminates the need for frequent Google Maps API calls.
- **Offline Support**: Works without internet connection.
- **Fast Performance**: Local data access is much faster than API calls.
- **Structured Data**: Well-organized data structure for easy integration.
- **Maintainable**: Easy to update and maintain location information.

## Contributing

Contributions to improve the location dataset are welcome. Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature.
3. Add or update location data.
4. Submit a pull request.

## Data Sources

The location data is compiled from various reliable sources including:

- Official government records
- OpenStreetMap data
- Verified local sources
- Photon OpenSearch dataset
- Google Maps API (limited usage)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For any queries or suggestions, please open an issue in the repository.

## Future Enhancements

- [ ] Add more detailed address information
- [ ] Include postal codes
- [ ] Add landmarks and points of interest
- [ ] Implement search by coordinates
- [ ] Add support for multiple languages
- [ ] Improve geocoding accuracy
- [ ] Add data validation tools
- [ ] Implement automated data updates
