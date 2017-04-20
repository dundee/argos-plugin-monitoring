
.PHONY: clean

upload:
	python setup.py sdist bdist_wheel upload

install:
	python setup.py install

clean:
	-rm -fR argos_plugin_monitoring.egg-info/ build/ dist
