public class Exp3 {

    private static final String[] CORPUS = {
            "The quick brown fox jumps over the lazy dog",
            "A fast blue hedgehog runs quickly",
            "The cat is running after the mouse"
    };

    private static final String[] WORDS = {
            "the", "a", "quick", "brown", "fast", "blue", "lazy",
            "fox", "dog", "hedgehog", "cat", "mouse",
            "jumps", "runs", "running", "after", "is", "over", "quickly"
    };
    private static final String[] TAGS = {
            "DT", "DT", "JJ", "JJ", "JJ", "JJ", "JJ",
            "NN", "NN", "NN", "NN", "NN",
            "VBZ", "VBZ", "VBG", "IN", "VBZ", "IN", "RB"
    };

    private static final String[] STOCHASTIC_WORDS = {
            "the", "quick", "brown", "fox", "jumps"
    };
    private static final String[][] STOCHASTIC_TAGS = {
            { "DT" }, { "JJ" }, { "JJ" }, { "NN" }, { "VBZ" }
    };

    public static String ruleBasedTagWord(String word) {
        for (int i = 0; i < WORDS.length; i++) {
            if (word.equalsIgnoreCase(WORDS[i])) {
                return TAGS[i];
            }
        }
        return "NN";
    }

    public static String stochasticTagWord(String word) {
        for (int i = 0; i < STOCHASTIC_WORDS.length; i++) {
            if (word.equalsIgnoreCase(STOCHASTIC_WORDS[i])) {
                return STOCHASTIC_TAGS[i][0];
            }
        }
        return "NN";
    }

    public static void tagSentence(String sentence, boolean useRuleBased) {
        String[] words = sentence.split(" ");
        for (String word : words) {
            System.out.print(word + "/" + (useRuleBased ? ruleBasedTagWord(word) : stochasticTagWord(word)) + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        System.out.println("Rule-Based Tagger:");
        for (String sentence : CORPUS) {
            tagSentence(sentence, true);
        }

        System.out.println("\nStochastic Tagger:");
        for (String sentence : CORPUS) {
            tagSentence(sentence, false);
        }
    }
}
