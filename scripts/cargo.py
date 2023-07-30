import glob
from pathlib import Path
import shutil
import tomlkit
import logging

logger = logging.getLogger()


def command_cargo():
    libcheck_path = Path("../../library-checker-problems")

    with open("./Cargo.toml", "r") as f:
        cargo_toml = tomlkit.load(f)

    bins = tomlkit.document()

    for tomlpath in glob.glob(str(libcheck_path / "**/info.toml"), recursive=True):
        if "test" not in Path(tomlpath).parts:
            prob_dir = Path(tomlpath).parent
            prob_name = prob_dir.name
    #        print('%s = { problem = "https://judge.yosupo.jp/problem/%s"}' % (prob_name,prob_name) )

            item = tomlkit.inline_table()
            item.add("problem", "https://judge.yosupo.jp/problem/%s" % prob_name)
            
            bins.add(prob_name , item)

    cargo_toml["package.metadata.cargo-compete.bin"] = bins

    with open("Cargo.toml", "w", encoding="utf8") as f:
        tomlkit.dump(cargo_toml, f)
