.. -*- coding: utf-8; mode: rst -*-

============
mx3_camera.c
============



.. _xref_struct_mx3_camera_dev:

struct mx3_camera_dev
=====================

.. c:type:: struct mx3_camera_dev

    i.MX3x camera (CSI) object



Definition
----------

.. code-block:: c

  struct mx3_camera_dev {
    struct clk * clk;
    void __iomem * base;
    struct mx3_camera_pdata * pdata;
    unsigned long platform_flags;
    unsigned long mclk;
    struct list_head capture;
    spinlock_t lock;
    struct mx3_camera_buffer * active;
    struct idmac_channel * idmac_channel[1];
    struct soc_camera_host soc_host;
  };



Members
-------

:``struct clk * clk``:
    pointer to clock

:``void __iomem * base``:
    remapped register base address

:``struct mx3_camera_pdata * pdata``:
    platform data

:``unsigned long platform_flags``:
    platform flags

:``unsigned long mclk``:
    master clock frequency in Hz

:``struct list_head capture``:
    list of capture videobuffers

:``spinlock_t lock``:
    protects video buffer lists

:``struct mx3_camera_buffer * active``:
    active video buffer

:``struct idmac_channel * idmac_channel[1]``:
    array of pointers to IPU DMAC DMA channels

:``struct soc_camera_host soc_host``:
    embedded soc_host object



