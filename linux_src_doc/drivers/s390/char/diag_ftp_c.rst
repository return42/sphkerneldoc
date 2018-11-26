.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/char/diag_ftp.c

.. _`diag_ftp_ldfpl`:

struct diag_ftp_ldfpl
=====================

.. c:type:: struct diag_ftp_ldfpl

    load file FTP parameter list (LDFPL)

.. _`diag_ftp_ldfpl.definition`:

Definition
----------

.. code-block:: c

    struct diag_ftp_ldfpl {
        u64 bufaddr;
        u64 buflen;
        u64 offset;
        u64 intparm;
        u64 transferred;
        u64 fsize;
        u64 failaddr;
        u64 spare;
        u8 fident[HMCDRV_FTP_FIDENT_MAX];
    }

.. _`diag_ftp_ldfpl.members`:

Members
-------

bufaddr
    real buffer address (at 4k boundary)

buflen
    length of buffer

offset
    dir/file offset

intparm
    interruption parameter (unused)

transferred
    bytes transferred

fsize
    file size, filled on GET

failaddr
    failing address

spare
    padding

fident
    file name - ASCII

.. _`diag_ftp_handler`:

diag_ftp_handler
================

.. c:function:: void diag_ftp_handler(struct ext_code extirq, unsigned int param32, unsigned long param64)

    FTP services IRQ handler

    :param extirq:
        external interrupt (sub-) code
    :type extirq: struct ext_code

    :param param32:
        32-bit interruption parameter from \ :c:type:`struct diag_ftp_ldfpl <diag_ftp_ldfpl>`\ 
    :type param32: unsigned int

    :param param64:
        unused (for 64-bit interrupt parameters)
    :type param64: unsigned long

.. _`diag_ftp_2c4`:

diag_ftp_2c4
============

.. c:function:: int diag_ftp_2c4(struct diag_ftp_ldfpl *fpl, enum hmcdrv_ftp_cmdid cmd)

    DIAGNOSE X'2C4' service call

    :param fpl:
        pointer to prepared LDFPL
    :type fpl: struct diag_ftp_ldfpl \*

    :param cmd:
        FTP command to be executed
    :type cmd: enum hmcdrv_ftp_cmdid

.. _`diag_ftp_2c4.description`:

Description
-----------

Performs a DIAGNOSE X'2C4' call with (input/output) FTP parameter list
\ ``fpl``\  and FTP function code \ ``cmd``\ . In case of an error the function does
nothing and returns an (negative) error code.

.. _`diag_ftp_2c4.notes`:

Notes
-----

1. This function only initiates a transfer, so the caller must wait
for completion (asynchronous execution).
2. The FTP parameter list \ ``fpl``\  must be aligned to a double-word boundary.
3. fpl->bufaddr must be a real address, 4k aligned

.. _`diag_ftp_cmd`:

diag_ftp_cmd
============

.. c:function:: ssize_t diag_ftp_cmd(const struct hmcdrv_ftp_cmdspec *ftp, size_t *fsize)

    executes a DIAG X'2C4' FTP command, targeting a HMC

    :param ftp:
        pointer to FTP command specification
    :type ftp: const struct hmcdrv_ftp_cmdspec \*

    :param fsize:
        return of file size (or NULL if undesirable)
    :type fsize: size_t \*

.. _`diag_ftp_cmd.attention`:

Attention
---------

Notice that this function is not reentrant - so the caller
must ensure locking.

.. _`diag_ftp_cmd.return`:

Return
------

number of bytes read/written or a (negative) error code

.. _`diag_ftp_startup`:

diag_ftp_startup
================

.. c:function:: int diag_ftp_startup( void)

    startup of FTP services, when running on z/VM

    :param void:
        no arguments
    :type void: 

.. _`diag_ftp_startup.return`:

Return
------

0 on success, else an (negative) error code

.. _`diag_ftp_shutdown`:

diag_ftp_shutdown
=================

.. c:function:: void diag_ftp_shutdown( void)

    shutdown of FTP services, when running on z/VM

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.

