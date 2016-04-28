.. -*- coding: utf-8; mode: rst -*-

.. _API-parport-announce-port:

=====================
parport_announce_port
=====================

*man parport_announce_port(9)*

*4.6.0-rc5*

tell device drivers about a parallel port


Synopsis
========

.. c:function:: void parport_announce_port( struct parport * port )

Arguments
=========

``port``
    parallel port to announce


Description
===========

After a port driver has registered a parallel port with
parport_register_port, and performed any necessary initialisation or
adjustments, it should call ``parport_announce_port`` in order to notify
all device drivers that have called ``parport_register_driver``. Their
``attach`` functions will be called, with ``port`` as the parameter.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
