.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/kernfs.h

.. _`kernfs_enable_ns`:

kernfs_enable_ns
================

.. c:function:: void kernfs_enable_ns(struct kernfs_node *kn)

    enable namespace under a directory

    :param kn:
        directory of interest, should be empty
    :type kn: struct kernfs_node \*

.. _`kernfs_enable_ns.description`:

Description
-----------

This is to be called right after \ ``kn``\  is created to enable namespace
under it.  All children of \ ``kn``\  must have non-NULL namespace tags and
only the ones which match the super_block's tag will be visible.

.. _`kernfs_ns_enabled`:

kernfs_ns_enabled
=================

.. c:function:: bool kernfs_ns_enabled(struct kernfs_node *kn)

    test whether namespace is enabled

    :param kn:
        the node to test
    :type kn: struct kernfs_node \*

.. _`kernfs_ns_enabled.description`:

Description
-----------

Test whether namespace filtering is enabled for the children of \ ``ns``\ .

.. _`kernfs_path`:

kernfs_path
===========

.. c:function:: int kernfs_path(struct kernfs_node *kn, char *buf, size_t buflen)

    build full path of a given node

    :param kn:
        kernfs_node of interest
    :type kn: struct kernfs_node \*

    :param buf:
        buffer to copy \ ``kn``\ 's name into
    :type buf: char \*

    :param buflen:
        size of \ ``buf``\ 
    :type buflen: size_t

.. _`kernfs_path.description`:

Description
-----------

If \ ``kn``\  is NULL result will be "(null)".

Returns the length of the full path.  If the full length is equal to or
greater than \ ``buflen``\ , \ ``buf``\  contains the truncated path with the trailing
'\0'.  On error, -errno is returned.

.. This file was automatic generated / don't edit.

