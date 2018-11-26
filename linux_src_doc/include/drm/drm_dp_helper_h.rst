.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/drm_dp_helper.h

.. _`drm_dp_aux_msg`:

struct drm_dp_aux_msg
=====================

.. c:type:: struct drm_dp_aux_msg

    DisplayPort AUX channel transaction

.. _`drm_dp_aux_msg.definition`:

Definition
----------

.. code-block:: c

    struct drm_dp_aux_msg {
        unsigned int address;
        u8 request;
        u8 reply;
        void *buffer;
        size_t size;
    }

.. _`drm_dp_aux_msg.members`:

Members
-------

address
    address of the (first) register to access

request
    contains the type of transaction (see DP_AUX_* macros)

reply
    upon completion, contains the reply type of the transaction

buffer
    pointer to a transmission or reception buffer

size
    size of \ ``buffer``\ 

.. _`drm_dp_aux_cec`:

struct drm_dp_aux_cec
=====================

.. c:type:: struct drm_dp_aux_cec

    DisplayPort CEC-Tunneling-over-AUX

.. _`drm_dp_aux_cec.definition`:

Definition
----------

.. code-block:: c

    struct drm_dp_aux_cec {
        struct mutex lock;
        struct cec_adapter *adap;
        const char *name;
        struct device *parent;
        struct delayed_work unregister_work;
    }

.. _`drm_dp_aux_cec.members`:

Members
-------

lock
    mutex protecting this struct

adap
    the CEC adapter for CEC-Tunneling-over-AUX support.

name
    name of the CEC adapter

parent
    parent device of the CEC adapter

unregister_work
    unregister the CEC adapter

.. _`drm_dp_aux`:

struct drm_dp_aux
=================

.. c:type:: struct drm_dp_aux

    DisplayPort AUX channel

.. _`drm_dp_aux.definition`:

Definition
----------

.. code-block:: c

    struct drm_dp_aux {
        const char *name;
        struct i2c_adapter ddc;
        struct device *dev;
        struct drm_crtc *crtc;
        struct mutex hw_mutex;
        struct work_struct crc_work;
        u8 crc_count;
        ssize_t (*transfer)(struct drm_dp_aux *aux, struct drm_dp_aux_msg *msg);
        unsigned i2c_nack_count;
        unsigned i2c_defer_count;
        struct drm_dp_aux_cec cec;
    }

.. _`drm_dp_aux.members`:

Members
-------

name
    user-visible name of this AUX channel and the I2C-over-AUX adapter

ddc
    I2C adapter that can be used for I2C-over-AUX communication

dev
    pointer to struct device that is the parent for this AUX channel

crtc
    backpointer to the crtc that is currently using this AUX channel

hw_mutex
    internal mutex used for locking transfers

crc_work
    worker that captures CRCs for each frame

crc_count
    counter of captured frame CRCs

transfer
    transfers a message representing a single AUX transaction

i2c_nack_count
    Counts I2C NACKs, used for DP validation.

i2c_defer_count
    Counts I2C DEFERs, used for DP validation.

cec
    struct containing fields used for CEC-Tunneling-over-AUX.

.. _`drm_dp_aux.description`:

Description
-----------

The .dev field should be set to a pointer to the device that implements
the AUX channel.

The .name field may be used to specify the name of the I2C adapter. If set to
NULL, \ :c:func:`dev_name`\  of .dev will be used.

Drivers provide a hardware-specific implementation of how transactions
are executed via the .transfer() function. A pointer to a drm_dp_aux_msg
structure describing the transaction is passed into this function. Upon
success, the implementation should return the number of payload bytes
that were transferred, or a negative error-code on failure. Helpers
propagate errors from the .transfer() function, with the exception of
the -EBUSY error, which causes a transaction to be retried. On a short,
helpers will return -EPROTO to make it simpler to check for failure.

