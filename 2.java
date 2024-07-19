import java.util.Scanner;
   public class MonoalphabeticCipher {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the plaintext:");
        String plaintext = scanner.nextLine().toLowerCase();
        System.out.println("Enter the cipher key (26 unique lowercase letters):");
        String cipherKey = scanner.nextLine().toLowerCase();
        String ciphertext = encrypt(plaintext, cipherKey);
        System.out.println("Encrypted Text: " + ciphertext);
        int[] frequencies = new int[26];
        for (char c : ciphertext.toCharArray()) {
            if (c >= 'a' && c <= 'z') {
                frequencies[c - 'a']++;
            }
        }
        System.out.println("Frequency of each letter:");
        for (int i = 0; i < 26; i++) {
            System.out.println((char) (i + 'a') + ": " + frequencies[i]);
        }
        scanner.close();
    }
    private static String encrypt(String text, String key) {
        StringBuilder encrypted = new StringBuilder();
        for (char c : text.toCharArray()) {
            if (c >= 'a' && c <= 'z') {
                int originalPosition = c - 'a';
                encrypted.append(key.charAt(originalPosition));
            } else {
                encrypted.append(c);  
            }
        }
        return encrypted.toString();
    }
}
