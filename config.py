import os

class Config:
    """configuration settings for the shop management system"""
    
    # file settings
    DEFAULT_DATA_FILE = "shop_data.csv"
    DEFAULT_EXPORT_JSON = "shop_export.json"
    DEFAULT_EXPORT_CSV = "shop_export.csv"
    
    # display settings
    TABLE_WIDTH = 120
    SEPARATOR_CHAR = "="
    LINE_CHAR = "-"
    
    # field settings
    PRODUCT_FIELDS = ['product_id', 'name', 'category', 'price', 'quantity', 'supplier', 'date_added']
    
    # business logic settings
    LOW_STOCK_THRESHOLD = 10
    
    @staticmethod
    def get_data_directory():
        """get or create data directory"""
        data_dir = "data"
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        return data_dir