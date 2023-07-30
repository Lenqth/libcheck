

import glob
from pathlib import Path
import subprocess
import os

def command_generate():
    libcheck_path = Path("../../library-checker-problems")

    problems = []

    for tomlpath in glob.glob(str(libcheck_path / "**/info.toml"), recursive=True):
        tomlpath = Path(tomlpath)
        if "test" not in tomlpath.parts:
            git_files = subprocess.check_output("git ls-files %s" % tomlpath.parent.relative_to(libcheck_path), shell=True, cwd=libcheck_path).splitlines()
            recent_git_files = max(
                map(lambda item: (Path(libcheck_path) / item.decode()).stat().st_mtime, git_files)
            )
            
            if (tomlpath.parent / "in").exists():
                in_files = (tomlpath.parent / "in").iterdir()
                recent_in_files = max(
                    map(lambda item: item.stat().st_mtime, in_files)
                )
                f = recent_git_files > recent_in_files
            else:
                f = True
            
            if f:
                problem_name = tomlpath.parent.name
                problems.append(problem_name)

    generate_py = str(libcheck_path / "generate.py")
    command = "python %s -p %s" % ( generate_py ," ".join(problems) )
    os.system(command)