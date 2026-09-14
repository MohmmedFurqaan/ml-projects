import numpy as np

def fit_and_score(models, X_train, X_test, y_train, y_test):
    '''Fits and evaluate the given ml estimator.

    Args:
        models (dict[str]) : Dictionary of the model to being trained up
        X_train : training set of the data (include features)
        X_test : testing set of the data used for evaluating.
        y_train : training set of the data (include target valuse).
        y_test : testing set of the data.

    Returns:
        model_score (dictionary) -> provide the score achieved up from the model.
    '''

    # set up the random seed 
    np.random.seed(42)

    # create the dictionar to keep the model score 
    model_score = {}

    # iterate to the model
    for name, model in models.items():
        model.fit(X_train, y_train)

        # evaluate the score to the model_score.
        model_score[name] = model.score(X_test, y_test)

    return model_score