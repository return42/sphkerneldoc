.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/mtd/onfi.h

.. _`onfi_params`:

struct onfi_params
==================

.. c:type:: struct onfi_params

    ONFI specific parameters that will be reused

.. _`onfi_params.definition`:

Definition
----------

.. code-block:: c

    struct onfi_params {
        int version;
        u16 tPROG;
        u16 tBERS;
        u16 tR;
        u16 tCCS;
        u16 async_timing_mode;
        u16 vendor_revision;
        u8 vendor[88];
    }

.. _`onfi_params.members`:

Members
-------

version
    ONFI version (BCD encoded), 0 if ONFI is not supported

tPROG
    Page program time

tBERS
    Block erase time

tR
    Page read time

tCCS
    Change column setup time

async_timing_mode
    Supported asynchronous timing mode

vendor_revision
    Vendor specific revision number

vendor
    Vendor specific data

.. This file was automatic generated / don't edit.

