# austyle_img

### Description
Don't you hate it when you take a photo with your iPhone and it saves as a .heic file?
Nothing works with .heic files! This script converts .heic files to .png files.

### Get Started
```
# Install poetry (package manager)
brew install poetry

# Install pipx (utility for installing and running Python applications in isolated environments)
brew install pipx

# Install poe (task runner)
pipx install poethepoet --index-url https://pypi.org/simple

# Install repo dependencies
poetry install

# Activate poetry environment
poetry env activate
```

### Convert Image
```
# Convert .heic to .png
poe convert_img --fmt 'png' --path '</path/to/image/image_name.HEIC'
```

### Linting
```
# Lint
poe lint

# Lint and Fix
poe lint -- --fix
```

