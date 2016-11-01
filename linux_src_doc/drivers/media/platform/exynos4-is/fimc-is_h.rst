.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/exynos4-is/fimc-is.h

.. _`fimc_is`:

struct fimc_is
==============

.. c:type:: struct fimc_is

    fimc-is data structure

.. _`fimc_is.definition`:

Definition
----------

.. code-block:: c

    struct fimc_is {
        struct platform_device *pdev;
        struct pinctrl *pctrl;
        struct v4l2_device *v4l2_dev;
        struct fimc_is_firmware fw;
        struct fimc_is_memory memory;
        struct firmware *f_w;
        struct fimc_isp isp;
        struct fimc_is_sensor sensor[FIMC_IS_SENSORS_NUM];
        struct fimc_is_setfile setfile;
        struct v4l2_ctrl_handler ctrl_handler;
        struct mutex lock;
        spinlock_t slock;
        struct clk  *clocks[ISS_CLKS_MAX];
        void __iomem *regs;
        void __iomem *pmu_regs;
        int irq;
        wait_queue_head_t irq_queue;
        u8 lpm;
        unsigned long state;
        unsigned int sensor_index;
        struct i2h_cmd i2h_cmd;
        struct h2i_cmd h2i_cmd;
        struct is_fd_result_header fd_header;
        struct chain_config config[IS_SC_MAX];
        unsigned config_index;
        struct is_region *is_p_region;
        dma_addr_t is_dma_p_region;
        struct is_share_region *is_shared_region;
        struct is_af_info af;
        struct dentry *debugfs_entry;
    }

.. _`fimc_is.members`:

Members
-------

pdev
    pointer to FIMC-IS platform device

pctrl
    pointer to pinctrl structure for this device

v4l2_dev
    pointer to top the level v4l2_device

fw
    *undescribed*

memory
    *undescribed*

f_w
    *undescribed*

isp
    *undescribed*

setfile
    *undescribed*

ctrl_handler
    *undescribed*

lock
    mutex serializing video device and the subdev operations

slock
    spinlock protecting this data structure and the hw registers

clocks
    FIMC-LITE gate clock

regs
    MCUCTL mmapped registers region

pmu_regs
    PMU ISP mmapped registers region

irq
    *undescribed*

irq_queue
    interrupt handling waitqueue

lpm
    low power mode flag

state
    internal driver's state flags

sensor_index
    *undescribed*

i2h_cmd
    *undescribed*

h2i_cmd
    *undescribed*

fd_header
    *undescribed*

config_index
    *undescribed*

is_p_region
    *undescribed*

is_dma_p_region
    *undescribed*

is_shared_region
    *undescribed*

af
    *undescribed*

debugfs_entry
    *undescribed*

.. This file was automatic generated / don't edit.

