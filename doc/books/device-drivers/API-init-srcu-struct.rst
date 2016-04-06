
.. _API-init-srcu-struct:

================
init_srcu_struct
================

*man init_srcu_struct(9)*

*4.6.0-rc1*

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

Must invoke this on a given srcu_struct before passing that srcu_struct to any other function. Each srcu_struct represents a separate domain of SRCU protection.
