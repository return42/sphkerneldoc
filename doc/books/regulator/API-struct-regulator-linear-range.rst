
.. _API-struct-regulator-linear-range:

=============================
struct regulator_linear_range
=============================

*man struct regulator_linear_range(9)*

*4.6.0-rc1*

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

Specify a range of voltages for ``regulator_map_linar_range`` and ``regulator_list_linear_range``.
