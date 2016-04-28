.. -*- coding: utf-8; mode: rst -*-

.. _API-regulator-count-voltages:

========================
regulator_count_voltages
========================

*man regulator_count_voltages(9)*

*4.6.0-rc5*

count ``regulator_list_voltage`` selectors


Synopsis
========

.. c:function:: int regulator_count_voltages( struct regulator * regulator )

Arguments
=========

``regulator``
    regulator source


Description
===========

Returns number of selectors, or negative errno. Selectors are numbered
starting at zero, and typically correspond to bitfields in hardware
registers.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
