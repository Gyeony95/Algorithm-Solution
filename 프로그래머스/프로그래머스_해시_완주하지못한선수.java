package programers;

import java.util.Arrays;

public class ���α׷��ӽ�_�ؽ�_�����������Ѽ��� {

	public static void main(String[] args) {
		String[] dsad = {"marina", "josipa", "nikola", "vinko", "filipa"};
		String[] asdasdas = {"josipa", "filipa", "marina", "nikola"};
		
		System.out.println(solution(dsad, asdasdas));;
	}
	public static String solution(String[] participant, String[] completion) {
	      Arrays.sort(participant);//������������
	      Arrays.sort(completion);//������������
	        String result = "";
	            for(int i =0; i <completion.length; i++ ){//������ ���̸�ŭ �ݺ�
	                if(completion[i].equals(participant[i])){
	                    
	                }else{//���ĵǾ��⶧���� �ι迭�� ���� �ε����� �ٸ����� ������ �������� ���� �����
	                    result = participant[i];
	                    break;
	                }
	            }
	        if(result.equals("")){
	            result = participant[completion.length];
	        }         
	            return result;
	    }
	
	
}
