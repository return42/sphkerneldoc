.. -*- coding: utf-8; mode: rst -*-

.. _API-atapi-xlat:

==========
atapi_xlat
==========

*man atapi_xlat(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
