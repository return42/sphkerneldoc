.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/s3c-camif/camif-core.c

.. _`s3c_camif_find_format`:

s3c_camif_find_format
=====================

.. c:function:: const struct camif_fmt *s3c_camif_find_format(struct camif_vp *vp, const u32 *pixelformat, int index)

    lookup camif color format by fourcc or an index

    :param struct camif_vp \*vp:
        *undescribed*

    :param const u32 \*pixelformat:
        fourcc to match, ignored if null

    :param int index:
        index to the camif_formats array, ignored if negative

.. This file was automatic generated / don't edit.

