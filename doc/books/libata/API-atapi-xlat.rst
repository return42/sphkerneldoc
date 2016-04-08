
.. _API-atapi-xlat:

==========
atapi_xlat
==========

*man atapi_xlat(9)*

*4.6.0-rc1*

Initialize PACKET taskfile


Synopsis
========

.. c:function:: unsigned int atapi_xlat( struct ata_queued_cmd * qc )

Arguments
=========

``qc``
    command structure to be initialized


LOCKING
=======

spin_lock_irqsave(host lock)


RETURNS
=======

Zero on success, non-zero on failure.
