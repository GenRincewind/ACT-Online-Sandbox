while LANG=C IFS= read -r in ; do
    chmod 755 "$in"
done <file.txt