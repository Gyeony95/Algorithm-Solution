package programers;

import java.util.HashMap;

public class ���α׷��ӽ�_�ؽ�_�����������Ѽ���2 {

	public static void main(String[] args) {
		String[] participant = {"mislav", "stanko", "mislav", "ana"};
		String[] completion = {"stanko", "ana", "mislav"};
		
		System.out.println(solution(participant, completion));;//���
	}
	public static String solution(String[] participant, String[] completion) {
	     String result = "";
		 HashMap<String, Integer> completionHm = new HashMap<String, Integer>();//�ؽøʼ���
		 for(int i =0; i< completion.length; i++) {//�����ڸ� ��� �ؽøʿ� �־����
			 int count = completionHm.getOrDefault(completion[i], 0);//�������� ī��Ʈ, �ؽøʿ� �����ڰ� ��ϵǾ����� ������ 0
			 completionHm.put(completion[i], count+1);//ó������̸� 1 �ι�°����̸� 2 �̷��� �ߺ�üũ������
		 }
		 
		 for(int i =0; i < participant.length; i++) {//������ ���̸�ŭ �ݺ�
			 if(completionHm.getOrDefault(participant[i], 0)== 0) {//�����ڸ�Ͽ� ������ 0����ȯ�ϰ� ����� ����
				 result = participant[i];
				 return result;
			 }else {//�����ڸ�Ͽ� ������ �������� ī��Ʈ�� �ϳ��� �ٿ����� �ٽ� put����(�����)
				 completionHm.put(participant[i], completionHm.get(participant[i])-1);
			 }
		 } 
		 
		 return result;
	 }
	
	
}
