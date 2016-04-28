.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-drm-bridge:

=================
struct drm_bridge
=================

*man struct drm_bridge(9)*

*4.6.0-rc5*

central DRM bridge control structure


Synopsis
========

.. code-block:: c

    struct drm_bridge {
      struct drm_device * dev;
      struct drm_encoder * encoder;
      struct drm_bridge * next;
    #ifdef CONFIG_OF
      struct device_node * of_node;
    #endif
      struct list_head list;
      const struct drm_bridge_funcs * funcs;
      void * driver_private;
    };


Members
=======

dev
    DRM device this bridge belongs to

encoder
    encoder to which this bridge is connected

next
    the next bridge in the encoder chain

of_node
    device node pointer to the bridge

list
    to keep track of all added bridges

funcs
    control functions

driver_private
    pointer to the bridge driver's internal context


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
