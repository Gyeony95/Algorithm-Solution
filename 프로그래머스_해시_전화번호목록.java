package programers;

import java.util.HashMap;
import java.util.Hashtable;
import java.util.Set;

import javax.swing.text.html.HTMLDocument.Iterator;

//�ּ� : https://programmers.co.kr/learn/courses/30/lessons/42577

public class ���α׷��ӽ�_�ؽ�_��ȭ��ȣ��� {

	public static void main(String[] args) {

	}

	public boolean solution(String[] phone_book) {
		boolean answer = true;
		mLabel:
		for(int i = 0; i <phone_book.length; i++) {
			for(int j = i; j < phone_book.length; j++) {// j�� i�� ������ �ֳ��ϸ� �Ʒ� ���������� �ι� �����ٰű� ����
				if(i != j) {
					if(phone_book[i].startsWith(phone_book[j]) || phone_book[j].startsWith(phone_book[i])) {
						//phone_book[i]�� phone_book[j]�� ���ξ��϶��� �� �ݴ��϶��� üũ����
						answer = false;
						break mLabel;//false������ ������ break label�� ���� ���� �ΰ��� �ѹ��� �������� 
					}
				}
			}
		}
		return answer;
	}
}
