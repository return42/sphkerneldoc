
.. _API-regulator-set-load:

==================
regulator_set_load
==================

*man regulator_set_load(9)*

*4.6.0-rc1*

set regulator load


Synopsis
========

.. c:function:: int regulator_set_load( struct regulator * regulator, int uA_load )

Arguments
=========

``regulator``
    regulator source

``uA_load``
    load current


Description
===========

Notifies the regulator core of a new device load. This is then used by DRMS (if enabled by constraints) to set the most efficient regulator operating mode for the new regulator
loading.

Consumer devices notify their supply regulator of the maximum power they will require (can be taken from device datasheet in the power consumption tables) when they change
operational status and hence power state. Examples of operational state changes that can affect power


consumption are
===============

-

o Device is opened / closed. o Device I/O is about to begin or has just finished. o Device is idling in between work.

This information is also exported via sysfs to userspace.

DRMS will sum the total requested load on the regulator and change to the most efficient operating mode if platform constraints allow.

On error a negative errno is returned.
