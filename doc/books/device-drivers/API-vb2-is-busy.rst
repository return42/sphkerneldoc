
.. _API-vb2-is-busy:

===========
vb2_is_busy
===========

*man vb2_is_busy(9)*

*4.6.0-rc1*

return busy status of the queue


Synopsis
========

.. c:function:: bool vb2_is_busy( struct vb2_queue * q )

Arguments
=========

``q``
    videobuf queue


Description
===========

This function checks if queue has any buffers allocated.
