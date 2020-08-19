package programers;

import java.util.HashMap;
import java.util.Hashtable;
import java.util.Set;

import javax.swing.text.html.HTMLDocument.Iterator;

public class 프로그래머스_해시_위장 {

	public static void main(String[] args) {
		
		String clothes[][] = {{"crow_mask", "headgear"},{"blue_sunglasses", "eyewear"},{"smoky_makeup", "headgear"},{"crow_mask2", "face"}};
		System.out.println(solution(clothes));;
	}
	
	 public static int solution(String[][] clothes) {
		 
		 String arr[] = new String[clothes.length];
		 int k = 0;
	     int answer = 1;

	     HashMap<String, String> ht = new HashMap<String, String>();
		 HashMap<String, Integer> ht2 = new HashMap<String, Integer>();
			for(int a = 0; a <clothes.length; a++) {
				ht.putIfAbsent(clothes[a][1], clothes[a][0]);//들어있는게 없으면 집어넣음
				if(!ht.get(clothes[a][1]).equals(clothes[a][0])) {//이것이 같은 카테고리의 첫번쨰가 아니라면
					ht2.put(clothes[a][1], ht2.get(clothes[a][1])+1);//ht2에도 같은 카테고리의 밸류를 +1해서 덮어씌우고
				}else {//같은카테고리의 첫번쨰라면
					ht2.put(clothes[a][1], 1);//ht2에 카테고리 밸류를 1로 해서 집어넣음
					arr[k] = clothes[a][1];//배열에는 카테고리의 중복되지 않은 이름들이담기고
					k++;//k변수에는 중복하지 않은 카테고리 갯수를 담음
				}
			}
		  for(int i = 0; i <k; i++) {//중복하지 않은 카테고리 갯수만큼 반복
			  answer = answer*(ht2.get(arr[i])+1); 
		  }		
	        return answer-1;
	    }

}
