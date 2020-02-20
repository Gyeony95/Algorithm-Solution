package programers;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.StringTokenizer;

public class 프로그래머스_정렬_Level2_가장큰수 {

	public static void main(String[] args) {
		int[] numbers = { 6, 10, 2,20};
		System.out.println(solution(numbers));
	}
	
		public static String solution(int[] numbers) {
			 String answer = "";
		        
		        ArrayList<String> arr = new ArrayList<String>();
		        
		        for(int i=0; i<numbers.length; i++) {
		            arr.add(String.valueOf(numbers[i]));//arraylist에 숫자들 저장
		        }
		     
		        
		        for(int i=0; i<arr.size(); i++) {
		            if(!arr.get(i).equals("0")) {//0이아니라면
		                break;//종료
		            }
		            
		            if(i==arr.size()-1) {
		                return "0";
		            }
		        }
		        
		        Collections.sort(arr, new Comparator<String>() {
		            @Override
		            public int compare(String arg0, String arg1) {
		            	System.out.println("arg1+arg0 : "+arg1+arg0 +"  arg0+arg1 : "+arg0+arg1);
		                return (arg1+arg0).compareTo(arg0+arg1);
		            }
		        });
		        
		      
		                
		        
		        for(int i=0; i<arr.size(); i++) {
		            answer += arr.get(i);
		        }
		        
		        return answer;
	}
	
	

}
