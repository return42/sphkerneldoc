.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/char/hmcdrv_cache.c

.. _`hmcdrv_cache_entry`:

struct hmcdrv_cache_entry
=========================

.. c:type:: struct hmcdrv_cache_entry

    file cache (only used on read/dir)

.. _`hmcdrv_cache_entry.definition`:

Definition
----------

.. code-block:: c

    struct hmcdrv_cache_entry {
        enum hmcdrv_ftp_cmdid id;
        char fname;
        size_t fsize;
        loff_t ofs;
        unsigned long timeout;
        void *content;
        size_t len;
    }

.. _`hmcdrv_cache_entry.members`:

Members
-------

id
    FTP command ID

fname
    file name

fsize
    file size

ofs
    start of content within file (-1 if no cached content)

timeout
    cache timeout in jiffies

content
    kernel-space buffer, 4k aligned

len
    size of \ ``content``\  cache (0 if caching disabled)

.. _`hmcdrv_cache_entry.description`:

Description
-----------

Notice that the first three members (id, fname, fsize) are cached on all
read/dir requests. But content is cached only under some preconditions.
Uncached content is signalled by a negative value of \ ``ofs``\ .

.. _`hmcdrv_cache_get`:

hmcdrv_cache_get
================

.. c:function:: ssize_t hmcdrv_cache_get(const struct hmcdrv_ftp_cmdspec *ftp)

    looks for file data/content in read cache

    :param const struct hmcdrv_ftp_cmdspec \*ftp:
        pointer to FTP command specification

.. _`hmcdrv_cache_get.return`:

Return
------

number of bytes read from cache or a negative number if nothing
in content cache (for the file/cmd specified in \ ``ftp``\ )

.. _`hmcdrv_cache_do`:

hmcdrv_cache_do
===============

.. c:function:: ssize_t hmcdrv_cache_do(const struct hmcdrv_ftp_cmdspec *ftp, hmcdrv_cache_ftpfunc func)

    do a HMC drive CD/DVD transfer with cache update

    :param const struct hmcdrv_ftp_cmdspec \*ftp:
        pointer to FTP command specification

    :param hmcdrv_cache_ftpfunc func:
        FTP transfer function to be used

.. _`hmcdrv_cache_do.return`:

Return
------

number of bytes read/written or a (negative) error code

.. _`hmcdrv_cache_cmd`:

hmcdrv_cache_cmd
================

.. c:function:: ssize_t hmcdrv_cache_cmd(const struct hmcdrv_ftp_cmdspec *ftp, hmcdrv_cache_ftpfunc func)

    perform a cached HMC drive CD/DVD transfer

    :param const struct hmcdrv_ftp_cmdspec \*ftp:
        pointer to FTP command specification

    :param hmcdrv_cache_ftpfunc func:
        FTP transfer function to be used

.. _`hmcdrv_cache_cmd.attention`:

Attention
---------

Notice that this function is not reentrant - so the caller
must ensure exclusive execution.

.. _`hmcdrv_cache_cmd.return`:

Return
------

number of bytes read/written or a (negative) error code

.. _`hmcdrv_cache_startup`:

hmcdrv_cache_startup
====================

.. c:function:: int hmcdrv_cache_startup(size_t cachesize)

    startup of HMC drive cache

    :param size_t cachesize:
        cache size

.. _`hmcdrv_cache_startup.return`:

Return
------

0 on success, else a (negative) error code

.. _`hmcdrv_cache_shutdown`:

hmcdrv_cache_shutdown
=====================

.. c:function:: void hmcdrv_cache_shutdown( void)

    shutdown of HMC drive cache

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.

