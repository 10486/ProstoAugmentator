from pathlib import Path
import shutil
path = Path(input("Путь до config файла: "))
shutil.copy(path, Path(os.path.dirname(os.path.abspath(__file__)))/"config"/"translator.yaml")
