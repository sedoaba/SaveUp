import 'package:flutter/material.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:saveup/Screens/Login_Screen.dart';
import 'firebase_options.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp(
    options: DefaultFirebaseOptions.currentPlatform,
  );
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'SaveUp',
      theme: ThemeData(
     
      
        primarySwatch: Colors.blue,
      ),
      home: const Login_Screen()
    );
  }
}


