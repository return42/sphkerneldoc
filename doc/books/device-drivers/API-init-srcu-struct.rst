.. -*- coding: utf-8; mode: rst -*-

.. _API-init-srcu-struct:

================
init_srcu_struct
================

*man init_srcu_struct(9)*

*4.6.0-rc5*

initialize a sleep-RCU structure


Synopsis
========

.. c:function:: int init_srcu_struct( struct srcu_struct * sp )

Arguments
=========

``sp``
    structure to initialize.


Description
===========

Must invoke this on a given srcu_struct before passing that
srcu_struct to any other function. Each srcu_struct represents a
separate domain of SRCU protection.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
