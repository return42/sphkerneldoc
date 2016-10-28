.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ptp/ptp_pch.c

.. _`pch_ts_regs`:

struct pch_ts_regs
==================

.. c:type:: struct pch_ts_regs

    IEEE 1588 registers

.. _`pch_ts_regs.definition`:

Definition
----------

.. code-block:: c

    struct pch_ts_regs {
        u32 control;
        u32 event;
        u32 addend;
        u32 accum;
        u32 test;
        u32 ts_compare;
        u32 rsystime_lo;
        u32 rsystime_hi;
        u32 systime_lo;
        u32 systime_hi;
        u32 trgt_lo;
        u32 trgt_hi;
        u32 asms_lo;
        u32 asms_hi;
        u32 amms_lo;
        u32 amms_hi;
        u32 ch_control;
        u32 ch_event;
        u32 tx_snap_lo;
        u32 tx_snap_hi;
        u32 rx_snap_lo;
        u32 rx_snap_hi;
        u32 src_uuid_lo;
        u32 src_uuid_hi;
        u32 can_status;
        u32 can_snap_lo;
        u32 can_snap_hi;
        u32 ts_sel;
        u32 ts_st[6];
        u32 reserve1[14];
        u32 stl_max_set_en;
        u32 stl_max_set;
        u32 reserve2[13];
        u32 srst;
    }

.. _`pch_ts_regs.members`:

Members
-------

control
    *undescribed*

event
    *undescribed*

addend
    *undescribed*

accum
    *undescribed*

test
    *undescribed*

ts_compare
    *undescribed*

rsystime_lo
    *undescribed*

rsystime_hi
    *undescribed*

systime_lo
    *undescribed*

systime_hi
    *undescribed*

trgt_lo
    *undescribed*

trgt_hi
    *undescribed*

asms_lo
    *undescribed*

asms_hi
    *undescribed*

amms_lo
    *undescribed*

amms_hi
    *undescribed*

ch_control
    *undescribed*

ch_event
    *undescribed*

tx_snap_lo
    *undescribed*

tx_snap_hi
    *undescribed*

rx_snap_lo
    *undescribed*

rx_snap_hi
    *undescribed*

src_uuid_lo
    *undescribed*

src_uuid_hi
    *undescribed*

can_status
    *undescribed*

can_snap_lo
    *undescribed*

can_snap_hi
    *undescribed*

ts_sel
    *undescribed*

stl_max_set_en
    *undescribed*

stl_max_set
    *undescribed*

srst
    *undescribed*

.. _`pch_dev`:

struct pch_dev
==============

.. c:type:: struct pch_dev

    Driver private data

.. _`pch_dev.definition`:

Definition
----------

.. code-block:: c

    struct pch_dev {
        struct pch_ts_regs __iomem *regs;
        struct ptp_clock *ptp_clock;
        struct ptp_clock_info caps;
        int exts0_enabled;
        int exts1_enabled;
        u32 mem_base;
        u32 mem_size;
        u32 irq;
        struct pci_dev *pdev;
        spinlock_t register_lock;
    }

.. _`pch_dev.members`:

Members
-------

regs
    *undescribed*

ptp_clock
    *undescribed*

caps
    *undescribed*

exts0_enabled
    *undescribed*

exts1_enabled
    *undescribed*

mem_base
    *undescribed*

mem_size
    *undescribed*

irq
    *undescribed*

pdev
    *undescribed*

register_lock
    *undescribed*

.. _`pch_params`:

struct pch_params
=================

.. c:type:: struct pch_params

    1588 module parameter

.. _`pch_params.definition`:

Definition
----------

.. code-block:: c

    struct pch_params {
        u8 station[STATION_ADDR_LEN];
    }

.. _`pch_params.members`:

Members
-------

.. _`pch_set_station_address`:

pch_set_station_address
=======================

.. c:function:: int pch_set_station_address(u8 *addr, struct pci_dev *pdev)

    This API sets the station address used by IEEE 1588 hardware when looking at PTP traffic on the  ethernet interface

    :param u8 \*addr:
        dress which contain the column separated address to be used.

    :param struct pci_dev \*pdev:
        *undescribed*

.. This file was automatic generated / don't edit.

