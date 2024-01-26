# MWE.reflex.con.venv.y.makefile

```bash
cd my_app_name
python3 -m venv .venv
echo reflex >> requirements.txt
source .venv/bin/activate
# pip install reflex --use-deprecated=legacy-resolver
pip install reflex
reflex init
```
# TODO: plantilla minima ? (basic)
