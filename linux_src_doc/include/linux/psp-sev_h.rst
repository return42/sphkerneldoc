.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/psp-sev.h

.. _`sev_data_init`:

struct sev_data_init
====================

.. c:type:: struct sev_data_init

    INIT command parameters

.. _`sev_data_init.definition`:

Definition
----------

.. code-block:: c

    struct sev_data_init {
        u32 flags;
        u32 reserved;
        u64 tmr_address;
        u32 tmr_len;
    }

.. _`sev_data_init.members`:

Members
-------

flags
    processing flags

reserved
    *undescribed*

tmr_address
    system physical address used for SEV-ES

tmr_len
    len of tmr_address

.. _`sev_data_pek_csr`:

struct sev_data_pek_csr
=======================

.. c:type:: struct sev_data_pek_csr

    PEK_CSR command parameters

.. _`sev_data_pek_csr.definition`:

Definition
----------

.. code-block:: c

    struct sev_data_pek_csr {
        u64 address;
        u32 len;
    }

.. _`sev_data_pek_csr.members`:

Members
-------

address
    PEK certificate chain

len
    len of certificate

.. _`sev_data_pek_cert_import`:

struct sev_data_pek_cert_import
===============================

.. c:type:: struct sev_data_pek_cert_import

    PEK_CERT_IMPORT command parameters

.. _`sev_data_pek_cert_import.definition`:

Definition
----------

.. code-block:: c

    struct sev_data_pek_cert_import {
        u64 pek_cert_address;
        u32 pek_cert_len;
        u32 reserved;
        u64 oca_cert_address;
        u32 oca_cert_len;
    }

.. _`sev_data_pek_cert_import.members`:

Members
-------

pek_cert_address
    *undescribed*

pek_cert_len
    *undescribed*

reserved
    *undescribed*

oca_cert_address
    *undescribed*

oca_cert_len
    *undescribed*

.. _`sev_data_download_firmware`:

struct sev_data_download_firmware
=================================

.. c:type:: struct sev_data_download_firmware

    DOWNLOAD_FIRMWARE command parameters

.. _`sev_data_download_firmware.definition`:

Definition
----------

.. code-block:: c

    struct sev_data_download_firmware {
        u64 address;
        u32 len;
    }

.. _`sev_data_download_firmware.members`:

Members
-------

address
    physical address of firmware image

len
    len of the firmware image

.. _`sev_data_get_id`:

struct sev_data_get_id
======================

.. c:type:: struct sev_data_get_id

    GET_ID command parameters

.. _`sev_data_get_id.definition`:

Definition
----------

.. code-block:: c

    struct sev_data_get_id {
        u64 address;
        u32 len;
    }

.. _`sev_data_get_id.members`:

Members
-------

address
    physical address of region to place unique CPU ID(s)

len
    len of the region

.. _`sev_data_pdh_cert_export`:

struct sev_data_pdh_cert_export
===============================

.. c:type:: struct sev_data_pdh_cert_export

    PDH_CERT_EXPORT command parameters

.. _`sev_data_pdh_cert_export.definition`:

Definition
----------

.. code-block:: c

    struct sev_data_pdh_cert_export {
        u64 pdh_cert_address;
        u32 pdh_cert_len;
        u32 reserved;
        u64 cert_chain_address;
        u32 cert_chain_len;
    }

.. _`sev_data_pdh_cert_export.members`:

Members
-------

pdh_cert_address
    *undescribed*

pdh_cert_len
    *undescribed*

reserved
    *undescribed*

cert_chain_address
    PDH certificate chain

cert_chain_len
    len of PDH certificate chain

.. _`sev_data_decommission`:

struct sev_data_decommission
============================

.. c:type:: struct sev_data_decommission

    DECOMMISSION command parameters

.. _`sev_data_decommission.definition`:

Definition
----------

.. code-block:: c

    struct sev_data_decommission {
        u32 handle;
    }

.. _`sev_data_decommission.members`:

Members
-------

handle
    handle of the VM to decommission

.. _`sev_data_activate`:

struct sev_data_activate
========================

.. c:type:: struct sev_data_activate

    ACTIVATE command parameters

.. _`sev_data_activate.definition`:

Definition
----------

.. code-block:: c

    struct sev_data_activate {
        u32 handle;
        u32 asid;
    }

.. _`sev_data_activate.members`:

Members
-------

handle
    handle of the VM to activate

