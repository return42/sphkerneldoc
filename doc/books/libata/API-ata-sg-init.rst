.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-sg-init:

===========
ata_sg_init
===========

*man ata_sg_init(9)*

*4.6.0-rc5*

Associate command with scatter-gather table.


Synopsis
========

.. c:function:: void ata_sg_init( struct ata_queued_cmd * qc, struct scatterlist * sg, unsigned int n_elem )

Arguments
=========

``qc``
    Command to be associated

``sg``
    Scatter-gather table.

``n_elem``
    Number of elements in s/g table.


Description
===========

Initialize the data-related elements of queued_cmd ``qc`` to point to a
scatter-gather table ``sg``, containing ``n_elem`` elements.


LOCKING
=======

spin_lock_irqsave(host lock)


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
