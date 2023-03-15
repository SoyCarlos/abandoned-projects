import 'package:flutter/cupertino.dart';
import 'styles.dart';
import 'bills_tab.dart';
import 'chores_tab.dart';
import 'pantry_tab.dart';

class RoomiesApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return CupertinoApp(
      home: RoomiesChoresPage(),
    );
  }
}

class RoomiesChoresPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return CupertinoTabScaffold(
      tabBar: CupertinoTabBar(
        items: const <BottomNavigationBarItem>[
          BottomNavigationBarItem(
            icon: Icon(CupertinoIcons.shopping_cart),
            title: Text('Pantry'),
          ),
          BottomNavigationBarItem(
            icon: Icon(CupertinoIcons.delete_simple),
            title: Text('Chores'),
          ),
          BottomNavigationBarItem(
            icon: Icon(CupertinoIcons.group),
            title: Text('Bills'),
          ),
        ],
      ),
      tabBuilder: (context, index) {
        switch (index) {
          case 0:
            return CupertinoTabView(builder: (context) {
              return CupertinoPageScaffold(
                child: PantryTab(),
              );
            });
          case 1:
            return CupertinoTabView(builder: (context) {
              return CupertinoPageScaffold(
                child: ChoresTab(),
              );
            });
          case 2:
            return CupertinoTabView(builder: (context) {
              return CupertinoPageScaffold(
                child: BillsTab(),
              );
            });
        }
      },
    );
  }
}
