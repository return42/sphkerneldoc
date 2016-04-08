
.. _API-w1-reset-select-slave:

=====================
w1_reset_select_slave
=====================

*man w1_reset_select_slave(9)*

*4.6.0-rc1*

reset and select a slave


Synopsis
========

.. c:function:: int w1_reset_select_slave( struct w1_slave * sl )

Arguments
=========

``sl``
    the slave to select


Description
===========

Resets the bus and then selects the slave by sending either a skip rom or a rom match. A skip rom is issued if there is only one device registered on the bus. The w1 master lock
must be held.


Return
======

0=success, anything else=error
