package baekjoon;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

//���� : ���ڿ� S�� �־����� ��, SHA-256 �ؽð��� ���ϴ� ���α׷��� �ۼ��Ͻÿ�.
//�Է� : ù° �ٿ� ���ڿ� S�� �־�����. S�� ���ĺ� �빮�ڿ� �ҹ���, �׸��� ���ڷθ� �̷���� ������, ���̴� �ִ� 50�̴�.

public class beakjoon10930_SHA256 {

	public static void main(String[] args) {
		System.out.println(testMD5("Baekjoon"));;
		
	}
	
	public static String testMD5(String str){

		String MD5 = ""; 

		try{

			MessageDigest md = MessageDigest.getInstance("MD5"); 
			md.update(str.getBytes()); 
			byte byteData[] = md.digest();
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

