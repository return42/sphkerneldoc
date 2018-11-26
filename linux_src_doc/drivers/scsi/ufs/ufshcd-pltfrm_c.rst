.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/ufs/ufshcd-pltfrm.c

.. _`ufshcd_parse_regulator_info`:

ufshcd_parse_regulator_info
===========================

.. c:function:: int ufshcd_parse_regulator_info(struct ufs_hba *hba)

    get regulator info from device tree

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

.. _`ufshcd_parse_regulator_info.description`:

Description
-----------

Get regulator info from device tree for vcc, vccq, vccq2 power supplies.
If any of the supplies are not defined it is assumed that they are always-on
and hence return zero. If the property is defined but parsing is failed
then return corresponding error.

.. _`ufshcd_pltfrm_suspend`:

ufshcd_pltfrm_suspend
=====================

.. c:function:: int ufshcd_pltfrm_suspend(struct device *dev)

    suspend power management function

    :param dev:
        pointer to device handle
    :type dev: struct device \*

.. _`ufshcd_pltfrm_suspend.description`:

Description
-----------

Returns 0 if successful
Returns non-zero otherwise

.. _`ufshcd_pltfrm_resume`:

ufshcd_pltfrm_resume
====================

.. c:function:: int ufshcd_pltfrm_resume(struct device *dev)

    resume power management function

    :param dev:
        pointer to device handle
    :type dev: struct device \*

.. _`ufshcd_pltfrm_resume.description`:

Description
-----------

Returns 0 if successful
Returns non-zero otherwise

.. _`ufshcd_pltfrm_init`:

ufshcd_pltfrm_init
==================

.. c:function:: int ufshcd_pltfrm_init(struct platform_device *pdev, struct ufs_hba_variant_ops *vops)

    probe routine of the driver

    :param pdev:
        pointer to Platform device handle
    :type pdev: struct platform_device \*

    :param vops:
        pointer to variant ops
    :type vops: struct ufs_hba_variant_ops \*

.. _`ufshcd_pltfrm_init.description`:

Description
-----------

Returns 0 on success, non-zero value on failure

.. This file was automatic generated / don't edit.

