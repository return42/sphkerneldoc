.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/i2c/busses/i2c-tegra.c

.. _`tegra_i2c_hw_feature`:

struct tegra_i2c_hw_feature
===========================

.. c:type:: struct tegra_i2c_hw_feature

    Different HW support on Tegra

.. _`tegra_i2c_hw_feature.definition`:

Definition
----------

.. code-block:: c

    struct tegra_i2c_hw_feature {
        bool has_continue_xfer_support;
        bool has_per_pkt_xfer_complete_irq;
        bool has_single_clk_source;
        bool has_config_load_reg;
        int clk_divisor_hs_mode;
        int clk_divisor_std_fast_mode;
        u16 clk_divisor_fast_plus_mode;
        bool has_multi_master_mode;
        bool has_slcg_override_reg;
    }

.. _`tegra_i2c_hw_feature.members`:

Members
-------

has_continue_xfer_support
    Continue transfer supports.

has_per_pkt_xfer_complete_irq
    Has enable/disable capability for transfer
    complete interrupt per packet basis.

has_single_clk_source
    The i2c controller has single clock source. Tegra30
    and earlier Socs has two clock sources i.e. div-clk and
    fast-clk.

has_config_load_reg
    Has the config load register to load the new
    configuration.

clk_divisor_hs_mode
    Clock divisor in HS mode.

clk_divisor_std_fast_mode
    Clock divisor in standard/fast mode. It is
    applicable if there is no fast clock source i.e. single clock
    source.

clk_divisor_fast_plus_mode
    *undescribed*

has_multi_master_mode
    *undescribed*

has_slcg_override_reg
    *undescribed*

.. _`tegra_i2c_dev`:

struct tegra_i2c_dev
====================

.. c:type:: struct tegra_i2c_dev

    per device i2c context

.. _`tegra_i2c_dev.definition`:

Definition
----------

.. code-block:: c

    struct tegra_i2c_dev {
        struct device *dev;
        const struct tegra_i2c_hw_feature *hw;
        struct i2c_adapter adapter;
        struct clk *div_clk;
        struct clk *fast_clk;
        struct reset_control *rst;
        void __iomem *base;
        int cont_id;
        int irq;
        bool irq_disabled;
        int is_dvc;
        struct completion msg_complete;
        int msg_err;
        u8 *msg_buf;
        size_t msg_buf_remaining;
        int msg_read;
        u32 bus_clk_rate;
        u16 clk_divisor_non_hs_mode;
        bool is_suspended;
        bool is_multimaster_mode;
        spinlock_t xfer_lock;
    }

.. _`tegra_i2c_dev.members`:

Members
-------

dev
    device reference for power management

hw
    Tegra i2c hw feature.

adapter
    core i2c layer adapter information

div_clk
    clock reference for div clock of i2c controller.

fast_clk
    clock reference for fast clock of i2c controller.

rst
    *undescribed*

base
    ioremapped registers cookie

cont_id
    i2c controller id, used for for packet header

irq
    irq number of transfer complete interrupt

irq_disabled
    *undescribed*

is_dvc
    identifies the DVC i2c controller, has a different register layout

msg_complete
    transfer completion notifier

msg_err
    error code for completed message

msg_buf
    pointer to current message data

msg_buf_remaining
    size of unsent data in the message buffer

msg_read
    identifies read transfers

bus_clk_rate
    current i2c bus clock rate

clk_divisor_non_hs_mode
    *undescribed*

is_suspended
    prevents i2c controller accesses after suspend is called

is_multimaster_mode
    *undescribed*

xfer_lock
    *undescribed*

.. This file was automatic generated / don't edit.

