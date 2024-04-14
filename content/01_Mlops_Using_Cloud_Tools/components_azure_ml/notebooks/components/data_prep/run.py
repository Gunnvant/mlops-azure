import pandas as pd 
from sklearn.model_selection import train_test_split
import numpy as np
from argparse import ArgumentParser
import os


def main():
    print("Start")
    parser = ArgumentParser()
    parser.add_argument("--train_data",type=str,help="path to train data")
    parser.add_argument("--train",type=str,help="path of train data")
    parser.add_argument("--test",type=str,help="path of test data")
    args = parser.parse_args()
    train_df = pd.read_csv(args.train_data)
    y = train_df['price_range'].values
    X = train_df.drop('price_range',axis=1).values 
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)
    np.save(os.path.join(args.train,"X_train.npy"),X_train)
    np.save(os.path.join(args.test,"X_test.npy"),X_test)
    np.save(os.path.join(args.train,"y_train.npy"),y_train)
    np.save(os.path.join(args.test,"y_test.npy"),y_test)
if __name__=="__main__":
    main()