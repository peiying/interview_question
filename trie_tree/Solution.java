package peiying.com;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {
    private TrieNode root;
    private List<String> wordList;
    public Solution() {
        root = new TrieNode();
    }
    public void addWord(String word) {
        root.addWord(word.toLowerCase());
    }
    public List<String> getWords() {
        TrieNode temp = root.getNode("b", root);
        wordList = root.getWords(temp, "");
        return wordList;
    }
    public static void main(String[] args) {
        Solution s = new Solution();
        s.addWord("abce");
        s.addWord("abcd");
        s.addWord("acdfeg");
        s.addWord("bag");
        for (String str : s.getWords()) {
            System.out.println(str);
        }
    }
}

class TrieNode {
    private boolean isWord;
    private boolean hasChildren;
    private char character;
    private Map<Character, TrieNode> children = new HashMap<Character, TrieNode>();
    private List<String> wordList = new ArrayList<String>();
    public TrieNode() {
        hasChildren = false;
        isWord = false;
    }
    public TrieNode(String word) {
        this();
        addWord(word);
    }
    public void addWord(String word) {
        if (word == null || word.length() == 0)
            return;
        char firstChar = word.charAt(0);
        if (!children.containsKey(firstChar)) {
            this.hasChildren = true;
            if (word.length() > 1) {
                TrieNode tn = new TrieNode();
                children.put(firstChar, tn);
                children.get(firstChar).addWord(word.substring(1));
            }
            else {
                children.put(firstChar, new TrieNode());
                children.get(firstChar).isWord = true;
            }
            children.get(firstChar).character = firstChar;
        }

        else if (word.length() > 1) {
            children.get(firstChar).addWord(word.substring(1));
        } else {
            children.get(firstChar).isWord = true;
            children.get(firstChar).addWord(word.substring(1));
        }

    }

    public TrieNode getNode(String s, TrieNode node) {
        if (s == null || s.length() == 0) {
            return node;
        }
        char temp = s.charAt(0);
        if (node.children.containsKey(temp)) {
            return getNode(s.substring(1), node.children.get(temp));
        }
        return null;
    }
    public List<String> getWords(TrieNode node, String chars) {
        chars += node.character;
        if (node.isWord) {
            wordList.add(chars.trim());
        }
        if (node.hasChildren) {
            for (Character c : node.children.keySet()) {
                getWords(node.children.get(c), chars);
            }
        }
        else {
            chars = "";
        }
        Collections.sort(wordList);
        return wordList;
    }
}
