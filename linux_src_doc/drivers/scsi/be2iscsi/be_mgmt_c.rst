.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/be2iscsi/be_mgmt.c

.. _`beiscsi_modify_eq_delay`:

beiscsi_modify_eq_delay
=======================

.. c:function:: int beiscsi_modify_eq_delay(struct beiscsi_hba *phba, struct be_set_eqd *set_eqd, int num)

    2016 Broadcom All rights reserved.

    :param struct beiscsi_hba \*phba:
        *undescribed*

    :param struct be_set_eqd \*set_eqd:
        *undescribed*

    :param int num:
        *undescribed*

.. _`beiscsi_modify_eq_delay.description`:

Description
-----------

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License version 2
as published by the Free Software Foundation.  The full GNU General
Public License is included in this distribution in the file called COPYING.

.. _`beiscsi_modify_eq_delay.written-by`:

Written by
----------

Jayamohan Kallickal (jayamohan.kallickal@broadcom.com)

.. _`beiscsi_modify_eq_delay.contact-information`:

Contact Information
-------------------

linux-drivers@broadcom.com

Emulex
3333 Susan Street
Costa Mesa, CA 92626

.. _`mgmt_open_connection`:

mgmt_open_connection
====================

.. c:function:: int mgmt_open_connection(struct beiscsi_hba *phba, struct sockaddr *dst_addr, struct beiscsi_endpoint *beiscsi_ep, struct be_dma_mem *nonemb_cmd)

    Establish a TCP CXN

    :param struct beiscsi_hba \*phba:
        *undescribed*

    :param struct sockaddr \*dst_addr:
        Destination Address

    :param struct beiscsi_endpoint \*beiscsi_ep:
        ptr to device endpoint struct

    :param struct be_dma_mem \*nonemb_cmd:
        ptr to memory allocated for command

.. _`mgmt_open_connection.description`:

Description
-----------

return

.. _`mgmt_open_connection.success`:

Success
-------

Tag number of the MBX Command issued

.. _`mgmt_open_connection.failure`:

Failure
-------

Error code

.. _`beiscsi_if_set_vlan`:

beiscsi_if_set_vlan
===================

.. c:function:: int beiscsi_if_set_vlan(struct beiscsi_hba *phba, uint16_t vlan_tag)

    Issue and wait for CMD completion

    :param struct beiscsi_hba \*phba:
        device private structure instance

    :param uint16_t vlan_tag:
        VLAN tag

.. _`beiscsi_if_set_vlan.description`:

Description
-----------

Issue the MBX Cmd and wait for the completion of the
command.

returns

.. _`beiscsi_if_set_vlan.success`:

Success
-------

0

.. _`beiscsi_if_set_vlan.failure`:

Failure
-------

Non-Xero Value

.. _`beiscsi_boot_logout_sess`:

beiscsi_boot_logout_sess
========================

.. c:function:: unsigned int beiscsi_boot_logout_sess(struct beiscsi_hba *phba)

    Logout from boot FW session

    :param struct beiscsi_hba \*phba:
        Device priv structure instance

.. _`beiscsi_boot_logout_sess.description`:

Description
-----------

return
the TAG used for MBOX Command

.. _`beiscsi_boot_reopen_sess`:

beiscsi_boot_reopen_sess
========================

.. c:function:: unsigned int beiscsi_boot_reopen_sess(struct beiscsi_hba *phba)

    Reopen boot session

    :param struct beiscsi_hba \*phba:
        Device priv structure instance

.. _`beiscsi_boot_reopen_sess.description`:

Description
-----------

return
the TAG used for MBOX Command

.. _`beiscsi_boot_get_sinfo`:

beiscsi_boot_get_sinfo
======================

.. c:function:: unsigned int beiscsi_boot_get_sinfo(struct beiscsi_hba *phba)

    Get boot session info

    :param struct beiscsi_hba \*phba:
        device priv structure instance

.. _`beiscsi_boot_get_sinfo.description`:

Description
-----------

Fetches the boot_struct.s_handle info from FW.
return
the TAG used for MBOX Command

.. _`beiscsi_boot_get_shandle`:

beiscsi_boot_get_shandle
========================

.. c:function:: int beiscsi_boot_get_shandle(struct beiscsi_hba *phba, unsigned int *s_handle)

    Get boot session handle

    :param struct beiscsi_hba \*phba:
        device priv structure instance

    :param unsigned int \*s_handle:
        session handle returned for boot session.

.. _`beiscsi_boot_get_shandle.description`:

Description
-----------

return

.. _`beiscsi_boot_get_shandle.success`:

Success
-------

1

.. _`beiscsi_boot_get_shandle.failure`:

Failure
-------

negative

.. _`beiscsi_drvr_ver_disp`:

beiscsi_drvr_ver_disp
=====================

.. c:function:: ssize_t beiscsi_drvr_ver_disp(struct device *dev, struct device_attribute *attr, char *buf)

    Display the driver Name and Version

    :param struct device \*dev:
        ptr to device not used.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param char \*buf:
        contains formatted text driver name and version

.. _`beiscsi_drvr_ver_disp.description`:

Description
-----------

return
size of the formatted string

.. _`beiscsi_fw_ver_disp`:

beiscsi_fw_ver_disp
===================

.. c:function:: ssize_t beiscsi_fw_ver_disp(struct device *dev, struct device_attribute *attr, char *buf)

    Display Firmware Version

    :param struct device \*dev:
        ptr to device not used.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param char \*buf:
        contains formatted text Firmware version

.. _`beiscsi_fw_ver_disp.description`:

Description
-----------

return
size of the formatted string

.. _`beiscsi_active_session_disp`:

beiscsi_active_session_disp
===========================

.. c:function:: ssize_t beiscsi_active_session_disp(struct device *dev, struct device_attribute *attr, char *buf)

    Display Sessions Active

    :param struct device \*dev:
        ptr to device not used.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param char \*buf:
        contains formatted text Session Count

.. _`beiscsi_active_session_disp.description`:

Description
-----------

return
size of the formatted string

.. _`beiscsi_free_session_disp`:

beiscsi_free_session_disp
=========================

.. c:function:: ssize_t beiscsi_free_session_disp(struct device *dev, struct device_attribute *attr, char *buf)

    Display Avaliable Session

    :param struct device \*dev:
        ptr to device not used.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param char \*buf:
        contains formatted text Session Count

.. _`beiscsi_free_session_disp.description`:

Description
-----------

return
size of the formatted string

.. _`beiscsi_adap_family_disp`:

beiscsi_adap_family_disp
========================

.. c:function:: ssize_t beiscsi_adap_family_disp(struct device *dev, struct device_attribute *attr, char *buf)

    Display adapter family.

    :param struct device \*dev:
        ptr to device to get priv structure

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param char \*buf:
        contains formatted text driver name and version

.. _`beiscsi_adap_family_disp.description`:

Description
-----------

return
size of the formatted string

.. _`beiscsi_phys_port_disp`:

beiscsi_phys_port_disp
======================

.. c:function:: ssize_t beiscsi_phys_port_disp(struct device *dev, struct device_attribute *attr, char *buf)

    Display Physical Port Identifier

    :param struct device \*dev:
        ptr to device not used.

    :param struct device_attribute \*attr:
        device attribute, not used.

    :param char \*buf:
        contains formatted text port identifier

.. _`beiscsi_phys_port_disp.description`:

Description
-----------

return
size of the formatted string

.. This file was automatic generated / don't edit.

