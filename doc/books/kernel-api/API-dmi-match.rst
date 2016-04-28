.. -*- coding: utf-8; mode: rst -*-

.. _API-dmi-match:

=========
dmi_match
=========

*man dmi_match(9)*

*4.6.0-rc5*

compare a string to the dmi field (if exists)


Synopsis
========

.. c:function:: bool dmi_match( enum dmi_field f, const char * str )

Arguments
=========

``f``
    DMI field identifier

``str``
    string to compare the DMI field to


Description
===========

Returns true if the requested field equals to the str (including NULL).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
