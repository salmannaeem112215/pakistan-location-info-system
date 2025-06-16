// GeoPoint Model
class GeoPoint {
  final double lat;
  final double lon;

  GeoPoint({required this.lat, required this.lon});

  factory GeoPoint.fromJson(List<dynamic> json) {
    if (json.length != 2) {
      throw Exception("Invalid geoPoints format");
    }
    return GeoPoint(
      lat: (json[0] ?? 0).toDouble(),
      lon: (json[1] ?? 0).toDouble(),
    );
  }

  List<double> toJson() {
    return [lat, lon];
  }
}

// Address Model
class Address {
  final String name;
  final GeoPoint geoPoint;

  Address({required this.name, required this.geoPoint});

  factory Address.fromJson(Map<String, dynamic> json) {
    final geo = json['geoPoints'];
    if (geo == null || geo is! List || geo.length != 2) {
      throw Exception(
        "Skipping address '${json['name']}' due to invalid geoPoints",
      );
    }
    return Address(name: json['name'], geoPoint: GeoPoint.fromJson(geo));
  }

  Map<String, dynamic> toJson() {
    return {'name': name, 'geoPoints': geoPoint.toJson()};
  }
}

// City Model
class City {
  final String city;
  final GeoPoint geoPoint;
  final List<Address> all;
  final List<String> popular;

  City({
    required this.city,
    required this.geoPoint,
    required this.all,
    required this.popular,
  });

  factory City.fromJson(Map<String, dynamic> json) {
    final geo = json['geoPoints'];
    if (geo == null || geo is! List || geo.length != 2) {
      throw Exception(
        "Skipping city '${json['city']}' due to invalid geoPoints",
      );
    }

    final allAddresses =
        (json['all'] as List<dynamic>?)
            ?.map((e) {
              try {
                return Address.fromJson(e);
              } catch (e) {
                print(e);
                return null;
              }
            })
            .whereType<Address>()
            .toList() ??
        [];

    final popularList =
        (json['popular'] as List<dynamic>?)
            ?.map((e) => e.toString())
            .toList() ??
        [];

    return City(
      city: json['city'],
      geoPoint: GeoPoint.fromJson(geo),
      all: allAddresses,
      popular: popularList,
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'city': city,
      'geoPoints': geoPoint.toJson(),
      'all': all.map((e) => e.toJson()).toList(),
      'popular': popular,
    };
  }
}

class LocationModel {
  final String province;
  final String city;
  final String? area;
  final GeoPoint geoPoint;

  LocationModel({
    required this.province,
    required this.city,
    this.area,
    required this.geoPoint,
  });

  @override
  String toString() {
    return 'LocationModel(province: $province, city: $city, area: $area, geoPoint: (${geoPoint.lat}, ${geoPoint.lon}))';
  }
}
