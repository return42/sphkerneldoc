
.. _API-debugfs-create-devm-seqfile:

===========================
debugfs_create_devm_seqfile
===========================

*man debugfs_create_devm_seqfile(9)*

*4.6.0-rc1*

create a debugfs file that is bound to device.


Synopsis
========

.. c:function:: struct dentry ⋆ debugfs_create_devm_seqfile( struct device * dev, const char * name, struct dentry * parent, int (*read_fn) struct seq_file *s, void *data )

Arguments
=========

``dev``
    device related to this debugfs file.

``name``
    name of the debugfs file.

``parent``
    a pointer to the parent dentry for this file. This should be a directory dentry if set. If this parameter is ``NULL``, then the file will be created in the root of the debugfs
    filesystem.

``read_fn``
    function pointer called to print the seq_file content.
