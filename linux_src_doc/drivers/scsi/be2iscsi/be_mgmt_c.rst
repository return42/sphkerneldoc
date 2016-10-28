.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/be2iscsi/be_mgmt.c

.. _`mgmt_reopen_session`:

mgmt_reopen_session
===================

.. c:function:: unsigned int mgmt_reopen_session(struct beiscsi_hba *phba, unsigned int reopen_type, unsigned int sess_handle)

    Reopen a session based on reopen_type

    :param struct beiscsi_hba \*phba:
        Device priv structure instance

    :param unsigned int reopen_type:
        Type of reopen_session FW should do.

    :param unsigned int sess_handle:
        Session Handle of the session to be re-opened

.. _`mgmt_reopen_session.description`:

Description
-----------

return
the TAG used for MBOX Command

.. _`mgmt_get_port_name`:

mgmt_get_port_name
==================

.. c:function:: int mgmt_get_port_name(struct be_ctrl_info *ctrl, struct beiscsi_hba *phba)

    Get port name for the function

    :param struct be_ctrl_info \*ctrl:
        ptr to Ctrl Info

    :param struct beiscsi_hba \*phba:
        ptr to the dev priv structure

.. _`mgmt_get_port_name.description`:

Description
-----------

Get the alphanumeric character for port

.. _`mgmt_get_fw_config`:

mgmt_get_fw_config
==================

.. c:function:: int mgmt_get_fw_config(struct be_ctrl_info *ctrl, struct beiscsi_hba *phba)

    Get the FW config for the function

    :param struct be_ctrl_info \*ctrl:
        ptr to Ctrl Info

    :param struct beiscsi_hba \*phba:
        ptr to the dev priv structure

.. _`mgmt_get_fw_config.description`:

Description
-----------

Get the FW config and resources available for the function.
The resources are created based on the count received here.

return

.. _`mgmt_get_fw_config.success`:

Success
-------

0

.. _`mgmt_get_fw_config.failure`:

Failure
-------

Non-Zero Value

.. _`mgmt_epfw_cleanup`:

mgmt_epfw_cleanup
=================

.. c:function:: int mgmt_epfw_cleanup(struct beiscsi_hba *phba, unsigned short ulp_num)

    Inform FW to cleanup data structures.

    :param struct beiscsi_hba \*phba:
        pointer to dev priv structure

    :param unsigned short ulp_num:
        ULP number.

.. _`mgmt_epfw_cleanup.description`:

Description
-----------

return

.. _`mgmt_epfw_cleanup.success`:

Success
-------

0

.. _`mgmt_epfw_cleanup.failure`:

Failure
-------

Non-Zero Value

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

.. _`be_mgmt_get_boot_shandle`:

be_mgmt_get_boot_shandle
========================

.. c:function:: int be_mgmt_get_boot_shandle(struct beiscsi_hba *phba, unsigned int *s_handle)

    Get the session handle

    :param struct beiscsi_hba \*phba:
        device priv structure instance

    :param unsigned int \*s_handle:
        session handle returned for boot session.

.. _`be_mgmt_get_boot_shandle.description`:

Description
-----------

Get the boot target session handle. In case of
crashdump mode driver has to issue and MBX Cmd
for FW to login to boot target

return

.. _`be_mgmt_get_boot_shandle.success`:

Success
-------

0

.. _`be_mgmt_get_boot_shandle.failure`:

Failure
-------

Non-Zero value

.. _`mgmt_set_vlan`:

mgmt_set_vlan
=============

.. c:function:: int mgmt_set_vlan(struct beiscsi_hba *phba, uint16_t vlan_tag)

    Issue and wait for CMD completion

    :param struct beiscsi_hba \*phba:
        device private structure instance

    :param uint16_t vlan_tag:
        VLAN tag

.. _`mgmt_set_vlan.description`:

Description
-----------

Issue the MBX Cmd and wait for the completion of the
command.

returns

.. _`mgmt_set_vlan.success`:

Success
-------

0

.. _`mgmt_set_vlan.failure`:

Failure
-------

Non-Xero Value

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

.. _`beiscsi_logout_fw_sess`:

beiscsi_logout_fw_sess
======================

.. c:function:: int beiscsi_logout_fw_sess(struct beiscsi_hba *phba, uint32_t fw_sess_handle)

    Firmware Session Logout

    :param struct beiscsi_hba \*phba:
        Device priv structure instance

    :param uint32_t fw_sess_handle:
        FW session handle

.. _`beiscsi_logout_fw_sess.description`:

Description
-----------

Logout from the FW established sessions.
returns

.. _`beiscsi_logout_fw_sess.success`:

Success
-------

0

.. _`beiscsi_logout_fw_sess.failure`:

Failure
-------

Non-Zero Value

.. This file was automatic generated / don't edit.

