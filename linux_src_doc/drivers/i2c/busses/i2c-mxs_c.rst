.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/i2c/busses/i2c-mxs.c

.. _`mxs_i2c_dev`:

struct mxs_i2c_dev
==================

.. c:type:: struct mxs_i2c_dev

    per device, private MXS-I2C data

.. _`mxs_i2c_dev.definition`:

Definition
----------

.. code-block:: c

    struct mxs_i2c_dev {
        struct device *dev;
        enum mxs_i2c_devtype dev_type;
        void __iomem *regs;
        struct completion cmd_complete;
        int cmd_err;
        struct i2c_adapter adapter;
        uint32_t timing0;
        uint32_t timing1;
        uint32_t timing2;
        struct dma_chan *dmach;
        uint32_t pio_data[2];
        uint32_t addr_data;
        struct scatterlist sg_io[2];
        bool dma_read;
    }

.. _`mxs_i2c_dev.members`:

Members
-------

dev
    driver model device node

dev_type
    distinguish i.MX23/i.MX28 features

regs
    IO registers pointer

cmd_complete
    completion object for transaction wait

cmd_err
    error code for last transaction

adapter
    i2c subsystem adapter node

timing0
    *undescribed*

timing1
    *undescribed*

timing2
    *undescribed*

dmach
    *undescribed*

addr_data
    *undescribed*

dma_read
    *undescribed*

.. This file was automatic generated / don't edit.

