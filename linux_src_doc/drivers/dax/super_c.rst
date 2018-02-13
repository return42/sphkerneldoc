.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dax/super.c

.. _`__bdev_dax_supported`:

\__bdev_dax_supported
=====================

.. c:function:: int __bdev_dax_supported(struct super_block *sb, int blocksize)

    Check if the device supports dax for filesystem

    :param struct super_block \*sb:
        The superblock of the device

    :param int blocksize:
        The block size of the device

.. _`__bdev_dax_supported.description`:

Description
-----------

This is a library function for filesystems to check if the block device
can be mounted with dax option.

.. _`__bdev_dax_supported.return`:

Return
------

negative errno if unsupported, 0 if supported.

.. _`dax_device`:

struct dax_device
=================

.. c:type:: struct dax_device

    anchor object for dax services

.. _`dax_device.definition`:

Definition
----------

.. code-block:: c

    struct dax_device {
        struct hlist_node list;
        struct inode inode;
        struct cdev cdev;
        const char *host;
        void *private;
        unsigned long flags;
        const struct dax_operations *ops;
    }

.. _`dax_device.members`:

Members
-------

list
    *undescribed*

inode
    core vfs

cdev
    optional character interface for "device dax"

host
    optional name for lookups where the device path is not available

private
    dax driver private data

flags
    state and boolean properties

ops
    *undescribed*

.. _`dax_direct_access`:

dax_direct_access
=================

.. c:function:: long dax_direct_access(struct dax_device *dax_dev, pgoff_t pgoff, long nr_pages, void **kaddr, pfn_t *pfn)

    translate a device pgoff to an absolute pfn

    :param struct dax_device \*dax_dev:
        a dax_device instance representing the logical memory range

    :param pgoff_t pgoff:
        offset in pages from the start of the device to translate

    :param long nr_pages:
        number of consecutive pages caller can handle relative to \ ``pfn``\ 

    :param void \*\*kaddr:
        output parameter that returns a virtual address mapping of pfn

    :param pfn_t \*pfn:
        output parameter that returns an absolute pfn translation of \ ``pgoff``\ 

.. _`dax_direct_access.return`:

Return
------

negative errno if an error occurs, otherwise the number of
pages accessible at the device relative \ ``pgoff``\ .

.. _`dax_get_by_host`:

dax_get_by_host
===============

.. c:function:: struct dax_device *dax_get_by_host(const char *host)

    temporary lookup mechanism for filesystem-dax

    :param const char \*host:
        alternate name for the device registered by a dax driver

.. _`inode_dax`:

inode_dax
=========

.. c:function:: struct dax_device *inode_dax(struct inode *inode)

    convert a public inode into its dax_dev

    :param struct inode \*inode:
        An inode with i_cdev pointing to a dax_dev

.. _`inode_dax.description`:

Description
-----------

Note this is not equivalent to \ :c:func:`to_dax_dev`\  which is for private
internal use where we know the inode filesystem type == dax_fs_type.

.. This file was automatic generated / don't edit.

