
.. _API-drm-release:

===========
drm_release
===========

*man drm_release(9)*

*4.6.0-rc1*

release method for DRM file


Synopsis
========

.. c:function:: int drm_release( struct inode * inode, struct file * filp )

Arguments
=========

``inode``
    device inode

``filp``
    file pointer.


Description
===========

This function must be used by drivers as their . ``release`` #file_operations method. It frees any resources associated with the open file, and if this is the last open file for
the DRM device also proceeds to call ``drm_lastclose``.


RETURNS
=======

Always succeeds and returns 0.
