.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-sas-async-probe:

===================
ata_sas_async_probe
===================

*man ata_sas_async_probe(9)*

*4.6.0-rc5*

simply schedule probing and return


Synopsis
========

.. c:function:: void ata_sas_async_probe( struct ata_port * ap )

Arguments
=========

``ap``
    Port to probe


Description
===========

For batch scheduling of probe for sas attached ata devices, assumes the
port has already been through ``ata_sas_port_init``


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
