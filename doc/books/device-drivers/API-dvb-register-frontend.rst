.. -*- coding: utf-8; mode: rst -*-

.. _API-dvb-register-frontend:

=====================
dvb_register_frontend
=====================

*man dvb_register_frontend(9)*

*4.6.0-rc5*

Registers a DVB frontend at the adapter


Synopsis
========

.. c:function:: int dvb_register_frontend( struct dvb_adapter * dvb, struct dvb_frontend * fe )

Arguments
=========

``dvb``
    pointer to the dvb adapter

``fe``
    pointer to the frontend struct


Description
===========

Allocate and initialize the private data needed by the frontend core to
manage the frontend and calls ``dvb_register_device`` to register a new
frontend. It also cleans the property cache that stores the frontend
parameters and selects the first available delivery system.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
