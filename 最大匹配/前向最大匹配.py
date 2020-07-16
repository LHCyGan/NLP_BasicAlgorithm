# -*- encoding:utf-8 -*-
# author: liuheng


class ForwardSearch:

    def __init__(self, filename1: "训练语料", filename2: "测试语料", filename3: "生成结果", MAX_LEN):
        self.file1 = filename1
        self.file2 = filename2
        self.file3 = filename3

        self.max_len = MAX_LEN

    def _get_dic(self):
        # TODO: 读取文本返回词典列表
        with open(self.file1, 'r', encoding='utf8') as f:
            try:
                file_content = f.read().split()
            finally:
                f.close()
        chars = list(set(file_content))
        return chars

    def _read_file(self):
        dic = self._get_dic()

        h = open(self.file3, 'w', encoding='utf8')
        with open(self.file2, 'r', encoding='utf8') as f:
            lines = f.readlines()
        # 分别对每行做正向最大匹配
        for line in lines:
            my_list = []
            len_hang = len(line)
            while len_hang > 0:
                tryWord = line[0:self.max_len]
                while tryWord not in dic:
                    if len(tryWord) == 1:
                        break
                    tryWord = tryWord[0:len(tryWord)-1]
                my_list.append(tryWord)
                line = line[len(tryWord):]
                len_hang = len(line)
            # 将分词写入生成文件
            for t in my_list:
                if t == '\n':
                    h.write(t)
                else:
                    h.write(t + '\n')
        h.close()


if __name__ == '__main__':
    fs = ForwardSearch()