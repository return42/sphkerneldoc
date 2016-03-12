#!/usr/bin/env bash
# -*- coding: utf-8; mode: sh -*-
# ----------------------------------------------------------------------------
# Purpose: create rst-tree from the linux kernel sources
# ----------------------------------------------------------------------------

source $(dirname ${BASH_SOURCE[0]})/setup.sh

# ----------------------------------------------------------------------------
# Config
# ----------------------------------------------------------------------------

LINUX_DOC="${LINUX_SRC_TREE}/Documentation"
VERBOSE=${VERBOSE-0}

# ----------------------------------------------------------------------------
main(){
    rstHeading "autodoc Linux projects" part
# ----------------------------------------------------------------------------

    case $1 in
        linux-tv)
            linux-tv
            ;;
        *)
            echo
	    echo "usage:"
            echo
	    echo "    [VERBOSE=1] \\"
	    echo "    $0 [linux-tv]"
            echo
            ;;
    esac
}

# ----------------------------------------------------------------------------
linux-tv(){
    rstHeading "LinuxTV media tree"
# ----------------------------------------------------------------------------

    local SRC="drivers/media"
    local PRJ_AUTODOC="${AUTODOC_FOLDER}/linux_tv"

    local tmp_file=$(mktemp)
    local tmp_file_log=$(mktemp)

    local src_file
    local ext
    local fname
    local rst_file

    pushd "${LINUX_SRC_TREE}/${SRC}" > /dev/null
    echo
    for src_file in $(find ./ -name '*.h' -or -name '*.c'); do

        src_file="${src_file:2}"
        ext="${src_file##*.}"
        fname="${src_file%.*}"
        rst_file="${PRJ_AUTODOC}/${fname}_${ext}.rst"

        rm -f "${tmp_file}"
        rm -f "${tmp_file_log}"

        "$KERNEL_DOC_SCRIPT" -rst "${src_file}" > "$tmp_file" 2> "$tmp_file_log"

        if [[ -s "$tmp_file" ]]; then

            info_msg "autodoc file '${src_file}'"
            mkdir -p $(dirname "$rst_file")

            {   echo ".. -*- coding: utf-8; mode: rst -*-"
                rstHeading "$(basename $src_file)"  part-nc
                echo
                cat "$tmp_file"
            }  > "$rst_file"

            rm -f "${tmp_file}"

            if [[ -s "$tmp_file_log" ]]; then
                mv "$tmp_file_log" "${rst_file}.autodoc.log"
                [[ 0 < $VERBOSE ]] && cat "${rst_file}.autodoc.log"
            fi
        else
            [[ 0 < $VERBOSE ]] && info_msg "file $src_file has no doc-strings"
        fi
    done
    popd > /dev/null

    insert_index_files "${PRJ_AUTODOC}"
}


# ----------------------------------------------------------------------------
main "$@"
# ----------------------------------------------------------------------------
