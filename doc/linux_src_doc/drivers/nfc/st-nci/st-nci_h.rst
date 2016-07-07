.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/nfc/st-nci/st-nci.h

.. _`nfc_vendor_cmds`:

enum nfc_vendor_cmds
====================

.. c:type:: enum nfc_vendor_cmds

    supported nfc vendor commands

.. _`nfc_vendor_cmds.definition`:

Definition
----------

.. code-block:: c

    enum nfc_vendor_cmds {
        FACTORY_MODE,
        HCI_CLEAR_ALL_PIPES,
        HCI_DM_PUT_DATA,
        HCI_DM_UPDATE_AID,
        HCI_DM_GET_INFO,
        HCI_DM_GET_DATA,
        HCI_DM_DIRECT_LOAD,
        HCI_DM_RESET,
        HCI_GET_PARAM,
        HCI_DM_FIELD_GENERATOR,
        LOOPBACK,
        HCI_DM_FWUPD_START,
        HCI_DM_FWUPD_END,
        HCI_DM_VDC_MEASUREMENT_VALUE,
        HCI_DM_VDC_VALUE_COMPARISON,
        MANUFACTURER_SPECIFIC
    };

.. _`nfc_vendor_cmds.constants`:

Constants
---------

FACTORY_MODE
    Allow to set the driver into a mode where no secure element
    are activated. It does not consider any NFC_ATTR_VENDOR_DATA.

HCI_CLEAR_ALL_PIPES
    Allow to execute a HCI clear all pipes command.
    It does not consider any NFC_ATTR_VENDOR_DATA.

HCI_DM_PUT_DATA
    Allow to configure specific CLF registry as for example
    RF trimmings or low level drivers configurations (I2C, SPI, SWP).

HCI_DM_UPDATE_AID
    Allow to configure an AID routing into the CLF routing
    table following RF technology, CLF mode or protocol.

HCI_DM_GET_INFO
    Allow to retrieve CLF information.

HCI_DM_GET_DATA
    Allow to retrieve CLF configurable data such as low
    level drivers configurations or RF trimmings.

HCI_DM_DIRECT_LOAD
    Allow to load a firmware into the CLF. A complete
    packet can be more than 8KB.

HCI_DM_RESET
    Allow to run a CLF reset in order to "commit" CLF
    configuration changes without CLF power off.

HCI_GET_PARAM
    Allow to retrieve an HCI CLF parameter (for example the
    white list).

HCI_DM_FIELD_GENERATOR
    Allow to generate different kind of RF
    technology. When using this command to anti-collision is done.

LOOPBACK
    Allow to echo a command and test the Dh to CLF connectivity.

HCI_DM_FWUPD_START
    Allow to put CLF into firmware update mode. It is a
    specific CLF command as there is no GPIO for this.

HCI_DM_FWUPD_END
    Allow to complete firmware update.

HCI_DM_VDC_MEASUREMENT_VALUE
    Allow to measure the field applied on the
    CLF antenna. A value between 0 and 0x0f is returned. 0 is maximum.

HCI_DM_VDC_VALUE_COMPARISON
    Allow to compare the field applied on the
    CLF antenna to a reference value.

MANUFACTURER_SPECIFIC
    Allow to retrieve manufacturer specific data
    received during a NCI_CORE_INIT_CMD.

.. This file was automatic generated / don't edit.

