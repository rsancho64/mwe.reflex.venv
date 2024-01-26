# MWE.reflex.con.venv.y.makefile

```bash
cd my_app_name
python3 -m venv .venv
echo reflex >> requirements.txt
source .venv/bin/activate # bash
.venv/Scripts/activate # powershell
pip install reflex  --use-deprecated=legacy-resolver  # en linux, mejor
pip install reflex                                    # powershell
reflex init
```
# TODO: plantilla minima ? (basic)
