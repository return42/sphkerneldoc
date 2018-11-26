.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/ufs/ufs-qcom.c

.. _`ufs_qcom_cfg_timers`:

ufs_qcom_cfg_timers
===================

.. c:function:: int ufs_qcom_cfg_timers(struct ufs_hba *hba, u32 gear, u32 hs, u32 rate, bool update_link_startup_timer)

    zero in case of a failure

    :param hba:
        *undescribed*
    :type hba: struct ufs_hba \*

    :param gear:
        *undescribed*
    :type gear: u32

    :param hs:
        *undescribed*
    :type hs: u32

    :param rate:
        *undescribed*
    :type rate: u32

    :param update_link_startup_timer:
        *undescribed*
    :type update_link_startup_timer: bool

.. _`ufs_qcom_advertise_quirks`:

ufs_qcom_advertise_quirks
=========================

.. c:function:: void ufs_qcom_advertise_quirks(struct ufs_hba *hba)

    advertise the known QCOM UFS controller quirks

    :param hba:
        host controller instance
    :type hba: struct ufs_hba \*

.. _`ufs_qcom_advertise_quirks.description`:

Description
-----------

QCOM UFS host controller might have some non standard behaviours (quirks)
than what is specified by UFSHCI specification. Advertise all such
quirks to standard UFS host controller driver so standard takes them into
account.

.. _`ufs_qcom_setup_clocks`:

ufs_qcom_setup_clocks
=====================

.. c:function:: int ufs_qcom_setup_clocks(struct ufs_hba *hba, bool on, enum ufs_notify_change_status status)

    enables/disable clocks

    :param hba:
        host controller instance
    :type hba: struct ufs_hba \*

    :param on:
        If true, enable clocks else disable them.
    :type on: bool

    :param status:
        PRE_CHANGE or POST_CHANGE notify
    :type status: enum ufs_notify_change_status

.. _`ufs_qcom_setup_clocks.description`:

Description
-----------

Returns 0 on success, non-zero on failure.

.. _`ufs_qcom_init`:

ufs_qcom_init
=============

.. c:function:: int ufs_qcom_init(struct ufs_hba *hba)

    bind phy with controller

    :param hba:
        host controller instance
    :type hba: struct ufs_hba \*

.. _`ufs_qcom_init.description`:

Description
-----------

Binds PHY with controller and powers up PHY enabling clocks
and regulators.

Returns -EPROBE_DEFER if binding fails, returns negative error
on phy power up failure and returns zero on success.

.. _`ufs_qcom_probe`:

ufs_qcom_probe
==============

.. c:function:: int ufs_qcom_probe(struct platform_device *pdev)

    probe routine of the driver

    :param pdev:
        pointer to Platform device handle
    :type pdev: struct platform_device \*

.. _`ufs_qcom_probe.description`:

Description
-----------

Return zero for success and non-zero for failure

.. _`ufs_qcom_remove`:

ufs_qcom_remove
===============

.. c:function:: int ufs_qcom_remove(struct platform_device *pdev)

    set driver_data of the device to NULL

    :param pdev:
        pointer to platform device handle
    :type pdev: struct platform_device \*

.. _`ufs_qcom_remove.description`:

Description
-----------

Always returns 0

.. This file was automatic generated / don't edit.

