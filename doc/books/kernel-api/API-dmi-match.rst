
.. _API-dmi-match:

=========
dmi_match
=========

*man dmi_match(9)*

*4.6.0-rc1*

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
