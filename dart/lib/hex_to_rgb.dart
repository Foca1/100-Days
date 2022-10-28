//https://www.codewars.com/kata/5282b48bb70058e4c4000fa7/train/dart

Map<String, int> hexToRGB(String hex) {
  List<String> hexSplited = [
    hex.substring(1, 3),
    hex.substring(3, 5),
    hex.substring(5, 7)
  ];
  var rgb = hexSplited.map((e) => int.parse(e, radix: 16));

  return {'r': rgb.elementAt(0), 'g': rgb.elementAt(1), 'b': rgb.elementAt(2)};
}
