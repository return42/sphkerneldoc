.. -*- coding: utf-8; mode: rst -*-

============
amba-pl08x.c
============


.. _`vendor_data`:

struct vendor_data
==================

.. c:type:: vendor_data

    vendor-specific config parameters for PL08x derivatives


.. _`vendor_data.definition`:

Definition
----------

.. code-block:: c

  struct vendor_data {
    u8 channels;
    bool dualmaster;
    bool nomadik;
    bool pl080s;
  };


.. _`vendor_data.members`:

Members
-------

:``channels``:
    the number of channels available in this variant

:``dualmaster``:
    whether this version supports dual AHB masters or not.

:``nomadik``:
    whether the channels have Nomadik security extension bits
    that need to be checked for permission before use and some registers are
    missing

:``pl080s``:
    whether this version is a PL080S, which has separate register and
    LLI word for transfer size.




.. _`pl08x_bus_data`:

struct pl08x_bus_data
=====================

.. c:type:: pl08x_bus_data

    information of source or destination busses for a transfer


.. _`pl08x_bus_data.definition`:

Definition
----------

.. code-block:: c

  struct pl08x_bus_data {
    dma_addr_t addr;
    u8 maxwidth;
    u8 buswidth;
  };


.. _`pl08x_bus_data.members`:

Members
-------

:``addr``:
    current address

:``maxwidth``:
    the maximum width of a transfer on this bus

:``buswidth``:
    the width of this bus in bytes: 1, 2 or 4




.. _`pl08x_phy_chan`:

struct pl08x_phy_chan
=====================

.. c:type:: pl08x_phy_chan

    holder for the physical channels


.. _`pl08x_phy_chan.definition`:

Definition
----------

.. code-block:: c

  struct pl08x_phy_chan {
    unsigned int id;
    spinlock_t lock;
    struct pl08x_dma_chan * serving;
    bool locked;
  };


.. _`pl08x_phy_chan.members`:

Members
-------

:``id``:
    physical index to this channel

:``lock``:
    a lock to use when altering an instance of this struct

:``serving``:
    the virtual channel currently being served by this physical
    channel

:``locked``:
    channel unavailable for the system, e.g. dedicated to secure
    world




.. _`pl08x_sg`:

struct pl08x_sg
===============

.. c:type:: pl08x_sg

    structure containing data per sg


.. _`pl08x_sg.definition`:

Definition
----------

.. code-block:: c

  struct pl08x_sg {
    dma_addr_t src_addr;
    dma_addr_t dst_addr;
    size_t len;
    struct list_head node;
  };


.. _`pl08x_sg.members`:

Members
-------

:``src_addr``:
    src address of sg

:``dst_addr``:
    dst address of sg

:``len``:
    transfer len in bytes

:``node``:
    node for txd's dsg_list




.. _`pl08x_txd`:

struct pl08x_txd
================

.. c:type:: pl08x_txd

    wrapper for struct dma_async_tx_descriptor


.. _`pl08x_txd.definition`:

Definition
----------

.. code-block:: c

  struct pl08x_txd {
    struct virt_dma_desc vd;
    struct list_head dsg_list;
    dma_addr_t llis_bus;
    u32 * llis_va;
    u32 cctl;
    u32 ccfg;
    bool done;
    bool cyclic;
  };


.. _`pl08x_txd.members`:

Members
-------

:``vd``:
    virtual DMA descriptor

:``dsg_list``:
    list of children sg's

:``llis_bus``:
    DMA memory address (physical) start for the LLIs

:``llis_va``:
    virtual memory address start for the LLIs

:``cctl``:
    control reg values for current txd

:``ccfg``:
    config reg values for current txd

:``done``:
    this marks completed descriptors, which should not have their
    mux released.

:``cyclic``:
    indicate cyclic transfers




.. _`pl08x_dma_chan`:

struct pl08x_dma_chan
=====================

.. c:type:: pl08x_dma_chan

    this structure wraps a DMA ENGINE channel


.. _`pl08x_dma_chan.definition`:

Definition
----------

.. code-block:: c

  struct pl08x_dma_chan {
    struct virt_dma_chan vc;
    struct pl08x_phy_chan * phychan;
    const char * name;
    const struct pl08x_channel_data * cd;
    struct pl08x_txd * at;
    struct pl08x_driver_data * host;
    enum pl08x_dma_chan_state state;
    bool slave;
    int signal;
    unsigned mux_use;
  };


.. _`pl08x_dma_chan.members`:

Members
-------

:``vc``:
    wrappped virtual channel

:``phychan``:
    the physical channel utilized by this channel, if there is one

:``name``:
    name of channel

:``cd``:
    channel platform data

:``at``:
    active transaction on this channel

:``host``:
    a pointer to the host (internal use)

:``state``:
    whether the channel is idle, paused, running etc

:``slave``:
    whether this channel is a device (slave) or for memcpy

:``signal``:
    the physical DMA request signal which this channel is using

:``mux_use``:
    count of descriptors using this DMA request signal setting




.. _`pl08x_driver_data`:

struct pl08x_driver_data
========================

.. c:type:: pl08x_driver_data

    the local state holder for the PL08x


.. _`pl08x_driver_data.definition`:

Definition
----------

.. code-block:: c

  struct pl08x_driver_data {
    struct dma_device slave;
    struct dma_device memcpy;
    void __iomem * base;
    struct amba_device * adev;
    const struct vendor_data * vd;
    struct pl08x_platform_data * pd;
    struct pl08x_phy_chan * phy_chans;
    struct dma_pool * pool;
    u8 lli_buses;
    u8 mem_buses;
  };


.. _`pl08x_driver_data.members`:

Members
-------

:``slave``:
    slave engine for this instance

:``memcpy``:
    memcpy engine for this instance

:``base``:
    virtual memory base (remapped) for the PL08x

:``adev``:
    the corresponding AMBA (PrimeCell) bus entry

:``vd``:
    vendor data for this PL08x variant

:``pd``:
    platform data passed in from the platform/machine

:``phy_chans``:
    array of data for the physical channels

:``pool``:
    a pool for the LLI descriptors

:``lli_buses``:
    bitmask to or in to LLI pointer selecting AHB port for LLI
    fetches

:``mem_buses``:
    set to indicate memory transfers on AHB2.


