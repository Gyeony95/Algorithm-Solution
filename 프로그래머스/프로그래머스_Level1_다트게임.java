package programers;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class ���α׷��ӽ�_Level1_��Ʈ���� {
	// static BufferedReader reader = new BufferedReader(new
	// InputStreamReader(System.in));
	static StringTokenizer token;

	public static void main(String[] args) throws IOException {

		System.out.println(solution("1S*10D*3S*"));
		

	}

	public static int solution(String dartResult) throws IOException {
		token = new StringTokenizer(dartResult);

		int answer = 0;
		int lastScore = 0;
		int currentScore = 0;
		char[] ch = token.nextToken().toCharArray();
		
		
		for (int i = 0; i < ch.length; i++) {
			
			if(48 <= (int)ch[i] && 57 >=  (int)ch[i]) {
				if((int)ch[i+1] == 48) {//������ 10�϶�
					currentScore = 10;
					i++;
				}else {
					currentScore = (int)ch[i] - 48;//�ش� ���� ����
				}
			}
			
			try {
				if((int)ch[i] == 83) {//�̱�
					if((int)ch[i+1] >= 48 && (int)ch[i+1] <= 57 ) {//�������� ���ڶ��
						answer = answer+currentScore;
						lastScore = currentScore;
					}
					
				}if((int)ch[i] == 68) {//����
					currentScore = currentScore*currentScore;
					if((int)ch[i+1] >= 48 && (int)ch[i+1] <= 57 ) {
						answer = answer+currentScore;
						lastScore = currentScore;
					}
					
				}if((int)ch[i] == 84) {//Ʈ����
					currentScore= currentScore*currentScore*currentScore;
					if((int)ch[i+1] >= 48 && (int)ch[i+1] <= 57 ) {
						answer = answer+currentScore;
						lastScore = currentScore;
					}
					
				}if((int)ch[i] == 35) {//#
					currentScore = currentScore*-1;
					answer = answer + currentScore;
					lastScore = currentScore;

				}if((int)ch[i] == 42) {//*
					answer += lastScore;
					currentScore = currentScore*2;
					answer = answer + currentScore;
					lastScore = currentScore;
				}
				
				
			}catch(Exception e) {
				answer += currentScore;
				return answer;
			}
			
			System.out.println("currentScore1  "+currentScore);
			System.out.println("answer1  "+answer);

		}

		return answer;
	}

}
