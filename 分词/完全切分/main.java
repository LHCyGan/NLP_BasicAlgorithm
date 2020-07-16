public static List<String> segmentFully(String text, TreeMap<String, Attribute> dictionary)
{
	List<String> wordList = new LinkedList<String>();
	for (int i=0;i<text.length();i++){
		for(int j=i+1;j<=text.length();j++){
			String word = text.subString(i, j);
			if(dictionary.containsKey(word))
				wordList.add(word);
		}
	}
	return wordList;
}