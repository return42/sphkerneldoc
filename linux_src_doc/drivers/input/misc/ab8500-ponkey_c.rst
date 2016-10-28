.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/input/misc/ab8500-ponkey.c

.. _`ab8500_ponkey`:

struct ab8500_ponkey
====================

.. c:type:: struct ab8500_ponkey

    ab8500 ponkey information

.. _`ab8500_ponkey.definition`:

Definition
----------

.. code-block:: c

    struct ab8500_ponkey {
        struct input_dev *idev;
        struct ab8500 *ab8500;
        int irq_dbf;
        int irq_dbr;
    }

.. _`ab8500_ponkey.members`:

Members
-------

idev
    *undescribed*

ab8500
    ab8500 parent

irq_dbf
    irq number for falling transition

irq_dbr
    irq number for rising transition

.. This file was automatic generated / don't edit.

