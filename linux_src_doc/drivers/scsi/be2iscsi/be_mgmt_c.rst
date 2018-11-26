.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/be2iscsi/be_mgmt.c

.. _`mgmt_open_connection`:

mgmt_open_connection
====================

.. c:function:: int mgmt_open_connection(struct beiscsi_hba *phba, struct sockaddr *dst_addr, struct beiscsi_endpoint *beiscsi_ep, struct be_dma_mem *nonemb_cmd)

    Establish a TCP CXN

    :param phba:
        *undescribed*
    :type phba: struct beiscsi_hba \*

    :param dst_addr:
        Destination Address
    :type dst_addr: struct sockaddr \*

    :param beiscsi_ep:
        ptr to device endpoint struct
    :type beiscsi_ep: struct beiscsi_endpoint \*

    :param nonemb_cmd:
        ptr to memory allocated for command
    :type nonemb_cmd: struct be_dma_mem \*

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

.. _`beiscsi_get_initiator_name`:

beiscsi_get_initiator_name
==========================

.. c:function:: int beiscsi_get_initiator_name(struct beiscsi_hba *phba, char *name, bool cfg)

    read initiator name from flash

    :param phba:
        device priv structure
    :type phba: struct beiscsi_hba \*

    :param name:
        buffer pointer
    :type name: char \*

    :param cfg:
        fetch user configured
    :type cfg: bool

.. _`beiscsi_if_set_vlan`:

beiscsi_if_set_vlan
===================

.. c:function:: int beiscsi_if_set_vlan(struct beiscsi_hba *phba, uint16_t vlan_tag)

    Issue and wait for CMD completion

    :param phba:
        device private structure instance
    :type phba: struct beiscsi_hba \*

    :param vlan_tag:
        VLAN tag
    :type vlan_tag: uint16_t

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

    :param phba:
        Device priv structure instance
    :type phba: struct beiscsi_hba \*

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

    :param phba:
        Device priv structure instance
    :type phba: struct beiscsi_hba \*

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

    :param phba:
        device priv structure instance
    :type phba: struct beiscsi_hba \*

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

    :param phba:
        device priv structure instance
    :type phba: struct beiscsi_hba \*

    :param s_handle:
        session handle returned for boot session.
    :type s_handle: unsigned int \*

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

    :param dev:
        ptr to device not used.
    :type dev: struct device \*

    :param attr:
        device attribute, not used.
    :type attr: struct device_attribute \*

    :param buf:
        contains formatted text driver name and version
    :type buf: char \*

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

    :param dev:
        ptr to device not used.
    :type dev: struct device \*

    :param attr:
        device attribute, not used.
    :type attr: struct device_attribute \*

    :param buf:
        contains formatted text Firmware version
    :type buf: char \*

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

    :param dev:
        ptr to device not used.
    :type dev: struct device \*

    :param attr:
        device attribute, not used.
    :type attr: struct device_attribute \*

    :param buf:
        contains formatted text Session Count
    :type buf: char \*

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

    :param dev:
        ptr to device not used.
    :type dev: struct device \*

    :param attr:
        device attribute, not used.
    :type attr: struct device_attribute \*

    :param buf:
        contains formatted text Session Count
    :type buf: char \*

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

    :param dev:
        ptr to device to get priv structure
    :type dev: struct device \*

    :param attr:
        device attribute, not used.
    :type attr: struct device_attribute \*

    :param buf:
        contains formatted text driver name and version
    :type buf: char \*

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

    :param dev:
        ptr to device not used.
    :type dev: struct device \*

    :param attr:
        device attribute, not used.
    :type attr: struct device_attribute \*

    :param buf:
        contains formatted text port identifier
    :type buf: char \*

.. _`beiscsi_phys_port_disp.description`:

Description
-----------

return
size of the formatted string

.. This file was automatic generated / don't edit.

