import os
import csv
import platform
from os import path
import pandas as pd
from datetime import datetime
from collections import Counter


def create_hist(artist, title):
    """
    Check if the file already exists: in case it does
    append an additional line to the file, otherwise
    write ex-novo a file, adds the fiels (column names),
    and the new line. The check is performed in the directory of this file, that
    will be the same directory in which the .csv will be stored.
    """
    csv_dir = os.path.dirname(os.path.realpath(__file__))   
    if path.exists(csv_dir + "\\" + "history.csv") is False:
        with open(csv_dir + "\\" + "history.csv", "w", newline = "") as csvfile:
            # Add column names with this list
            fields = ["Artist", "Title", "Datetime"]
            # Based on DictWriter, a new line with header is added.
            # Then, the actual row is appended to the file
            writer = csv.DictWriter(csvfile, fieldnames = fields)
            writer.writeheader()
            writer.writerow({"Artist": artist, "Title": title, 
                             "Datetime": datetime.now().strftime("%d/%m/%y %H:%M:%S")})
    else:
        with open(csv_dir + "\\" + "history.csv", "a", newline = "") as csvfile:  # "a" stands for append
            writer = csv.writer(csvfile)
            # Once the file is already there, it is only necessary to
            # append the row through a list
            new_row = [artist, title, datetime.now().strftime("%d/%m/%y %H:%M:%S")]
            writer.writerow(new_row)     
    df = pd.read_csv(csv_dir + "\\" + "history.csv")
    """
    We created a list of tuples from the dataframe to allow
    easier comparison, beacuse they needed to be sorted (with Counter).
    A nested list is produced and then reversed so that 
    the most searched parameters will be displayed first.
    """
    art_tit_list = [(r[1] [0], r[1] [1]) for r in df.iterrows()]
    sorted_dict = dict(Counter(art_tit_list))
    list_for_df = [[k[0].replace("_", " "), k[1].replace("_", " ")] for k, v in sorted_dict.items()] [::-1]
    upd_df = pd.DataFrame(list_for_df, columns = ["----------------","----------------"]).head(3)
    # CODE FOR MOST SEARCHED QUERIES
    art_tit_list = [ (r[1][0], r[1][1]) for r in df.iterrows() ]
    sorted_dict = dict(Counter(art_tit_list))
     # show only artist and song
    list_for_df = [ [k[0].replace("_", " "), k[1].replace("_", " ")] for k, v in sorted_dict.items() ]
    upd_df = pd.DataFrame(list_for_df, columns = ["----------------","----------------"]).head(3)    
    
    """
    # CODE FOR MOST RECENT QUERIES
    upd_df = df.iloc[::-1]
    upd_df = upd_df.drop_duplicates(subset = ["Artist", "Title"],
                                    keep = "first") # first because it would be the most recent
    upd_df.reset_index(inplace = True, drop = True)
    upd_df = upd_df[["Artist", "Title"]]
    upd_df = upd_df.head(3)
    upd_df["Artist"] = upd_df["Artist"].str.replace("_", " ")
    upd_df["Title"] = upd_df["Title"].str.replace("_", " ")
    upd_df = upd_df.rename(columns = {"Artist":"----------------",
                                      "Title":"----------------"})
    """
    
    return upd_df
