import sklearn

models_dict = {
    "LinearRegression": sklearn.linear_model.LinearRegression,
    "DecisionTreeRegressor": sklearn.tree.DecisionTreeRegressor,
    "SupportVectorRegressor": sklearn.svm.SVR,
    "KNearestRegressor": sklearn.neighbors.KNeighborsRegressor,

    "LogisticRegression": sklearn.linear_model.LogisticRegression,
    "DecisionTreeClassifier": sklearn.tree.DecisionTreeClassifier,
    "SupportVectorClassifier": sklearn.svm.SVC,
    "KNearestClassifier": sklearn.neighbors.KNeighborsClassifier,
}