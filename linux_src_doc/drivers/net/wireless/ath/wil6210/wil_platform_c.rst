.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/wil6210/wil_platform.c

.. _`wil_platform_init`:

wil_platform_init
=================

.. c:function:: void *wil_platform_init(struct device *dev, struct wil_platform_ops *ops, const struct wil_platform_rops *rops, void *wil_handle)

    wil6210 platform module init

    :param struct device \*dev:
        *undescribed*

    :param struct wil_platform_ops \*ops:
        *undescribed*

    :param const struct wil_platform_rops \*rops:
        *undescribed*

    :param void \*wil_handle:
        *undescribed*

.. _`wil_platform_init.description`:

Description
-----------

The function must be called before all other functions in this module.
It returns a handle which is used with the rest of the API

.. This file was automatic generated / don't edit.

