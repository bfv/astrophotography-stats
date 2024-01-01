
import os
import tomllib

targets: list[str] = []

'''
The target name is by default derived from the directory name, unless there's a file `target.info` in the directory.
The file should be in toml format:

[target]
name=M101
contained = [ "M65", "M66, "NGC3628" ]
transients = [ "SN2023ixf" ]

the transitents property is optional
'''

def get_target_info(dir: str) -> str | None:
    name = None
    cfgfile = os.path.join(dir, "target.info")
    if os.path.exists(cfgfile):

        with open(cfgfile, "rb") as f:
            cfg = tomllib.load(f)
            try:
                name = cfg["target"]["name"]
            except:
                pass

    if name == None:
        name = os.path.basename(os.path.normpath(dir))
        print("------------------> No info for:", dir)

    targets.append(name)
    
    return name

if __name__ == "__main__":
    print(get_target_info(r"D:\onedrive\_2023\m39"))
