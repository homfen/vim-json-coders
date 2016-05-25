import sys
import json
import codecs

def main():
    infile = codecs.getreader('utf-8')(sys.stdin)
    outfile = codecs.getwriter('utf-8')(sys.stdout)
    with infile:
        try:
            obj = json.load(infile)
        except ValueError, e:
            raise SystemExit(e)
    with outfile:
        json.dump(obj, outfile, sort_keys=True, separators=(',', ': '), ensure_ascii=False)
        outfile.write('\n')

if __name__ == '__main__':
    main()
