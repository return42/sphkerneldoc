.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/uwb/drp-ie.c

.. _`uwb_drp_ie_update`:

uwb_drp_ie_update
=================

.. c:function:: int uwb_drp_ie_update(struct uwb_rsv *rsv)

    update a reservation's DRP IE

    :param struct uwb_rsv \*rsv:
        the reservation

.. _`uwb_drp_ie_to_bm`:

uwb_drp_ie_to_bm
================

.. c:function:: void uwb_drp_ie_to_bm(struct uwb_mas_bm *bm, const struct uwb_ie_drp *drp_ie)

    convert DRP allocation fields to a bitmap

    :param struct uwb_mas_bm \*bm:
        *undescribed*

    :param const struct uwb_ie_drp \*drp_ie:
        the DRP IE that contains the allocation fields.

.. _`uwb_drp_ie_to_bm.description`:

Description
-----------

The input format is an array of MAS allocation fields (16 bit Zone
bitmap, 16 bit MAS bitmap) as described in [ECMA-368] section
16.8.6. The output is a full 256 bit MAS bitmap.

We go over all the allocation fields, for each allocation field we
know which zones are impacted. We iterate over all the zones
impacted and call a function that will set the correct MAS bits in
each zone.

.. This file was automatic generated / don't edit.