An AUX channel can also be used to transport I2C messages to a sink. A
typical application of that is to access an EDID that's present in the
sink device. The .transfer() function can also be used to execute such
transactions. The \ :c:func:`drm_dp_aux_register`\  function registers an I2C
adapter that can be passed to \ :c:func:`drm_probe_ddc`\ . Upon removal, drivers
should call \ :c:func:`drm_dp_aux_unregister`\  to remove the I2C adapter.
The I2C adapter uses long transfers by default; if a partial response is
received, the adapter will drop down to the size given by the partial
response for this transaction only.

Note that the aux helper code assumes that the .transfer() function
only modifies the reply field of the drm_dp_aux_msg structure.  The
retry logic and i2c helpers assume this is the case.

.. _`drm_dp_dpcd_readb`:

drm_dp_dpcd_readb
=================

.. c:function:: ssize_t drm_dp_dpcd_readb(struct drm_dp_aux *aux, unsigned int offset, u8 *valuep)

    read a single byte from the DPCD

    :param aux:
        DisplayPort AUX channel
    :type aux: struct drm_dp_aux \*

    :param offset:
        address of the register to read
    :type offset: unsigned int

    :param valuep:
        location where the value of the register will be stored
    :type valuep: u8 \*

.. _`drm_dp_dpcd_readb.description`:

Description
-----------

Returns the number of bytes transferred (1) on success, or a negative
error code on failure.

.. _`drm_dp_dpcd_writeb`:

drm_dp_dpcd_writeb
==================

.. c:function:: ssize_t drm_dp_dpcd_writeb(struct drm_dp_aux *aux, unsigned int offset, u8 value)

    write a single byte to the DPCD

    :param aux:
        DisplayPort AUX channel
    :type aux: struct drm_dp_aux \*

    :param offset:
        address of the register to write
    :type offset: unsigned int

    :param value:
        value to write to the register
    :type value: u8

.. _`drm_dp_dpcd_writeb.description`:

Description
-----------

Returns the number of bytes transferred (1) on success, or a negative
error code on failure.

.. _`drm_dp_desc`:

struct drm_dp_desc
==================

.. c:type:: struct drm_dp_desc

    DP branch/sink device descriptor

.. _`drm_dp_desc.definition`:

Definition
----------

.. code-block:: c

    struct drm_dp_desc {
        struct drm_dp_dpcd_ident ident;
        u32 quirks;
    }

.. _`drm_dp_desc.members`:

Members
-------

ident
    DP device identification from DPCD 0x400 (sink) or 0x500 (branch).

quirks
    Quirks; use \ :c:func:`drm_dp_has_quirk`\  to query for the quirks.

.. _`drm_dp_quirk`:

enum drm_dp_quirk
=================

.. c:type:: enum drm_dp_quirk

    Display Port sink/branch device specific quirks

.. _`drm_dp_quirk.definition`:

Definition
----------

.. code-block:: c

    enum drm_dp_quirk {
        DP_DPCD_QUIRK_CONSTANT_N
    };

.. _`drm_dp_quirk.constants`:

Constants
---------

DP_DPCD_QUIRK_CONSTANT_N

    The device requires main link attributes Mvid and Nvid to be limited
    to 16 bits. So will give a constant value (0x8000) for compatability.

.. _`drm_dp_quirk.description`:

Description
-----------

Display Port sink and branch devices in the wild have a variety of bugs, try
to collect them here. The quirks are shared, but it's up to the drivers to
implement workarounds for them.

.. _`drm_dp_has_quirk`:

drm_dp_has_quirk
================

.. c:function:: bool drm_dp_has_quirk(const struct drm_dp_desc *desc, enum drm_dp_quirk quirk)

    does the DP device have a specific quirk

    :param desc:
        Device decriptor filled by \ :c:func:`drm_dp_read_desc`\ 
    :type desc: const struct drm_dp_desc \*

    :param quirk:
        Quirk to query for
    :type quirk: enum drm_dp_quirk

.. _`drm_dp_has_quirk.description`:

Description
-----------

Return true if DP device identified by \ ``desc``\  has \ ``quirk``\ .

.. This file was automatic generated / don't edit.

