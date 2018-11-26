.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/iwl-drv.c

.. _`iwl_drv`:

struct iwl_drv
==============

.. c:type:: struct iwl_drv

    drv common data

.. _`iwl_drv.definition`:

Definition
----------

.. code-block:: c

    struct iwl_drv {
        struct list_head list;
        struct iwl_fw fw;
        struct iwl_op_mode *op_mode;
        struct iwl_trans *trans;
        struct device *dev;
        int fw_index;
        char firmware_name[64];
        struct completion request_firmware_complete;
    #ifdef CONFIG_IWLWIFI_DEBUGFS
        struct dentry *dbgfs_drv;
        struct dentry *dbgfs_trans;
        struct dentry *dbgfs_op_mode;
    #endif
    }

.. _`iwl_drv.members`:

Members
-------

list
    list of drv structures using this opmode

fw
    the iwl_fw structure

op_mode
    the running op_mode

trans
    transport layer

dev
    for debug prints only

fw_index
    firmware revision to try loading

firmware_name
    composite filename of ucode file to load

request_firmware_complete
    the firmware has been obtained from user space

dbgfs_drv
    *undescribed*

dbgfs_trans
    *undescribed*

dbgfs_op_mode
    *undescribed*

.. _`iwl_tlv_calib_data`:

struct iwl_tlv_calib_data
=========================

.. c:type:: struct iwl_tlv_calib_data

    parse the default calib data from TLV

.. _`iwl_tlv_calib_data.definition`:

Definition
----------

.. code-block:: c

    struct iwl_tlv_calib_data {
        __le32 ucode_type;
        struct iwl_tlv_calib_ctrl calib;
    }

.. _`iwl_tlv_calib_data.members`:

Members
-------

ucode_type
    the uCode to which the following default calib relates.

calib
    default calibrations.

.. _`iwl_req_fw_callback`:

iwl_req_fw_callback
===================

.. c:function:: void iwl_req_fw_callback(const struct firmware *ucode_raw, void *context)

    callback when firmware was loaded

    :param ucode_raw:
        *undescribed*
    :type ucode_raw: const struct firmware \*

    :param context:
        *undescribed*
    :type context: void \*

.. _`iwl_req_fw_callback.description`:

Description
-----------

If loaded successfully, copies the firmware into buffers
for the card to fetch (via DMA).

.. This file was automatic generated / don't edit.

