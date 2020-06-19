import pandas as pd
import os as os
from sklearn.linear_model import LinearRegression


class HurstForQ:
    df_hurst_for_q = pd.DataFrame

    def __init__(self):
        print("hurst for q")
        self.df_hurst_for_q = pd.DataFrame(columns=['File', 'q', 'Coefficient', 'Intercept', 'R2'])

    def calc_hurst_for_file(self, q_dump_file):
        q_data = pd.read_csv(q_dump_file)
        each_q = q_data.groupby('q')
        q_values = each_q.groups.keys()

        # df_hurst_for_q.columns = ['File', 'q', 'Coefficient', 'Intercept', 'R2']

        for q in q_values:
            fluctuations_for_a_q = q_data[(q_data['q'] == q)]
            coef, intercept, rsquared = self.calc_hurst_for_a_q(fluctuations_for_a_q)
            # print(q_dump_file, q, coef, intercept, rsquared)
            file_path, file_name = os.path.split(q_dump_file)
            print(file_name)
            file_name_without_ext = os.path.splitext(file_name)
            new_row = {'File': file_name_without_ext[0], 'q': q, 'Coefficient': coef, 'Intercept': intercept,
                       'R2': rsquared}
            self.df_hurst_for_q = self.df_hurst_for_q.append(new_row, ignore_index=True)
        # print(self.df_hurst_for_q.head())
        self.df_hurst_for_q.to_csv('/home/bhaduri/MEGA/supersymmetry/Results/Hurst_for_q.csv')


    def calc_hurst_for_a_q(self, fluctuations_for_a_q):
        # print(fluctuations_for_a_q)
        X = fluctuations_for_a_q.iloc[:, 1].values.reshape(-1, 1)
        Y = fluctuations_for_a_q.iloc[:, 2].values.reshape(-1, 1)
        # print(X)
        # print(Y)
        linear_regressor = LinearRegression()  # create object for the class
        linear_regressor.fit(X, Y)
        coef = linear_regressor.coef_[0][0]
        intercept = linear_regressor.intercept_[0]
        rsquared = linear_regressor.score(X, Y)
        return coef, intercept, rsquared

    def calc_hurst_for_a_folder(self, folder_name):

        for root, dirs, files in os.walk(folder_name):
            for file in files:
                file_name_with_ext = os.path.join(root, file)
                # print(file_name_with_ext)
                self.calc_hurst_for_file(file_name_with_ext)
