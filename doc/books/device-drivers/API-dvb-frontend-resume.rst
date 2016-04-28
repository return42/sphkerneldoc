.. -*- coding: utf-8; mode: rst -*-

.. _API-dvb-frontend-resume:

===================
dvb_frontend_resume
===================

*man dvb_frontend_resume(9)*

*4.6.0-rc5*

Resumes a Digital TV frontend


Synopsis
========

.. c:function:: int dvb_frontend_resume( struct dvb_frontend * fe )

Arguments
=========

``fe``
    pointer to the frontend struct


Description
===========

This function resumes the usual operation of the tuner after resume.

In order to resume the frontend, it calls the demod
``dvb_frontend_ops``.\ ``init``.

If ``dvb_frontend_ops``.tuner_ops. ``resume`` is available, It, it
calls it. Otherwise,t will call
``dvb_frontend_ops``.tuner_ops. ``init``, if available.

Once tuner and demods are resumed, it will enforce that the SEC voltage
and tone are restored to their previous values and wake up the
frontend's kthread in order to retune the frontend.

The drivers should also call ``dvb_frontend_resume`` as part of their
handler for the ``device_driver``.\ ``resume``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
