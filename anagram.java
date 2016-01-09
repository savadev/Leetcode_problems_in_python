/*
This program checks if the two strings are anagram. 
If they are , it returns True.
Else False.

Approach:
Two hash tables. One for each string. It contains key as character and value as freq of the character.
If the two hash tables has same keys and frequencies then they are anagrams.
Else they aren't.

Naive approach but still O(N) time.
*/
import java.util.*;
import java.util.Hashtable;
import java.util.Set;
public class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }
        else if(s.length() == 0 && t.length() == 0){
            return true;
        }
        Hashtable<Character, Integer> dict_s = new Hashtable<Character, Integer>();
        Hashtable<Character, Integer> dict_t = new Hashtable<Character, Integer>();
        
        // process s
        for (int i = 0, n = s.length(); i < n; i++) {
            char c = s.charAt(i);
            int count = dict_s.containsKey(c) ? dict_s.get(c) : 0;
            dict_s.put(c, count + 1);
        }
        // process t
        for (int i = 0, n = t.length(); i < n; i++) {
            char c = t.charAt(i);
            int count = dict_t.containsKey(c) ? dict_t.get(c) : 0;
            dict_t.put(c, count + 1);
        }
        
        // Now check the hash tables
        Set<Character> keys = dict_s.keySet();
        for(Character key: keys){
            int t_count = dict_t.containsKey(key) ? dict_t.get(key) : 0;
            if(dict_s.get(key) != t_count){
                return false;
            }
        }
        return true;
    }
}
