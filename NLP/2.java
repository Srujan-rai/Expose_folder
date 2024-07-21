/*
 * Find the bigram count for the given corpus. Apply Laplace smoothing and find the bigram probabilities after add-one smoothing (up to 4 decimal places)
 */

public class Exp2 {

     public static int countBigrams(String[] corpus, String word1, String word2) {
        int count = 0;
        for (String sentence : corpus) {
            String[] words = sentence.split(" ");
            for (int i = 0; i < words.length - 1; i++) {
                if (word1.equalsIgnoreCase(words[i]) && word2.equalsIgnoreCase(words[i + 1])) {
                    count++;
                }
            }
        }
        return count;
    }

    public static int countUnigrams(String[] corpus, String word) {
        int count = 0;
        for (String sentence : corpus) {
            for (String w : sentence.split(" ")) {
                if (word.equalsIgnoreCase(w)) {
                    count++;
                }
            }
        }
        return count;
    }

    public static void main(String[] args) {
        String[] corpus = {
                "There is a big garden",
                "Children play in the garden",
                "They play inside beautiful garden"
        };
        String[] testWords = "They play in a big garden".split(" ");
        double probability = 1;
        int vocabularySize = 9;

        for (int i = 0; i < testWords.length - 1; i++) {
            probability *= (double) (countBigrams(corpus, testWords[i], testWords[i + 1]) + 1)
                    / (countUnigrams(corpus, testWords[i]) + vocabularySize);
        }

        System.out.printf("Probability: %.8f%n", probability);
    }
}
