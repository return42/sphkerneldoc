.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/char/hmcdrv_ftp.c

.. _`hmcdrv_ftp_ops`:

struct hmcdrv_ftp_ops
=====================

.. c:type:: struct hmcdrv_ftp_ops

    HMC drive FTP operations

.. _`hmcdrv_ftp_ops.definition`:

Definition
----------

.. code-block:: c

    struct hmcdrv_ftp_ops {
        int (* startup) (void);
        void (* shutdown) (void);
        ssize_t (* transfer) (const struct hmcdrv_ftp_cmdspec *ftp,size_t *fsize);
    }

.. _`hmcdrv_ftp_ops.members`:

Members
-------

startup
    startup function

shutdown
    shutdown function

transfer
    *undescribed*

.. _`hmcdrv_ftp_cmd_getid`:

hmcdrv_ftp_cmd_getid
====================

.. c:function:: enum hmcdrv_ftp_cmdid hmcdrv_ftp_cmd_getid(const char *cmd, int len)

    determine FTP command ID from a command string

    :param const char \*cmd:
        FTP command string (NOT zero-terminated)

    :param int len:
        length of FTP command string in \ ``cmd``\ 

.. _`hmcdrv_ftp_parse`:

hmcdrv_ftp_parse
================

.. c:function:: int hmcdrv_ftp_parse(char *cmd, struct hmcdrv_ftp_cmdspec *ftp)

    HMC drive FTP command parser

    :param char \*cmd:
        FTP command string "<cmd> <filename>"

    :param struct hmcdrv_ftp_cmdspec \*ftp:
        Pointer to FTP command specification buffer (output)

.. _`hmcdrv_ftp_parse.return`:

Return
------

0 on success, else a (negative) error code

.. _`hmcdrv_ftp_do`:

hmcdrv_ftp_do
=============

.. c:function:: ssize_t hmcdrv_ftp_do(const struct hmcdrv_ftp_cmdspec *ftp)

    perform a HMC drive FTP, with data from kernel-space

    :param const struct hmcdrv_ftp_cmdspec \*ftp:
        pointer to FTP command specification

.. _`hmcdrv_ftp_do.return`:

Return
------

number of bytes read/written or a negative error code

.. _`hmcdrv_ftp_probe`:

hmcdrv_ftp_probe
================

.. c:function:: int hmcdrv_ftp_probe( void)

    probe for the HMC drive FTP service

    :param  void:
        no arguments

.. _`hmcdrv_ftp_probe.return`:

Return
------

0 if service is available, else an (negative) error code

.. _`hmcdrv_ftp_cmd`:

hmcdrv_ftp_cmd
==============

.. c:function:: ssize_t hmcdrv_ftp_cmd(char __kernel *cmd, loff_t offset, char __user *buf, size_t len)

    Perform a HMC drive FTP, with data from user-space

    :param char __kernel \*cmd:
        FTP command string "<cmd> <filename>"

    :param loff_t offset:
        file position to read/write

    :param char __user \*buf:
        user-space buffer for read/written directory/file

    :param size_t len:
        size of \ ``buf``\  (read/dir) or number of bytes to write

.. _`hmcdrv_ftp_cmd.description`:

Description
-----------

This function must not be called before \ :c:func:`hmcdrv_ftp_startup`\  was called.

.. _`hmcdrv_ftp_cmd.return`:

Return
------

number of bytes read/written or a negative error code

.. _`hmcdrv_ftp_startup`:

hmcdrv_ftp_startup
==================

.. c:function:: int hmcdrv_ftp_startup( void)

    startup of HMC drive FTP functionality for a dedicated (owner) instance

    :param  void:
        no arguments

.. _`hmcdrv_ftp_startup.return`:

Return
------

0 on success, else an (negative) error code

.. _`hmcdrv_ftp_shutdown`:

hmcdrv_ftp_shutdown
===================

.. c:function:: void hmcdrv_ftp_shutdown( void)

    shutdown of HMC drive FTP functionality for a dedicated (owner) instance

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.

