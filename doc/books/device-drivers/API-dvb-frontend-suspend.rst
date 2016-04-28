.. -*- coding: utf-8; mode: rst -*-

.. _API-dvb-frontend-suspend:

====================
dvb_frontend_suspend
====================

*man dvb_frontend_suspend(9)*

*4.6.0-rc5*

Suspends a Digital TV frontend


Synopsis
========

.. c:function:: int dvb_frontend_suspend( struct dvb_frontend * fe )

Arguments
=========

``fe``
    pointer to the frontend struct


Description
===========

This function prepares a Digital TV frontend to suspend.

In order to prepare the tuner to suspend, if
``dvb_frontend_ops``.tuner_ops. ``suspend`` is available, it calls it.
Otherwise, it will call ``dvb_frontend_ops``.tuner_ops. ``sleep``, if
available.

It will also call ``dvb_frontend_ops``.\ ``sleep`` to put the demod to
suspend.

The drivers should also call ``dvb_frontend_suspend`` as part of their
handler for the ``device_driver``.\ ``suspend``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
