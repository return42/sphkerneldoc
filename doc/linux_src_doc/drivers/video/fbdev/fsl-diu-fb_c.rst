.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/video/fbdev/fsl-diu-fb.c

.. _`fsl_diu_data`:

struct fsl_diu_data
===================

.. c:type:: struct fsl_diu_data

    per-DIU data structure

.. _`fsl_diu_data.definition`:

Definition
----------

.. code-block:: c

    struct fsl_diu_data {
        dma_addr_t dma_addr;
        struct fb_info fsl_diu_info[NUM_AOIS];
        struct mfb_info mfb[NUM_AOIS];
        struct device_attribute dev_attr;
        unsigned int irq;
        enum fsl_diu_monitor_port monitor_port;
        struct diu __iomem *diu_reg;
        spinlock_t reg_lock;
        u8 dummy_aoi[4 * 4 * 4];
        struct diu_ad dummy_ad;
        struct diu_ad ad[NUM_AOIS];
        u8 gamma[256 * 3];
        __le16 cursor[MAX_CURS * MAX_CURS];
        __le16 blank_cursor[MAX_CURS * MAX_CURS];
        uint8_t edid_data[EDID_LENGTH];
        bool has_edid;
    }

.. _`fsl_diu_data.members`:

Members
-------

dma_addr
    DMA address of this structure

fsl_diu_info
    fb_info objects, one per AOI

dev_attr
    sysfs structure

irq
    IRQ

monitor_port
    the monitor port this DIU is connected to

diu_reg
    pointer to the DIU hardware registers

reg_lock
    spinlock for register access

dummy_aoi
    video buffer for the 4x4 32-bit dummy AOI

dummy_ad
    *undescribed*

ad
    Area Descriptors for each real AOI

gamma
    gamma color table

cursor
    hardware cursor data

has_edid
    *undescribed*

.. _`fsl_diu_data.dummy_ad`:

dummy_ad
--------

DIU Area Descriptor for the dummy AOI

.. _`fsl_diu_data.description`:

Description
-----------

This data structure must be allocated with 32-byte alignment, so that the
internal fields can be aligned properly.

.. _`fsl_diu_name_to_port`:

fsl_diu_name_to_port
====================

.. c:function:: enum fsl_diu_monitor_port fsl_diu_name_to_port(const char *s)

    convert a port name to a monitor port enum

    :param const char \*s:
        *undescribed*

.. _`fsl_diu_name_to_port.description`:

Description
-----------

Takes the name of a monitor port ("dvi", "lvds", or "dlvds") and returns
the enum fsl_diu_monitor_port that corresponds to that string.

For compatibility with older versions, a number ("0", "1", or "2") is also
supported.

If the string is unknown, DVI is assumed.

If the particular port is not supported by the platform, another port
(platform-specific) is chosen instead.

.. _`fsl_diu_get_pixel_format`:

fsl_diu_get_pixel_format
========================

.. c:function:: u32 fsl_diu_get_pixel_format(unsigned int bits_per_pixel)

    return the pixel format for a given color depth

    :param unsigned int bits_per_pixel:
        *undescribed*

.. _`fsl_diu_get_pixel_format.description`:

Description
-----------

The pixel format is a 32-bit value that determine which bits in each
pixel are to be used for each color.  This is the default function used
if the platform does not define its own version.

.. This file was automatic generated / don't edit.

