import os


def main():
    res =[]
    for root, dirs, files in os.walk('.'):
        if 'seq.in' in files:
            with open(os.path.join(root, 'seq.in')) as data_file, \
                    open(os.path.join(root, 'seq.out')) as label_file:
                data_lines = data_file.readlines()
                label_lines = label_file.readlines()
                cnt = 0
                count=1
                for data, label in zip(data_lines, label_lines):
                    data_sep = data.strip().split()
                    label_sep = label.strip().split()
                    if len(data_sep) != len(label_sep):
                        cnt += 1
                        res.append(count)
                    count+=1
                    
                if cnt:
                    print(root, cnt, sep='\n')
                    print(set(res))
                else:
                    print("all correct! congratulations!")


if __name__ == '__main__':
    main()
