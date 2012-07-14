#! /bin/bash

DIR="_build bin"

main ()
{
    # Report the purpose
    cat << EOF 
========================================================================
This is a very simplistic build script which will help to keep things
tidy
========================================================================

Cleaning everything up.

EOF

    rm -r ${DIR}

    cat << EOF
Preparing ${DIR}

EOF

    mkdir ${DIR}

    cat << EOF
Compiling.

EOF

    # Use cmake
    cd ${DIR}
    cmake ..
    make
    cd ..

    return 0
}

main $@

# vim: tw=72
