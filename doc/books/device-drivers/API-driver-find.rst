
.. _API-driver-find:

===========
driver_find
===========

*man driver_find(9)*

*4.6.0-rc1*

locate driver on a bus by its name.


Synopsis
========

.. c:function:: struct device_driver ⋆ driver_find( const char * name, struct bus_type * bus )

Arguments
=========

``name``
    name of the driver.

``bus``
    bus to scan for the driver.


Description
===========

Call ``kset_find_obj`` to iterate over list of drivers on a bus to find driver by name. Return driver if found.

This routine provides no locking to prevent the driver it returns from being unregistered or unloaded while the caller is using it. The caller is responsible for preventing this.
