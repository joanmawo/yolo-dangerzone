all:
	@python baye.py
	@python graficador.py

clean:
	@rm -f *.txt
	@rm -f *.png
