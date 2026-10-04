import pandas as pd
import pandasai as pai

class dataprocessing:
    def __init__(self, product_csv: str, product_attributes_csv: str):
        self.product_df = pd.read_csv(product_csv)
        self.product_attributes_df = pd.read_csv(product_attributes_csv)

    def readCSV(self):
        return self.df
    
    def pivotFiles(self):
        attrs_wide = self.product_attributes_df.pivot_table(
            index="product_id", columns="attribute_name", values="attribute_value", aggfunc="first"
        ).reset_index()

        merged = self.product_df.merge(attrs_wide, on="product_id", how="left")
        return merged