
.. _API-rio-basic-attach:

================
rio_basic_attach
================

*man rio_basic_attach(9)*

*4.6.0-rc1*


Synopsis
========

.. c:function:: int rio_basic_attach( void )

Arguments
=========

``void``
    no arguments


Description
===========

When this enumeration/discovery method is loaded as a module this function registers its specific enumeration and discover routines for all available RapidIO mport devices. The
“scan” command line parameter controls ability of the module to start RapidIO enumeration/discovery automatically.

Returns 0 for success or -EIO if unable to register itself.

This enumeration/discovery method cannot be unloaded and therefore does not provide a matching cleanup_module routine.
