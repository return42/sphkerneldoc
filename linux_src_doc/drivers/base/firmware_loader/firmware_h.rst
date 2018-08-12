.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/base/firmware_loader/firmware.h

.. _`fw_opt`:

enum fw_opt
===========

.. c:type:: enum fw_opt

    options to control firmware loading behaviour

.. _`fw_opt.definition`:

Definition
----------

.. code-block:: c

    enum fw_opt {
        FW_OPT_UEVENT,
        FW_OPT_NOWAIT,
        FW_OPT_USERHELPER,
        FW_OPT_NO_WARN,
        FW_OPT_NOCACHE,
        FW_OPT_NOFALLBACK
    };

.. _`fw_opt.constants`:

Constants
---------

FW_OPT_UEVENT
    Enables the fallback mechanism to send a kobject uevent
    when the firmware is not found. Userspace is in charge to load the
    firmware using the sysfs loading facility.

FW_OPT_NOWAIT
    Used to describe the firmware request is asynchronous.

FW_OPT_USERHELPER
    Enable the fallback mechanism, in case the direct
    filesystem lookup fails at finding the firmware.  For details refer to
    \ :c:func:`firmware_fallback_sysfs`\ .

FW_OPT_NO_WARN
    Quiet, avoid printing warning messages.

FW_OPT_NOCACHE
    Disables firmware caching. Firmware caching is used to
    cache the firmware upon suspend, so that upon resume races against the
    firmware file lookup on storage is avoided. Used for calls where the
    file may be too big, or where the driver takes charge of its own
    firmware caching mechanism.

FW_OPT_NOFALLBACK
    Disable the fallback mechanism. Takes precedence over
    \ :c:type:`struct FW_OPT_UEVENT <FW_OPT_UEVENT>`\  and \ :c:type:`struct FW_OPT_USERHELPER <FW_OPT_USERHELPER>`\ .

.. This file was automatic generated / don't edit.