asid
    asid assigned to the VM

.. _`sev_data_deactivate`:

struct sev_data_deactivate
==========================

.. c:type:: struct sev_data_deactivate

    DEACTIVATE command parameters

.. _`sev_data_deactivate.definition`:

Definition
----------

.. code-block:: c

    struct sev_data_deactivate {
        u32 handle;
    }

.. _`sev_data_deactivate.members`:

Members
-------

handle
    handle of the VM to deactivate

.. _`sev_data_guest_status`:

struct sev_data_guest_status
============================

.. c:type:: struct sev_data_guest_status

    SEV GUEST_STATUS command parameters

.. _`sev_data_guest_status.definition`:

Definition
----------

.. code-block:: c

    struct sev_data_guest_status {
        u32 handle;
        u32 policy;
        u32 asid;
        u8 state;
    }

.. _`sev_data_guest_status.members`:

Members
-------

handle
    handle of the VM to retrieve status

policy
    policy information for the VM

asid
    current ASID of the VM

state
    current state of the VM

.. _`sev_data_launch_start`:

struct sev_data_launch_start
============================

.. c:type:: struct sev_data_launch_start

    LAUNCH_START command parameters

.. _`sev_data_launch_start.definition`:

Definition
----------

.. code-block:: c

    struct sev_data_launch_start {
        u32 handle;
        u32 policy;
        u64 dh_cert_address;
        u32 dh_cert_len;
        u32 reserved;
        u64 session_address;
        u32 session_len;
    }

.. _`sev_data_launch_start.members`:

Members
-------

handle
    handle assigned to the VM

policy
    guest launch policy

dh_cert_address
    physical address of DH certificate blob

dh_cert_len
    len of DH certificate blob

reserved
    *undescribed*

session_address
    physical address of session parameters

session_len
    len of session parameters

.. _`sev_data_launch_update_data`:

struct sev_data_launch_update_data
==================================

.. c:type:: struct sev_data_launch_update_data

    LAUNCH_UPDATE_DATA command parameter

.. _`sev_data_launch_update_data.definition`:

Definition
----------

.. code-block:: c

    struct sev_data_launch_update_data {
        u32 handle;
        u32 reserved;
        u64 address;
        u32 len;
    }

.. _`sev_data_launch_update_data.members`:

Members
-------

handle
    handle of the VM to update

reserved
    *undescribed*

address
    physical address of memory region to encrypt

len
    len of memory to be encrypted

.. _`sev_data_launch_update_vmsa`:

struct sev_data_launch_update_vmsa
==================================

.. c:type:: struct sev_data_launch_update_vmsa

    LAUNCH_UPDATE_VMSA command

.. _`sev_data_launch_update_vmsa.definition`:

Definition
----------

.. code-block:: c

    struct sev_data_launch_update_vmsa {
        u32 handle;
        u32 reserved;
        u64 address;
        u32 len;
    }

.. _`sev_data_launch_update_vmsa.members`:

Members
-------

handle
    handle of the VM

reserved
    *undescribed*

address
    physical address of memory region to encrypt

len
    len of memory region to encrypt

.. _`sev_data_launch_measure`:

struct sev_data_launch_measure
==============================

.. c:type:: struct sev_data_launch_measure

    LAUNCH_MEASURE command parameters

.. _`sev_data_launch_measure.definition`:

Definition
----------

.. code-block:: c

    struct sev_data_launch_measure {
        u32 handle;
        u32 reserved;
        u64 address;
        u32 len;
    }

.. _`sev_data_launch_measure.members`:

Members
-------

handle
    handle of the VM to process

reserved
    *undescribed*

address
    physical address containing the measurement blob

len
    len of measurement blob

.. _`sev_data_launch_secret`:

struct sev_data_launch_secret
=============================

.. c:type:: struct sev_data_launch_secret

    LAUNCH_SECRET command parameters

.. _`sev_data_launch_secret.definition`:

Definition
----------

.. code-block:: c

    struct sev_data_launch_secret {
        u32 handle;
        u32 reserved1;
        u64 hdr_address;
        u32 hdr_len;
        u32 reserved2;
        u64 guest_address;
        u32 guest_len;
        u32 reserved3;
        u64 trans_address;
        u32 trans_len;
    }

.. _`sev_data_launch_secret.members`:

Members
-------

handle
    handle of the VM to process

reserved1
    *undescribed*

