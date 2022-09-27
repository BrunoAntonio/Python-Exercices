from utils import functions as func

from scikeras.wrappers import KerasClassifier
from keras.utils import plot_model

def result(exercice):
    # get the exercice
    if exercice == "exercice_a":
        test_set = func.test_set_a()
    elif exercice == "exercice_b":
        test_set = func.test_set_b()
        
    # get the data
    X,y = func.test_set_preparation(exercice, test_set)
    
    # get the model
    model = KerasClassifier(model=func.create_model, input_dim=X.shape[1], units=16, learning_rate=0.001, decay=0.0001, activation="relu")
    
    # get the results
    accuracy, standard_deviation, parameters = func.model_pipeline(model, X, y)
    
    # get model weights and summary
    best_model = func.create_model(X.shape[1], parameters["units"], parameters["learning_rate"], parameters["decay"], parameters["activation"])
    
    if exercice == "exercice_a":
        best_model.save("weights/exercice_a.h5")
        plot_model(best_model, to_file="models/exercice_a.png")
    elif exercice == "exercice_b":
        best_model.save("weights/exercice_b.h5")
        plot_model(best_model, to_file="models/exercice_b.png")
    
    print("Accuracy: {acc}\nStandard_deviation: {std}\nParameters: {param}".format(acc=accuracy, std=standard_deviation, param=parameters))

if __name__ == "__main__":
    # choose the exercice to be done
    result("exercice_b")
    
    