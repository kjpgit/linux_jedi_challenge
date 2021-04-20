Don't look!

find . -type f -not -name a -not -name b -not -name c -not -name db-backup -not -name .ssh_config -delete

find /level2/ -maxdepth 1 -type f  -print0 | xargs -0 grep -lZ virus | xargs -t -0 -n1 mv -t /level2/virus/
