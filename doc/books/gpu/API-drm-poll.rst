.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-poll:

========
drm_poll
========

*man drm_poll(9)*

*4.6.0-rc5*

poll method for DRM file


Synopsis
========

.. c:function:: unsigned int drm_poll( struct file * filp, struct poll_table_struct * wait )

Arguments
=========

``filp``
    file pointer

``wait``
    poll waiter table


Description
===========

This function must be used by drivers as their .\ ``read``
#file_operations method iff they use DRM events for asynchronous
signalling to userspace. Since events are used by the KMS API for vblank
and page flip completion this means all modern display drivers must use
it.

See also ``drm_read``.


RETURNS
=======

Mask of POLL flags indicating the current status of the file.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
