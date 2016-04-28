.. -*- coding: utf-8; mode: rst -*-

.. _API---request-module:

================
__request_module
================

*man __request_module(9)*

*4.6.0-rc5*

try to load a kernel module


Synopsis
========

.. c:function:: int __request_module( bool wait, const char * fmt, ... )

Arguments
=========

``wait``
    wait (or not) for the operation to complete

``fmt``
    printf style format string for the name of the module @...:
    arguments as specified in the format string

``...``
    variable arguments


Description
===========

Load a module using the user mode module loader. The function returns
zero on success or a negative errno code or positive exit code from
“modprobe” on failure. Note that a successful module load does not mean
the module did not then unload and exit on an error of its own. Callers
must check that the service they requested is now available not blindly
invoke it.

If module auto-loading support is disabled then this function becomes a
no-operation.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
