package com.oopjava;

public class Heart extends Organ {
  private int bpm;
  private String medicalCondition;

  public Heart(String name, String medicalCondition, int bpm) {
    super(name, medicalCondition);
    this.medicalCondition = medicalCondition;
    this.bpm = bpm;
  }
  public void getDetails() {
    System.out.println("current bpm:" + this.bpm);
    System.out.println("medical Condition:" + this.medicalCondition);
    System.out.println("\t1. Set bpm");
  }
  public void setBpm(int bpm) {
    this.bpm = bpm;
  }

  public int getBpm() {
    return bpm;
  }

  public void setMedicalCondition(String medicalCondition) {
    this.medicalCondition = medicalCondition;
  }

  public String getMedicalCondition() {
    return medicalCondition;
  }
}
