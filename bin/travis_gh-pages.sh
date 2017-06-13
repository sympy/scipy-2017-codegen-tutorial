SOURCE_BRANCH="master"
TARGET_BRANCH="gh-pages"

if [ "$TRAVIS_PULL_REQUEST" != "false" -o "$TRAVIS_BRANCH" != "$SOURCE_BRANCH" ]; then
    echo "Skipping deploy"
    exit 0
fi

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

git config user.name "Travis CI"
git config user.email "$COMMIT_AUTHOR_EMAIL"
git commit -m "Latest notebooks"
git remote add origin-pages https://${GH_TOKEN}@github.com/sympy/scipy-2017-codegen-tutorial.git > /dev/null 2>&1
git push --quiet -f --set-upstream origin-pages gh-pages
