class Solution {
    public int solution(int a, int b) {
        
        String aStr = String.valueOf(a); // 정수 -> 문자열 변환
        String bStr = String.valueOf(b); // 정수 -> 문자열 변환
        
        String aAndb = aStr + bStr;
        int aa = 2 * a * b;
        return (Integer.parseInt(aAndb) > aa) ? Integer.parseInt(aAndb) : aa;
    
    }
}