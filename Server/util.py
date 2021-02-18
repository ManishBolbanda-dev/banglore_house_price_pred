import json
import pickle
import numpy as np

location = None
data_columns = None
model = None

def get_estimated_price(loc,sqft,bhk,bath):

    try:
       loc_index = data_columns.index(loc.lower())
    except:
       loc_index = -1

    x = np.zeros(len(data_columns))
    x[0] = sqft
    x[1] = bhk
    x[2] = bath
    if loc_index>0:
        x[loc_index] = 1

    return round(model.predict([x])[0], 2)

# def get_estimated_price(l,sqft,bhk,bath):
#     try:
#         loc_index = data_columns.index(l.lower())
#     except:
#         loc_index = -1
#
#     x = np.zeros(len(data_columns))
#     x[0] = sqft
#     x[1] = bath
#     x[2] = bhk
#     if loc_index>=0:
#         x[loc_index] = 1
#
#     return round(model.predict([x])[0],2)

def get_location_names():
    loan_saved_artifacts()
    return location

def loan_saved_artifacts():
    print('loading files')
    global location
    global data_columns
    with open('../Artifacts/columns.json','r') as f:
        data_columns = json.load(f)['data_columns']
        location = data_columns[3:]
        # print(location)
    global model
    if model is None:
        with open('../Artifacts/banglore_home_price_model.pickle', "rb") as f:
            model = pickle.load(f)
            print("Loading of data is done...")

if __name__ == "__main__":
    loan_saved_artifacts()
    print(get_estimated_price('1st phase jp nagar',1000,2,2))
    print(get_estimated_price('1st phase jp nagar', 1000, 3, 2))
    print(get_estimated_price('1st phase jp nagar', 1000, 2, 3))
    print(get_estimated_price('1st phase jp nagar', 1000, 3, 3))