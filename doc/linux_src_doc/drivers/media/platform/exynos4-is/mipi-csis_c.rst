.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/exynos4-is/mipi-csis.c

.. _`csis_state`:

struct csis_state
=================

.. c:type:: struct csis_state

    the driver's internal state data structure

.. _`csis_state.definition`:

Definition
----------

.. code-block:: c

    struct csis_state {
        struct mutex lock;
        struct media_pad pads[CSIS_PADS_NUM];
        struct v4l2_subdev sd;
        u8 index;
        struct platform_device *pdev;
        struct phy *phy;
        void __iomem *regs;
        struct regulator_bulk_data supplies[CSIS_NUM_SUPPLIES];
        struct clk  *clock[NUM_CSIS_CLOCKS];
        int irq;
        u32 interrupt_mask;
        u32 flags;
        u32 clk_frequency;
        u32 hs_settle;
        u32 num_lanes;
        u32 max_num_lanes;
        u8 wclk_ext;
        const struct csis_pix_format *csis_fmt;
        struct v4l2_mbus_framefmt format;
        spinlock_t slock;
        struct csis_pktbuf pkt_buf;
        struct s5pcsis_event events[S5PCSIS_NUM_EVENTS];
    }

.. _`csis_state.members`:

Members
-------

lock
    mutex serializing the subdev and power management operations,
    protecting \ ``format``\  and \ ``flags``\  members

pads
    CSIS pads array

sd
    v4l2_subdev associated with CSIS device instance

index
    the hardware instance index

pdev
    CSIS platform device

phy
    pointer to the CSIS generic PHY

regs
    mmaped I/O registers memory

supplies
    CSIS regulator supplies

clock
    CSIS clocks

irq
    requested s5p-mipi-csis irq number

interrupt_mask
    interrupt mask of the all used interrupts

flags
    the state variable for power and streaming control

clk_frequency
    *undescribed*

hs_settle
    HS-RX settle time

num_lanes
    number of MIPI-CSI data lanes used

max_num_lanes
    maximum number of MIPI-CSI data lanes supported

wclk_ext
    CSI wrapper clock: 0 - bus clock, 1 - external SCLK_CAM

csis_fmt
    current CSIS pixel format

format
    common media bus format for the source and sink pad

slock
    spinlock protecting structure members below

pkt_buf
    the frame embedded (non-image) data buffer

events
    MIPI-CSIS event (error) counters

.. _`csis_pix_format`:

struct csis_pix_format
======================

.. c:type:: struct csis_pix_format

    CSIS pixel format description

.. _`csis_pix_format.definition`:

Definition
----------

.. code-block:: c

    struct csis_pix_format {
        unsigned int pix_width_alignment;
        u32 code;
        u32 fmt_reg;
        u8 data_alignment;
    }

.. _`csis_pix_format.members`:

Members
-------

pix_width_alignment
    horizontal pixel alignment, width will be
    multiple of 2^pix_width_alignment

code
    corresponding media bus code

fmt_reg
    S5PCSIS_CONFIG register value

data_alignment
    MIPI-CSI data alignment in bits

.. This file was automatic generated / don't edit.

