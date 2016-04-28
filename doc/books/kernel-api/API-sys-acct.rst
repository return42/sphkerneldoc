.. -*- coding: utf-8; mode: rst -*-

.. _API-sys-acct:

========
sys_acct
========

*man sys_acct(9)*

*4.6.0-rc5*

enable/disable process accounting


Synopsis
========

.. c:function:: long sys_acct( const char __user * name )

Arguments
=========

``name``
    file name for accounting records or NULL to shutdown accounting


Description
===========

Returns 0 for success or negative errno values for failure.

``sys_acct`` is the only system call needed to implement process
accounting. It takes the name of the file where accounting records
should be written. If the filename is NULL, accounting will be shutdown.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
