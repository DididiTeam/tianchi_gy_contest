

if __name__ == '__main__':
    with open("../data/mid/etl.data") as f:
        content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    