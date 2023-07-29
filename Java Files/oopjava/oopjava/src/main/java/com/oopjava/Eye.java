package com.oopjava;

import java.util.Scanner;

public class Eye extends Organ {
  private final String color;
  private boolean closed;
  private final String medicalCondition;
  private final String name;
  public Eye(String name, String medicalCondition, String color) {
    super(name, medicalCondition);
    this.name = name;
    this.medicalCondition = medicalCondition;
    this.color = color;
  }
  public void getDetails() {
    System.out.println("vision:" + this.medicalCondition);
    if (this.closed) {
      System.out.println("1. open eye");
    } else {
      System.out.println("1. close eye");
    }
  }

  public boolean isClosed() {
    return closed;
  }

  public String getMedicalCondition() {
    return medicalCondition;
  }

  public String getName() {
    return name;
  }

  public void setClosed(boolean closed) {
    this.closed = closed;
  }

  public String getColor() {
    return color;
  }
}
