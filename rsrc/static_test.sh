#!/bin/bash
# Dump Environment (so that we can check PATH, UT_FLAGS, etc.)
 set -e
 set -x
 IS_IN_TRAVIS=false
 PYTHON_COMMAND=python
  
 if [ "$TRAVIS_OS_NAME" == "osx" ]
 then
	PYTHON_COMMAND=python3
 fi
 
 if [ "$CI" = 'true' ] && [ "$TRAVIS" = 'true' ]
 then
      IS_IN_TRAVIS=true
 fi
  
 if [ "$IS_IN_TRAVIS" = 'false' ] || [ "$TRAVIS_PYTHON_VERSION" = '3.6' ]
 then
     python -m vulture gopem/ rsrc/ setup.py --min-confidence 65 --exclude=gopem,build,.eggs --sort-by-size .
	 python -m bandit -r gopem -s B322
	 python rsrc/version_check.py
	 python -m pydocstyle
 fi