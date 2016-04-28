.. -*- coding: utf-8; mode: rst -*-

.. _API-dvb-frontend-reinitialise:

=========================
dvb_frontend_reinitialise
=========================

*man dvb_frontend_reinitialise(9)*

*4.6.0-rc5*

forces a reinitialisation at the frontend


Synopsis
========

.. c:function:: void dvb_frontend_reinitialise( struct dvb_frontend * fe )

Arguments
=========

``fe``
    pointer to the frontend struct


Description
===========

Calls ``dvb_frontend_ops``.\ ``init`` and
``dvb_frontend_ops``.tuner_ops. ``init``, and resets SEC tone and
voltage (for Satellite systems).


NOTE
====

Currently, this function is used only by one driver (budget-av). It
seems to be due to address some special issue with that specific
frontend.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
