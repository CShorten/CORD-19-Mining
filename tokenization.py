def build_topK_Dicts(df, df_text_col_name):
	import nltk
	nltk.download('punkt');
	from nltk.tokenize import word_tokenize

	freq_counter = {}
	for i in df[df_text_col_name]:
		tok_seq = word_tokenize(i)
		for tok in tok_seq:
			if tok in freq_counter.keys():
				freq_counter[tok] += 1
			else:
				freq_counter[tok] = 1

	import operator
	sorted_dict = sorted(freq_counter.items(),
		key=operator.itemgetter(1))

	top_K_list = sorted_dict[-29_999:]

	text_index_dict = {}
	index_text_dict = {}

	counter = 1 # save 0 for padding

	for i in range(len(top_K_list)):
		text_index_dict[top_K_list[i][0]] = counter
		index_text_dict[counter] = top_K_list[i][0]
		counter += 1

	index_text_dict[30_000] = "Unknown"

	return text_index_dict, index_text_dict

def text_to_index(seq, text_index_dict):
	import nltk
	nltk.download('punkt')
	from nltk.tokenize import word_tokenize

	idx_list = []
	tok_list = word_tokenize(seq)
	for tok in tok_lst:
		if tok not in text_index_dict.keys():
			idx_list.append(30_000)
		else:
			idx_list.append(text_index_dict[tok])
	return idx_list

def index_to_text(idx_list, index_text_dict):
	word = ""
	for idx in idx_list:
		word += index_text_dict[idx]
		word += " "
	return word
