.. -*- coding: utf-8; mode: rst -*-

.. _API-wimax-state-change:

==================
wimax_state_change
==================

*man wimax_state_change(9)*

*4.6.0-rc5*

Set the current state of a WiMAX device


Synopsis
========

.. c:function:: void wimax_state_change( struct wimax_dev * wimax_dev, enum wimax_st new_state )

Arguments
=========

``wimax_dev``
    WiMAX device descriptor (properly referenced)

``new_state``
    New state to switch to


Description
===========

This implements the state changes for the wimax devices. It will

- verify that the state transition is legal (for now it'll just print a
warning if not) according to the table in linux/wimax.h's documentation
for 'enum wimax_st'.

- perform the actions needed for leaving the current state and whichever
are needed for entering the new state.

- issue a report to user space indicating the new state (and an optional
payload with information about the new state).


NOTE
====

``wimax_dev`` must be locked


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
