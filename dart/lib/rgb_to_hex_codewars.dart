//https://www.codewars.com/kata/513e08acc600c94f01000001/train/dart

import 'package:convert/convert.dart';

String rgb(int r, int g, int b) {
  r = r.clamp(0, 255);
  g = g.clamp(0, 255);
  b = b.clamp(0, 255);
  return hex.encode([r, g, b]).toUpperCase();
}
