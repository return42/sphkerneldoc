.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iommu/rockchip-iommu.c

.. _`rk_wait_for`:

rk_wait_for
===========

.. c:function::  rk_wait_for( COND,  MS)

    This is NOT safe for use in interrupt context.

    :param  COND:
        *undescribed*

    :param  MS:
        *undescribed*

.. _`rk_wait_for.description`:

Description
-----------

Note that it's important that we check the condition again after having
timed out, since the timeout could be due to preemption or similar and
we've never had a chance to check the condition before the timeout.

.. This file was automatic generated / don't edit.

