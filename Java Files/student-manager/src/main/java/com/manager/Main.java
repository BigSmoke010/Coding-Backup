package com.manager;

import javax.swing.plaf.nimbus.State;
import java.sql.*;
import java.util.ArrayList;
import java.util.Scanner;

/**
 * @author sqlitetutorial.net
 */
public class Main {
  public static Connection connect() throws SQLException {
    Connection connection = DriverManager.getConnection("jdbc:sqlite:./students.db");
    if (connection != null) {
      System.out.println("successfully connected to database!");
      connection.createStatement().execute("CREATE TABLE IF NOT EXISTS students (name TEXT, " +
              "MATHEMATICS INTEGER, SCIENCE INTEGER, ENGLISH INTEGER, HISTORY INTEGER, GEOGRAPHY INTEGER, " +
              "PHYSICS INTEGER, CHEMISTRY INTEGER, BIOLOGY INTEGER, COMPUTER_SCIENCE INTEGER, " +
              "LITERATURE INTEGER, ECONOMICS INTEGER, PSYCHOLOGY INTEGER, SOCIOLOGY INTEGER, " +
              "PHYSICAL_EDUCATION INTEGER)");

      return connection;
    }
    return null;
  }
  public enum Subject {
    MATHEMATICS,
    SCIENCE,
    ENGLISH,
    HISTORY,
    GEOGRAPHY,
    PHYSICS,
    CHEMISTRY,
    BIOLOGY,
    COMPUTER_SCIENCE,
    LITERATURE,
    ECONOMICS,
    PSYCHOLOGY,
    SOCIOLOGY,
    PHYSICAL_EDUCATION
  }
  public static void InsertData(Connection conn, String data) throws SQLException {
    PreparedStatement statement = conn.prepareStatement("INSERT INTO students (name, MATHEMATICS, SCIENCE, ENGLISH, HISTORY, GEOGRAPHY, " +
            "PHYSICS, CHEMISTRY, BIOLOGY, COMPUTER_SCIENCE, LITERATURE, ECONOMICS, PSYCHOLOGY, SOCIOLOGY, PHYSICAL_EDUCATION) " +
            "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)");

    String[] parts = data.split(",");
    String name = parts[0].split(":")[1].strip();
    for (int i = 1; i < parts.length; i++) {
      String[] gradeParts = parts[i].split(":");
      String subject = gradeParts[0].trim();
      int grade = Integer.parseInt(gradeParts[1].trim());
      statement.setInt(getSubjectIndex(Subject.valueOf(subject.toUpperCase())), grade);
    }

    statement.setString(1, name);
    statement.execute();
    System.out.println("Successfully inserted data");
    main_prompt(conn);
  }
  public static int getSubjectIndex(Subject subject) {
    return subject.ordinal() + 2;
  }

  public static Subject getSubjectName(int index) {
    return Subject.values()[index - 2];
  }
  public static double calculateAverage(Connection conn, String studentName) throws SQLException {
    String sql = "SELECT * FROM students WHERE name = ?";
    PreparedStatement statement = conn.prepareStatement(sql);
    statement.setString(1, studentName);
    ResultSet resultSet = statement.executeQuery();

    int totalGrades = 0;
    int gradeCount = 0;
    while (resultSet.next()) {
      for (int i = 2; i <= 15; i++) { // Assuming columns 2 to 15 correspond to the subjects
        int grade = resultSet.getInt(i);
        totalGrades += grade;
        gradeCount++;
      }
    }

    if (gradeCount > 0) {
      return (double) totalGrades / gradeCount;
    } else {
      return 0.0;
    }
  }
  public static void getData(Connection conn, String student_name) throws SQLException {
    if (student_name.equals("")) {
      String sql = "SELECT * FROM students";
      Statement statement = conn.createStatement();
      ResultSet resultSet = statement.executeQuery(sql);

      while (resultSet.next()) {
        String name = resultSet.getString("name");
        System.out.print("Name: " + name + ", ");
        for (int i = 2; i <= 15; i++) {
          Subject subject = getSubjectName(i);
          int grade = resultSet.getInt(subject.name());
          if (grade > 0) {
            System.out.print(subject.name() + ": " + grade + ", ");
          }
        }
      }
    } else if (!student_name.equals("")) {
      String sql = "SELECT * FROM students WHERE name = '" + student_name.strip() + "'";
      Statement statement = conn.createStatement();
      ResultSet resultSet = statement.executeQuery(sql);
      while (resultSet.next()) {
        String name = resultSet.getString("name");
        System.out.print("Name: " + name + ", ");
        for (int i = 2; i <= 15; i++) {
          Subject subject = getSubjectName(i);
          int grade = resultSet.getInt(subject.name());
          if (grade > 0) {
            System.out.print(subject.name() + ": " + grade + ", ");
          }
        }

        System.out.println();
      }
    }
    System.out.println();
    main_prompt(conn);
  }

  public static void deleteData(Connection conn, String name) throws SQLException {
    String sql = "DELETE FROM students WHERE name = '" + name + "'";
    Statement statement = conn.createStatement();
    statement.execute(sql);
    System.out.println("deleted data Successfully");
  }

  public static void main_prompt(Connection connection) throws SQLException {
    Scanner reader = new Scanner(System.in);

    if (connection != null) {
      System.out.print("do you want to get/insert/delete data?:");
      String answer = reader.nextLine().strip();
      if (answer.equals("insert")) {
        System.out.print("please enter student name and grades: ");
        answer = reader.nextLine();
        InsertData(connection, answer);

      } else if (answer.equals("get")) {
        System.out.print("Do you want to get all/search data or calculate average:");
        answer = reader.nextLine();
        if (answer.equals("all")) {
          getData(connection, "");
        } else if (answer.equals("search")) {
          System.out.print("name of student:");
          answer = reader.nextLine();
          getData(connection, answer);
        } else if (answer.equals("calculate")) {
          System.out.print("name of the student:");
          answer = reader.nextLine();
          System.out.println(answer +"'s average is :" + calculateAverage(connection, answer));
        }
      } else if (answer.equals("delete")) {
        System.out.print("name of student to delete:");
        answer = reader.nextLine();
        deleteData(connection, answer);
      }

    }
    reader.close();
  }

  public static void main(String[] args) throws SQLException {
    Connection connection = connect();
    if (connection != null) {
      main_prompt(connection);
    }
  }
}
