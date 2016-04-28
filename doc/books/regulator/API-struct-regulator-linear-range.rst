.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-regulator-linear-range:

=============================
struct regulator_linear_range
=============================

*man struct regulator_linear_range(9)*

*4.6.0-rc5*

specify linear voltage ranges


Synopsis
========

.. code-block:: c

    struct regulator_linear_range {
      unsigned int min_uV;
      unsigned int min_sel;
      unsigned int max_sel;
      unsigned int uV_step;
    };


Members
=======

min_uV
    Lowest voltage in range

min_sel
    Lowest selector for range

max_sel
    Highest selector for range

uV_step
    Step size


Description
===========

Specify a range of voltages for ``regulator_map_linar_range`` and
``regulator_list_linear_range``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
