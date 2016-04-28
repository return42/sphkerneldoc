.. -*- coding: utf-8; mode: rst -*-

.. _API-bus-unregister:

==============
bus_unregister
==============

*man bus_unregister(9)*

*4.6.0-rc5*

remove a bus from the system


Synopsis
========

.. c:function:: void bus_unregister( struct bus_type * bus )

Arguments
=========

``bus``
    bus.


Description
===========

Unregister the child subsystems and the bus itself. Finally, we call
``bus_put`` to release the refcount


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
