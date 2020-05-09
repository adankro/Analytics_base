from config import Config
from extractors import MysqlExtractor

mysql_extractor = MysqlExtractor(
    Config.MYSQL_HOST, Config.MYSQL_USER, Config.MYSQL_PASSWORD)
mysql_extractor.export_table_to_excel('table')
