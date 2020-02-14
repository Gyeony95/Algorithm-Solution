package programers;

import java.util.HashMap;

public class 프로그래머스_해시_완주하지못한선수2 {

	public static void main(String[] args) {
		String[] participant = {"mislav", "stanko", "mislav", "ana"};
		String[] completion = {"stanko", "ana", "mislav"};
		
		System.out.println(solution(participant, completion));;//출력
	}
	public static String solution(String[] participant, String[] completion) {
	     String result = "";
		 HashMap<String, Integer> completionHm = new HashMap<String, Integer>();//해시맵선언
		 for(int i =0; i< completion.length; i++) {//완주자를 모두 해시맵에 넣어놓음
			 int count = completionHm.getOrDefault(completion[i], 0);//동명이인 카운트, 해시맵에 완주자가 등록되어있지 않으면 0
			 completionHm.put(completion[i], count+1);//처음등록이면 1 두번째등록이면 2 이렇게 중복체크를해줌
		 }
		 
		 for(int i =0; i < participant.length; i++) {//참가자 길이만큼 반복
			 if(completionHm.getOrDefault(participant[i], 0)== 0) {//완주자목록에 없으면 0을반환하고 그즉시 리턴
				 result = participant[i];
				 return result;
			 }else {//완주자목록에 있을시 동명이인 카운트를 하나씩 줄여가며 다시 put해줌(덮어쓰기)
				 completionHm.put(participant[i], completionHm.get(participant[i])-1);
			 }
		 } 
		 
		 return result;
	 }
	
	
}
