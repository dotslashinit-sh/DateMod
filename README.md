# Date Modifier
Date Modifier (`DateMod` for short) is a program to extract and modify the creation and modification date-time of files.

## Usage
1) To extract date information, use
  ```
  $ python extract.py <root-directory> <file-extension> <output-file>
  ```
  The filenames and datetime information are stored in a JSON file.
  An example usage would be
  ```
  $ python extract.py 'Pictures' '.png' 'Pictures.json'
  ```
2) To modify the time information, use
  ```
  $ python modify.py <dateinfo-file> <root-directory>
  ```
  An example usage would be,
  ```
  $ python modify.py 'Pictures.json' 'Pictures'
  ```
