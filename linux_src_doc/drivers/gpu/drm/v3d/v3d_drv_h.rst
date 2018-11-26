.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/v3d/v3d_drv.h

.. _`wait_for`:

wait_for
========

.. c:function::  wait_for( COND,  MS)

    magic (register) wait macro

    :param COND:
        *undescribed*
    :type COND: 

    :param MS:
        *undescribed*
    :type MS: 

.. _`wait_for.description`:

Description
-----------

Does the right thing for modeset paths when run under kdgb or similar atomic
contexts. Note that it's important that we check the condition again after
having timed out, since the timeout could be due to preemption or similar and
we've never had a chance to check the condition before the timeout.

.. This file was automatic generated / don't edit.

