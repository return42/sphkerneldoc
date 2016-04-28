.. -*- coding: utf-8; mode: rst -*-

.. _API-dmi-check-system:

================
dmi_check_system
================

*man dmi_check_system(9)*

*4.6.0-rc5*

check system DMI data


Synopsis
========

.. c:function:: int dmi_check_system( const struct dmi_system_id * list )

Arguments
=========

``list``
    array of dmi_system_id structures to match against All non-null
    elements of the list must match their slot's (field index's) data
    (i.e., each list string must be a substring of the specified DMI
    slot's string data) to be considered a successful match.


Description
===========

Walk the blacklist table running matching functions until someone
returns non zero or we hit the end. Callback function is called for each
successful match. Returns the number of matches.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
