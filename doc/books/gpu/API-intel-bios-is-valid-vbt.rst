
.. _API-intel-bios-is-valid-vbt:

=======================
intel_bios_is_valid_vbt
=======================

*man intel_bios_is_valid_vbt(9)*

*4.6.0-rc1*

does the given buffer contain a valid VBT


Synopsis
========

.. c:function:: bool intel_bios_is_valid_vbt( const void * buf, size_t size )

Arguments
=========

``buf``
    pointer to a buffer to validate

``size``
    size of the buffer


Description
===========

Returns true on valid VBT.
