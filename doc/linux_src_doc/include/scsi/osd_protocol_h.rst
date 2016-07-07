.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/scsi/osd_protocol.h

.. _`osd_sec_set_caps`:

osd_sec_set_caps
================

.. c:function:: void osd_sec_set_caps(struct osd_capability_head *cap, u16 bit_mask)

    set cap-bits into the capabilities header

    :param struct osd_capability_head \*cap:
        The osd_capability_head to set cap bits to.

    :param u16 bit_mask:
        Use an ORed list of enum osd_capability_bit_masks values

.. _`osd_sec_set_caps.description`:

Description
-----------

permissions_bit_mask is unaligned use below to set into caps
in a version independent way

.. This file was automatic generated / don't edit.

