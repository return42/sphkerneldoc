
.. _API-bdgrab:

======
bdgrab
======

*man bdgrab(9)*

*4.6.0-rc1*

- Grab a reference to an already referenced block device


Synopsis
========

.. c:function:: struct block_device ⋆ bdgrab( struct block_device * bdev )

Arguments
=========

``bdev``
    Block device to grab a reference to.
