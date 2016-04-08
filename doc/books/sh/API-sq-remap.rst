
.. _API-sq-remap:

========
sq_remap
========

*man sq_remap(9)*

*4.6.0-rc1*

Map a physical address through the Store Queues


Synopsis
========

.. c:function:: unsigned long sq_remap( unsigned long phys, unsigned int size, const char * name, pgprot_t prot )

Arguments
=========

``phys``
    Physical address of mapping.

``size``
    Length of mapping.

``name``
    User invoking mapping.

``prot``
    Protection bits.


Description
===========

Remaps the physical address ``phys`` through the next available store queue address of ``size`` length. ``name`` is logged at boot time as well as through the sysfs interface.
