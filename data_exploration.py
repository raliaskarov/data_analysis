# functions in reading data

# technical function to profile table        
def profile(df):

    value_types = [[c, df[c].apply(lambda x: type(x)).unique().tolist()] for c in df.columns]

    print('DATAFRAME:')
    print(f'{format(df.shape[0],",d")} rows | {df.shape[1]} columns')
    print(f'{format(df.size,",d")} datapoints')
    print(f'{format(df.memory_usage(deep = False).sum()/1000000,".1f")}MB disk space')

    print('------------------------')

    print('DTYPES:')
    print(df.dtypes)

    print('------------------------')

    print('VALUE TYPES:')
    for v in value_types:
        print(f'{v[0]}: {v[1]}')

    print('------------------------')
    print('COLUMNS:')
    print(df.columns.tolist())
    
    
    # sample output:
    """
    DATAFRAME:
    10,602 rows | 4 columns
    42,408 datapoints
    0.3MB disk space
    ------------------------
    DTYPES:
    Country       object
    Period        object
    Value        float64
    Indicator     object
    dtype: object
    ------------------------
    VALUE TYPES:
    Country: [<class 'str'>]
    Period: [<class 'str'>]
    Value: [<class 'float'>]
    Indicator: [<class 'str'>]
    ------------------------
    COLUMNS:
    ['Country', 'Period', 'Value', 'Indicator']
    """
