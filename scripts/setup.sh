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

# SCRIPT_FOLDER: Ordner mit den Skripten für die Setups
#
SCRIPT_FOLDER="${REPO_ROOT}/scripts"


LINUX_SRC_TREE=/where/is/your/linux/clone
AUTODOC_FOLDER="${REPO_ROOT}/linux_src_doc"
LINUX_MISC_DOC="${REPO_ROOT}/linux_misc_doc"

KERNEL_DOC_SCRIPT="${SCRIPT_FOLDER}/kernel-doc"


# TEMPLATES: Ordner in dem die vorlagen für die Setups zu finden sind
#
TEMPLATES="${REPO_ROOT}/templates"

# CACHE: Ordner in dem die Downloads und Builds gecached werden
#
#CACHE=${REPO_ROOT}/cache

# CONFIG: Ordner unter dem die Konfiguration eines Hosts gesichert werden soll
#
#CONFIG="${REPO_ROOT}/config_$(hostname)"

# WWW_USER: Benutzer für die Prozesse des WEB-Servers
#
#WWW_USER=www-data

# WWW_FOLDER: Ordner in dem die Resourcen des WEB-Servers liegen
#
#WWW_FOLDER=/var/www

# =========
# toolchain
# =========

# THREE_WAY_MERGE_CMD: Kommando oder Funktion mit der ein (interaktives)
# drei-Wege Merge gemacht werden kann. Das Kommando muss die vier Argumente für
# Dateinamen entgegennehmen.
#
#    $THREE_WAY_MERGE_CMD {mine} {yours} {ancestor} {merged}
#
#THREE_WAY_MERGE_CMD=merge3FilesWithEmacs

# MERGE_CMD: Kommando oder Funktion mit der ein (interaktiver) Merge gemacht
# werden kann. Das Kommando muss die drei Argumente für Dateinamen
# entgegennehmen.
#
#     $MERGE_CMD {file_a} {file_b} {merged}
#
#MERGE_CMD=merge2FilesWithEmacs

# DIFF_CMD: Kommando oder Funktion mit der ein diff angezeigt werden soll. Im
# Default wird ``colordiff`` verwendet, wenn das nicht vorhanden ist, dann wird
# das ganz normale ``diff`` verwendet.
#
#DIFF_CMD=colordiff

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
    exit
else
    source "${REPO_ROOT}/tool_config.sh"
fi

if [[ ! -r "${LINUX_SRC_TREE}" ]]; then
    echo "ERROR: can't find linux source at: ${LINUX_SRC_TREE}"
    exit
fi

if [[ ! -e "${SCRIPT_FOLDER}/common.sh" ]]; then
    echo "ERROR: can't source file common.sh"
    exit
else
   source ${SCRIPT_FOLDER}/common.sh
   checkEnviroment
fi

