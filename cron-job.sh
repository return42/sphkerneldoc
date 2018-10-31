#!/usr/bin/env bash
# -*- coding: utf-8; mode: sh -*-

PATH=~/.local/bin:/usr/bin:/bin
source $(dirname ${BASH_SOURCE[0]})/utils/site-bash/setup.sh

## ==============================================================================
## cron job to build & dist project / repository.
## ==============================================================================
##
## The cron-job checks if the conditions for a new build are fulfilled and
## triggers a new build process if necessary. In the cron-tab you can call the
## job every 15min::
##
##   */15 * * * * /share/sphkerneldoc/cron-job.sh  >> ~/sphkerneldoc-cron.LOG  2>&1
##
## In Apache, the site configuration could look something like this::
##
##   Alias /prj /var/www/prj
##   <Directory /var/www/prj>
##
##       Require all granted
##
##       Order deny,allow
##       Deny from all
##       Allow from all
##       AllowOverride None
##
##       <IfModule mod_autoindex.c>
##           Options +Indexes +FollowSymLinks
##
##           HeaderName /chrome/header.shtml
##           ReadmeName /chrome/footer.shtml
##       </IfModule>
## </Directory>
##
##
## PRJ_NAME: the short-name of this project
##
PRJ_NAME="sphkerneldoc"

## The REPO_DIST folder contains all build products that are synchronized 1:1 to
## RSYNC_DEST. The folder can be viewed via the ONLINE_URL.

REPO_DIST="${REPO_ROOT}/dist"
ONLINE_URL="https://darmarit.cloud/prj/${PRJ_NAME}"
RSYNC_DEST="/var/www/prj/${PRJ_NAME}"
#RSYNC_DEST="user@remote:/var/www/prj/${PRJ_NAME}"

# BUILD variables

BUILD_STAMP=$(/bin/date +%Y_%m_%d-%H_%M_%S)
LOGFILE="${REPO_DIST}/${PRJ_NAME}-build.LOG-${BUILD_STAMP}.txt"

BUILD_STATE_FAILED="(re-) build failed"
BUILD_STATE_SUCCEED="(re-) build succeed"
BUILD_STATE_NONE="build is up-to-date"
BUILD_STATE=$BUILD_STATE_FAILED
BUILD_START=""
BUILD_END=""
BUILD_HEADER=""

ERRORS=()
BUILD_EXIT_CODE=0
RSYNC_EXIT_CODE=0

# ----------------------------------------------------------------------------
build_cmd(){
# ----------------------------------------------------------------------------

    make clean all-HTML books.man books.pdf
    #make clean all-reST all-HTML books.man books.pdf
    #rm -rf linux_src_doc
    #git checkout linux_src_doc
}

# ----------------------------------------------------------------------------
rsync_cmd(){
    rstHeading 'SYNC ...' chapter-nc
# ----------------------------------------------------------------------------

    rstBlock "destination: ${RSYNC_DEST}"
    rsync -av "${REPO_DIST}/" "${RSYNC_DEST}/"
    RSYNC_EXIT_CODE=$?
    if [ $RSYNC_EXIT_CODE != 0 ]; then
	ERRORS+=("rsync failed" )
    fi
}

# ----------------------------------------------------------------------------
build_repo(){
    rstHeading "build: ${ONLINE_URL} || ${BUILD_STAMP}" part-nc
# ----------------------------------------------------------------------------

    BUILD_START=`date`
    pushd "$REPO_ROOT" > /dev/null

    git checkout master > /dev/null 2>&1
    git fetch origin master  > /dev/null 2>&1

    if [ `git rev-list HEAD...origin/master --count` != 0 ] ; then
        rstBlock 'master branch has been updated // new build ...'

        rstHeading 'CHANGES ...' chapter-nc
	echo
	git diff master origin/master

        rstHeading 'MERGE ...' chapter-nc
	echo
	git merge origin/master

	rstHeading 'BUILD ...' chapter-nc
	echo
	build_cmd
	BUILD_EXIT_CODE=$?
	if [ $BUILD_EXIT_CODE == 0 ]; then
	    BUILD_STATE="$BUILD_STATE_SUCCEED"
	    rsync_cmd
	else
	    BUILD_STATE="$BUILD_STATE_FAILED"
	    ERRORS+=("$BUILD_STATE" )
	fi

    else
        rstBlock 'reposetory is up-to-date / no need to build again.'
	BUILD_EXIT_CODE=0
	BUILD_STATE="${BUILD_STATE_NONE}"
    fi
    BUILD_END=`date`
    popd > /dev/null

    return $BUILD_EXIT_CODE
}

# ----------------------------------------------------------------------------
_add_header(){
# ----------------------------------------------------------------------------
    local _STATE="ERROR"
    rm -f "${LOGFILE}.temp"

    [[ ${RSYNC_EXIT_CODE} == 0 &&  ${BUILD_EXIT_CODE} == 0 ]] && _STATE="OK"

    echo "\
==============================================================================
$(hostname): [$_STATE] build **$PRJ_NAME** ($(date))
==============================================================================

  build state: ${BUILD_STATE}
        start: ${BUILD_START}
          end: ${BUILD_END}

  rsync dest: ${RSYNC_DEST}
        exit: ${RSYNC_EXIT_CODE}" >> "${LOGFILE}.temp"

    for ((i = 0; i < ${#ERRORS[@]}; i++)); do
	echo "ERROR $i: '${ERRORS[i]}'" >> "${LOGFILE}.temp"
    done
    cat "${LOGFILE}" >> "${LOGFILE}.temp"
    cat "${LOGFILE}.temp" > "${LOGFILE}"
    rm -f "${LOGFILE}.temp"
}

# ----------------------------------------------------------------------------
main () {
# ----------------------------------------------------------------------------

    rm -f "${LOGFILE}"
    mkdir -p "${REPO_DIST}"
    echo "build-log: ${LOGFILE}"
    build_repo >>"${LOGFILE}" 2>&1

    echo "build-state: [${BUILD_EXIT_CODE}] ${BUILD_STATE}"
    echo "rsync: [${RSYNC_EXIT_CODE}]"

    _add_header

    if [[ $BUILD_STATE == $BUILD_STATE_SUCCEED ]]; then
	rsync -a "${LOGFILE}" "${RSYNC_DEST}/last-build.LOG"
    fi
    exit $EXIT_CODE
}

# ==============================================================================
main $*
# ==============================================================================
