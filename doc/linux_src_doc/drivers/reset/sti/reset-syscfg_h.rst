.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/reset/sti/reset-syscfg.h

.. _`syscfg_reset_probe`:

syscfg_reset_probe
==================

.. c:function:: int syscfg_reset_probe(struct platform_device *pdev)

    platform device probe function used by syscfg reset controller drivers. This registers a reset controller configured by the OF match data for the compatible device which should be of type "struct syscfg_reset_controller_data".

    :param struct platform_device \*pdev:
        platform device

.. This file was automatic generated / don't edit.

