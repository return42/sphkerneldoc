
.. _API-ata-sas-port-stop:

=================
ata_sas_port_stop
=================

*man ata_sas_port_stop(9)*

*4.6.0-rc1*

Undo ``ata_sas_port_start``


Synopsis
========

.. c:function:: void ata_sas_port_stop( struct ata_port * ap )

Arguments
=========

``ap``
    Port to shut down


Description
===========

May be used as the ``port_stop`` entry in ata_port_operations.


LOCKING
=======

Inherited from caller.
