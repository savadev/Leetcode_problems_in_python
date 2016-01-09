/*
Check if the two strings are anagram
This is an efficient approach but not the best
Create a 26 size array 
For each character in S, increment the count of the character  by 1
The character postion can be get if u subtract it from 'a' 

Now for each character in t, decrement the count of the character by 1

In the end if all the postions of the interger array is 0 it is a anagram
*/
public class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }
        else if(s.length() == 0 && t.length() == 0){
            return true;
        }
        
        int[] count = new int[26];
        for(int i =0;  i < s.length(); i++){
            count[s.charAt(i) - 'a']++;
            count[t.charAt(i) - 'a']--;
        }
        for(int x: count){
            if(x != 0){
                return false;
            }
        }
        

        return true;
    }
}
