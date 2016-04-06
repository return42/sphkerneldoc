
.. _API-kmsg-dump-unregister:

====================
kmsg_dump_unregister
====================

*man kmsg_dump_unregister(9)*

*4.6.0-rc1*

unregister a kmsg dumper.


Synopsis
========

.. c:function:: int kmsg_dump_unregister( struct kmsg_dumper * dumper )

Arguments
=========

``dumper``
    pointer to the kmsg_dumper structure


Description
===========

Removes a dump device from the system. Returns zero on success and ``-EINVAL`` otherwise.
