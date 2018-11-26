.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/char/sclp_ftp.c

.. _`sclp_ftp_txcb`:

sclp_ftp_txcb
=============

.. c:function:: void sclp_ftp_txcb(struct sclp_req *req, void *data)

    Diagnostic Test FTP services SCLP command callback

    :param req:
        *undescribed*
    :type req: struct sclp_req \*

    :param data:
        *undescribed*
    :type data: void \*

.. _`sclp_ftp_rxcb`:

sclp_ftp_rxcb
=============

.. c:function:: void sclp_ftp_rxcb(struct evbuf_header *evbuf)

    Diagnostic Test FTP services receiver event callback

    :param evbuf:
        *undescribed*
    :type evbuf: struct evbuf_header \*

.. _`sclp_ftp_et7`:

sclp_ftp_et7
============

.. c:function:: int sclp_ftp_et7(const struct hmcdrv_ftp_cmdspec *ftp)

    start a Diagnostic Test FTP Service SCLP request

    :param ftp:
        pointer to FTP descriptor
    :type ftp: const struct hmcdrv_ftp_cmdspec \*

.. _`sclp_ftp_et7.return`:

Return
------

0 on success, else a (negative) error code

.. _`sclp_ftp_cmd`:

sclp_ftp_cmd
============

.. c:function:: ssize_t sclp_ftp_cmd(const struct hmcdrv_ftp_cmdspec *ftp, size_t *fsize)

    executes a HMC related SCLP Diagnose (ET7) FTP command

    :param ftp:
        pointer to FTP command specification
    :type ftp: const struct hmcdrv_ftp_cmdspec \*

    :param fsize:
        return of file size (or NULL if undesirable)
    :type fsize: size_t \*

.. _`sclp_ftp_cmd.attention`:

Attention
---------

Notice that this function is not reentrant - so the caller
must ensure locking.

.. _`sclp_ftp_cmd.return`:

Return
------

number of bytes read/written or a (negative) error code

.. _`sclp_ftp_startup`:

sclp_ftp_startup
================

.. c:function:: int sclp_ftp_startup( void)

    startup of FTP services, when running on LPAR

    :param void:
        no arguments
    :type void: 

.. _`sclp_ftp_shutdown`:

sclp_ftp_shutdown
=================

.. c:function:: void sclp_ftp_shutdown( void)

    shutdown of FTP services, when running on LPAR

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.

