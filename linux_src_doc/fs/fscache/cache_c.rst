.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/fscache/cache.c

.. _`fscache_init_cache`:

fscache_init_cache
==================

.. c:function:: void fscache_init_cache(struct fscache_cache *cache, const struct fscache_cache_ops *ops, const char *idfmt,  ...)

    Initialise a cache record

    :param struct fscache_cache \*cache:
        The cache record to be initialised

    :param const struct fscache_cache_ops \*ops:
        The cache operations to be installed in that record

    :param const char \*idfmt:
        Format string to define identifier

    :param ... :
        sprintf-style arguments

.. _`fscache_init_cache.description`:

Description
-----------

Initialise a record of a cache and fill in the name.

See Documentation/filesystems/caching/backend-api.txt for a complete
description.

.. _`fscache_add_cache`:

fscache_add_cache
=================

.. c:function:: int fscache_add_cache(struct fscache_cache *cache, struct fscache_object *ifsdef, const char *tagname)

    Declare a cache as being open for business

    :param struct fscache_cache \*cache:
        The record describing the cache

    :param struct fscache_object \*ifsdef:
        The record of the cache object describing the top-level index

    :param const char \*tagname:
        The tag describing this cache

.. _`fscache_add_cache.description`:

Description
-----------

Add a cache to the system, making it available for netfs's to use.

See Documentation/filesystems/caching/backend-api.txt for a complete
description.

.. _`fscache_io_error`:

fscache_io_error
================

.. c:function:: void fscache_io_error(struct fscache_cache *cache)

    Note a cache I/O error

    :param struct fscache_cache \*cache:
        The record describing the cache

.. _`fscache_io_error.description`:

Description
-----------

Note that an I/O error occurred in a cache and that it should no longer be
used for anything.  This also reports the error into the kernel log.

See Documentation/filesystems/caching/backend-api.txt for a complete
description.

.. _`fscache_withdraw_cache`:

fscache_withdraw_cache
======================

.. c:function:: void fscache_withdraw_cache(struct fscache_cache *cache)

    Withdraw a cache from the active service

    :param struct fscache_cache \*cache:
        The record describing the cache

.. _`fscache_withdraw_cache.description`:

Description
-----------

Withdraw a cache from service, unbinding all its cache objects from the
netfs cookies they're currently representing.

See Documentation/filesystems/caching/backend-api.txt for a complete
description.

.. This file was automatic generated / don't edit.

