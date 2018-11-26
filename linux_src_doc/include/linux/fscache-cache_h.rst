.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/fscache-cache.h

.. _`fscache_get_retrieval`:

fscache_get_retrieval
=====================

.. c:function:: struct fscache_retrieval *fscache_get_retrieval(struct fscache_retrieval *op)

    Get an extra reference on a retrieval operation

    :param op:
        The retrieval operation to get a reference on
    :type op: struct fscache_retrieval \*

.. _`fscache_get_retrieval.description`:

Description
-----------

Get an extra reference on a retrieval operation.

.. _`fscache_enqueue_retrieval`:

fscache_enqueue_retrieval
=========================

.. c:function:: void fscache_enqueue_retrieval(struct fscache_retrieval *op)

    Enqueue a retrieval operation for processing

    :param op:
        The retrieval operation affected
    :type op: struct fscache_retrieval \*

.. _`fscache_enqueue_retrieval.description`:

Description
-----------

Enqueue a retrieval operation for processing by the FS-Cache thread pool.

.. _`fscache_retrieval_complete`:

fscache_retrieval_complete
==========================

.. c:function:: void fscache_retrieval_complete(struct fscache_retrieval *op, int n_pages)

    Record (partial) completion of a retrieval

    :param op:
        The retrieval operation affected
    :type op: struct fscache_retrieval \*

    :param n_pages:
        The number of pages to account for
    :type n_pages: int

.. _`fscache_put_retrieval`:

fscache_put_retrieval
=====================

.. c:function:: void fscache_put_retrieval(struct fscache_retrieval *op)

    Drop a reference to a retrieval operation

    :param op:
        The retrieval operation affected
    :type op: struct fscache_retrieval \*

.. _`fscache_put_retrieval.description`:

Description
-----------

Drop a reference to a retrieval operation.

.. _`fscache_object_destroyed`:

fscache_object_destroyed
========================

.. c:function:: void fscache_object_destroyed(struct fscache_cache *cache)

    Note destruction of an object in a cache

    :param cache:
        The cache from which the object came
    :type cache: struct fscache_cache \*

.. _`fscache_object_destroyed.description`:

Description
-----------

Note the destruction and deallocation of an object record in a cache.

.. _`fscache_object_lookup_error`:

fscache_object_lookup_error
===========================

.. c:function:: void fscache_object_lookup_error(struct fscache_object *object)

    Note an object encountered an error

    :param object:
        The object on which the error was encountered
    :type object: struct fscache_object \*

.. _`fscache_object_lookup_error.description`:

Description
-----------

Note that an object encountered a fatal error (usually an I/O error) and
that it should be withdrawn as soon as possible.

.. _`fscache_set_store_limit`:

fscache_set_store_limit
=======================

.. c:function:: void fscache_set_store_limit(struct fscache_object *object, loff_t i_size)

    Set the maximum size to be stored in an object

    :param object:
        The object to set the maximum on
    :type object: struct fscache_object \*

    :param i_size:
        The limit to set in bytes
    :type i_size: loff_t

.. _`fscache_set_store_limit.description`:

Description
-----------

Set the maximum size an object is permitted to reach, implying the highest
byte that may be written.  Intended to be called by the \ :c:func:`attr_changed`\  op.

See Documentation/filesystems/caching/backend-api.txt for a complete
description.

.. _`fscache_end_io`:

fscache_end_io
==============

.. c:function:: void fscache_end_io(struct fscache_retrieval *op, struct page *page, int error)

    End a retrieval operation on a page

    :param op:
        The FS-Cache operation covering the retrieval
    :type op: struct fscache_retrieval \*

    :param page:
        The page that was to be fetched
    :type page: struct page \*

    :param error:
        The error code (0 if successful)
    :type error: int

.. _`fscache_end_io.description`:

Description
-----------

Note the end of an operation to retrieve a page, as covered by a particular
operation record.

.. _`fscache_use_cookie`:

fscache_use_cookie
==================

.. c:function:: bool fscache_use_cookie(struct fscache_object *object)

    Request usage of cookie attached to an object

    :param object:
        Object description
    :type object: struct fscache_object \*

.. _`fscache_use_cookie.description`:

Description
-----------

Request usage of the cookie attached to an object.  NULL is returned if the
relinquishment had reduced the cookie usage count to 0.

.. _`fscache_unuse_cookie`:

fscache_unuse_cookie
====================

.. c:function:: void fscache_unuse_cookie(struct fscache_object *object)

    Cease usage of cookie attached to an object

    :param object:
        Object description
    :type object: struct fscache_object \*

.. _`fscache_unuse_cookie.description`:

Description
-----------

Cease usage of the cookie attached to an object.  When the users count
reaches zero then the cookie relinquishment will be permitted to proceed.

.. This file was automatic generated / don't edit.

