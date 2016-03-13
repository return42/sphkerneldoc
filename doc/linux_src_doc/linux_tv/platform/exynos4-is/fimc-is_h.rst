.. -*- coding: utf-8; mode: rst -*-

=========
fimc-is.h
=========



.. _xref_struct_fimc_is:

struct fimc_is
==============

.. c:type:: struct fimc_is

    fimc-is data structure



Definition
----------

.. code-block:: c

  struct fimc_is {
    struct platform_device * pdev;
    struct pinctrl * pctrl;
    struct v4l2_device * v4l2_dev;
    struct vb2_alloc_ctx * alloc_ctx;
    struct mutex lock;
    spinlock_t slock;
    struct clk * clocks[ISS_CLKS_MAX];
    void __iomem * regs;
    void __iomem * pmu_regs;
    wait_queue_head_t irq_queue;
    u8 lpm;
    unsigned long state;
  };



Members
-------

:``struct platform_device * pdev``:
    pointer to FIMC-IS platform device

:``struct pinctrl * pctrl``:
    pointer to pinctrl structure for this device

:``struct v4l2_device * v4l2_dev``:
    pointer to top the level v4l2_device

:``struct vb2_alloc_ctx * alloc_ctx``:
    videobuf2 memory allocator context

:``struct mutex lock``:
    mutex serializing video device and the subdev operations

:``spinlock_t slock``:
    spinlock protecting this data structure and the hw registers

:``struct clk * clocks[ISS_CLKS_MAX]``:
    FIMC-LITE gate clock

:``void __iomem * regs``:
    MCUCTL mmapped registers region

:``void __iomem * pmu_regs``:
    PMU ISP mmapped registers region

:``wait_queue_head_t irq_queue``:
    interrupt handling waitqueue

:``u8 lpm``:
    low power mode flag

:``unsigned long state``:
    internal driver's state flags



