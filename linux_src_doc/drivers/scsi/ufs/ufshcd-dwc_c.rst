.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/ufs/ufshcd-dwc.c

.. _`ufshcd_dwc_program_clk_div`:

ufshcd_dwc_program_clk_div
==========================

.. c:function:: void ufshcd_dwc_program_clk_div(struct ufs_hba *hba, u32 divider_val)

    This function programs the clk divider value. This value is needed to provide 1 microsecond tick to unipro layer.

    :param hba:
        Private Structure pointer
    :type hba: struct ufs_hba \*

    :param divider_val:
        clock divider value to be programmed
    :type divider_val: u32

.. _`ufshcd_dwc_link_is_up`:

ufshcd_dwc_link_is_up
=====================

.. c:function:: int ufshcd_dwc_link_is_up(struct ufs_hba *hba)

    Check if link is up

    :param hba:
        private structure poitner
    :type hba: struct ufs_hba \*

.. _`ufshcd_dwc_link_is_up.description`:

Description
-----------

Returns 0 on success, non-zero value on failure

.. _`ufshcd_dwc_connection_setup`:

ufshcd_dwc_connection_setup
===========================

.. c:function:: int ufshcd_dwc_connection_setup(struct ufs_hba *hba)

    This function configures both the local side (host) and the peer side (device) unipro attributes to establish the connection to application/ cport. This function is not required if the hardware is properly configured to have this connection setup on reset. But invoking this function does no harm and should be fine even working with any ufs device.

    :param hba:
        pointer to drivers private data
    :type hba: struct ufs_hba \*

.. _`ufshcd_dwc_connection_setup.description`:

Description
-----------

Returns 0 on success non-zero value on failure

.. _`ufshcd_dwc_link_startup_notify`:

ufshcd_dwc_link_startup_notify
==============================

.. c:function:: int ufshcd_dwc_link_startup_notify(struct ufs_hba *hba, enum ufs_notify_change_status status)

    UFS Host DWC specific link startup sequence

    :param hba:
        private structure poitner
    :type hba: struct ufs_hba \*

    :param status:
        Callback notify status
    :type status: enum ufs_notify_change_status

.. _`ufshcd_dwc_link_startup_notify.description`:

Description
-----------

Returns 0 on success, non-zero value on failure

.. This file was automatic generated / don't edit.

