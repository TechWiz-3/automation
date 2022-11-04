BIN=/usr/local/bin

default:
	@printf "targets:\n  make install\n  make uninstall\n"

install:
	install -m755 stats $(BIN)/stats
	mkdir ~/.wise-stats/
	cp todo.txt ~/.wise-stats/todo.txt

uninstall:
	rm -f $(BIN)/stats
	rm -rf ~/.wise-stats
