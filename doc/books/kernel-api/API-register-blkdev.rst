
.. _API-register-blkdev:

===============
register_blkdev
===============

*man register_blkdev(9)*

*4.6.0-rc1*

register a new block device


Synopsis
========

.. c:function:: int register_blkdev( unsigned int major, const char * name )

Arguments
=========

``major``
    the requested major device number [1..255]. If ``major``\ =0, try to allocate any unused major number.

``name``
    the name of the new block device as a zero terminated string


Description
===========

The ``name`` must be unique within the system.

The return value depends on the ``major`` input parameter. - if a major device number was requested in range [1..255] then the function returns zero on success, or a negative error
code - if any unused major number was requested with ``major``\ =0 parameter then the return value is the allocated major number in range [1..255] or a negative error code
otherwise
