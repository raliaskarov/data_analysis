# function to merge few excel files into 
# can use file and subfolder names to create identifier column
def merge_files(data_path, file_name_column = None, folder_name_column = None):
    combined_data = []
    for dirpath, dirnames, filenames in os.walk(data_path):
        if filenames:
            if folder_name_column:
                label = os.path.basename(dirpath)

            for file in filenames:
                if file.endswith('.xlsx'):
                    file_path = os.path.join(dirpath, file)
                    df = pd.read_excel(file_path)
                    if folder_name_column:
                        df[folder_name_column] = label
                    if file_name_column:
                        df[file_name_column] = file.replace('.xlsx', '')
                    combined_data.append(df)
    df = pd.concat(combined_data, ignore_index = True)
    return df
