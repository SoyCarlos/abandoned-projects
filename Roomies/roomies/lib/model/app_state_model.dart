import 'package:flutter/foundation.dart' as foundation;

class AppStateModel extends foundation.ChangeNotifier {
  void loadProducts() {
    notifyListeners();
  }
}
