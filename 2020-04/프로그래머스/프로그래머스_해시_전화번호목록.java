package programers;

import java.util.HashMap;
import java.util.Hashtable;
import java.util.Set;

import javax.swing.text.html.HTMLDocument.Iterator;

//주소 : https://programmers.co.kr/learn/courses/30/lessons/42577

public class 프로그래머스_해시_전화번호목록 {

	public static void main(String[] args) {

	}

	public boolean solution(String[] phone_book) {
		boolean answer = true;
		mLabel:
		for(int i = 0; i <phone_book.length; i++) {
			for(int j = i; j < phone_book.length; j++) {// j를 i로 설정함 왜냐하면 아래 이프문에서 두번 비교해줄거기 때문
				if(i != j) {
					if(phone_book[i].startsWith(phone_book[j]) || phone_book[j].startsWith(phone_book[i])) {
						//phone_book[i]가 phone_book[j]의 접두어일때와 그 반대일때를 체크해줌
						answer = false;
						break mLabel;//false판정이 났으면 break label을 통해 포문 두개를 한번에 빠져나감 
					}
				}
			}
		}
		return answer;
	}
}
