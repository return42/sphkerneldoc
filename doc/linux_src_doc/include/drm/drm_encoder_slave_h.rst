.. -*- coding: utf-8; mode: rst -*-

===================
drm_encoder_slave.h
===================


.. _`drm_encoder_slave_funcs`:

struct drm_encoder_slave_funcs
==============================

.. c:type:: drm_encoder_slave_funcs

    Entry points exposed by a slave encoder driver


.. _`drm_encoder_slave_funcs.definition`:

Definition
----------

.. code-block:: c

  struct drm_encoder_slave_funcs {
    void (* set_config) (struct drm_encoder *encoder,void *params);
  };


.. _`drm_encoder_slave_funcs.members`:

Members
-------

:``set_config``:
    Initialize any encoder-specific modesetting parameters.
    The meaning of the ``params`` parameter is implementation
    dependent. It will usually be a structure with DVO port
    data format settings or timings. It's not required for
    the new parameters to take effect until the next mode
    is set.




.. _`drm_encoder_slave_funcs.description`:

Description
-----------

Most of its members are analogous to the function pointers in
:c:type:`struct drm_encoder_helper_funcs <drm_encoder_helper_funcs>` and they can optionally be used to
initialize the latter. Connector-like methods (e.g. ``get_modes`` and
``set_property``\ ) will typically be wrapped around and only be called
if the encoder is the currently selected one for the connector.



.. _`drm_encoder_slave`:

struct drm_encoder_slave
========================

.. c:type:: drm_encoder_slave

    Slave encoder struct


.. _`drm_encoder_slave.definition`:

Definition
----------

.. code-block:: c

  struct drm_encoder_slave {
    struct drm_encoder base;
    const struct drm_encoder_slave_funcs * slave_funcs;
    void * slave_priv;
    void * bus_priv;
  };


.. _`drm_encoder_slave.members`:

Members
-------

:``base``:
    DRM encoder object.

:``slave_funcs``:
    Slave encoder callbacks.

:``slave_priv``:
    Slave encoder private data.

:``bus_priv``:
    Bus specific data.




.. _`drm_encoder_slave.description`:

Description
-----------

A :c:type:`struct drm_encoder_slave <drm_encoder_slave>` has two sets of callbacks, ``slave_funcs`` and the
ones in ``base``\ . The former are never actually called by the common
CRTC code, it's just a convenience for splitting the encoder
functions in an upper, GPU-specific layer and a (hopefully)
GPU-agnostic lower layer: It's the GPU driver responsibility to
call the slave methods when appropriate.

:c:func:`drm_i2c_encoder_init` provides a way to get an implementation of
this.



.. _`drm_i2c_encoder_driver`:

struct drm_i2c_encoder_driver
=============================

.. c:type:: drm_i2c_encoder_driver

    


.. _`drm_i2c_encoder_driver.definition`:

Definition
----------

.. code-block:: c

  struct drm_i2c_encoder_driver {
  };


.. _`drm_i2c_encoder_driver.members`:

Members
-------




.. _`drm_i2c_encoder_driver.description`:

Description
-----------


Describes a device driver for an encoder connected to the GPU
through an I2C bus. In addition to the entry points in ``i2c_driver``
an ``encoder_init`` function should be provided. It will be called to
give the driver an opportunity to allocate any per-encoder data
structures and to initialize the ``slave_funcs`` and (optionally)
``slave_priv`` members of ``encoder``\ .



.. _`drm_i2c_encoder_get_client`:

drm_i2c_encoder_get_client
==========================

.. c:function:: struct i2c_client *drm_i2c_encoder_get_client (struct drm_encoder *encoder)

    Get the I2C client corresponding to an encoder

    :param struct drm_encoder \*encoder:

        *undescribed*



.. _`drm_i2c_encoder_register`:

drm_i2c_encoder_register
========================

.. c:function:: int drm_i2c_encoder_register (struct module *owner, struct drm_i2c_encoder_driver *driver)

    Register an I2C encoder driver

    :param struct module \*owner:
        Module containing the driver.

    :param struct drm_i2c_encoder_driver \*driver:
        Driver to be registered.



.. _`drm_i2c_encoder_unregister`:

drm_i2c_encoder_unregister
==========================

.. c:function:: void drm_i2c_encoder_unregister (struct drm_i2c_encoder_driver *driver)

    Unregister an I2C encoder driver

    :param struct drm_i2c_encoder_driver \*driver:
        Driver to be unregistered.

