import java.util.Random;
import java.util.Scanner;

public class Hangman {
  public static void main(String[] args) {
    System.out.println("Welcome to Hangman!");
    String[] words = {
        "computer", "programming", "software", "algorithm", "internet",
        "database", "java", "python", "javascript", "developer",
        "application", "network", "security", "framework", "variable",
        "function", "interface", "debugging", "operating", "keyboard"
    };
    Scanner reader = new Scanner(System.in);
    Random random = new Random();
    int numOfTries = 5;
    String chosenWord = words[random.nextInt(words.length)];
    String hiddenWord = "";
    for (int i = 0; i < chosenWord.length(); i++) {
      hiddenWord += "_ ";
    }
    String revealedHidden = hiddenWord.replace(" ", "");
    while (!revealedHidden.equals(chosenWord) && numOfTries > 0) {
      System.out.println("You have " + numOfTries + " tries remaining");
      String guess = reader.nextLine();
      String prevHidden = hiddenWord;
      boolean correctGuess = false;
      for (int i = 0; i < chosenWord.length(); i++) {
        if (chosenWord.charAt(i) == guess.charAt(0)) {
          hiddenWord = hiddenWord.substring(0, 2 * i) + guess + hiddenWord.substring(2 * i + 1);
          correctGuess = true;
        }
      }
      if (!correctGuess) {
        numOfTries--;
      }
      System.out.println(hiddenWord);
      revealedHidden = hiddenWord.replace(" ", "");
    }
    if (revealedHidden.equals(chosenWord)) {
      System.out.println("Congratulations! You won!");
    } else {
      System.out.println("Sorry, you lost. The word was: " + chosenWord);
    }
    reader.close();
  }
}
