package programers;

import java.util.HashMap;
import java.util.Hashtable;
import java.util.Set;

import javax.swing.text.html.HTMLDocument.Iterator;

public class ���α׷��ӽ�_�ؽ�_���� {

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
				ht.putIfAbsent(clothes[a][1], clothes[a][0]);//����ִ°� ������ �������
				if(!ht.get(clothes[a][1]).equals(clothes[a][0])) {//�̰��� ���� ī�װ��� ù������ �ƴ϶��
					ht2.put(clothes[a][1], ht2.get(clothes[a][1])+1);//ht2���� ���� ī�װ��� ����� +1�ؼ� ������
				}else {//����ī�װ��� ù�������
					ht2.put(clothes[a][1], 1);//ht2�� ī�װ� ����� 1�� �ؼ� �������
					arr[k] = clothes[a][1];//�迭���� ī�װ��� �ߺ����� ���� �̸����̴���
					k++;//k�������� �ߺ����� ���� ī�װ� ������ ����
				}
			}
		  for(int i = 0; i <k; i++) {//�ߺ����� ���� ī�װ� ������ŭ �ݺ�
			  answer = answer*(ht2.get(arr[i])+1); 
		  }		
	        return answer-1;
	    }

}
