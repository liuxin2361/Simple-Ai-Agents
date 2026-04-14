import yaml

def get_api_keys( key_name: str, config_path:str = "./code/utils/config.yaml") -> dict:
    """
    YAMLファイルからAPIキーを読み取ります。
    Args:
        config_path (str): APIキーが保存されているYAMLファイルのパス。
    Returns:
        dict: APIキーの辞書。
    """
    try:
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
            return config.get(key_name, {})
    except Exception as e:
        print(f"APIキーの読み取りに失敗しました: {e}")
        return {}
    