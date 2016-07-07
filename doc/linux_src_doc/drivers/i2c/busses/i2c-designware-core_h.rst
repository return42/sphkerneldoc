.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/i2c/busses/i2c-designware-core.h

.. _`dw_i2c_dev`:

struct dw_i2c_dev
=================

.. c:type:: struct dw_i2c_dev

    private i2c-designware data

.. _`dw_i2c_dev.definition`:

Definition
----------

.. code-block:: c

    struct dw_i2c_dev {
        struct device *dev;
        void __iomem *base;
        struct completion cmd_complete;
        struct clk *clk;
        u32 (* get_clk_rate_khz) (struct dw_i2c_dev *dev);
        struct dw_pci_controller *controller;
        int cmd_err;
        struct i2c_msg *msgs;
        int msgs_num;
        int msg_write_idx;
        u32 tx_buf_len;
        u8 *tx_buf;
        int msg_read_idx;
        u32 rx_buf_len;
        u8 *rx_buf;
        int msg_err;
        unsigned int status;
        u32 abort_source;
        int irq;
        u32 accessor_flags;
        struct i2c_adapter adapter;
        u32 functionality;
        u32 master_cfg;
        unsigned int tx_fifo_depth;
        unsigned int rx_fifo_depth;
        int rx_outstanding;
        u32 sda_hold_time;
        u32 sda_falling_time;
        u32 scl_falling_time;
        u16 ss_hcnt;
        u16 ss_lcnt;
        u16 fs_hcnt;
        u16 fs_lcnt;
        int (* acquire_lock) (struct dw_i2c_dev *dev);
        void (* release_lock) (struct dw_i2c_dev *dev);
        bool pm_runtime_disabled;
    }

.. _`dw_i2c_dev.members`:

Members
-------

dev
    driver model device node

base
    IO registers pointer

cmd_complete
    tx completion indicator

clk
    input reference clock

get_clk_rate_khz
    *undescribed*

controller
    *undescribed*

cmd_err
    run time hadware error code

msgs
    points to an array of messages currently being transfered

msgs_num
    the number of elements in msgs

msg_write_idx
    the element index of the current tx message in the msgs
    array

tx_buf_len
    the length of the current tx buffer

tx_buf
    the current tx buffer

msg_read_idx
    the element index of the current rx message in the msgs
    array

rx_buf_len
    the length of the current rx buffer

rx_buf
    the current rx buffer

msg_err
    error status of the current transfer

status
    i2c master status, one of STATUS\_\*

abort_source
    copy of the TX_ABRT_SOURCE register

irq
    interrupt number for the i2c master

accessor_flags
    *undescribed*

adapter
    i2c subsystem adapter node

functionality
    *undescribed*

master_cfg
    *undescribed*

tx_fifo_depth
    depth of the hardware tx fifo

rx_fifo_depth
    depth of the hardware rx fifo

rx_outstanding
    current master-rx elements in tx fifo

sda_hold_time
    *undescribed*

sda_falling_time
    *undescribed*

scl_falling_time
    *undescribed*

ss_hcnt
    standard speed HCNT value

ss_lcnt
    standard speed LCNT value

fs_hcnt
    fast speed HCNT value

fs_lcnt
    fast speed LCNT value

acquire_lock
    function to acquire a hardware lock on the bus

release_lock
    function to release a hardware lock on the bus

pm_runtime_disabled
    true if pm runtime is disabled

.. _`dw_i2c_dev.description`:

Description
-----------

HCNT and LCNT parameters can be used if the platform knows more accurate
values than the one computed based only on the input clock frequency.
Leave them to be \ ``0``\  if not used.

.. This file was automatic generated / don't edit.

