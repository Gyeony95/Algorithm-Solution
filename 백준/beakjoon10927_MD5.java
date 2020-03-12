package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.StringTokenizer;

//�ؽ�
//https://www.acmicpc.net/problem/10927
//���� : ���ڿ� S�� �־����� ��, MD5 �ؽð��� ���ϴ� ���α׷��� �ۼ��Ͻÿ�.
//�Է� : ù° �ٿ� ���ڿ� S�� �־�����. S�� ���ĺ� �빮�ڿ� �ҹ���, �׸��� ���ڷθ� �̷���� ������, ���̴� �ִ� 50�̴�.

public class beakjoon10927_MD5 {	  
	public static void main(String[] args) throws IOException {
		 BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		 StringTokenizer token = new StringTokenizer(br.readLine());
		System.out.println(testMD5(token.nextToken()));;
	
	}
	public static String testMD5(String str){
		String MD5 = ""; 
		try{
			//MessageDigest �ν��Ͻ� ����
			MessageDigest md = MessageDigest.getInstance("MD5"); //MD5�������� ��ȣȭ �Ѵٴ� �ǹ�
			//�ؽð� ������Ʈ -> ������Ʈ ȣ�� �Ҷ����� MD5���ο� digest���� ���ŵ� ���������� digest()�޼��带 ȣ���ϸ� �� ���� �����ü�����
			md.update(str.getBytes()); 
			byte byteData[] = md.digest();//�� ������
			StringBuffer sb = new StringBuffer(); 
			for(int i = 0 ; i < byteData.length ; i++){
				sb.append(Integer.toString((byteData[i]&0xff) + 0x100, 16).substring(1));
			}
			MD5 = sb.toString();
		}catch(NoSuchAlgorithmException e){
			e.printStackTrace(); 
			MD5 = null; 
		}
		return MD5;
	}

}

