.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/pxa_camera.c

.. _`pxa_mbus_packing`:

enum pxa_mbus_packing
=====================

.. c:type:: enum pxa_mbus_packing

    data packing types on the media-bus

.. _`pxa_mbus_packing.definition`:

Definition
----------

.. code-block:: c

    enum pxa_mbus_packing {
        PXA_MBUS_PACKING_NONE,
        PXA_MBUS_PACKING_2X8_PADHI,
        PXA_MBUS_PACKING_EXTEND16
    };

.. _`pxa_mbus_packing.constants`:

Constants
---------

PXA_MBUS_PACKING_NONE
    no packing, bit-for-bit transfer to RAM, one
    sample represents one pixel

PXA_MBUS_PACKING_2X8_PADHI
    16 bits transferred in 2 8-bit samples, in the
    possibly incomplete byte high bits are padding

PXA_MBUS_PACKING_EXTEND16
    sample width (e.g., 10 bits) has to be extended
    to 16 bits

.. _`pxa_mbus_order`:

enum pxa_mbus_order
===================

.. c:type:: enum pxa_mbus_order

    sample order on the media bus

.. _`pxa_mbus_order.definition`:

Definition
----------

.. code-block:: c

    enum pxa_mbus_order {
        PXA_MBUS_ORDER_LE,
        PXA_MBUS_ORDER_BE
    };

.. _`pxa_mbus_order.constants`:

Constants
---------

PXA_MBUS_ORDER_LE
    least significant sample first

PXA_MBUS_ORDER_BE
    most significant sample first

.. _`pxa_mbus_layout`:

enum pxa_mbus_layout
====================

.. c:type:: enum pxa_mbus_layout

    planes layout in memory

.. _`pxa_mbus_layout.definition`:

Definition
----------

.. code-block:: c

    enum pxa_mbus_layout {
        PXA_MBUS_LAYOUT_PACKED,
        PXA_MBUS_LAYOUT_PLANAR_2Y_U_V,
        PXA_MBUS_LAYOUT_PLANAR_2Y_C,
        PXA_MBUS_LAYOUT_PLANAR_Y_C
    };

.. _`pxa_mbus_layout.constants`:

Constants
---------

PXA_MBUS_LAYOUT_PACKED
    color components packed

PXA_MBUS_LAYOUT_PLANAR_2Y_U_V
    YUV components stored in 3 planes (4:2:2)

PXA_MBUS_LAYOUT_PLANAR_2Y_C
    YUV components stored in a luma and a
    chroma plane (C plane is half the size
    of Y plane)

PXA_MBUS_LAYOUT_PLANAR_Y_C
    YUV components stored in a luma and a
    chroma plane (C plane is the same size
    as Y plane)

.. _`pxa_mbus_pixelfmt`:

struct pxa_mbus_pixelfmt
========================

.. c:type:: struct pxa_mbus_pixelfmt

    Data format on the media bus

.. _`pxa_mbus_pixelfmt.definition`:

Definition
----------

.. code-block:: c

    struct pxa_mbus_pixelfmt {
        const char *name;
        u32 fourcc;
        enum pxa_mbus_packing packing;
        enum pxa_mbus_order order;
        enum pxa_mbus_layout layout;
        u8 bits_per_sample;
    }

.. _`pxa_mbus_pixelfmt.members`:

Members
-------

name
    Name of the format

fourcc
    Fourcc code, that will be obtained if the data is
    stored in memory in the following way:

packing
    Type of sample-packing, that has to be used

order
    Sample order when storing in memory

layout
    Planes layout in memory

bits_per_sample
    How many bits the bridge has to sample

.. _`pxa_mbus_lookup`:

struct pxa_mbus_lookup
======================

.. c:type:: struct pxa_mbus_lookup

    Lookup FOURCC IDs by mediabus codes for pass-through

.. _`pxa_mbus_lookup.definition`:

Definition
----------

.. code-block:: c

    struct pxa_mbus_lookup {
        u32 code;
        struct pxa_mbus_pixelfmt fmt;
    }

.. _`pxa_mbus_lookup.members`:

