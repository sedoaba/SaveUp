import 'package:flutter/material.dart';
import 'package:flutter/src/foundation/key.dart';
import 'package:flutter/src/widgets/framework.dart';

class Login_Screen extends StatefulWidget {
  const Login_Screen({Key? key}) : super(key: key);

  @override
  State<Login_Screen> createState() => _Login_ScreenState();
}

class  _Login_ScreenState extends State<Login_Screen> {
  TextEditingController UserNameController = TextEditingController();
  TextEditingController PasswordController = TextEditingController();
  @override
  Widget build(BuildContext context) {
    return Scaffold(
     appBar: AppBar(
       toolbarHeight: 200,
       flexibleSpace: Container(
        color: Colors.purple[900],
          child: Column(
           children:  const [Text('Welcome back')],
        ),
        ),
      ),
      body: ListView(
        children: <Widget>[
          Container(
            padding: const EdgeInsets.all(10),
            alignment: Alignment.center,
            child: TextField(
              controller: UserNameController,
              decoration:const  InputDecoration(
                border: InputBorder.none,
                labelText: "User Name",
                hintText: "Enter your User Name",
              ),
            ),
          ),
          Container(
             padding: const EdgeInsets.all(10),
            child: TextField(
              controller: PasswordController,
              obscureText: true,
              decoration: const InputDecoration(
                border: InputBorder.none,
                labelText: "Password",
                hintText: "Enter Password",
              ),
            ),
          ),
          TextButton(onPressed: () {}, child: const Text("Forgot Password")),
          Container(
            color: Colors.purple[900],
            height: 50,
            padding: const EdgeInsets.fromLTRB(10, 0, 10, 0),
            child: ElevatedButton(onPressed: () {}, child:const Text("Login")),
          ),
          Row(
            children: [
              const Text("Do not have an account?"),
              ElevatedButton(onPressed: () {}, child: Text("SignUp"))
            ],
          )
        ],
      ),
    );
  }
}
