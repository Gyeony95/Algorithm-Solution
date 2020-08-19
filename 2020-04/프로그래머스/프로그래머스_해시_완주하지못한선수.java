package programers;

import java.util.Arrays;

public class 프로그래머스_해시_완주하지못한선수 {

	public static void main(String[] args) {
		String[] dsad = {"marina", "josipa", "nikola", "vinko", "filipa"};
		String[] asdasdas = {"josipa", "filipa", "marina", "nikola"};
		
		System.out.println(solution(dsad, asdasdas));;
	}
	public static String solution(String[] participant, String[] completion) {
	      Arrays.sort(participant);//오름차순정렬
	      Arrays.sort(completion);//오름차순정렬
	        String result = "";
	            for(int i =0; i <completion.length; i++ ){//완주자 길이만큼 반복
	                if(completion[i].equals(participant[i])){
	                    
	                }else{//정렬되었기때문에 두배열의 같은 인덱스에 다른값이 있으면 완주하지 못한 사람임
	                    result = participant[i];
	                    break;
	                }
	            }
	        if(result.equals("")){
	            result = participant[completion.length];
	        }         
	            return result;
	    }
	
	
}
