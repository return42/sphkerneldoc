
.. _API-dev-valid-name:

==============
dev_valid_name
==============

*man dev_valid_name(9)*

*4.6.0-rc1*

check if name is okay for network device


Synopsis
========

.. c:function:: bool dev_valid_name( const char * name )

Arguments
=========

``name``
    name string


Description
===========

Network device names need to be valid file names to to allow sysfs to work. We also disallow any kind of whitespace.
