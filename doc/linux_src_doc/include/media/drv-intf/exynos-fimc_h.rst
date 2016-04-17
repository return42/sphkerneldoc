.. -*- coding: utf-8; mode: rst -*-

=============
exynos-fimc.h
=============


.. _`fimc_source_info`:

struct fimc_source_info
=======================

.. c:type:: fimc_source_info

    video source description required for the host interface configuration


.. _`fimc_source_info.definition`:

Definition
----------

.. code-block:: c

  struct fimc_source_info {
    enum fimc_bus_type fimc_bus_type;
    enum fimc_bus_type sensor_bus_type;
    u16 flags;
    u16 mux_id;
  };


.. _`fimc_source_info.members`:

Members
-------

:``fimc_bus_type``:
    FIMC camera input type

:``sensor_bus_type``:
    image sensor bus type, MIPI, ITU-R BT.601 etc.

:``flags``:
    the parallel sensor bus flags defining signals polarity (V4L2_MBUS\_\*)

:``mux_id``:
    FIMC camera interface multiplexer index (separate for MIPI and ITU)




.. _`fimc_fmt`:

struct fimc_fmt
===============

.. c:type:: fimc_fmt

    color format data structure


.. _`fimc_fmt.definition`:

Definition
----------

.. code-block:: c

  struct fimc_fmt {
    u32 mbus_code;
    char * name;
    u32 fourcc;
    u32 color;
    u16 memplanes;
    u16 colplanes;
    u8 colorspace;
    u8 depth[FIMC_MAX_PLANES];
    u16 mdataplanes;
    u16 flags;
    #define FMT_FLAGS_CAM		(1 \\\lt;\\\lt; 0)
    #define FMT_FLAGS_M2M_IN	(1 \\\lt;\\\lt; 1)
    #define FMT_FLAGS_M2M_OUT	(1 \\\lt;\\\lt; 2)
    #define FMT_FLAGS_M2M		(1 \\\lt;\\\lt; 1 | 1 \\\lt;\\\lt; 2)
    #define FMT_HAS_ALPHA		(1 \\\lt;\\\lt; 3)
    #define FMT_FLAGS_COMPRESSED	(1 \\\lt;\\\lt; 4)
    #define FMT_FLAGS_WRITEBACK	(1 \\\lt;\\\lt; 5)
    #define FMT_FLAGS_RAW_BAYER	(1 \\\lt;\\\lt; 6)
    #define FMT_FLAGS_YUV		(1 \\\lt;\\\lt; 7)
  };


.. _`fimc_fmt.members`:

Members
-------

:``mbus_code``:
    media bus pixel code, -1 if not applicable

:``name``:
    format description

:``fourcc``:
    fourcc code for this format, 0 if not applicable

:``color``:
    the driver's private color format id

:``memplanes``:
    number of physically non-contiguous data planes

:``colplanes``:
    number of physically contiguous data planes

:``colorspace``:
    v4l2 colorspace (V4L2_COLORSPACE\_\*)

:``depth[FIMC_MAX_PLANES]``:
    per plane driver's private 'number of bits per pixel'

:``mdataplanes``:
    bitmask indicating meta data plane(s), (1 << plane_no)

:``flags``:
    flags indicating which operation mode format applies to


