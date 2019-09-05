import argparse 
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('a', type = int, help = 'integer')
parser.add_argument('b', type = int, help = 'integer')
args = parser.parse_args()
print(args.a, args.b)
import math_lib as ml
if __name__ == '__main__':
    X = ml.div(args.a,args.b)
    Y = ml.add(args.a,args.b)
    print(X)
    print(Y)
