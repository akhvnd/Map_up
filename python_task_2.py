
# Answer-1: Distance Matrix Calculation
import numpy as np
import pandas as pd
data= pd.read_csv('C:\\Users\\HP\\Downloads\\MapUp-Data-Assessment-F-main\\datasets\\dataset-3.csv')

def calculate_distance_matrix(input_df):
    def cal_dis_mat(input_df):
        distances = {}

        for row in input_df.itertuples(index=False):
            distances.setdefault(row.id_start, {})[row.id_end] = row.distance
            distances.setdefault(row.id_end, {})[row.id_start] = row.distance
        out_df = pd.DataFrame(distances).fillna(0)
        out_df = out_df.add(out_df.T, fill_value=0)
        return out_df

    in_data =  {'id_start':data['id_start'],'id_end':data['id_end'],'distance':data['distance']}
    in_df = pd.DataFrame(in_data)
    result = cal_dis_mat(in_df)
    return result




