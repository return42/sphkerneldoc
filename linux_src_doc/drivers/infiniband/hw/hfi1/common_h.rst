.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/hfi1/common.h

.. _`hfi1_mcast_nr`:

HFI1_MCAST_NR
=============

.. c:function::  HFI1_MCAST_NR()

    4 bits of multicast range and 1 bit for collective range

.. _`hfi1_mcast_nr.example`:

Example
-------

.. code-block:: c

    For 24 bit LID space,


.. _`hfi1_mcast_nr.multicast-range`:

Multicast range
---------------

0xF00000 to 0xF7FFFF

.. _`hfi1_mcast_nr.collective-range`:

Collective range
----------------

0xF80000 to 0xFFFFFE

.. This file was automatic generated / don't edit.

