
.. _API-ata-dump-status:

===============
ata_dump_status
===============

*man ata_dump_status(9)*

*4.6.0-rc1*

user friendly display of error info


Synopsis
========

.. c:function:: void ata_dump_status( unsigned id, struct ata_taskfile * tf )

Arguments
=========

``id``
    id of the port in question

``tf``
    ptr to filled out taskfile


Description
===========

Decode and dump the ATA error/status registers for the user so that they have some idea what really happened at the non make-believe layer.


LOCKING
=======

inherited from caller
