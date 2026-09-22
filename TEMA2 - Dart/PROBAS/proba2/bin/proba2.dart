import 'dart:io';
import 'dart:mirrors';
void main() {
  //Definición de variables
  String? nome = null;
  late String apelido;
  nome = "Iago";
  nome = null;
  const cadea = "Lou";
  final data = DateTime.now();
  var _ = 5;

  stdout.write("Introduce o teu nome: ");
  String nom = stdin.readLineSync() ?? "";
  String? nom2 = stdin.readLineSync();

  Object obxeto = "Messi";
  obxeto = 1;
  if (obxeto is String){
    int lonx;
    lonx = obxeto.length;
  }

  dynamic outro = 20;
  bool esPar = (outro as int).isEven;

  String? nulo = null;
  String proba = nulo ?? "Pepe";

  print("Hola $proba. Cuenta ${proba.length}");

  String concatenar = 
  "Hola caracola"
  "Me llamo Messi"
  "El GOAT";

  int numero = int.parse("saf");
  int? numero2 = int.tryParse("sadf");

  (String, int) rexistro = ("Diego", 20);
  print("Rexistro : ${rexistro.$1}");

  ({String nomex, int idadex}) rexistro2 = (nomex: "Iago", idadex: 33);
  print(rexistro2);
  print("Rexistro2: ${rexistro2.nomex} ---- ${rexistro2.idadex}");

}
