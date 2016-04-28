.. -*- coding: utf-8; mode: rst -*-

.. _API-fc-vport-create:

===============
fc_vport_create
===============

*man fc_vport_create(9)*

*4.6.0-rc5*

Admin App or LLDD requests creation of a vport


Synopsis
========

.. c:function:: struct fc_vport * fc_vport_create( struct Scsi_Host * shost, int channel, struct fc_vport_identifiers * ids )

Arguments
=========

``shost``
    scsi host the virtual port is connected to.

``channel``
    channel on shost port connected to.

``ids``
    The world wide names, FC4 port roles, etc for the virtual port.


Notes
=====

This routine assumes no locks are held on entry.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