Members
-------

code
    mediabus pixel-code

fmt
    pixel format description

.. _`pxa_camera_format_xlate`:

struct pxa_camera_format_xlate
==============================

.. c:type:: struct pxa_camera_format_xlate

    match between host and sensor formats

.. _`pxa_camera_format_xlate.definition`:

Definition
----------

.. code-block:: c

    struct pxa_camera_format_xlate {
        u32 code;
        const struct pxa_mbus_pixelfmt *host_fmt;
    }

.. _`pxa_camera_format_xlate.members`:

Members
-------

code
    code of a sensor provided format

host_fmt
    host format after host translation from code

.. _`pxa_camera_format_xlate.description`:

Description
-----------

Host and sensor translation structure. Used in table of host and sensor
formats matchings in pxa_camera_device. A host can override the generic list
generation by implementing \ :c:func:`get_formats`\ , and use it for format checks and
format setup.

.. _`pxa_init_dma_channel`:

pxa_init_dma_channel
====================

.. c:function:: int pxa_init_dma_channel(struct pxa_camera_dev *pcdev, struct pxa_buffer *buf, int channel, struct scatterlist *sg, int sglen)

    init dma descriptors

    :param pcdev:
        pxa camera device
    :type pcdev: struct pxa_camera_dev \*

    :param buf:
        pxa camera buffer
    :type buf: struct pxa_buffer \*

    :param channel:
        dma channel (0 => 'Y', 1 => 'U', 2 => 'V')
    :type channel: int

    :param sg:
        dma scatter list
    :type sg: struct scatterlist \*

    :param sglen:
        dma scatter list length
    :type sglen: int

.. _`pxa_init_dma_channel.description`:

Description
-----------

Prepares the pxa dma descriptors to transfer one camera channel.

Returns 0 if success or -ENOMEM if no memory is available

.. _`pxa_dma_start_channels`:

pxa_dma_start_channels
======================

.. c:function:: void pxa_dma_start_channels(struct pxa_camera_dev *pcdev)

    start DMA channel for active buffer

    :param pcdev:
        pxa camera device
    :type pcdev: struct pxa_camera_dev \*

.. _`pxa_dma_start_channels.description`:

Description
-----------

Initialize DMA channels to the beginning of the active video buffer, and
start these channels.

.. _`pxa_camera_start_capture`:

pxa_camera_start_capture
========================

.. c:function:: void pxa_camera_start_capture(struct pxa_camera_dev *pcdev)

    start video capturing

    :param pcdev:
        camera device
    :type pcdev: struct pxa_camera_dev \*

.. _`pxa_camera_start_capture.description`:

Description
-----------

Launch capturing. DMA channels should not be active yet. They should get
activated at the end of frame interrupt, to capture only whole frames, and
never begin the capture of a partial frame.

.. _`pxa_camera_check_link_miss`:

pxa_camera_check_link_miss
==========================

.. c:function:: void pxa_camera_check_link_miss(struct pxa_camera_dev *pcdev, dma_cookie_t last_submitted, dma_cookie_t last_issued)

    check missed DMA linking

    :param pcdev:
        camera device
    :type pcdev: struct pxa_camera_dev \*

    :param last_submitted:
        an opaque DMA cookie for last submitted
    :type last_submitted: dma_cookie_t

    :param last_issued:
        an opaque DMA cookie for last issued
    :type last_issued: dma_cookie_t

.. _`pxa_camera_check_link_miss.description`:

Description
-----------

The DMA chaining is done with DMA running. This means a tiny temporal window
remains, where a buffer is queued on the chain, while the chain is already
stopped. This means the tailed buffer would never be transferred by DMA.
This function restarts the capture for this corner case, where :
- \ :c:func:`DADR`\  == DADDR_STOP
- a videobuffer is queued on the pcdev->capture list

Please check the "DMA hot chaining timeslice issue" in
Documentation/media/v4l-drivers/pxa_camera.rst

.. _`pxa_camera_check_link_miss.context`:

Context
-------

should only be called within the dma irq handler

.. This file was automatic generated / don't edit.

