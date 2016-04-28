.. -*- coding: utf-8; mode: rst -*-

.. _API-security-module-enable:

======================
security_module_enable
======================

*man security_module_enable(9)*

*4.6.0-rc5*

Load given security module on boot ?


Synopsis
========

.. c:function:: int security_module_enable( const char * module )

Arguments
=========

``module``
    the name of the module


Description
===========

Each LSM must pass this method before registering its own operations to
avoid security registration races. This method may also be used to check
if your LSM is currently loaded during kernel initialization.


Return true if
==============

-The passed LSM is the one chosen by user at boot time, -or the passed
LSM is configured as the default and the user did not choose an
alternate LSM at boot time. Otherwise, return false.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
