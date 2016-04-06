
.. _API-struct-drm-dp-aux:

=================
struct drm_dp_aux
=================

*man struct drm_dp_aux(9)*

*4.6.0-rc1*

DisplayPort AUX channel


Synopsis
========

.. code-block:: c

    struct drm_dp_aux {
      const char * name;
      struct i2c_adapter ddc;
      struct device * dev;
      struct mutex hw_mutex;
      ssize_t (* transfer) (struct drm_dp_aux *aux,struct drm_dp_aux_msg *msg);
    };


Members
=======

name
    user-visible name of this AUX channel and the I2C-over-AUX adapter

ddc
    I2C adapter that can be used for I2C-over-AUX communication

dev
    pointer to struct device that is the parent for this AUX channel

hw_mutex
    internal mutex used for locking transfers

transfer
    transfers a message representing a single AUX transaction


Description
===========

The .dev field should be set to a pointer to the device that implements the AUX channel.

The .name field may be used to specify the name of the I2C adapter. If set to NULL, ``dev_name`` of .dev will be used.

Drivers provide a hardware-specific implementation of how transactions are executed via the . ``transfer`` function. A pointer to a drm_dp_aux_msg structure describing the
transaction is passed into this function. Upon success, the implementation should return the number of payload bytes that were transferred, or a negative error-code on failure.
Helpers propagate errors from the .\ ``transfer`` function, with the exception of the -EBUSY error, which causes a transaction to be retried. On a short, helpers will return
-EPROTO to make it simpler to check for failure.

An AUX channel can also be used to transport I2C messages to a sink. A typical application of that is to access an EDID that's present in the sink device. The .\ ``transfer``
function can also be used to execute such transactions. The ``drm_dp_aux_register`` function registers an I2C adapter that can be passed to ``drm_probe_ddc``. Upon removal, drivers
should call ``drm_dp_aux_unregister`` to remove the I2C adapter. The I2C adapter uses long transfers by default; if a partial response is received, the adapter will drop down to
the size given by the partial response for this transaction only.

Note that the aux helper code assumes that the . ``transfer`` function only modifies the reply field of the drm_dp_aux_msg structure. The retry logic and i2c helpers assume
this is the case.
