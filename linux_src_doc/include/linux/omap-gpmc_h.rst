.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/omap-gpmc.h

.. _`gpmc_omap_onenand_set_timings`:

gpmc_omap_onenand_set_timings
=============================

.. c:function:: int gpmc_omap_onenand_set_timings(struct device *dev, int cs, int freq, int latency, struct gpmc_onenand_info *info)

    set optimized sync timings.

    :param struct device \*dev:
        *undescribed*

    :param int cs:
        Chip Select Region

    :param int freq:
        Chip frequency

    :param int latency:
        Burst latency cycle count

    :param struct gpmc_onenand_info \*info:
        Structure describing parameters used

.. _`gpmc_omap_onenand_set_timings.description`:

Description
-----------

Sets optimized timings for the \ ``cs``\  region based on \ ``freq``\  and \ ``latency``\ .
Updates the \ ``info``\  structure based on the GPMC settings.

.. This file was automatic generated / don't edit.

