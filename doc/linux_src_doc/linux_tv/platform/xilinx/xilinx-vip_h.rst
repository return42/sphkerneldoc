.. -*- coding: utf-8; mode: rst -*-

============
xilinx-vip.h
============



.. _xref_struct_xvip_device:

struct xvip_device
==================

.. c:type:: struct xvip_device

    Xilinx Video IP device structure



Definition
----------

.. code-block:: c

  struct xvip_device {
    struct v4l2_subdev subdev;
    struct device * dev;
    void __iomem * iomem;
    struct clk * clk;
    u32 saved_ctrl;
  };



Members
-------

:``struct v4l2_subdev subdev``:
    V4L2 subdevice

:``struct device * dev``:
    (OF) device

:``void __iomem * iomem``:
    device I/O register space remapped to kernel virtual memory

:``struct clk * clk``:
    video core clock

:``u32 saved_ctrl``:
    saved control register for resume / suspend





.. _xref_struct_xvip_video_format:

struct xvip_video_format
========================

.. c:type:: struct xvip_video_format

    Xilinx Video IP video format description



Definition
----------

.. code-block:: c

  struct xvip_video_format {
    unsigned int vf_code;
    unsigned int width;
    const char * pattern;
    unsigned int code;
    unsigned int bpp;
    u32 fourcc;
    const char * description;
  };



Members
-------

:``unsigned int vf_code``:
    AXI4 video format code

:``unsigned int width``:
    AXI4 format width in bits per component

:``const char * pattern``:
    CFA pattern for Mono/Sensor formats

:``unsigned int code``:
    media bus format code

:``unsigned int bpp``:
    bytes per pixel (when stored in memory)

:``u32 fourcc``:
    V4L2 pixel format FCC identifier

:``const char * description``:
    format description, suitable for userspace



