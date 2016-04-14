.. -*- coding: utf-8; mode: rst -*-

=====
nfc.h
=====

.. _`nfc_commands`:

enum nfc_commands
=================

.. c:type:: enum nfc_commands

    supported nfc commands



Constants
---------

:``NFC_CMD_UNSPEC``:
    unspecified command

:``NFC_CMD_GET_DEVICE``:
    request information about a device (requires
    ``NFC_ATTR_DEVICE_INDEX``\ ) or dump request to get a list of all nfc devices

:``NFC_CMD_DEV_UP``:
    turn on the nfc device
    (requires ``NFC_ATTR_DEVICE_INDEX``\ )

:``NFC_CMD_DEV_DOWN``:
    turn off the nfc device
    (requires ``NFC_ATTR_DEVICE_INDEX``\ )

:``NFC_CMD_DEP_LINK_UP``:
    -- undescribed --

:``NFC_CMD_DEP_LINK_DOWN``:
    -- undescribed --

:``NFC_CMD_START_POLL``:
    start polling for targets using the given protocols
    (requires ``NFC_ATTR_DEVICE_INDEX`` and ``NFC_ATTR_PROTOCOLS``\ )

:``NFC_CMD_STOP_POLL``:
    stop polling for targets (requires
    ``NFC_ATTR_DEVICE_INDEX``\ )

:``NFC_CMD_GET_TARGET``:
    dump all targets found by the previous poll (requires
    ``NFC_ATTR_DEVICE_INDEX``\ )

:``NFC_EVENT_TARGETS_FOUND``:
    event emitted when a new target is found
    (it sends ``NFC_ATTR_DEVICE_INDEX``\ )

:``NFC_EVENT_DEVICE_ADDED``:
    event emitted when a new device is registred
    (it sends ``NFC_ATTR_DEVICE_NAME``\ , ``NFC_ATTR_DEVICE_INDEX`` and
    ``NFC_ATTR_PROTOCOLS``\ )

:``NFC_EVENT_DEVICE_REMOVED``:
    event emitted when a device is removed
    (it sends ``NFC_ATTR_DEVICE_INDEX``\ )

:``NFC_EVENT_TARGET_LOST``:
    -- undescribed --

:``NFC_EVENT_TM_ACTIVATED``:
    event emitted when the adapter is activated in
    target mode.

:``NFC_EVENT_TM_DEACTIVATED``:
    -- undescribed --

:``NFC_CMD_LLC_GET_PARAMS``:
    request LTO, RW, and MIUX parameters for a device

:``NFC_CMD_LLC_SET_PARAMS``:
    set one or more of LTO, RW, and MIUX parameters for
    a device. LTO must be set before the link is up otherwise -EINPROGRESS
    is returned. RW and MIUX can be set at anytime and will be passed in
    subsequent CONNECT and CC messages.
    If one of the passed parameters is wrong none is set and -EINVAL is
    returned.

:``NFC_CMD_ENABLE_SE``:
    Enable the physical link to a specific secure element.::

            Once enabled a secure element will handle card emulation mode, i.e.
            starting a poll from a device which has a secure element enabled means
            we want to do SE based card emulation.

:``NFC_CMD_DISABLE_SE``:
    Disable the physical link to a specific secure element.

:``NFC_CMD_LLC_SDREQ``:
    -- undescribed --

:``NFC_EVENT_LLC_SDRES``:
    -- undescribed --

:``NFC_CMD_FW_DOWNLOAD``:
    Request to Load/flash firmware, or event to inform
    that some firmware was loaded

:``NFC_EVENT_SE_ADDED``:
    Event emitted when a new secure element is discovered.::

            This typically will be sent whenever a new NFC controller with either
            an embedded SE or an UICC one connected to it through SWP.

:``NFC_EVENT_SE_REMOVED``:
    Event emitted when a secure element is removed from
    the system, as a consequence of e.g. an NFC controller being unplugged.

:``NFC_EVENT_SE_CONNECTIVITY``:
    This event is emitted whenever a secure element
    is requesting connectivity access. For example a UICC SE may need to
    talk with a sleeping modem and will notify this need by sending this
    event. It is then up to userspace to decide if it will wake the modem
    up or not.

:``NFC_EVENT_SE_TRANSACTION``:
    This event is sent when an application running on
    a specific SE notifies us about the end of a transaction. The parameter
    for this event is the application ID (AID).

