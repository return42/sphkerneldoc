.. -*- coding: utf-8; mode: rst -*-

===========
intel_i2c.c
===========


.. _`psb_intel_i2c_create`:

psb_intel_i2c_create
====================

.. c:function:: struct psb_intel_i2c_chan *psb_intel_i2c_create (struct drm_device *dev, const u32 reg, const char *name)

    instantiate an Intel i2c bus using the specified GPIO reg

    :param struct drm_device \*dev:
        DRM device

    :param const u32 reg:
        GPIO reg to use

    :param const char \*name:
        name for this bus



.. _`psb_intel_i2c_create.description`:

Description
-----------

Creates and registers a new i2c bus with the Linux i2c layer, for use
in output probing and control (e.g. DDC or SDVO control functions).

Possible values for ``reg`` include::

  ``GPIOA``
  ``GPIOB``
  ``GPIOC``
  ``GPIOD``
  ``GPIOE``
  ``GPIOF``
  ``GPIOG``
  ``GPIOH``

see PRM for details on how these different busses are used.



.. _`psb_intel_i2c_destroy`:

psb_intel_i2c_destroy
=====================

.. c:function:: void psb_intel_i2c_destroy (struct psb_intel_i2c_chan *chan)

    unregister and free i2c bus resources

    :param struct psb_intel_i2c_chan \*chan:

        *undescribed*



.. _`psb_intel_i2c_destroy.description`:

Description
-----------

Unregister the adapter from the i2c layer, then free the structure.

