class Solution {
    public int solution(int n) {
        int sum = 0;
        if(isOdd(n)) { // 매개변수가 홀수라면
            for(int i=1; i<=n; i++) {
                if(isOdd(i))
                    sum += i; // 홀수인 모든 양의 정수를 더한다
                else
                    continue;
            }
        }
        else { // 매개변수가 짝수라면 
            for(int i=0; i<=n; i++) {
                if(!isOdd(i)) 
                    sum += i*i; //짝수인 제곱의 합을 더함
                else
                    continue;
            }
        }
        return sum;
    }
    public static boolean isOdd(int num) {
        return ( (num%2 == 0) ? false : true );
    }
}