.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/base/firmware_loader/fallback.h

.. _`firmware_fallback_config`:

struct firmware_fallback_config
===============================

.. c:type:: struct firmware_fallback_config

    firmware fallback configuration settings

.. _`firmware_fallback_config.definition`:

Definition
----------

.. code-block:: c

    struct firmware_fallback_config {
        unsigned int force_sysfs_fallback;
        unsigned int ignore_sysfs_fallback;
        int old_timeout;
        int loading_timeout;
    }

.. _`firmware_fallback_config.members`:

Members
-------

force_sysfs_fallback
    force the sysfs fallback mechanism to be used
    as if one had enabled CONFIG_FW_LOADER_USER_HELPER_FALLBACK=y.
    Useful to help debug a CONFIG_FW_LOADER_USER_HELPER_FALLBACK=y
    functionality on a kernel where that config entry has been disabled.

ignore_sysfs_fallback
    force to disable the sysfs fallback mechanism.
    This emulates the behaviour as if we had set the kernel
    config CONFIG_FW_LOADER_USER_HELPER=n.

old_timeout
    for internal use

loading_timeout
    the timeout to wait for the fallback mechanism before
    giving up, in seconds.

.. _`firmware_fallback_config.description`:

Description
-----------

Helps describe and fine tune the fallback mechanism.

.. This file was automatic generated / don't edit.

