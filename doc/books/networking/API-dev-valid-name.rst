.. -*- coding: utf-8; mode: rst -*-

.. _API-dev-valid-name:

==============
dev_valid_name
==============

*man dev_valid_name(9)*

*4.6.0-rc5*

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

Network device names need to be valid file names to to allow sysfs to
work. We also disallow any kind of whitespace.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
