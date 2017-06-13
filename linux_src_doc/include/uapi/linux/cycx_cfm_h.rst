.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/linux/cycx_cfm.h

.. _`cycx_fw_info`:

struct cycx_fw_info
===================

.. c:type:: struct cycx_fw_info

    firmware module information. \ ``codeid``\  - firmware ID \ ``version``\  - firmware version number \ ``adapter``\  - compatible adapter types \ ``memsize``\  - minimum memory size \ ``reserved``\  - reserved \ ``startoffs``\  - entry point offset \ ``winoffs``\  - dual-port memory window offset \ ``codeoffs``\  - code load offset \ ``codesize``\  - code size \ ``dataoffs``\  - configuration data load offset \ ``datasize``\  - configuration data size

.. _`cycx_fw_info.definition`:

Definition
----------

.. code-block:: c

    struct cycx_fw_info {
        unsigned short codeid;
        unsigned short version;
        unsigned short adapter;
        unsigned long memsize;
        unsigned short reserved;
        unsigned short startoffs;
        unsigned short winoffs;
        unsigned short codeoffs;
        unsigned long codesize;
        unsigned short dataoffs;
        unsigned long datasize;
    }

.. _`cycx_fw_info.members`:

Members
-------

codeid
    *undescribed*

version
    *undescribed*

adapter
    *undescribed*

memsize
    *undescribed*

reserved
    *undescribed*

startoffs
    *undescribed*

winoffs
    *undescribed*

codeoffs
    *undescribed*

codesize
    *undescribed*

dataoffs
    *undescribed*

datasize
    *undescribed*

.. _`cycx_firmware`:

struct cycx_firmware
====================

.. c:type:: struct cycx_firmware

    CYCX firmware file structure \ ``signature``\  - CFM file signature \ ``version``\  - file format version \ ``checksum``\  - info + image \ ``reserved``\  - reserved \ ``descr``\  - description string \ ``info``\  - firmware module info \ ``image``\  - code image (variable size)

.. _`cycx_firmware.definition`:

Definition
----------

.. code-block:: c

    struct cycx_firmware {
        char signature;
        unsigned short version;
        unsigned short checksum;
        unsigned short reserved;
        char descr;
        struct cycx_fw_info info;
        unsigned char image;
    }

.. _`cycx_firmware.members`:

Members
-------

signature
    *undescribed*

version
    *undescribed*

checksum
    *undescribed*

reserved
    *undescribed*

descr
    *undescribed*

info
    *undescribed*

image
    *undescribed*

.. This file was automatic generated / don't edit.

