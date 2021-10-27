from pathlib import Path
import shutil
import os
path = Path(input("Путь до config файла: "))
package_path = Path(os.path.dirname(os.path.abspath(__file__)))
shutil.move(path, package_path/"config"/"translator.yaml")
