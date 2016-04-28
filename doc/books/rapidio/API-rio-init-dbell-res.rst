.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-init-dbell-res:

==================
rio_init_dbell_res
==================

*man rio_init_dbell_res(9)*

*4.6.0-rc5*

Initialize a RIO doorbell resource


Synopsis
========

.. c:function:: void rio_init_dbell_res( struct resource * res, u16 start, u16 end )

Arguments
=========

``res``
    resource struct

``start``
    start of doorbell range

``end``
    end of doorbell range


Description
===========

This function is used to initialize the fields of a resource for use as
a doorbell resource. It initializes a range of doorbell messages using
the start and end arguments.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
