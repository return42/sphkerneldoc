.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/drm_encoder_slave.h

.. _`drm_encoder_slave_funcs`:

struct drm_encoder_slave_funcs
==============================

.. c:type:: struct drm_encoder_slave_funcs

    Entry points exposed by a slave encoder driver

.. _`drm_encoder_slave_funcs.definition`:

Definition
----------

.. code-block:: c

    struct drm_encoder_slave_funcs {
        void (* set_config) (struct drm_encoder *encoder,void *params);
        void (* destroy) (struct drm_encoder *encoder);
        void (* dpms) (struct drm_encoder *encoder, int mode);
        void (* save) (struct drm_encoder *encoder);
        void (* restore) (struct drm_encoder *encoder);
        bool (* mode_fixup) (struct drm_encoder *encoder,const struct drm_display_mode *mode,struct drm_display_mode *adjusted_mode);
        int (* mode_valid) (struct drm_encoder *encoder,struct drm_display_mode *mode);
        void (* mode_set) (struct drm_encoder *encoder,struct drm_display_mode *mode,struct drm_display_mode *adjusted_mode);
        enum drm_connector_status (* detect) (struct drm_encoder *encoder,struct drm_connector *connector);
        int (* get_modes) (struct drm_encoder *encoder,struct drm_connector *connector);
        int (* create_resources) (struct drm_encoder *encoder,struct drm_connector *connector);
        int (* set_property) (struct drm_encoder *encoder,struct drm_connector *connector,struct drm_property *property,uint64_t val);
    }

.. _`drm_encoder_slave_funcs.members`:

Members
-------

set_config
    Initialize any encoder-specific modesetting parameters.
    The meaning of the \ ``params``\  parameter is implementation
    dependent. It will usually be a structure with DVO port
    data format settings or timings. It's not required for
    the new parameters to take effect until the next mode
    is set.

destroy
    *undescribed*

dpms
    *undescribed*

save
    *undescribed*

restore
    *undescribed*

mode_fixup
    *undescribed*

mode_valid
    *undescribed*

mode_set
    *undescribed*

detect
    *undescribed*

get_modes
    *undescribed*

create_resources
    *undescribed*

set_property
    *undescribed*

.. _`drm_encoder_slave_funcs.description`:

Description
-----------

Most of its members are analogous to the function pointers in
\ :c:type:`struct drm_encoder_helper_funcs <drm_encoder_helper_funcs>` and they can optionally be used to
initialize the latter. Connector-like methods (e.g. \ ``get_modes``\  and
\ ``set_property``\ ) will typically be wrapped around and only be called
if the encoder is the currently selected one for the connector.

.. _`drm_encoder_slave`:

struct drm_encoder_slave
========================

.. c:type:: struct drm_encoder_slave

    Slave encoder struct

.. _`drm_encoder_slave.definition`:

Definition
----------

.. code-block:: c

    struct drm_encoder_slave {
        struct drm_encoder base;
        const struct drm_encoder_slave_funcs *slave_funcs;
        void *slave_priv;
        void *bus_priv;
    }

.. _`drm_encoder_slave.members`:

Members
-------

base
    DRM encoder object.

slave_funcs
    Slave encoder callbacks.

slave_priv
    Slave encoder private data.

bus_priv
    Bus specific data.

.. _`drm_encoder_slave.description`:

Description
-----------

A \ :c:type:`struct drm_encoder_slave <drm_encoder_slave>` has two sets of callbacks, \ ``slave_funcs``\  and the
ones in \ ``base``\ . The former are never actually called by the common
CRTC code, it's just a convenience for splitting the encoder
functions in an upper, GPU-specific layer and a (hopefully)
GPU-agnostic lower layer: It's the GPU driver responsibility to
call the slave methods when appropriate.

\ :c:func:`drm_i2c_encoder_init`\  provides a way to get an implementation of
this.

.. _`drm_i2c_encoder_driver`:

struct drm_i2c_encoder_driver
=============================

.. c:type:: struct drm_i2c_encoder_driver


.. _`drm_i2c_encoder_driver.definition`:

Definition
----------

.. code-block:: c

    struct drm_i2c_encoder_driver {
        struct i2c_driver i2c_driver;
        int (* encoder_init) (struct i2c_client *client,struct drm_device *dev,struct drm_encoder_slave *encoder);
    }

.. _`drm_i2c_encoder_driver.members`:

Members
-------

i2c_driver
    *undescribed*

encoder_init
    *undescribed*

.. _`drm_i2c_encoder_driver.description`:

Description
-----------

Describes a device driver for an encoder connected to the GPU
through an I2C bus. In addition to the entry points in \ ``i2c_driver``\ 
an \ ``encoder_init``\  function should be provided. It will be called to
give the driver an opportunity to allocate any per-encoder data
structures and to initialize the \ ``slave_funcs``\  and (optionally)
\ ``slave_priv``\  members of \ ``encoder``\ .

.. _`drm_i2c_encoder_get_client`:

drm_i2c_encoder_get_client
==========================

.. c:function:: struct i2c_client *drm_i2c_encoder_get_client(struct drm_encoder *encoder)

    Get the I2C client corresponding to an encoder

    :param struct drm_encoder \*encoder:
        *undescribed*

.. _`drm_i2c_encoder_register`:

drm_i2c_encoder_register
========================

.. c:function:: int drm_i2c_encoder_register(struct module *owner, struct drm_i2c_encoder_driver *driver)

    Register an I2C encoder driver

    :param struct module \*owner:
        Module containing the driver.

    :param struct drm_i2c_encoder_driver \*driver:
        Driver to be registered.

.. _`drm_i2c_encoder_unregister`:

drm_i2c_encoder_unregister
==========================

.. c:function:: void drm_i2c_encoder_unregister(struct drm_i2c_encoder_driver *driver)

    Unregister an I2C encoder driver

    :param struct drm_i2c_encoder_driver \*driver:
        Driver to be unregistered.

.. This file was automatic generated / don't edit.

