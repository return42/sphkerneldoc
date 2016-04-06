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

    echo
    pushd "${LINUX_SRC_TREE}" > /dev/null
    while read line; do
        if [[ -d "$line" ]]; then
            autodoc_folder "$line" "${AUTODOC_FOLDER}"
        else
            autodoc_file "$line" "${AUTODOC_FOLDER}"
        fi
    done < "$SCRIPT_FOLDER/src_filelist"
    insert_index_files "${AUTODOC_FOLDER}"

}
# ----------------------------------------------------------------------------
autodoc_folder() {
# ----------------------------------------------------------------------------

    local SRC="$1"
    local PRJ_AUTODOC="$2"

    local src_file
    for src_file in $(find "${1}" -name '*.h' -or -name '*.c'); do
        autodoc_file "$src_file" "$PRJ_AUTODOC"
    done
    popd > /dev/null
}

# ----------------------------------------------------------------------------
autodoc_file() {
# ----------------------------------------------------------------------------

    local src_file="${1}"
    local ext="${src_file##*.}"
    local fname="${src_file%.*}"
    local rst_file="${2}/${fname}_${ext}.rst"

    local tmp_file=$(mktemp)
    local tmp_file_log=$(mktemp)

    rm -f "${tmp_file}"
    rm -f "${tmp_file_log}"

    "$KERNEL_DOC_SCRIPT" -no-doc-sections -rst "${src_file}" > "$tmp_file" 2> "$tmp_file_log"

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

}




# ----------------------------------------------------------------------------
main "$@"
# ----------------------------------------------------------------------------



