.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/acpi/acpi_adxl.c

.. _`adxl_get_component_names`:

adxl_get_component_names
========================

.. c:function:: const char * const *adxl_get_component_names( void)

    get list of memory component names Returns NULL terminated list of string names

    :param void:
        no arguments
    :type void: 

.. _`adxl_get_component_names.description`:

Description
-----------

Give the caller a pointer to the list of memory component names
e.g. { "SystemAddress", "ProcessorSocketId", "ChannelId", ... NULL }
Caller should count how many strings in order to allocate a buffer
for the return from \ :c:func:`adxl_decode`\ .

.. _`adxl_decode`:

adxl_decode
===========

.. c:function:: int adxl_decode(u64 addr, u64 component_values)

    ask BIOS to decode a system address to memory address

    :param addr:
        the address to decode
    :type addr: u64

    :param component_values:
        pointer to array of values for each component
        Returns 0 on success, negative error code otherwise
    :type component_values: u64

.. _`adxl_decode.description`:

Description
-----------

The index of each value returned in the array matches the index of
each component name returned by \ :c:func:`adxl_get_component_names`\ .
Components that are not defined for this address translation (e.g.
mirror channel number for a non-mirrored address) are set to ~0ull.

.. This file was automatic generated / don't edit.

