.. -*- coding: utf-8; mode: rst -*-

==============
soc_mediabus.h
==============


.. _`soc_mbus_packing`:

enum soc_mbus_packing
=====================

.. c:type:: soc_mbus_packing

    data packing types on the media-bus


.. _`soc_mbus_packing.definition`:

Definition
----------

.. code-block:: c

    enum soc_mbus_packing {
      SOC_MBUS_PACKING_NONE,
      SOC_MBUS_PACKING_2X8_PADHI,
      SOC_MBUS_PACKING_2X8_PADLO,
      SOC_MBUS_PACKING_EXTEND16,
      SOC_MBUS_PACKING_VARIABLE,
      SOC_MBUS_PACKING_1_5X8,
      SOC_MBUS_PACKING_EXTEND32
    };


.. _`soc_mbus_packing.constants`:

Constants
---------

:``SOC_MBUS_PACKING_NONE``:
    no packing, bit-for-bit transfer to RAM, one
    sample represents one pixel

:``SOC_MBUS_PACKING_2X8_PADHI``:
    16 bits transferred in 2 8-bit samples, in the

                                    possibly incomplete byte high bits are padding

:``SOC_MBUS_PACKING_2X8_PADLO``:
    as above, but low bits are padding

:``SOC_MBUS_PACKING_EXTEND16``:
    sample width (e.g., 10 bits) has to be extended
    to 16 bits

:``SOC_MBUS_PACKING_VARIABLE``:
    compressed formats with variable packing

:``SOC_MBUS_PACKING_1_5X8``:
    used for packed YUV 4:2:0 formats, where 4
    pixels occupy 6 bytes in RAM

:``SOC_MBUS_PACKING_EXTEND32``:
    sample width (e.g., 24 bits) has to be extended
    to 32 bits


.. _`soc_mbus_order`:

enum soc_mbus_order
===================

.. c:type:: soc_mbus_order

    sample order on the media bus


.. _`soc_mbus_order.definition`:

Definition
----------

.. code-block:: c

    enum soc_mbus_order {
      SOC_MBUS_ORDER_LE,
      SOC_MBUS_ORDER_BE
    };


.. _`soc_mbus_order.constants`:

Constants
---------

:``SOC_MBUS_ORDER_LE``:
    least significant sample first

:``SOC_MBUS_ORDER_BE``:
    most significant sample first


.. _`soc_mbus_layout`:

enum soc_mbus_layout
====================

.. c:type:: soc_mbus_layout

    planes layout in memory


.. _`soc_mbus_layout.definition`:

Definition
----------

.. code-block:: c

    enum soc_mbus_layout {
      SOC_MBUS_LAYOUT_PACKED,
      SOC_MBUS_LAYOUT_PLANAR_2Y_U_V,
      SOC_MBUS_LAYOUT_PLANAR_2Y_C,
      SOC_MBUS_LAYOUT_PLANAR_Y_C
    };


.. _`soc_mbus_layout.constants`:

Constants
---------

:``SOC_MBUS_LAYOUT_PACKED``:
    color components packed

:``SOC_MBUS_LAYOUT_PLANAR_2Y_U_V``:
    YUV components stored in 3 planes (4:2:2)

:``SOC_MBUS_LAYOUT_PLANAR_2Y_C``:
    YUV components stored in a luma and a
    chroma plane (C plane is half the size
    of Y plane)

:``SOC_MBUS_LAYOUT_PLANAR_Y_C``:
    YUV components stored in a luma and a
    chroma plane (C plane is the same size
    as Y plane)


.. _`soc_mbus_pixelfmt`:

struct soc_mbus_pixelfmt
========================

.. c:type:: soc_mbus_pixelfmt

    Data format on the media bus


.. _`soc_mbus_pixelfmt.definition`:

Definition
----------

.. code-block:: c

  struct soc_mbus_pixelfmt {
    const char * name;
    u32 fourcc;
    enum soc_mbus_packing packing;
    enum soc_mbus_order order;
    u8 bits_per_sample;
  };


.. _`soc_mbus_pixelfmt.members`:

Members
-------

:``name``:
    Name of the format

:``fourcc``:
    Fourcc code, that will be obtained if the data is

:``packing``:
    Type of sample-packing, that has to be used

:``order``:
    Sample order when storing in memory

:``bits_per_sample``:
    How many bits the bridge has to sample




.. _`soc_mbus_lookup`:

struct soc_mbus_lookup
======================

.. c:type:: soc_mbus_lookup

    Lookup FOURCC IDs by mediabus codes for pass-through


.. _`soc_mbus_lookup.definition`:

Definition
----------

.. code-block:: c

  struct soc_mbus_lookup {
    u32 code;
    struct soc_mbus_pixelfmt fmt;
  };


.. _`soc_mbus_lookup.members`:

Members
-------

:``code``:
    mediabus pixel-code

:``fmt``:
    pixel format description


