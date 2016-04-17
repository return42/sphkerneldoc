.. -*- coding: utf-8; mode: rst -*-

===============
drm_dp_helper.h
===============


.. _`drm_dp_aux_msg`:

struct drm_dp_aux_msg
=====================

.. c:type:: drm_dp_aux_msg

    DisplayPort AUX channel transaction


.. _`drm_dp_aux_msg.definition`:

Definition
----------

.. code-block:: c

  struct drm_dp_aux_msg {
    unsigned int address;
    u8 request;
    u8 reply;
    void * buffer;
    size_t size;
  };


.. _`drm_dp_aux_msg.members`:

Members
-------

:``address``:
    address of the (first) register to access

:``request``:
    contains the type of transaction (see DP_AUX\_\* macros)

:``reply``:
    upon completion, contains the reply type of the transaction

:``buffer``:
    pointer to a transmission or reception buffer

:``size``:
    size of ``buffer``




.. _`drm_dp_aux`:

struct drm_dp_aux
=================

.. c:type:: drm_dp_aux

    DisplayPort AUX channel


.. _`drm_dp_aux.definition`:

Definition
----------

.. code-block:: c

  struct drm_dp_aux {
    const char * name;
    struct i2c_adapter ddc;
    struct device * dev;
    struct mutex hw_mutex;
    ssize_t (* transfer) (struct drm_dp_aux *aux,struct drm_dp_aux_msg *msg);
  };


.. _`drm_dp_aux.members`:

Members
-------

:``name``:
    user-visible name of this AUX channel and the I2C-over-AUX adapter

:``ddc``:
    I2C adapter that can be used for I2C-over-AUX communication

:``dev``:
    pointer to struct device that is the parent for this AUX channel

:``hw_mutex``:
    internal mutex used for locking transfers

:``transfer``:
    transfers a message representing a single AUX transaction




.. _`drm_dp_aux.description`:

Description
-----------

The .dev field should be set to a pointer to the device that implements
the AUX channel.

The .name field may be used to specify the name of the I2C adapter. If set to
NULL, :c:func:`dev_name` of .dev will be used.

Drivers provide a hardware-specific implementation of how transactions
are executed via the .:c:func:`transfer` function. A pointer to a drm_dp_aux_msg
structure describing the transaction is passed into this function. Upon
success, the implementation should return the number of payload bytes
that were transferred, or a negative error-code on failure. Helpers
propagate errors from the .:c:func:`transfer` function, with the exception of
the -EBUSY error, which causes a transaction to be retried. On a short,
helpers will return -EPROTO to make it simpler to check for failure.

An AUX channel can also be used to transport I2C messages to a sink. A
typical application of that is to access an EDID that's present in the
sink device. The .:c:func:`transfer` function can also be used to execute such
transactions. The :c:func:`drm_dp_aux_register` function registers an I2C
adapter that can be passed to :c:func:`drm_probe_ddc`. Upon removal, drivers
should call :c:func:`drm_dp_aux_unregister` to remove the I2C adapter.
The I2C adapter uses long transfers by default; if a partial response is
received, the adapter will drop down to the size given by the partial
response for this transaction only.

Note that the aux helper code assumes that the .:c:func:`transfer` function
only modifies the reply field of the drm_dp_aux_msg structure.  The
retry logic and i2c helpers assume this is the case.



.. _`drm_dp_dpcd_readb`:

drm_dp_dpcd_readb
=================

.. c:function:: ssize_t drm_dp_dpcd_readb (struct drm_dp_aux *aux, unsigned int offset, u8 *valuep)

    read a single byte from the DPCD

    :param struct drm_dp_aux \*aux:
        DisplayPort AUX channel

    :param unsigned int offset:
        address of the register to read

    :param u8 \*valuep:
        location where the value of the register will be stored



.. _`drm_dp_dpcd_readb.description`:

Description
-----------

Returns the number of bytes transferred (1) on success, or a negative
error code on failure.



.. _`drm_dp_dpcd_writeb`:

drm_dp_dpcd_writeb
==================

.. c:function:: ssize_t drm_dp_dpcd_writeb (struct drm_dp_aux *aux, unsigned int offset, u8 value)

    write a single byte to the DPCD

    :param struct drm_dp_aux \*aux:
        DisplayPort AUX channel

    :param unsigned int offset:
        address of the register to write

    :param u8 value:
        value to write to the register



.. _`drm_dp_dpcd_writeb.description`:

Description
-----------

Returns the number of bytes transferred (1) on success, or a negative
error code on failure.

