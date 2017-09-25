.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/firewire/iso-resources.h

.. _`fw_iso_resources`:

struct fw_iso_resources
=======================

.. c:type:: struct fw_iso_resources

    manages channel/bandwidth allocation

.. _`fw_iso_resources.definition`:

Definition
----------

.. code-block:: c

    struct fw_iso_resources {
        u64 channels_mask;
        struct fw_unit *unit;
        struct mutex mutex;
        unsigned int channel;
        unsigned int bandwidth;
        unsigned int bandwidth_overhead;
        int generation;
        bool allocated;
    }

.. _`fw_iso_resources.members`:

Members
-------

channels_mask
    if the device does not support all channel numbers, set this
    bit mask to something else than the default (all ones)

unit
    *undescribed*

mutex
    *undescribed*

channel
    *undescribed*

bandwidth
    *undescribed*

bandwidth_overhead
    *undescribed*

generation
    *undescribed*

allocated
    *undescribed*

.. _`fw_iso_resources.description`:

Description
-----------

This structure manages (de)allocation of isochronous resources (channel and
bandwidth) for one isochronous stream.

.. This file was automatic generated / don't edit.

