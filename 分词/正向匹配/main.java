public static List<String> segmentFully(String text, TreeMap<String, Attribute> dictionary)
{
	List<String> wordList = new LinkedList<String>();
	for (int i=0;i<text.length();){
		String longestWord = text.subString(i, i+1);
		for(int j=i+1;j<=text.length();j++){
			String word = text.subString(i, j);
			if(dictionary.containsKey(word))
			{
				if (word.length() > longestWord.length())
					longestWord = word;
			}
		}
		wordList.add(longestWord)
		i += longestWord.length();
	}
	return wordList;
}