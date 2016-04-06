
.. _API-kmsg-dump-register:

==================
kmsg_dump_register
==================

*man kmsg_dump_register(9)*

*4.6.0-rc1*

register a kernel log dumper.


Synopsis
========

.. c:function:: int kmsg_dump_register( struct kmsg_dumper * dumper )

Arguments
=========

``dumper``
    pointer to the kmsg_dumper structure


Description
===========

Adds a kernel log dumper to the system. The dump callback in the structure will be called when the kernel oopses or panics and must be set. Returns zero on success and ``-EINVAL``
or ``-EBUSY`` otherwise.
