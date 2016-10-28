.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/char/sclp_ftp.c

.. _`sclp_ftp_txcb`:

sclp_ftp_txcb
=============

.. c:function:: void sclp_ftp_txcb(struct sclp_req *req, void *data)

    Diagnostic Test FTP services SCLP command callback

    :param struct sclp_req \*req:
        *undescribed*

    :param void \*data:
        *undescribed*

.. _`sclp_ftp_rxcb`:

sclp_ftp_rxcb
=============

.. c:function:: void sclp_ftp_rxcb(struct evbuf_header *evbuf)

    Diagnostic Test FTP services receiver event callback

    :param struct evbuf_header \*evbuf:
        *undescribed*

.. _`sclp_ftp_et7`:

sclp_ftp_et7
============

.. c:function:: int sclp_ftp_et7(const struct hmcdrv_ftp_cmdspec *ftp)

    start a Diagnostic Test FTP Service SCLP request

    :param const struct hmcdrv_ftp_cmdspec \*ftp:
        pointer to FTP descriptor

.. _`sclp_ftp_et7.return`:

Return
------

0 on success, else a (negative) error code

.. _`sclp_ftp_cmd`:

sclp_ftp_cmd
============

.. c:function:: ssize_t sclp_ftp_cmd(const struct hmcdrv_ftp_cmdspec *ftp, size_t *fsize)

    executes a HMC related SCLP Diagnose (ET7) FTP command

    :param const struct hmcdrv_ftp_cmdspec \*ftp:
        pointer to FTP command specification

    :param size_t \*fsize:
        return of file size (or NULL if undesirable)

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

    :param  void:
        no arguments

.. _`sclp_ftp_shutdown`:

sclp_ftp_shutdown
=================

.. c:function:: void sclp_ftp_shutdown( void)

    shutdown of FTP services, when running on LPAR

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.

