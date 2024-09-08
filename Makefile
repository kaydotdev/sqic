# Build the software, test it, generate the results and plots, and compile the
# manuscript PDF.
#
# Runs the individual Makefiles from code/ and manuscript/.

.PHONY: all
all:
	make -C code all

.PHONY: clean
clean:
	make -C code clean
