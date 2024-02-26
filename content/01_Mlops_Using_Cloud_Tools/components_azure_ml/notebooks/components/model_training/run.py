import numpy as np 
import mlflow
from sklearn.linear_model import LogisticRegression
import os
from argparse import ArgumentParser

# Start Logging
mlflow.start_run()

# enable autologging
mlflow.sklearn.autolog()

os.makedirs("./outputs", exist_ok=True)

def main():
    print("Start")
    parser = ArgumentParser()
    parser.add_argument("--train",type=str,help="Path to train data")
    parser.add_argument("--test",type=str,help="Path to test data")
    parser.add_argument("--model_name",type=str,help="Name of the model")
    parser.add_argument("--model",type=str,help="Path to trained model")
    args = parser.parse_args()
    X_train = np.load(os.path.join(args.train,"X_train.npy"))
    X_test = np.load(os.path.join(args.test,"X_test.npy"))
    y_train = np.load(os.path.join(args.train,"y_train.npy"))
    y_test = np.load(os.path.join(args.test,"y_test.npy"))
    clf = LogisticRegression()
    clf.fit(X_train,y_train)
    y_pred = clf.predict(X_test)
    mlflow.sklearn.log_model(
        sk_model=clf,
        registered_model_name=args.model_name,
        artifact_path=args.model_name,
    )

    # Saving the model to a file
    mlflow.sklearn.save_model(
        sk_model=clf,
        path=os.path.join(args.model, "trained_model"),
    )

    # Stop Logging
    mlflow.end_run()

if __name__=="__main__":
    main()