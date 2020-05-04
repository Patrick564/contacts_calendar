# Contacts Calendar
A contacts page with django

In theme/static_src/package.json change:
    "start": "watch 'npm run build-postcss' ./src" ->
    "start": "watch \"npm run build-postcss\" ./src"

In settings.py put:
    NPM_BIN_PATH wiht the path of node/npm of your pc
