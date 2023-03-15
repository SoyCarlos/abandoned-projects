import 'package:flutter/cupertino.dart';
import 'package:provider/provider.dart';

import 'model/app_state_model.dart';

class BillsTab extends StatefulWidget {
  @override
  _BillsTabState createState() {
    return _BillsTabState();
  }
}

class _BillsTabState extends State<BillsTab> {
  @override
  Widget build(BuildContext context) {
    return Consumer<AppStateModel>(
      builder: (context, model, child) {
        return CustomScrollView(
          slivers: const <Widget>[
            CupertinoSliverNavigationBar(
              largeTitle: Text('Bills'),
            ),
          ],
        );
      },
    );
  }
}
