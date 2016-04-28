.. -*- coding: utf-8; mode: rst -*-

.. _API-dmi-get-system-info:

===================
dmi_get_system_info
===================

*man dmi_get_system_info(9)*

*4.6.0-rc5*

return DMI data value


Synopsis
========

.. c:function:: const char * dmi_get_system_info( int field )

Arguments
=========

``field``
    data index (see enum dmi_field)


Description
===========

Returns one DMI data value, can be used to perform complex DMI data
checks.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
