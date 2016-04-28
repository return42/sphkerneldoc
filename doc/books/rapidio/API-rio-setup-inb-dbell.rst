.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-setup-inb-dbell:

===================
rio_setup_inb_dbell
===================

*man rio_setup_inb_dbell(9)*

*4.6.0-rc5*

bind inbound doorbell callback


Synopsis
========

.. c:function:: int rio_setup_inb_dbell( struct rio_mport * mport, void * dev_id, struct resource * res, void (*dinb) struct rio_mport * mport, void *dev_id, u16 src, u16 dst, u16 info )

Arguments
=========

``mport``
    RIO master port to bind the doorbell callback

``dev_id``
    Device specific pointer to pass on event

``res``
    Doorbell message resource

``dinb``
    Callback to execute when doorbell is received


Description
===========

Adds a doorbell resource/callback pair into a port's doorbell event
list. Returns 0 if the request has been satisfied.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
