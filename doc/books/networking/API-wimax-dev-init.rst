
.. _API-wimax-dev-init:

==============
wimax_dev_init
==============

*man wimax_dev_init(9)*

*4.6.0-rc1*

initialize a newly allocated instance


Synopsis
========

.. c:function:: void wimax_dev_init( struct wimax_dev * wimax_dev )

Arguments
=========

``wimax_dev``
    WiMAX device descriptor to initialize.


Description
===========

Initializes fields of a freshly allocated ``wimax_dev`` instance. This function assumes that after allocation, the memory occupied by ``wimax_dev`` was zeroed.
