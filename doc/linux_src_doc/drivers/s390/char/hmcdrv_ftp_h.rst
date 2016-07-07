.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/char/hmcdrv_ftp.h

.. _`hmcdrv_ftp_cmdid`:

enum hmcdrv_ftp_cmdid
=====================

.. c:type:: enum hmcdrv_ftp_cmdid

    HMC drive FTP commands

.. _`hmcdrv_ftp_cmdid.definition`:

Definition
----------

.. code-block:: c

    enum hmcdrv_ftp_cmdid {
        HMCDRV_FTP_NOOP,
        HMCDRV_FTP_GET,
        HMCDRV_FTP_PUT,
        HMCDRV_FTP_APPEND,
        HMCDRV_FTP_DIR,
        HMCDRV_FTP_NLIST,
        HMCDRV_FTP_DELETE,
        HMCDRV_FTP_CANCEL
    };

.. _`hmcdrv_ftp_cmdid.constants`:

Constants
---------

HMCDRV_FTP_NOOP
    do nothing (only for probing)

HMCDRV_FTP_GET
    read a file

HMCDRV_FTP_PUT
    (over-) write a file

HMCDRV_FTP_APPEND
    append to a file

HMCDRV_FTP_DIR
    list directory long (ls -l)

HMCDRV_FTP_NLIST
    list files, no directories (name list)

HMCDRV_FTP_DELETE
    delete a file

HMCDRV_FTP_CANCEL
    cancel operation (SCLP/LPAR only)

.. _`hmcdrv_ftp_cmdspec`:

struct hmcdrv_ftp_cmdspec
=========================

.. c:type:: struct hmcdrv_ftp_cmdspec

    FTP command specification

.. _`hmcdrv_ftp_cmdspec.definition`:

Definition
----------

.. code-block:: c

    struct hmcdrv_ftp_cmdspec {
        enum hmcdrv_ftp_cmdid id;
        loff_t ofs;
        const char *fname;
        void __kernel *buf;
        size_t len;
    }

.. _`hmcdrv_ftp_cmdspec.members`:

Members
-------

id
    FTP command ID

ofs
    offset in file

fname
    filename (ASCII), null-terminated

buf
    kernel-space transfer data buffer, 4k aligned

len
    (max) number of bytes to transfer from/to \ ``buf``\ 

.. This file was automatic generated / don't edit.

