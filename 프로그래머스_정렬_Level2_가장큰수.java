package programers;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.StringTokenizer;

public class ���α׷��ӽ�_����_Level2_����ū�� {

	public static void main(String[] args) {
		int[] numbers = { 6, 10, 2,20};
		System.out.println(solution(numbers));
	}
	
		public static String solution(int[] numbers) {
			 String answer = "";
		        
		        ArrayList<String> arr = new ArrayList<String>();
		        
		        for(int i=0; i<numbers.length; i++) {
		            arr.add(String.valueOf(numbers[i]));//arraylist�� ���ڵ� ����
		        }
		     
		        
		        for(int i=0; i<arr.size(); i++) {
		            if(!arr.get(i).equals("0")) {//0�̾ƴ϶��
		                break;//����
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
