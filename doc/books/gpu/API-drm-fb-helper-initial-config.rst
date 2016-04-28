.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-fb-helper-initial-config:

============================
drm_fb_helper_initial_config
============================

*man drm_fb_helper_initial_config(9)*

*4.6.0-rc5*

setup a sane initial connector configuration


Synopsis
========

.. c:function:: int drm_fb_helper_initial_config( struct drm_fb_helper * fb_helper, int bpp_sel )

Arguments
=========

``fb_helper``
    fb_helper device struct

``bpp_sel``
    bpp value to use for the framebuffer configuration


Description
===========

Scans the CRTCs and connectors and tries to put together an initial
setup. At the moment, this is a cloned configuration across all heads
with a new framebuffer object as the backing store.

Note that this also registers the fbdev and so allows userspace to call
into the driver through the fbdev interfaces.

This function will call down into the ->fb_probe callback to let the
driver allocate and initialize the fbdev info structure and the drm
framebuffer used to back the fbdev. ``drm_fb_helper_fill_var`` and
``drm_fb_helper_fill_fix`` are provided as helpers to setup simple
default values for the fbdev info structure.


HANG DEBUGGING
==============

When you have fbcon support built-in or already loaded, this function
will do a full modeset to setup the fbdev console. Due to locking
misdesign in the VT/fbdev subsystem that entire modeset sequence has to
be done while holding console_lock. Until console_unlock is called no
dmesg lines will be sent out to consoles, not even serial console. This
means when your driver crashes, you will see absolutely nothing else but
a system stuck in this function, with no further output. Any kind of
``printk`` you place within your own driver or in the drm core modeset
code will also never show up.

Standard debug practice is to run the fbcon setup without taking the
console_lock as a hack, to be able to see backtraces and crashes on the
serial line. This can be done by setting the fb.lockless_register_fb=1
kernel cmdline option.

The other option is to just disable fbdev emulation since very likely
the first modest from userspace will crash in the same way, and is even
easier to debug. This can be done by setting the
drm_kms_helper.fbdev_emulation=0 kernel cmdline option.


RETURNS
=======

Zero if everything went ok, nonzero otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
