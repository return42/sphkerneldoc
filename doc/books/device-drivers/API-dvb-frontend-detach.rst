.. -*- coding: utf-8; mode: rst -*-

.. _API-dvb-frontend-detach:

===================
dvb_frontend_detach
===================

*man dvb_frontend_detach(9)*

*4.6.0-rc5*

Detaches and frees frontend specific data


Synopsis
========

.. c:function:: void dvb_frontend_detach( struct dvb_frontend * fe )

Arguments
=========

``fe``
    pointer to the frontend struct


Description
===========

This function should be called after ``dvb_unregister_frontend``. It
calls the SEC, tuner and demod release functions:
``dvb_frontend_ops``.release_sec,
``dvb_frontend_ops``.tuner_ops.release,
``dvb_frontend_ops``.analog_ops.release and
``dvb_frontend_ops``.release.

If the driver is compiled with CONFIG_MEDIA_ATTACH, it also decreases
the module reference count, needed to allow userspace to remove the
previously used DVB frontend modules.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
