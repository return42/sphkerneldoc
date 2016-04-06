
.. _API-drm-do-get-edid:

===============
drm_do_get_edid
===============

*man drm_do_get_edid(9)*

*4.6.0-rc1*

get EDID data using a custom EDID block read function


Synopsis
========

.. c:function:: struct edid ⋆ drm_do_get_edid( struct drm_connector * connector, int (*get_edid_block) void *data, u8 *buf, unsigned int block, size_t len, void * data )

Arguments
=========

``connector``
    connector we're probing

``get_edid_block``
    EDID block read function

``data``
    private data passed to the block read function


Description
===========

When the I2C adapter connected to the DDC bus is hidden behind a device that exposes a different interface to read EDID blocks this function can be used to get EDID data using a
custom block read function.

As in the general case the DDC bus is accessible by the kernel at the I2C level, drivers must make all reasonable efforts to expose it as an I2C adapter and use ``drm_get_edid``
instead of abusing this function.


Return
======

Pointer to valid EDID or NULL if we couldn't find any.
