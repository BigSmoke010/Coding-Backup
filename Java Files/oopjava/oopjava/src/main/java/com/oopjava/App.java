package com.oopjava;

import java.util.Scanner;

public class App {
  public static void main(String[] args) {
    Human jack = new Human("jack", 12, new Eye("Left Eye", "10/10", "Blue"), new Eye("Right Eye","8/10", "Blue"), new Heart("Heart", "good", 50));
    Scanner reader = new Scanner(System.in);
    int answer = 0;
    while (answer != 6) {
      System.out.println("Name: " + jack.getName());
      System.out.println("Age: " + jack.getAge());
      System.out.println("\t1. Left eye");
      System.out.println("\t2. Right eye");
      System.out.println("\t3. Heart");
      System.out.println("\t6. Quit");
      answer = reader.nextInt();
      if (answer == 1) {
        jack.getLefteye().getDetails();
        int response = reader.nextInt();
        if (response == 1) {
          jack.getLefteye().setClosed(!jack.getLefteye().isClosed());
          if (jack.getLefteye().isClosed()) {
            System.out.println(jack.getLefteye().getName() + " eye closed");
          } else {
            System.out.println(jack.getLefteye().getName() + " eye opened");
          }
        }
      } else if (answer == 2) {
        jack.getRighteye().getDetails();
        int response = reader.nextInt();
        if (response == 1) {
          jack.getRighteye().setClosed(!jack.getRighteye().isClosed());
          if (jack.getRighteye().isClosed()) {
            System.out.println(jack.getRighteye().getName() + " eye closed");
          } else {
            System.out.println(jack.getRighteye().getName() + " eye opened");
          }
        }
      } else if (answer == 3) {
      jack.getHeart().getDetails();
      int bpmsetter = reader.nextInt();
      if (bpmsetter == 1) {
        System.out.println("\tSet bpm: ");
        bpmsetter = reader.nextInt();
        jack.getHeart().setBpm(bpmsetter);
      }
      }
    }
    reader.close();
  }
}
