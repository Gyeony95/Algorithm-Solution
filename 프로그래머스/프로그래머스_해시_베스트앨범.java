package programers;

import java.awt.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.Hashtable;
import java.util.Set;

import javax.swing.text.html.HTMLDocument.Iterator;

import com.sun.javafx.collections.MappingChange.Map;

//�ּ� : https://programmers.co.kr/learn/courses/30/lessons/42579


public class ���α׷��ӽ�_�ؽ�_����Ʈ�ٹ� {

	public static void main(String[] args) {
		String[] genres = { "pop", "pop", "asd", "pop", "classic", "pop", "asd" };
		int[] plays = { 5000, 5000, 4000, 500011, 123456, 5000, 4000 };

		int[] arr = solution(genres, plays);

		for (int i = 0; i < arr.length; i++) {
			System.out.println(arr[i]);
		}
	}

	static HashMap<String, Integer> baseHm = new HashMap<String, Integer>();// �ؽøʼ���
	static HashMap<String, Integer> firstHm = new HashMap<String, Integer>();// �� ī�װ��� ���� ū��
	static HashMap<String, Integer> secondHm = new HashMap<String, Integer>();// ��ī�װ��� �ι����� ū��
	static HashMap<Integer, Integer> indexHm = new HashMap<Integer, Integer>();// �ε��� ���� ��ġ
	static HashMap<Integer, Integer> subIndexHm = new HashMap<Integer, Integer>();// �ε��� ���� ��ġ

	public static int[] solution(String[] genres, int[] plays) {

		String[] genresList = new String[genres.length]; // �ִ밹���� �帣�� ���̸�ŭ �迭����
		int k = 0;// �帣����Ʈ�� �ε����������� �帣�� ���� ����

		// �� ���Ƚ���� ���° �ε����� �ִ���
		for (int i = 0; i < plays.length; i++) {// �ε��� ������ġ �ؽøʿ� ����
			if (indexHm.getOrDefault(plays[i], -1) == -1) {// ó����
				indexHm.put(plays[i], i);//�׳� ���ڸ��� ����
			} else {// �ش��ϴ� ����� ���� ���°� ó���� �ƴϸ�
				indexSet(indexHm.get(plays[i]), i);//���� �����ڸ��� ã�������� ����Լ��� ����
			}
		}

		for (int i = 0; i < genres.length; i++) {
			// baseHm������ �� ī�װ��� ��������� ���� �� ����
			if (baseHm.getOrDefault(genres[i], -1) == -1) {// ó������ ���϶�
				baseHm.put(genres[i], plays[i]);
				genresList[k] = genres[i];// �帣�� �ߺ����� �迭�� ��
				k++;
			} else {// ó������ ���� �ƴҶ�
				baseHm.put(genres[i], baseHm.get(genres[i]) + plays[i]);// ����� �� ���ؼ� �����
			}
			// �Ʒ� ���ǹ��� ���� �� ī�װ��� ù��°�� ū ���� �ι�°�� ū ���� ���� �� ����
			if (firstHm.getOrDefault(genres[i], -1) == -1) {// �۽�Ʈ�ؽø� ó��
				firstHm.put(genres[i], plays[i]);
			} else {// ó�� �ƴҶ�
				if (firstHm.get(genres[i]) > plays[i]) {// ���ε��°����� ������ �ִ� ���� Ŭ��
					if (secondHm.getOrDefault(genres[i], -1) == -1) {// �������ؽø� ó��
						secondHm.put(genres[i], plays[i]);
					} else {// ������ �ؽøʵ� ó�� �ƴҶ�
						if (secondHm.get(genres[i]) >= plays[i]) {// ���� ���°����� ������ �ִ����� Ŭ��

						} else {// ���ε��°��� �� Ŭ��
							secondHm.put(genres[i], plays[i]);
						}
					}
				} else if (firstHm.get(genres[i]) == plays[i]) {// �������� ������
					secondHm.put(genres[i], plays[i]);// �����忡 �־����
				} else {// ������ �ִ� ������ ���ε��°��� Ŭ��
					secondHm.put(genres[i], firstHm.get(genres[i]));// ù��°�� �ִ� ���� �ι�°�� �ű��
					firstHm.put(genres[i], plays[i]);// ���ε��� ���� ù��°�� �־���
				}
			}
		}

		// baseHm�� �ִ� Ű���� value�� �� ������� ������
		ArrayList<String> keySetList = new ArrayList<>(baseHm.keySet());
		Collections.sort(keySetList, (o1, o2) -> (baseHm.get(o2).compareTo(baseHm.get(o1))));

		int[] answer = new int[k * 2];//�ӽ÷� �� �迭�� ���信 ����� �迭�� ���� �����
		for (int i = 0; i < k * 2; i++) {//�ϴ� ���� �񱳸����� �迭 ���ο� ���̰��� -1�� �־���
			answer[i] = -1;
		}

		for (String key : keySetList) {//������ ������ ArrayList�� ���������� �ݺ���
			for (int i = 0; i < k * 2; i++) {
				if (answer[i] == -1) {// ���ε�������ǹ�
					answer[i] = indexHm.get(firstHm.get(key));
					for (int j = 0; j < i; j++) {
						if (answer[j] == indexHm.get(firstHm.get(key))) {
							answer[i] = subIndexHm.get(indexHm.get(firstHm.get(key)));
							break;
						}
					}
					if (indexHm.getOrDefault(secondHm.get(key), -1) != -1) {// Ű������ �ι�° ū���� �ִٸ�
						i++;
						answer[i] = indexHm.get(secondHm.get(key));// �����ε����� �ι�°�� ū�������� �ε����� �־���
						for (int j = 0; j < i; j++) {
							if (answer[j] == indexHm.get(secondHm.get(key))) {
								answer[i] = subIndexHm.get(indexHm.get(secondHm.get(key)));
								break;
							}
						}
						break;
					} else {
						break;
					}
				}
			}

		}
		int realLength = 0;//���� ������ �迭�� �� ũ��
		for (int i = 0; i < k * 2; i++) {//�ӽù迭answer���� ���̷� �־���� -1���� ������ ���̸� ����
			if (answer[i] == -1) {
				break;
			} else {
				realLength++;
			}
		}

		int[] realanswer = new int[realLength];//���� ������̸�ŭ�� �迭����
		for (int i = 0; i < realanswer.length; i++) {
			realanswer[i] = answer[i];//���� �־���
		}

		return realanswer;
	}

	public static void indexSet(int key, int value) {//����Լ�
		if (subIndexHm.getOrDefault(key, -1) == -1) {//Ű�ε��°ɷ� get������ -1�� ���ϵǸ� ����ִٴ��ǹ�
			subIndexHm.put(key, value);//��������� put��
		} else {//�����������
			indexSet(subIndexHm.get(key), value);//Ű�� ���ºκ��� ���� �ƴ϶�� ���� �ƴѰ� Ű������ �ٽ� indexSet ȣ����, value�� ����
		}
	}

}
