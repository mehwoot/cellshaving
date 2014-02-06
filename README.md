## Repository for the Cell Shaving program.

## Windows

First, download https://github.com/mehwoot/cellshaving/raw/master/cell_shaving.zip and unzip the file.

You should now have a folder called "cellshaving".

Open command prompt and change directory to the upzipped folder

```cd cellshaving```

You should now be able to run the program by

```process.exe example1.csv -header```

You can write the output of the program to a file like so:

```process.exe example2.csv -header > output.csv```


## OSX / Linux

First ensure you have python installed.

```python --version```

Should output "Python 2.7.5" or something similiar.  If you do not have python installed, download it from http://python.org/download/

Now, download the code by running

```
git clone git@github.com:mehwoot/cellshaving.git
cd cellshaving
```

You should now be able to run the program by

```python process.py example1.csv -header```

You can write the output of the program to a file like so:

```python process.py example2.csv -header > output.csv```
