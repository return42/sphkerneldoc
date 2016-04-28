.. -*- coding: utf-8; mode: rst -*-

.. _API-wimax-state-get:

===============
wimax_state_get
===============

*man wimax_state_get(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
