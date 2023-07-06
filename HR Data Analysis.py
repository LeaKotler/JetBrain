import pandas as pd
import requests
import os
import pandas as pd

# config pandas

pd.set_option('display.max_columns', 100)

# scroll down to the bottom to implement your solution

if __name__ == '__main__':

    if not os.path.exists('../Data'):
        os.mkdir('../Data')

    # Download data if it is unavailable.
    if ('A_office_data.xml' not in os.listdir('../Data') and
        'B_office_data.xml' not in os.listdir('../Data') and
        'hr_data.xml' not in os.listdir('../Data')):
        print('A_office_data loading.')
        url = "https://www.dropbox.com/s/jpeknyzx57c4jb2/A_office_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/A_office_data.xml', 'wb').write(r.content)
        print('Loaded.')

        print('B_office_data loading.')
        url = "https://www.dropbox.com/s/hea0tbhir64u9t5/B_office_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/B_office_data.xml', 'wb').write(r.content)
        print('Loaded.')

        print('hr_data loading.')
        url = "https://www.dropbox.com/s/u6jzqqg1byajy0s/hr_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/hr_data.xml', 'wb').write(r.content)
        print('Loaded.')

        # All data in now loaded to the Data folder.

    # write your code here

    # Stage 1/5
    df_A = pd.read_xml('../Data/A_office_data.xml')
    df_B = pd.read_xml('../Data/B_office_data.xml')
    hr_data = pd.read_xml('../Data/hr_data.xml')

    df_A['index'] = df_A['employee_office_id'].apply(lambda x: 'A' + str(x))
    df_B['index'] = df_B['employee_office_id'].apply(lambda x: 'B' + str(x))

    df_A.set_index('index', inplace=True, drop=True)
    df_B.set_index('index', inplace=True, drop=True)
    hr_data.set_index('employee_id', inplace=True)

    # Stage 2/5
    df_all = pd.concat([df_A, df_B], axis=0)
    df_merged = df_all.merge(hr_data, how='left', left_index=True, right_index=True, indicator=True)
    df_merged_filtered = df_merged[df_merged._merge == 'both']
    df_merged_filtered = df_merged_filtered.drop(columns=['employee_office_id', '_merge'])
    df_merged_filtered.sort_index(inplace=True)

    # Stage 3/5
    # What are the departments of the top ten employees in terms of working hours?
    top_departments = list(df_merged_filtered.sort_values('average_monthly_hours', ascending=False)[:10]['Department'])

    # What is the total number of projects on which IT department employees with low salaries have worked?
    n_IT_low_salary_proj = df_merged_filtered.query('salary == "low" & Department=="IT"')['number_project'].sum()

    # What are the last evaluation scores and the satisfaction levels of the employees A4, B7064, and A3033
    employers = ['A4', 'B7064', 'A3033']
    df_employers = df_merged_filtered.loc[employers, ['last_evaluation', 'satisfaction_level']]
    df_employers_list = [list(row) for row in df_employers.values]

    # Stage 4/5

    def count_bigger_5(group):
        group_filtered = [value for value in group if value > 5]
        return len(group_filtered)

    stats = df_merged_filtered.groupby('left').agg({
                                                    # the median number of projects the employees in a group worked on, and how many employees worked on more than five projects;
                                                    'number_project': ['median', count_bigger_5],
                                                    # the mean and median time spent in the company;
                                                    'time_spend_company': ['mean', 'median'],
                                                    # the share of employees who've had work accidents;
                                                    'Work_accident': 'mean',
                                                    # the mean and standard deviation of the last evaluation score.
                                                    'last_evaluation': ['mean', 'std']})\
                                              .round(2)

    # Stage 5/5

    df_pivoted = df_merged_filtered.pivot_table(index='Department', columns=['left', 'salary'], values='average_monthly_hours', aggfunc='median')
    df_filter_1 = df_pivoted[(0.0, 'high')] < df_pivoted[(0.0, 'medium')]
    df_filter_2 = df_pivoted[(1.0, 'low')] < df_pivoted[(1.0, 'high')]
    df_pivoted_res_1 = df_pivoted[df_filter_1 | df_filter_2]


    df_pivoted_2 = df_merged_filtered.pivot_table(index='time_spend_company',
                                   columns='promotion_last_5years',
                                   values=['last_evaluation', 'satisfaction_level'],
                                   aggfunc=['max', 'mean', 'min']).round(2)
    df_filter = df_pivoted_2[('mean', 'last_evaluation', 0)] > df_pivoted_2[('mean', 'last_evaluation', 1)]
    df_pivoted_2_res_2 = df_pivoted_2[df_filter]

    print(df_pivoted_res_1.to_dict())
    print(df_pivoted_2_res_2.to_dict())