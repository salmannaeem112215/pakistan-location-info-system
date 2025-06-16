import 'dart:math';
import './model.dart';

class GeocodingData {
  final Map<String, List<City>> provinces;

  GeocodingData({required this.provinces});

  factory GeocodingData.fromJson(Map<String, dynamic> json) {
    final provincesMap = <String, List<City>>{};

    json.forEach((province, citiesJson) {
      final validCities =
          (citiesJson as List<dynamic>)
              .map((e) {
                try {
                  return City.fromJson(e);
                } catch (e) {
                  print(e);
                  return null;
                }
              })
              .whereType<City>()
              .toList();

      provincesMap[province] = validCities;
    });

    return GeocodingData(provinces: provincesMap);
  }

  Map<String, dynamic> toJson() {
    final map = <String, dynamic>{};
    provinces.forEach((province, cities) {
      map[province] = cities.map((e) => e.toJson()).toList();
    });
    return map;
  }

  /// ✅ Return list of all provinces
  List<String> getProvinces() {
    return provinces.keys.toList();
  }

  /// ✅ Return list of all cities
  List<String> getCities() {
    return provinces.values
        .expand((cities) => cities.map((c) => c.city))
        .toList();
  }

  /// ✅ Return list of areas by city name
  List<String> getAreasByCity(String cityName) {
    for (var cityList in provinces.values) {
      for (var city in cityList) {
        if (city.city.toLowerCase() == cityName.toLowerCase()) {
          return city.all.map((a) => a.name).toList();
        }
      }
    }
    return [];
  }

  /// ✅ Search cities by keyword
  List<String> citySearch(String keyword) {
    keyword = keyword.toLowerCase();
    return getCities().where((c) => c.toLowerCase().contains(keyword)).toList();
  }

  /// ✅ Search areas by city and keyword
  List<String> areaSearch(String cityName, String keyword) {
    final areas = getAreasByCity(cityName);
    keyword = keyword.toLowerCase();
    return areas.where((a) => a.toLowerCase().contains(keyword)).toList();
  }

  /// ✅ Find nearest location
  LocationModel? nearestLocationByGeopoint(GeoPoint inputPoint) {
    double minCityDist = double.infinity;
    City? nearestCity;
    String? provinceName;

    // Search nearest city
    provinces.forEach((province, cityList) {
      for (var city in cityList) {
        final dist = _distance(inputPoint, city.geoPoint);
        if (dist < minCityDist) {
          minCityDist = dist;
          nearestCity = city;
          provinceName = province;
        }
      }
    });

    if (nearestCity == null || provinceName == null) return null;

    // If city found but no areas
    if (nearestCity!.all.isEmpty) {
      return LocationModel(
        province: provinceName!,
        city: nearestCity!.city,
        area: null,
        geoPoint: nearestCity!.geoPoint,
      );
    }

    // Search nearest area within the city
    double minAreaDist = double.infinity;
    Address? nearestAddress;
    for (var addr in nearestCity!.all) {
      final dist = _distance(inputPoint, addr.geoPoint);
      if (dist < minAreaDist) {
        minAreaDist = dist;
        nearestAddress = addr;
      }
    }

    if (nearestAddress == null) {
      return LocationModel(
        province: provinceName!,
        city: nearestCity!.city,
        area: null,
        geoPoint: nearestCity!.geoPoint,
      );
    }

    return LocationModel(
      province: provinceName!,
      city: nearestCity!.city,
      area: nearestAddress.name,
      geoPoint: nearestAddress.geoPoint,
    );
  }

  /// ✅ Haversine formula for distance calculation
  double _distance(GeoPoint a, GeoPoint b) {
    const R = 6371; // Earth's radius in km
    final dLat = _deg2rad(b.lat - a.lat);
    final dLon = _deg2rad(b.lon - a.lon);
    final lat1 = _deg2rad(a.lat);
    final lat2 = _deg2rad(b.lat);

    final hav =
        sin(dLat / 2) * sin(dLat / 2) +
        sin(dLon / 2) * sin(dLon / 2) * cos(lat1) * cos(lat2);
    final c = 2 * atan2(sqrt(hav), sqrt(1 - hav));
    return R * c;
  }

  double _deg2rad(double deg) => deg * (pi / 180);
}
