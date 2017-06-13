if [ -d /tmp/$1 ]; then
    2>&1 echo "/tmp/$1 already exists"
    exit 1
fi
mv $1 /tmp/
git checkout gh-pages
git pull
git reset --hard HEAD~1
git clean -xfd
git rm -rf * > /dev/null
mv /tmp/$1/. .
git add -f .
git commit -m "Latest notebooks"
git push -f origin gh-pages
