.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/nfc/st21nfca/st21nfca.h

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
        HCI_DM_LOAD,
        HCI_DM_RESET,
        HCI_GET_PARAM,
        HCI_DM_FIELD_GENERATOR,
        HCI_LOOPBACK
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

HCI_DM_LOAD
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

HCI_LOOPBACK
    Allow to echo a command and test the Dh to CLF
    connectivity.

.. This file was automatic generated / don't edit.