hdr_address
    physical address containing the packet header

hdr_len
    len of packet header

reserved2
    *undescribed*

guest_address
    system physical address of guest memory region

guest_len
    len of guest_paddr

reserved3
    *undescribed*

trans_address
    physical address of transport memory buffer

trans_len
    len of transport memory buffer

.. _`sev_data_launch_finish`:

struct sev_data_launch_finish
=============================

.. c:type:: struct sev_data_launch_finish

    LAUNCH_FINISH command parameters

.. _`sev_data_launch_finish.definition`:

Definition
----------

.. code-block:: c

    struct sev_data_launch_finish {
        u32 handle;
    }

.. _`sev_data_launch_finish.members`:

Members
-------

handle
    handle of the VM to process

.. _`sev_data_send_start`:

struct sev_data_send_start
==========================

.. c:type:: struct sev_data_send_start

    SEND_START command parameters

.. _`sev_data_send_start.definition`:

Definition
----------

.. code-block:: c

    struct sev_data_send_start {
        u32 handle;
        u32 policy;
        u64 pdh_cert_address;
        u32 pdh_cert_len;
        u32 reserved1;
        u64 plat_cert_address;
        u32 plat_cert_len;
        u32 reserved2;
        u64 amd_cert_address;
        u32 amd_cert_len;
        u32 reserved3;
        u64 session_address;
        u32 session_len;
    }

.. _`sev_data_send_start.members`:

Members
-------

handle
    handle of the VM to process

policy
    policy information for the VM

pdh_cert_address
    physical address containing PDH certificate

pdh_cert_len
    len of PDH certificate

reserved1
    *undescribed*

plat_cert_address
    *undescribed*

plat_cert_len
    *undescribed*

reserved2
    *undescribed*

amd_cert_address
    *undescribed*

amd_cert_len
    *undescribed*

reserved3
    *undescribed*

session_address
    physical address containing Session data

session_len
    len of session data

.. _`sev_data_send_update_data`:

struct sev_data_send_update_data
================================

.. c:type:: struct sev_data_send_update_data

    SEND_UPDATE_DATA command

.. _`sev_data_send_update_data.definition`:

Definition
----------

.. code-block:: c

    struct sev_data_send_update_data {
        u32 handle;
        u32 reserved1;
        u64 hdr_address;
        u32 hdr_len;
        u32 reserved2;
        u64 guest_address;
        u32 guest_len;
        u32 reserved3;
        u64 trans_address;
        u32 trans_len;
    }

.. _`sev_data_send_update_data.members`:

Members
-------

handle
    handle of the VM to process

reserved1
    *undescribed*

hdr_address
    physical address containing packet header

hdr_len
    len of packet header

reserved2
    *undescribed*

guest_address
    physical address of guest memory region to send

guest_len
    len of guest memory region to send

reserved3
    *undescribed*

trans_address
    physical address of host memory region

trans_len
    len of host memory region

.. _`sev_data_send_update_vmsa`:

struct sev_data_send_update_vmsa
================================

.. c:type:: struct sev_data_send_update_vmsa

    SEND_UPDATE_VMSA command

.. _`sev_data_send_update_vmsa.definition`:

Definition
----------

.. code-block:: c

    struct sev_data_send_update_vmsa {
        u32 handle;
        u64 hdr_address;
        u32 hdr_len;
        u32 reserved2;
        u64 guest_address;
        u32 guest_len;
        u32 reserved3;
        u64 trans_address;
        u32 trans_len;
    }

.. _`sev_data_send_update_vmsa.members`:

Members
-------

handle
    handle of the VM to process

hdr_address
    physical address containing packet header

hdr_len
    len of packet header

reserved2
    *undescribed*

guest_address
    physical address of guest memory region to send

guest_len
    len of guest memory region to send

reserved3
    *undescribed*

trans_address
    physical address of host memory region

trans_len
    len of host memory region

.. _`sev_data_send_finish`:

struct sev_data_send_finish
===========================

.. c:type:: struct sev_data_send_finish

    SEND_FINISH command parameters

.. _`sev_data_send_finish.definition`:

Definition
----------

.. code-block:: c

    struct sev_data_send_finish {
        u32 handle;
    }

.. _`sev_data_send_finish.members`:

Members
-------

handle
    handle of the VM to process

.. _`sev_data_receive_start`:

struct sev_data_receive_start
=============================

