
.. _API-securityfs-create-dir:

=====================
securityfs_create_dir
=====================

*man securityfs_create_dir(9)*

*4.6.0-rc1*

create a directory in the securityfs filesystem


Synopsis
========

.. c:function:: struct dentry ⋆ securityfs_create_dir( const char * name, struct dentry * parent )

Arguments
=========

``name``
    a pointer to a string containing the name of the directory to create.

``parent``
    a pointer to the parent dentry for this file. This should be a directory dentry if set. If this parameter is ``NULL``, then the directory will be created in the root of the
    securityfs filesystem.


Description
===========

This function creates a directory in securityfs with the given ``name``.

This function returns a pointer to a dentry if it succeeds. This pointer must be passed to the ``securityfs_remove`` function when the file is to be removed (no automatic cleanup
happens if your module is unloaded, you are responsible here). If an error occurs, ``NULL`` will be returned.

If securityfs is not enabled in the kernel, the value ``-ENODEV`` is returned. It is not wise to check for this value, but rather, check for ``NULL`` or !\ ``NULL`` instead as to
eliminate the need for #ifdef in the calling code.
