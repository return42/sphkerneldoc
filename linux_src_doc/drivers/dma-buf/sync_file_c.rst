.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma-buf/sync_file.c

.. _`sync_file_create`:

sync_file_create
================

.. c:function:: struct sync_file *sync_file_create(struct dma_fence *fence)

    creates a sync file

    :param fence:
        fence to add to the sync_fence
    :type fence: struct dma_fence \*

.. _`sync_file_create.description`:

Description
-----------

Creates a sync_file containg \ ``fence``\ . This function acquires and additional
reference of \ ``fence``\  for the newly-created \ :c:type:`struct sync_file <sync_file>`\ , if it succeeds. The
sync_file can be released with fput(sync_file->file). Returns the
sync_file or NULL in case of error.

.. _`sync_file_get_fence`:

sync_file_get_fence
===================

.. c:function:: struct dma_fence *sync_file_get_fence(int fd)

    get the fence related to the sync_file fd

    :param fd:
        sync_file fd to get the fence from
    :type fd: int

.. _`sync_file_get_fence.description`:

Description
-----------

Ensures \ ``fd``\  references a valid sync_file and returns a fence that
represents all fence in the sync_file. On error NULL is returned.

.. _`sync_file_get_name`:

sync_file_get_name
==================

.. c:function:: char *sync_file_get_name(struct sync_file *sync_file, char *buf, int len)

    get the name of the sync_file

    :param sync_file:
        sync_file to get the fence from
    :type sync_file: struct sync_file \*

    :param buf:
        destination buffer to copy sync_file name into
    :type buf: char \*

    :param len:
        available size of destination buffer.
    :type len: int

.. _`sync_file_get_name.description`:

Description
-----------

Each sync_file may have a name assigned either by the user (when merging
sync_files together) or created from the fence it contains. In the latter
case construction of the name is deferred until use, and so requires
\ :c:func:`sync_file_get_name`\ .

.. _`sync_file_get_name.return`:

Return
------

a string representing the name.

.. _`sync_file_merge`:

sync_file_merge
===============

.. c:function:: struct sync_file *sync_file_merge(const char *name, struct sync_file *a, struct sync_file *b)

    merge two sync_files

    :param name:
        name of new fence
    :type name: const char \*

    :param a:
        sync_file a
    :type a: struct sync_file \*

    :param b:
        sync_file b
    :type b: struct sync_file \*

.. _`sync_file_merge.description`:

Description
-----------

Creates a new sync_file which contains copies of all the fences in both
\ ``a``\  and \ ``b``\ .  \ ``a``\  and \ ``b``\  remain valid, independent sync_file. Returns the
new merged sync_file or NULL in case of error.

.. This file was automatic generated / don't edit.

