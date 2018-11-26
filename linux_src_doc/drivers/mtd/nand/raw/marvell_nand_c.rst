.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/nand/raw/marvell_nand.c

.. _`to_cycles`:

TO_CYCLES
=========

.. c:function::  TO_CYCLES( ps,  period_ns)

    :param ps:
        Duration in pico-seconds
    :type ps: 

    :param period_ns:
        Clock period in nano-seconds
    :type period_ns: 

.. _`to_cycles.description`:

Description
-----------

Convert the duration in nano-seconds, then divide by the period and
return the number of clock periods.

.. This file was automatic generated / don't edit.

