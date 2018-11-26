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
        void __iomem *ext;
        struct completion cmd_complete;
        struct clk *clk;
        struct reset_control *rst;
        struct i2c_client *slave;
        u32 (*get_clk_rate_khz) (struct dw_i2c_dev *dev);
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
        u32 flags;
        struct i2c_adapter adapter;
        u32 functionality;
        u32 master_cfg;
        u32 slave_cfg;
        unsigned int tx_fifo_depth;
        unsigned int rx_fifo_depth;
        int rx_outstanding;
        struct i2c_timings timings;
        u32 sda_hold_time;
        u16 ss_hcnt;
        u16 ss_lcnt;
        u16 fs_hcnt;
        u16 fs_lcnt;
        u16 fp_hcnt;
        u16 fp_lcnt;
        u16 hs_hcnt;
        u16 hs_lcnt;
        int (*acquire_lock)(void);
        void (*release_lock)(void);
        bool shared_with_punit;
        void (*disable)(struct dw_i2c_dev *dev);
        void (*disable_int)(struct dw_i2c_dev *dev);
        int (*init)(struct dw_i2c_dev *dev);
        int (*set_sda_hold_time)(struct dw_i2c_dev *dev);
        int mode;
        struct i2c_bus_recovery_info rinfo;
    }

.. _`dw_i2c_dev.members`:

Members
-------

dev
    driver model device node

base
    IO registers pointer

ext
    *undescribed*

cmd_complete
    tx completion indicator

clk
    input reference clock

rst
    *undescribed*

slave
    represent an I2C slave device

get_clk_rate_khz
    *undescribed*

controller
    *undescribed*

cmd_err
    run time hadware error code

msgs
    points to an array of messages currently being transferred

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

flags
    *undescribed*

adapter
    i2c subsystem adapter node

functionality
    *undescribed*

master_cfg
    *undescribed*

slave_cfg
    configuration for the slave device

tx_fifo_depth
    depth of the hardware tx fifo

rx_fifo_depth
    depth of the hardware rx fifo

rx_outstanding
    current master-rx elements in tx fifo

timings
    bus clock frequency, SDA hold and other timings

sda_hold_time
    SDA hold value

ss_hcnt
    standard speed HCNT value

ss_lcnt
    standard speed LCNT value

fs_hcnt
    fast speed HCNT value

fs_lcnt
    fast speed LCNT value

fp_hcnt
    fast plus HCNT value

fp_lcnt
    fast plus LCNT value

hs_hcnt
    high speed HCNT value

hs_lcnt
    high speed LCNT value

acquire_lock
    function to acquire a hardware lock on the bus

release_lock
    function to release a hardware lock on the bus

shared_with_punit
    true if this bus is shared with the SoCs PUNIT

disable
    function to disable the controller

disable_int
    function to disable all interrupts

init
    function to initialize the I2C hardware

set_sda_hold_time
    *undescribed*

mode
    operation mode - DW_IC_MASTER or DW_IC_SLAVE

rinfo
    *undescribed*

.. _`dw_i2c_dev.description`:

Description
-----------

HCNT and LCNT parameters can be used if the platform knows more accurate
values than the one computed based only on the input clock frequency.
Leave them to be \ ``0``\  if not used.

.. This file was automatic generated / don't edit.

