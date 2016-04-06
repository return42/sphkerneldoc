#!/usr/bin/env bash
# -*- coding: utf-8; mode: sh -*-
# ----------------------------------------------------------------------------
# Purpose: print infos of setup
# ----------------------------------------------------------------------------

source $(dirname ${BASH_SOURCE[0]})/setup.sh

# ----------------------------------------------------------------------------
# Config
# ----------------------------------------------------------------------------

LINUX_DOC="${LINUX_SRC_TREE}/Documentation"
VERBOSE=${VERBOSE-0}

# ----------------------------------------------------------------------------
main(){
    rstHeading "sync kernel docs" part
# ----------------------------------------------------------------------------

    case $1 in
        test123)
            test123
            ;;
        *)
            echo
	    echo "usage:"
            echo
	    echo "    [VERBOSE=1] \\"
	    echo "    $0 [test123]"
            echo
            ;;
    esac
}


# ----------------------------------------------------------------------------
test123(){
    rstHeading "test some stuff"
# ----------------------------------------------------------------------------

    # may we need some filters? / at least we can include as plain text ...

    echo
    sync_literalinclude kernel-doc-nano-HOWTO.txt "${LINUX_MISC_DOC}" "kernel-doc nano-HOWTO"
    sync_literalinclude kernel-parameters.txt  "${LINUX_MISC_DOC}" "Kernel parameters"

    insert_index_files "${LINUX_MISC_DOC}"
}


# ----------------------------------------------------------------------------
sync_txt2rst(){
# ----------------------------------------------------------------------------

    # usage:   sync_txt <filename in linux_src/Documentation> <target folder>

    info_msg "sync doc: ${1%.*}.rst"
    mkdir -p "${2}"
    cp "${LINUX_DOC}/${1}"  "${2}/${1%.*}.rst"

}

# ----------------------------------------------------------------------------
sync_literalinclude(){
# ----------------------------------------------------------------------------

    # usage:   sync_txt <filename in linux_src/Documentation> <target folder> [title]

    local TITLE="${3-$(basename "${1}")}"
    local FILENAME="${1%.*}.txt"
    local target="${2}/${1%.*}"
    mkdir -p "${2}"

    info_msg "sync doc: ${1%.*}.rst"
    cp "${LINUX_DOC}/${1}"  "${target}.txt"

    {
        render_template "$TEMPLATES/literalinclude.rst"
        echo ""
    } > "${target}.rst"
}





# ----------------------------------------------------------------------------
main "$@"
# ----------------------------------------------------------------------------
