#!/usr/bin/env python3
# -*- coding: utf-8; mode: python -*-

u"""
    dbenv
    ~~~~~

    dbtools environment

    :copyright:  Copyright (C) 2016  Markus Heiser
    :license:    GPL V3.0, see LICENSE for details.
"""

from common import OS_ENV, FSPath

REPO_ROOT     = FSPath(OS_ENV.REPO_ROOT)
CACHE         = FSPath(OS_ENV.CACHE)
SCRIPT_FOLDER = FSPath(OS_ENV.SCRIPT_FOLDER)
TEMPLATES     = FSPath(OS_ENV.TEMPLATES)

DOC_FOLDER     = FSPath(OS_ENV.DOC_FOLDER)
AUTODOC_FOLDER = FSPath(OS_ENV.AUTODOC_FOLDER)
MIGRATION_FOLDER = FSPath(OS_ENV.MIGRATION_FOLDER)
LINUX_MISC_DOC = FSPath(OS_ENV.LINUX_MISC_DOC)

LINUX_SRC_TREE     = FSPath(OS_ENV.LINUX_SRC_TREE)
LINUX_DOCBOOK_ROOT = LINUX_SRC_TREE / u"Documentation" / u"DocBook"

KERNEL_DOC_SCRIPT  = FSPath(OS_ENV.KERNEL_DOC_SCRIPT)

