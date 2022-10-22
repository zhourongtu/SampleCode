new_contents = "hello:\n\ttouch inside_file"
all:
	mkdir -p subdir
	printf $(new_contents) | sed -e 's/^ //' > subdir/makefile
	cd subdir && $(MAKE)

clean:
	ls | grep -E -v "Makefile|*.c" |xargs rm -rf