package com.encryptioner;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        System.out.print("do you want to encrypt/decrypt?:");
        String answer = reader.nextLine();
        if (answer.equals("encrypt")) {
            System.out.print("enter file to encrypt:");
            String file = reader.nextLine();
            System.out.println(file);
            System.out.print("enter key:");
            int key = reader.nextInt();
            reader.nextLine();
            System.out.print("enter encryption output:");
            String output = reader.nextLine();
            try {
                BufferedReader filereader = new BufferedReader(new FileReader(file));
                String tempstr;
                String finalstr = "";
                while ((tempstr = filereader.readLine()) != null) {
                    finalstr += tempstr + "\n";
                }
                encrypt(finalstr.toCharArray(), key, output);
                filereader.close();
            } catch (FileNotFoundException e) {
                System.out.println("file not found");
            } catch (IOException e) {
                System.out.println("IO exception");
            }
        } else if (answer.equals("decrypt")) {
            System.out.print("enter file to decrypt:");
            String file = reader.nextLine();
            System.out.println(file);
            System.out.print("enter key:");
            int key = reader.nextInt();
            reader.nextLine();
            System.out.print("enter decryption output:");
            String output = reader.nextLine();
            try {
                BufferedReader filereader = new BufferedReader(new FileReader(file));
                String tempstr;
                String finalstr = "";
                while ((tempstr = filereader.readLine()) != null) {
                    finalstr += tempstr + "\n";
                }
                decrypt(finalstr.toCharArray(), key, output);
                filereader.close();
            } catch (FileNotFoundException e) {
                System.out.println("file not found");
            } catch (IOException e) {
                System.out.println("IO exception");
            }
        }
        reader.close();
    }

    public static void encrypt(char[] chars, int key, String out) throws IOException {
        for (int i = 0; i < chars.length; i++) {
            chars[i] += key;
        }
        BufferedWriter writer = new BufferedWriter(new FileWriter(out));
        writer.write(chars);
        writer.close();
    }

    public static void decrypt(char[] chars, int key, String out) throws IOException {
        for (int i = 0; i < chars.length; i++) {
            chars[i] -= key;
        }
        BufferedWriter writer = new BufferedWriter(new FileWriter(out));
        writer.write(chars);
        writer.close();
    }
}
