class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        // my_string의 s 이전 부분
        String prefix = my_string.substring(0, s); // "He"
        // 덮어쓸 부분과 연결된 중간 문자열
        String updatedPart = prefix.concat(overwrite_string); // "HelloWorl"
        // 덮어쓰기 이후 남은 부분
        String suffix = my_string.substring(s + overwrite_string.length()); // "d"
        // 최종 결합
        String result = updatedPart + suffix;
        return result;
    }
}
