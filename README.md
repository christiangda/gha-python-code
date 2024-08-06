# gha-python-code

This is a github action to test the native python and dependencies installed in the runner

## Development

### Setup

```bash
python -m venv venv
source venv/bin/activate
pip install pip --upgrade

pip install -r dev-requirements.txt
```

### Test Files

```bash
cat << EOF > test.json
{
 "glossary": {
  "title": "example glossary",
  "GlossDiv": {
   "title": "S",
   "GlossList": {
    "GlossEntry": {
     "ID": "SGML",
     "SortAs": "SGML",
     "GlossTerm": "Standard Generalized Markup Language",
     "Acronym": "SGML",
     "Abbrev": "ISO 8879:1986",
     "GlossDef": {
      "para": "A meta-markup language, used to create markup languages such as DocBook.",
      "GlossSeeAlso": [
       "GML",
       "XML"
      ]
     },
     "GlossSee": "markup"
    }
   }
  }
 }
}
EOF
```

```bash
cat << EOF > test.yaml
---
glossary:
  title: example glossary
  GlossDiv:
    title: S
    GlossList:
      GlossEntry:
        ID: SGML
        SortAs: SGML
        GlossTerm: Standard Generalized Markup Language
        Acronym: SGML
        Abbrev: ISO 8879:1986
        GlossDef:
          para: A meta-markup language, used to create markup languages such as DocBook.
          GlossSeeAlso:
            - GML
            - XML
        GlossSee: markup
EOF
```

### Test

A yaml file

```bash
python read_key.py --file test.yaml --key title
```

A json file

```bash
python read_key.py --file test.json --key title
```
