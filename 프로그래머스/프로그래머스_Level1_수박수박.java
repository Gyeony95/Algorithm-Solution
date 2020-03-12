package programers;

public class 프로그래머스_Level1_수박수박 {

	public static void main(String[] args) {
	   
		
	}
	 public String solution(int n) {
	     String answer = "";
		 for(int i =0; i < n; i ++) {
			 if(i%2 == 0) {
				 answer = answer+"수";
			 }else {
				 answer = answer+"박";
				}
		 }
		 
	    
	      return answer;
	  }



}
