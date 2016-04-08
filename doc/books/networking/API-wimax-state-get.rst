
.. _API-wimax-state-get:

===============
wimax_state_get
===============

*man wimax_state_get(9)*

*4.6.0-rc1*

Return the current state of a WiMAX device


Synopsis
========

.. c:function:: enum wimax_st wimax_state_get( struct wimax_dev * wimax_dev )

Arguments
=========

``wimax_dev``
    WiMAX device descriptor


Returns
=======

Current state of the device according to its driver.
