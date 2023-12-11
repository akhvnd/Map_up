# Answer 1: Car Matrix Generation
import numpy as np
import pandas as pd
data= pd.read_csv('C:\\Users\\HP\\Downloads\\MapUp-Data-Assessment-F-main\\datasets\\dataset-1.csv')

def generate_car_matrix (input_df):
    def gen_car_mat(input_df):
        out_df = input_df.pivot(index='id_1', columns='id_2', values='car')
        return out_df

    in_data = {'id_1':data['id_1'],'id_2':data['id_2'],'car':data['car']}
    df = pd.DataFrame(in_data)
    result = gen_car_mat(df).fillna(0).round(decimals=1)
    return result


# Answer 2: Car Type Count Calculation
def get_type_count(in_data):
    def gen_cat_mat(in_data):
        car_type = pd.Series([])
        for i in range(len(data)):
            if in_data["car"][i] <= 15:
                car_type[i] = 'low'

            elif in_data["car"][i] > 15 and in_data["car"][i] <= 25:
                car_type[i] = "medium"

            else:
                car_type[i] = 'high'

        data.insert(8, "Car Type", car_type)
        return data

    data1 = gen_cat_mat(data)

    car_type_counts = data1['Car Type'].value_counts()
    car_type_counts = dict(sorted(car_type_counts.items()))

    return car_type_counts



# Answer 3: Bus Count Index Retrieval
def get_bus_indexes(df):
    # Calculate the mean value of the 'bus' column
    mean_bus = df['bus'].mean()

    # filtering indices
    bus_indexes = df[df['bus'] > 2 * mean_bus].index.tolist()

    # Sort in ascending order
    bus_indexes.sort()

    return bus_indexes

# Answer 4:
def filter_routes(df):
    # average of "truck" column greater than 7
    in_df = df.groupby('route')['truck'].mean().reset_index()
    in_df = in_df[in_df['truck'] > 7]

    # sorted list
    sorted_routes = sorted(in_df['route'].unique())
    return sorted_routes



# Answer 5: Matrix Value Modification
def multiply_matrix(input_df):

    # multiplication logic
    in_df = input_df.applymap(lambda x: x * 0.75 if x > 20 else x * 1.25)

    # Roundoff
    result5 = in_df.round(1)

    return result5


