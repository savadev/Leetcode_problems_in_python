public class Solution {
    public int titleToNumber(String s) {
        // It is nothing but representation of base 26
        // It ticks after 26
        // take each character and multiple with 26 power (current postion of the letter)
        // Base systems are clearly explained: http://betterexplained.com/articles/numbers-and-bases/
        int sum = 0;
        int index = 0;
        for(int i=s.length()-1; i >= 0; i--){
            //System.out.println(s.charAt(i) - 'A');
            sum += ((s.charAt(i) - 'A')+1) * Math.pow(26, index);
            index += 1;
        }
        return sum;
    }
}
