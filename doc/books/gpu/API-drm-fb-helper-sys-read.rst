
.. _API-drm-fb-helper-sys-read:

======================
drm_fb_helper_sys_read
======================

*man drm_fb_helper_sys_read(9)*

*4.6.0-rc1*

wrapper around fb_sys_read


Synopsis
========

.. c:function:: ssize_t drm_fb_helper_sys_read( struct fb_info * info, char __user * buf, size_t count, loff_t * ppos )

Arguments
=========

``info``
    fb_info struct pointer

``buf``
    userspace buffer to read from framebuffer memory

``count``
    number of bytes to read from framebuffer memory

``ppos``
    read offset within framebuffer memory


Description
===========

A wrapper around fb_sys_read implemented by fbdev core
