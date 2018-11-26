.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/dccp/ccids/lib/tfrc.h

.. _`tfrc_ewma`:

tfrc_ewma
=========

.. c:function:: u32 tfrc_ewma(const u32 avg, const u32 newval, const u8 weight)

    Exponentially weighted moving average

    :param avg:
        *undescribed*
    :type avg: const u32

    :param newval:
        *undescribed*
    :type newval: const u32

    :param weight:
        Weight to be used as damping factor, in units of 1/10
    :type weight: const u8

.. This file was automatic generated / don't edit.

