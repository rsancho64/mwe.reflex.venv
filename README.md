# MWE.reflex.con.venv.y.makefile

- [ ] [read](https://medium.com/@HeCanThink/reflex-a-library-to-build-performant-and-customizable-web-apps-in-pure-python-2bfde0344af2) 

## build flow

mkdir my_app_name
cd my_app_name
python3 -m venv .venv
echo reflex >> requirements.txt
source .venv/bin/activate

# pip install reflex --use-deprecated=legacy-resolver
reflex init # TODO: plantilla minima ? (basic)