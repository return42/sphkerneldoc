
.. _API-drm-open:

========
drm_open
========

*man drm_open(9)*

*4.6.0-rc1*

open method for DRM file


Synopsis
========

.. c:function:: int drm_open( struct inode * inode, struct file * filp )

Arguments
=========

``inode``
    device inode

``filp``
    file pointer.


Description
===========

This function must be used by drivers as their . ``open`` #file_operations method. It looks up the correct DRM device and instantiates all the per-file resources for it.


RETURNS
=======

0 on success or negative errno value on falure.
