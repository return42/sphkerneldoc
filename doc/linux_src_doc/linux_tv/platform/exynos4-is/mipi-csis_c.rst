.. -*- coding: utf-8; mode: rst -*-

===========
mipi-csis.c
===========



.. _xref_struct_csis_state:

struct csis_state
=================

.. c:type:: struct csis_state

    the driver's internal state data structure



Definition
----------

.. code-block:: c

  struct csis_state {
    struct mutex lock;
    struct media_pad pads[CSIS_PADS_NUM];
    struct v4l2_subdev sd;
    u8 index;
    struct platform_device * pdev;
    struct phy * phy;
    void __iomem * regs;
    struct regulator_bulk_data supplies[CSIS_NUM_SUPPLIES];
    struct clk * clock[NUM_CSIS_CLOCKS];
    int irq;
    u32 interrupt_mask;
    u32 flags;
    u32 hs_settle;
    u32 num_lanes;
    u32 max_num_lanes;
    u8 wclk_ext;
    const struct csis_pix_format * csis_fmt;
    struct v4l2_mbus_framefmt format;
    spinlock_t slock;
    struct csis_pktbuf pkt_buf;
    struct s5pcsis_event events[S5PCSIS_NUM_EVENTS];
  };



Members
-------

:``struct mutex lock``:
    mutex serializing the subdev and power management operations,
           protecting **format** and **flags** members

:``struct media_pad pads[CSIS_PADS_NUM]``:
    CSIS pads array

:``struct v4l2_subdev sd``:
    v4l2_subdev associated with CSIS device instance

:``u8 index``:
    the hardware instance index

:``struct platform_device * pdev``:
    CSIS platform device

:``struct phy * phy``:
    pointer to the CSIS generic PHY

:``void __iomem * regs``:
    mmaped I/O registers memory

:``struct regulator_bulk_data supplies[CSIS_NUM_SUPPLIES]``:
    CSIS regulator supplies

:``struct clk * clock[NUM_CSIS_CLOCKS]``:
    CSIS clocks

:``int irq``:
    requested s5p-mipi-csis irq number

:``u32 interrupt_mask``:
    interrupt mask of the all used interrupts

:``u32 flags``:
    the state variable for power and streaming control

:``u32 hs_settle``:
    HS-RX settle time

:``u32 num_lanes``:
    number of MIPI-CSI data lanes used

:``u32 max_num_lanes``:
    maximum number of MIPI-CSI data lanes supported

:``u8 wclk_ext``:
    CSI wrapper clock: 0 - bus clock, 1 - external SCLK_CAM

:``const struct csis_pix_format * csis_fmt``:
    current CSIS pixel format

:``struct v4l2_mbus_framefmt format``:
    common media bus format for the source and sink pad

:``spinlock_t slock``:
    spinlock protecting structure members below

:``struct csis_pktbuf pkt_buf``:
    the frame embedded (non-image) data buffer

:``struct s5pcsis_event events[S5PCSIS_NUM_EVENTS]``:
    MIPI-CSIS event (error) counters





.. _xref_struct_csis_pix_format:

struct csis_pix_format
======================

.. c:type:: struct csis_pix_format

    CSIS pixel format description



Definition
----------

.. code-block:: c

  struct csis_pix_format {
    unsigned int pix_width_alignment;
    u32 code;
    u32 fmt_reg;
    u8 data_alignment;
  };



Members
-------

:``unsigned int pix_width_alignment``:
    horizontal pixel alignment, width will be
                          multiple of 2^pix_width_alignment

:``u32 code``:
    corresponding media bus code

:``u32 fmt_reg``:
    S5PCSIS_CONFIG register value

:``u8 data_alignment``:
    MIPI-CSI data alignment in bits



