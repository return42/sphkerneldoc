#!/usr/bin/env bash
# -*- coding: utf-8; mode: sh -*-
# ----------------------------------------------------------------------------
# Purpose:     common environment customization
# ----------------------------------------------------------------------------

if [[ -z "${REPO_ROOT}" ]]; then
    REPO_ROOT="$(dirname ${BASH_SOURCE[0]})"
    while([ -h "${REPO_ROOT}" ]); do
        REPO_ROOT=`readlink "${REPO_ROOT}"`
    done
    REPO_ROOT=$(cd ${REPO_ROOT}/.. && pwd -P )
fi

# ===============
# handsOn Scripts
# ===============

LINUX_SRC_TREE=/where/is/your/linux/clone
SCRIPT_FOLDER="${REPO_ROOT}/scripts"
DOC_FOLDER="${REPO_ROOT}/doc"
AUTODOC_FOLDER="${DOC_FOLDER}/linux_src_doc"
BOOKS_FOLDER="${DOC_FOLDER}/books"
LINUX_MISC_DOC="${DOC_FOLDER}/linux_misc_doc"
KERNEL_DOC_SCRIPT="${SCRIPT_FOLDER}/kernel-doc"
TEMPLATES="${REPO_ROOT}/templates"
CACHE=${REPO_ROOT}/cache

# ----------------------------------------------------------------------------
setupInfo () {
# ----------------------------------------------------------------------------
    rstHeading "setup info"
    echo "
REPO_ROOT      : ${REPO_ROOT}
SCRIPT_FOLDER  : ${SCRIPT_FOLDER}
TEMPLATES      : ${TEMPLATES}
CACHE          : ${CACHE}
CONFIG         : ${CONFIG}
DEB_ARCH       : ${DEB_ARCH}
LINUX_SRC_TREE : ${LINUX_SRC_TREE}

LSB (Linux Standard Base) and Distribution information.

DISTRIB_ID          : ${DISTRIB_ID}
DISTRIB_RELEASE     : ${DISTRIB_RELEASE}
DISTRIB_CODENAME    : ${DISTRIB_CODENAME}
DISTRIB_DESCRIPTION : ${DISTRIB_DESCRIPTION}

CWD : $(pwd -P)"
}

# ----------------------------------------------------------------------------
# load common scripts and check environment
# ----------------------------------------------------------------------------

if [[ ! -e "${REPO_ROOT}/tool_config.sh" ]]; then
    echo "ERROR: missing config file ${REPO_ROOT}/tool_config.sh"
    echo "       copy ${REPO_ROOT}/tool_config.sh.template to"
    echo "       tool_config.sh and set your environment within."
    exit 42
else
    source "${REPO_ROOT}/tool_config.sh"
fi

if [[ ! -r "${LINUX_SRC_TREE}" ]]; then
    echo "ERROR: can't find linux source at: ${LINUX_SRC_TREE}"
    echo "ERROR: check your ${REPO_ROOT}/tool_config.sh"
    exit 42
fi

if [[ ! -e "${SCRIPT_FOLDER}/common.sh" ]]; then
    echo "ERROR: can't source file common.sh"
    exit 42
else
   source ${SCRIPT_FOLDER}/common.sh
   checkEnviroment
fi