:``NFC_CMD_GET_SE``:
    Dump all discovered secure elements from an NFC controller.

:``NFC_CMD_SE_IO``:
    Send/Receive APDUs to/from the selected secure element.

:``NFC_CMD_ACTIVATE_TARGET``:
    Request NFC controller to reactivate target.

:``NFC_CMD_VENDOR``:
    Vendor specific command, to be implemented directly
    from the driver in order to support hardware specific operations.

:``__NFC_CMD_AFTER_LAST``:
    -- undescribed --


.. _`nfc_attrs`:

enum nfc_attrs
==============

.. c:type:: enum nfc_attrs

    supported nfc attributes



Constants
---------

:``NFC_ATTR_UNSPEC``:
    unspecified attribute

:``NFC_ATTR_DEVICE_INDEX``:
    index of nfc device

:``NFC_ATTR_DEVICE_NAME``:
    device name, max 8 chars

:``NFC_ATTR_PROTOCOLS``:
    nfc protocols - bitwise or-ed combination from
    NFC_PROTO_\\*_MASK constants

:``NFC_ATTR_TARGET_INDEX``:
    index of the nfc target

:``NFC_ATTR_TARGET_SENS_RES``:
    NFC-A targets extra information such as NFCID

:``NFC_ATTR_TARGET_SEL_RES``:
    NFC-A targets extra information (useful if the
    target is not NFC-Forum compliant)

:``NFC_ATTR_TARGET_NFCID1``:
    NFC-A targets identifier, max 10 bytes

:``NFC_ATTR_TARGET_SENSB_RES``:
    NFC-B targets extra information, max 12 bytes

:``NFC_ATTR_TARGET_SENSF_RES``:
    NFC-F targets extra information, max 18 bytes

:``NFC_ATTR_COMM_MODE``:
    Passive or active mode

:``NFC_ATTR_RF_MODE``:
    Initiator or target

:``NFC_ATTR_DEVICE_POWERED``:
    -- undescribed --

:``NFC_ATTR_IM_PROTOCOLS``:
    Initiator mode protocols to poll for

:``NFC_ATTR_TM_PROTOCOLS``:
    Target mode protocols to listen for

:``NFC_ATTR_LLC_PARAM_LTO``:
    Link TimeOut parameter

:``NFC_ATTR_LLC_PARAM_RW``:
    Receive Window size parameter

:``NFC_ATTR_LLC_PARAM_MIUX``:
    MIU eXtension parameter

:``NFC_ATTR_SE``:
    Available Secure Elements

:``NFC_ATTR_LLC_SDP``:
    -- undescribed --

:``NFC_ATTR_FIRMWARE_NAME``:
    Free format firmware version

:``NFC_ATTR_SE_INDEX``:
    Secure element index

:``NFC_ATTR_SE_TYPE``:
    Secure element type (UICC or EMBEDDED)

:``NFC_ATTR_SE_AID``:
    -- undescribed --

:``NFC_ATTR_FIRMWARE_DOWNLOAD_STATUS``:
    Firmware download operation status

:``NFC_ATTR_SE_APDU``:
    -- undescribed --

:``NFC_ATTR_TARGET_ISO15693_DSFID``:
    ISO 15693 Data Storage Format Identifier

:``NFC_ATTR_TARGET_ISO15693_UID``:
    ISO 15693 Unique Identifier

:``NFC_ATTR_SE_PARAMS``:
    Parameters data from an evt_transaction

:``NFC_ATTR_VENDOR_ID``:
    NFC manufacturer unique ID, typically an OUI

:``NFC_ATTR_VENDOR_SUBCMD``:
    Vendor specific sub command

:``NFC_ATTR_VENDOR_DATA``:
    Vendor specific data, to be optionally passed
    to a vendor specific command implementation

:``__NFC_ATTR_AFTER_LAST``:
    -- undescribed --


.. _`nfc_raw_header_size`:

NFC_RAW_HEADER_SIZE
===================

.. c:function:: NFC_RAW_HEADER_SIZE ()

    header info for raw socket packets First byte is the adapter index Second byte contains flags - 0x01 - Direction (0=RX, 1=TX) - 0x02-0x04 - Payload type (000=LLCP, 001=NCI, 010=HCI, 011=Digital, 100=Proprietary) - 0x05-0x80 - Reserved

