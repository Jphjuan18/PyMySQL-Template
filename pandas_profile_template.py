
def read_file():

        # create pandas df
        import pandas as pd
        from pandas_credentials import data

        df = pd.read_excel(data,index_col = 0)

        #df = pd.read_csv(data)

        print(df)

        df.info()

        
        
        return df

#q1 = read_file()
#q1

###
#def pandas_profile(data):
#    from pandas_profiling import ProfileReport
#    import re
#    df = read_file()
#    data_html = data.split('/')
#    data_html = data_html[-1]
#    data_html = data_html.split('.')
#    data_html = data_html[0]
#    report = ProfileReport(df)
#    report.to_file(f'{data_html}.html')
#    return print('Report Generated')
