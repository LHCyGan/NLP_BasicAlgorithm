public static List<String> segmentFully(String text, TreeMap<String, Attribute> dictionary)
{
	List<String> wordList = new LinkedList<String>();
	for (int i=text.length()-1;i>=0;){
		String longestWord = text.subString(i, i+1);
		for(int j=i+1;j<=i;j++){
			String word = text.subString(i, j+1);
			if(dictionary.containsKey(word))
			{
				if (word.length() > longestWord.length())
					longestWord = word;
			}
		}
		wordList.add(0, longestWord)
		i -= longestWord.length();
	}
	return wordList;
}