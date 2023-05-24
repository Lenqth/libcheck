import glob
from pathlib import Path
import shutil

HERE = Path(__file__).parent

def command_copy():
    libcheck_path = Path("../../library-checker-problems")

    def copy(src: Path, dest: Path):
        for item in src.glob("*"):
            dest_item = dest / item.name
            print(dest_item)
            
            if not dest_item.exists() or dest_item.stat().st_mtime < item.stat().st_mtime:
                shutil.copy2(item, dest_item)
        pass


    Path("./src/bin/").mkdir(parents=True, exist_ok=True)
    Path("./testcases/").mkdir(parents=True, exist_ok=True)

    with open(HERE / "template.yml") as tf:
        template_yml = tf.read()
        
    with open(HERE / "template.rs") as tf:
        template_rs = tf.read()

    for tomlpath in glob.glob(str(libcheck_path / "**/info.toml"), recursive=True):
        if "test" not in Path(tomlpath).parts:
            prob_dir = Path(tomlpath).parent
            prob_name = prob_dir.name

            rs = Path("./src/bin/%s.rs" % prob_name)
            yaml = Path("./testcases/%s.yml" % prob_name)
            
            if not rs.exists():
                with rs.open("w") as f:
                    f.write(
                        template_rs
                    )
            
            if not yaml.exists():
                with yaml.open("w") as f:
                    f.write(
                        template_yml.replace("<NAME>", prob_name)
                    )
                        

                Path("./testcases/%s" % prob_name).mkdir(parents=True, exist_ok=True)

                indir = Path("./testcases/%s/in/" % prob_name)
                outdir = Path("./testcases/%s/out/" % prob_name)
                indir.mkdir(parents=True, exist_ok=True)
                outdir.mkdir(parents=True, exist_ok=True)

                copy(prob_dir / "in", indir)
                copy(prob_dir / "out", outdir)

                prob_dir = Path(tomlpath).parent
                prob_name = prob_dir.name

