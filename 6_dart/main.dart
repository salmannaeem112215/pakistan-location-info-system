import 'dart:convert';
import 'dart:io';
import './geocoding_data.dart';
import './model.dart';

late GeocodingData geocodingData;
void main() {
  const filePath = 'geocoding.json';

  try {
    final fileContent = File(filePath).readAsStringSync();
    final jsonData = json.decode(fileContent);
    geocodingData = GeocodingData.fromJson(jsonData);

    // print('\n✅ --- Provinces ---');
    // final provinces = geocodingData.getProvinces();
    // provinces.forEach((province) => print(province));

    // print('\n✅ --- Cities ---');
    // final cities = geocodingData.getCities();
    // cities.forEach((city) => print(city));

    // print('\n✅ --- Areas of a city (Example: Abbottabad) ---');
    // final areas = geocodingData.getAreasByCity("Abbottabad");
    // areas.forEach((area) => print(area));

    // print('\n✅ --- City Search (keyword: abbot) ---');
    // final citySearchResult = geocodingData.citySearch("abbot");
    // citySearchResult.forEach((result) => print(result));

    // print('\n✅ --- Area Search (city: Abbottabad, keyword: heights) ---');
    // final areaSearchResult = geocodingData.areaSearch("Abbottabad", "heights");
    // areaSearchResult.forEach((result) => print(result));

    print('\n✅ --- Nearest Location Search ---');
    nearestLocationSearch(GeoPoint(lat: 34.15, lon: 73.20));
    nearestLocationSearch(
      GeoPoint(lat: 31.534464275533303, lon: 74.29891487834607),
    );
    nearestLocationSearch(
      GeoPoint(lat: 31.53343587733842, lon: 74.30784919455711),
    );
    nearestLocationSearch(
      GeoPoint(lat: 31.536481214903088, lon: 74.31335350022992),
    );
    nearestLocationSearch(GeoPoint(lat: 31.5372527, lon: 74.3040553));
  } catch (e) {
    print('Error: $e');
  }
}

void nearestLocationSearch(GeoPoint point) {
  final nearestLocation = geocodingData.nearestLocationByGeopoint(point);
  if (nearestLocation != null) {
    print(nearestLocation);
  } else {
    print("No nearby location found.");
  }
}
