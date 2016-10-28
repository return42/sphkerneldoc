.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mfd/ab8500-debugfs.c

.. _`ab8500_reg_range`:

struct ab8500_reg_range
=======================

.. c:type:: struct ab8500_reg_range


.. _`ab8500_reg_range.definition`:

Definition
----------

.. code-block:: c

    struct ab8500_reg_range {
        u8 first;
        u8 last;
        u8 perm;
    }

.. _`ab8500_reg_range.members`:

Members
-------

first
    the first address of the range

last
    the last address of the range

perm
    access permissions for the range

.. _`ab8500_prcmu_ranges`:

struct ab8500_prcmu_ranges
==========================

.. c:type:: struct ab8500_prcmu_ranges


.. _`ab8500_prcmu_ranges.definition`:

Definition
----------

.. code-block:: c

    struct ab8500_prcmu_ranges {
        u8 num_ranges;
        u8 bankid;
        const struct ab8500_reg_range *range;
    }

.. _`ab8500_prcmu_ranges.members`:

Members
-------

num_ranges
    the number of ranges in the list

bankid
    bank identifier

range
    the list of register ranges

.. This file was automatic generated / don't edit.