.. c:type:: struct sev_data_receive_start

    RECEIVE_START command parameters

.. _`sev_data_receive_start.definition`:

Definition
----------

.. code-block:: c

    struct sev_data_receive_start {
        u32 handle;
        u32 policy;
        u64 pdh_cert_address;
        u32 pdh_cert_len;
        u32 reserved1;
        u64 session_address;
        u32 session_len;
    }

.. _`sev_data_receive_start.members`:

Members
-------

handle
    handle of the VM to perform receive operation

policy
    *undescribed*

pdh_cert_address
    system physical address containing PDH certificate blob

pdh_cert_len
    len of PDH certificate blob

reserved1
    *undescribed*

session_address
    system physical address containing session blob

session_len
    len of session blob

.. _`sev_data_receive_update_data`:

struct sev_data_receive_update_data
===================================

.. c:type:: struct sev_data_receive_update_data

    RECEIVE_UPDATE_DATA command parameters

.. _`sev_data_receive_update_data.definition`:

Definition
----------

.. code-block:: c

    struct sev_data_receive_update_data {
        u32 handle;
        u32 reserved1;
        u64 hdr_address;
        u32 hdr_len;
        u32 reserved2;
        u64 guest_address;
        u32 guest_len;
        u32 reserved3;
        u64 trans_address;
        u32 trans_len;
    }

.. _`sev_data_receive_update_data.members`:

Members
-------

handle
    handle of the VM to update

reserved1
    *undescribed*

hdr_address
    physical address containing packet header blob

hdr_len
    len of packet header

reserved2
    *undescribed*

guest_address
    system physical address of guest memory region

guest_len
    len of guest memory region

reserved3
    *undescribed*

trans_address
    system physical address of transport buffer

trans_len
    len of transport buffer

.. _`sev_data_receive_update_vmsa`:

struct sev_data_receive_update_vmsa
===================================

.. c:type:: struct sev_data_receive_update_vmsa

    RECEIVE_UPDATE_VMSA command parameters

.. _`sev_data_receive_update_vmsa.definition`:

Definition
----------

.. code-block:: c

    struct sev_data_receive_update_vmsa {
        u32 handle;
        u32 reserved1;
        u64 hdr_address;
        u32 hdr_len;
        u32 reserved2;
        u64 guest_address;
        u32 guest_len;
        u32 reserved3;
        u64 trans_address;
        u32 trans_len;
    }

.. _`sev_data_receive_update_vmsa.members`:

Members
-------

handle
    handle of the VM to update

reserved1
    *undescribed*

hdr_address
    physical address containing packet header blob

hdr_len
    len of packet header

reserved2
    *undescribed*

guest_address
    system physical address of guest memory region

guest_len
    len of guest memory region

reserved3
    *undescribed*

trans_address
    system physical address of transport buffer

trans_len
    len of transport buffer

.. _`sev_data_receive_finish`:

struct sev_data_receive_finish
==============================

.. c:type:: struct sev_data_receive_finish

    RECEIVE_FINISH command parameters

.. _`sev_data_receive_finish.definition`:

Definition
----------

.. code-block:: c

    struct sev_data_receive_finish {
        u32 handle;
    }

.. _`sev_data_receive_finish.members`:

Members
-------

handle
    handle of the VM to finish

.. _`sev_data_dbg`:

struct sev_data_dbg
===================

.. c:type:: struct sev_data_dbg

    DBG_ENCRYPT/DBG_DECRYPT command parameters

.. _`sev_data_dbg.definition`:

Definition
----------

.. code-block:: c

    struct sev_data_dbg {
        u32 handle;
        u32 reserved;
        u64 src_addr;
        u64 dst_addr;
        u32 len;
    }

.. _`sev_data_dbg.members`:

Members
-------

handle
    handle of the VM to perform debug operation

reserved
    *undescribed*

src_addr
    source address of data to operate on

dst_addr
    destination address of data to operate on

len
    len of data to operate on

.. _`sev_platform_init`:

sev_platform_init
=================

.. c:function:: int sev_platform_init(int *error)

    perform SEV INIT command

    :param error:
        SEV command return code
    :type error: int \*

.. _`sev_platform_init.return`:

Return
------

0 if the SEV successfully processed the command
-%ENODEV    if the SEV device is not available
-%ENOTSUPP  if the SEV does not support SEV
-%ETIMEDOUT if the SEV command timed out
-%EIO       if the SEV returned a non-zero return code

