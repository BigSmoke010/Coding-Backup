import java.util.HashMap;
import java.util.Scanner;
import java.util.Random;

public class TicTacToe {
  private static HashMap<String, Character> board = new HashMap<String, Character>();
  static {
    board = new HashMap<String, Character>() {{
        put("tl", ' ');
        put("t", ' ');
        put("tr", ' ');
        put("l", ' ');
        put("m", ' ');
        put("r", ' ');
        put("bl", ' ');
        put("b", ' ');
        put("br", ' ');
    }};
  }
  private static Scanner reader = new Scanner(System.in);
  private static boolean won = false;
  private static Character botcharacter;
  private static Character humanChar;

  public static void main(String[] args) {
    System.out.print("choose your character:");
    humanChar = reader.nextLine().charAt(0);
    botcharacter = botcharpick(humanChar);
    while (won == false) {
      printBoard();
      setXO(humanChar);
      botsetXO(botcharacter);
      if (checkforWinner(humanChar)) {
        System.out.println("you win!");
        won = true;
      }
      if (checkforWinner(botcharacter)) {
        System.out.println("you lose!");
        won = true;
      }
    }
    reader.close();
  }
  private static void printBoard() {
    System.out.println(board.get("tl") + " | " + board.get("t") + " | " + board.get("tr"));
    System.out.println("--+---+--");
    System.out.println(board.get("l") + " | " + board.get("m") + " | " + board.get("r"));
    System.out.println("--+---+--");
    System.out.println(board.get("bl") + " | " + board.get("b") + " | " + board.get("br"));
  }
  private static void botsetXO(Character botchar) {
    String[] possibleChars = {"tl", "t", "tr", "l", "m", "r", "bl", "b", "br"};

    // First, check for winning moves
    for (String position : possibleChars) {
      if (board.get(position) == ' ') {
          board.put(position, botchar);
          if (checkforWinner(botchar)) {
              return; // Bot wins, no need to continue
          }
          board.put(position, ' '); // Undo move
      }
  }

  // Next, check for blocking opponent's winning moves
  for (String position : possibleChars) {
      if (board.get(position) == ' ') {
          board.put(position, humanChar); // Assume opponent's move
          if (checkforWinner(humanChar)) {
              board.put(position, botchar); // Block opponent's winning move
              return;
          }
          board.put(position, ' '); // Undo move
      }
  }

    Random random = new Random();
    String chosenPlace = possibleChars[random.nextInt(possibleChars.length)];
    while (board.get(chosenPlace) != ' ') {
      chosenPlace = possibleChars[random.nextInt(possibleChars.length)];
    }
    board.put(chosenPlace, botchar);
  }
  private static void setXO(Character charact) {
    System.out.print("where to put (tl|t|tr...):");
    String chosenplace = reader.nextLine();
    board.put(chosenplace, charact);
  }
  private static char botcharpick(Character charact) {
    Random random = new Random();
    char chosenCharacter = (char) (random.nextInt(26) + 'A');
    while (chosenCharacter == charact) {
      chosenCharacter = (char) (random.nextInt(26) + 'A');
    }
    return chosenCharacter;
  }
  private static boolean checkforWinner(Character charact) {
    String[] winningConditions = {
      "tl,t,tr", "l,m,r", "bl,b,br", "bl,m,tr",
      "tl,m,br", "t,m,b", "tr,r,br", "tl,l,bl"
    };

    for (String condition : winningConditions) {
      String[] positions = condition.split(",");
      Character firstChar = board.get(positions[0]);
      if (firstChar != ' ' && board.get(positions[1]) == firstChar && board.get(positions[2]) == firstChar) {
        if (firstChar == charact) {
          printBoard();
        return true;
      } else {
        printBoard();

        return false;
      }
      }

    }
    return false;
  }
}

