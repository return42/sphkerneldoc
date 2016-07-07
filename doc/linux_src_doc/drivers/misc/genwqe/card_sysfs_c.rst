.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/genwqe/card_sysfs.c

.. _`curr_bitstream_show`:

curr_bitstream_show
===================

.. c:function:: ssize_t curr_bitstream_show(struct device *dev, struct device_attribute *attr, char *buf)

    Show the current bitstream id

    :param struct device \*dev:
        *undescribed*

    :param struct device_attribute \*attr:
        *undescribed*

    :param char \*buf:
        *undescribed*

.. _`curr_bitstream_show.description`:

Description
-----------

There is a bug in some old versions of the CPLD which selects the
bitstream, which causes the IO_SLU_BITSTREAM register to report
unreliable data in very rare cases. This makes this sysfs
unreliable up to the point were a new CPLD version is being used.

Unfortunately there is no automatic way yet to query the CPLD
version, such that you need to manually ensure via programming
tools that you have a recent version of the CPLD software.

The proposed circumvention is to use a special recovery bitstream
on the backup partition (0) to identify problems while loading the
image.

.. _`next_bitstream_show`:

next_bitstream_show
===================

.. c:function:: ssize_t next_bitstream_show(struct device *dev, struct device_attribute *attr, char *buf)

    Show the next activated bitstream

    :param struct device \*dev:
        *undescribed*

    :param struct device_attribute \*attr:
        *undescribed*

    :param char \*buf:
        *undescribed*

.. _`next_bitstream_show.io_slc_cfgreg_softreset`:

IO_SLC_CFGREG_SOFTRESET
-----------------------

This register can only be accessed by the PF.

.. _`genwqe_is_visible`:

genwqe_is_visible
=================

.. c:function:: umode_t genwqe_is_visible(struct kobject *kobj, struct attribute *attr, int n)

    Determine if sysfs attribute should be visible or not

    :param struct kobject \*kobj:
        *undescribed*

    :param struct attribute \*attr:
        *undescribed*

    :param int n:
        *undescribed*

.. _`genwqe_is_visible.description`:

Description
-----------

VFs have restricted mmio capabilities, so not all sysfs entries
are allowed in VFs.

.. This file was automatic generated / don't edit.

