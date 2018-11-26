.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/wil6210/wil_platform.h

.. _`wil_platform_ops`:

struct wil_platform_ops
=======================

.. c:type:: struct wil_platform_ops

    wil platform module calls from this driver to platform driver

.. _`wil_platform_ops.definition`:

Definition
----------

.. code-block:: c

    struct wil_platform_ops {
        int (*bus_request)(void *handle, uint32_t kbps );
        int (*suspend)(void *handle, bool keep_device_power);
        int (*resume)(void *handle, bool device_powered_on);
        void (*uninit)(void *handle);
        int (*notify)(void *handle, enum wil_platform_event evt);
        int (*get_capa)(void *handle);
        void (*set_features)(void *handle, int features);
    }

.. _`wil_platform_ops.members`:

Members
-------

bus_request
    *undescribed*

suspend
    *undescribed*

resume
    *undescribed*

uninit
    *undescribed*

notify
    *undescribed*

get_capa
    *undescribed*

set_features
    *undescribed*

.. _`wil_platform_rops`:

struct wil_platform_rops
========================

.. c:type:: struct wil_platform_rops

    wil platform module callbacks from platform driver to this driver

.. _`wil_platform_rops.definition`:

Definition
----------

.. code-block:: c

    struct wil_platform_rops {
        int (*ramdump)(void *wil_handle, void *buf, uint32_t size);
        int (*fw_recovery)(void *wil_handle);
    }

.. _`wil_platform_rops.members`:

Members
-------

ramdump
    store a ramdump from the wil firmware. The platform
    driver may add additional data to the ramdump to
    generate the final crash dump.

fw_recovery
    start a firmware recovery process. Called as
    part of a crash recovery process which may include other
    related platform subsystems.

.. _`wil_platform_init`:

wil_platform_init
=================

.. c:function:: void *wil_platform_init(struct device *dev, struct wil_platform_ops *ops, const struct wil_platform_rops *rops, void *wil_handle)

    initialize the platform driver

    :param dev:
        *undescribed*
    :type dev: struct device \*

    :param ops:
        *undescribed*
    :type ops: struct wil_platform_ops \*

    :param rops:
        *undescribed*
    :type rops: const struct wil_platform_rops \*

    :param wil_handle:
        *undescribed*
    :type wil_handle: void \*

.. _`wil_platform_init.description`:

Description
-----------

\ ``dev``\  - pointer to the wil6210 device
\ ``ops``\  - structure with platform driver operations. Platform
driver will fill this structure with function pointers.
\ ``rops``\  - structure with callbacks from platform driver to
this driver. The platform driver copies the structure to
its own storage. Can be NULL if this driver does not
support crash recovery.
\ ``wil_handle``\  - context for this driver that will be passed
when platform driver invokes one of the callbacks in
rops. May be NULL if rops is NULL.

.. This file was automatic generated / don't edit.

