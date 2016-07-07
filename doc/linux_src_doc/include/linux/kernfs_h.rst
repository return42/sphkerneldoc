.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/kernfs.h

.. _`kernfs_enable_ns`:

kernfs_enable_ns
================

.. c:function:: void kernfs_enable_ns(struct kernfs_node *kn)

    enable namespace under a directory

    :param struct kernfs_node \*kn:
        directory of interest, should be empty

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

    :param struct kernfs_node \*kn:
        the node to test

.. _`kernfs_ns_enabled.description`:

Description
-----------

Test whether namespace filtering is enabled for the children of \ ``ns``\ .

.. This file was automatic generated / don't edit.

