import 'dart:io';

void main() {
  final String buf = stdin.readLineSync()!;
  final a = int.parse(buf.split(' ')[0]);
  final b = int.parse(buf.split(' ')[1]);
  print(a + b);  
}