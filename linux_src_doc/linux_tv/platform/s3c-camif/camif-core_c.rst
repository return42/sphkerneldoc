.. -*- coding: utf-8; mode: rst -*-

============
camif-core.c
============



.. _xref_s3c_camif_find_format:

s3c_camif_find_format
=====================

.. c:function:: const struct camif_fmt * s3c_camif_find_format (struct camif_vp * vp, const u32 * pixelformat, int index)

    lookup camif color format by fourcc or an index

    :param struct camif_vp * vp:

        _undescribed_

    :param const u32 * pixelformat:
        fourcc to match, ignored if null

    :param int index:
        index to the camif_formats array, ignored if negative


