
.. _API-bus-unregister:

==============
bus_unregister
==============

*man bus_unregister(9)*

*4.6.0-rc1*

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

Unregister the child subsystems and the bus itself. Finally, we call ``bus_put`` to release the refcount
