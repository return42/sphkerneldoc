
.. _API-dmi-get-system-info:

===================
dmi_get_system_info
===================

*man dmi_get_system_info(9)*

*4.6.0-rc1*

return DMI data value


Synopsis
========

.. c:function:: const char ⋆ dmi_get_system_info( int field )

Arguments
=========

``field``
    data index (see enum dmi_field)


Description
===========

Returns one DMI data value, can be used to perform complex DMI data checks.
