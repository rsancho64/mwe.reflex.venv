APPNAME = app0

eco:
	echo $(APPNAME)/ >> .gitignore
	echo $(APPNAME)/.web/ >> .gitignore
	echo $(APPNAME)/__pycache__/ >> .gitignore

build: 

	echo appfolder --------------------------
	mkdir -p $(APPNAME) &&\
	cd $(APPNAME) &&\
	ln -sf ../makefile . &&\
	ln -sf ../Makefile.venv . &&\
	ln -sf ../requirements.txt .
	echo venv --------------------------
	make venv &&\   
#	  # shell (.venv) iniciado (si no: make bash)
#	  # pip install reflex hecho # ya indicado en requirements.txt

#	# 	reflex init:
	cd $(APPNAME) &&\
	reflex init && # como hacerlo automatico?? \
	echo init done --------------------------

rmapp: $(APPNAME)/
	rm -f -r $(APPNAME)

clean: clean-venv
	rm -f -r .venv

# https://github.com/sio/Makefile.venv/blob/master/Makefile.venv
include Makefile.venv
