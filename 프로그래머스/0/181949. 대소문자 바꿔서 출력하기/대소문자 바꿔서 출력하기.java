import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next(); //문자열 입력
        char[] a_array = a.toCharArray(); //문자 배열로 변환
        
        StringBuilder sb = new StringBuilder();
        for(char c : a_array) {
            if(Character.isUpperCase(c)) {
                sb.append(Character.toLowerCase(c));
            }
            else if (Character.isLowerCase(c)) {
                sb.append(Character.toUpperCase(c));
            }
        }
        System.out.println(sb.toString());
    }
}