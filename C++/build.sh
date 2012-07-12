#! /bin/bash

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

    rm -r ./b{in,uild}

    cat << EOF
Preparing ./b{in,uild}.

EOF

    mkdir ./b{in,uild}

    cat << EOF
Compiling.

EOF

    # Use cmake
    cd build
    cmake ..
    make
    cd ..

    return 0
}

main $@

# vim: tw=72