.. _`sev_platform_status`:

sev_platform_status
===================

.. c:function:: int sev_platform_status(struct sev_user_data_status *status, int *error)

    perform SEV PLATFORM_STATUS command

    :param status:
        sev_user_data_status structure to be processed
    :type status: struct sev_user_data_status \*

    :param error:
        SEV command return code
    :type error: int \*

.. _`sev_platform_status.return`:

Return
------

0 if the SEV successfully processed the command
-%ENODEV    if the SEV device is not available
-%ENOTSUPP  if the SEV does not support SEV
-%ETIMEDOUT if the SEV command timed out
-%EIO       if the SEV returned a non-zero return code

.. _`sev_issue_cmd_external_user`:

sev_issue_cmd_external_user
===========================

.. c:function:: int sev_issue_cmd_external_user(struct file *filep, unsigned int id, void *data, int *error)

    issue SEV command by other driver with a file handle.

    :param filep:
        *undescribed*
    :type filep: struct file \*

    :param id:
        *undescribed*
    :type id: unsigned int

    :param data:
        *undescribed*
    :type data: void \*

    :param error:
        SEV command return code
    :type error: int \*

.. _`sev_issue_cmd_external_user.description`:

Description
-----------

This function can be used by other drivers to issue a SEV command on
behalf of userspace. The caller must pass a valid SEV file descriptor
so that we know that it has access to SEV device.

\ ``filep``\  - SEV device file pointer
\ ``cmd``\  - command to issue
\ ``data``\  - command buffer

.. _`sev_issue_cmd_external_user.return`:

Return
------

0 if the SEV successfully processed the command
-%ENODEV    if the SEV device is not available
-%ENOTSUPP  if the SEV does not support SEV
-%ETIMEDOUT if the SEV command timed out
-%EIO       if the SEV returned a non-zero return code
-%EINVAL    if the SEV file descriptor is not valid

.. _`sev_guest_deactivate`:

sev_guest_deactivate
====================

.. c:function:: int sev_guest_deactivate(struct sev_data_deactivate *data, int *error)

    perform SEV DEACTIVATE command

    :param data:
        *undescribed*
    :type data: struct sev_data_deactivate \*

    :param error:
        *undescribed*
    :type error: int \*

.. _`sev_guest_deactivate.return`:

Return
------

0 if the sev successfully processed the command
-%ENODEV    if the sev device is not available
-%ENOTSUPP  if the sev does not support SEV
-%ETIMEDOUT if the sev command timed out
-%EIO       if the sev returned a non-zero return code

.. _`sev_guest_activate`:

sev_guest_activate
==================

.. c:function:: int sev_guest_activate(struct sev_data_activate *data, int *error)

    perform SEV ACTIVATE command

    :param data:
        *undescribed*
    :type data: struct sev_data_activate \*

    :param error:
        *undescribed*
    :type error: int \*

.. _`sev_guest_activate.return`:

Return
------

0 if the sev successfully processed the command
-%ENODEV    if the sev device is not available
-%ENOTSUPP  if the sev does not support SEV
-%ETIMEDOUT if the sev command timed out
-%EIO       if the sev returned a non-zero return code

.. _`sev_guest_df_flush`:

sev_guest_df_flush
==================

.. c:function:: int sev_guest_df_flush(int *error)

    perform SEV DF_FLUSH command

    :param error:
        *undescribed*
    :type error: int \*

.. _`sev_guest_df_flush.return`:

Return
------

0 if the sev successfully processed the command
-%ENODEV    if the sev device is not available
-%ENOTSUPP  if the sev does not support SEV
-%ETIMEDOUT if the sev command timed out
-%EIO       if the sev returned a non-zero return code

.. _`sev_guest_decommission`:

sev_guest_decommission
======================

.. c:function:: int sev_guest_decommission(struct sev_data_decommission *data, int *error)

    perform SEV DECOMMISSION command

    :param data:
        *undescribed*
    :type data: struct sev_data_decommission \*

    :param error:
        *undescribed*
    :type error: int \*

.. _`sev_guest_decommission.return`:

Return
------

0 if the sev successfully processed the command
-%ENODEV    if the sev device is not available
-%ENOTSUPP  if the sev does not support SEV
-%ETIMEDOUT if the sev command timed out
-%EIO       if the sev returned a non-zero return code

.. This file was automatic generated / don't edit.

