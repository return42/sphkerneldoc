.. -*- coding: utf-8; mode: rst -*-

.. _API-sas-expander-alloc:

==================
sas_expander_alloc
==================

*man sas_expander_alloc(9)*

*4.6.0-rc5*

allocate an rphy for an end device


Synopsis
========

.. c:function:: struct sas_rphy * sas_expander_alloc( struct sas_port * parent, enum sas_device_type type )

Arguments
=========

``parent``
    which port

``type``
    SAS_EDGE_EXPANDER_DEVICE or SAS_FANOUT_EXPANDER_DEVICE


Description
===========

Allocates an SAS remote PHY structure, connected to ``parent``.


Returns
=======

SAS PHY allocated or ``NULL`` if the allocation failed.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
