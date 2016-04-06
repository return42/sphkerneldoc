
.. _API-dvb-unregister-frontend:

=======================
dvb_unregister_frontend
=======================

*man dvb_unregister_frontend(9)*

*4.6.0-rc1*

Unregisters a DVB frontend


Synopsis
========

.. c:function:: int dvb_unregister_frontend( struct dvb_frontend * fe )

Arguments
=========

``fe``
    pointer to the frontend struct


Description
===========

Stops the frontend kthread, calls ``dvb_unregister_device`` and frees the private frontend data allocated by ``dvb_register_frontend``.


NOTE
====

This function doesn't frees the memory allocated by the demod, by the SEC driver and by the tuner. In order to free it, an explicit call to ``dvb_frontend_detach`` is needed, after
calling this function.
