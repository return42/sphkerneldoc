
.. _API-drm-fb-helper-sys-write:

=======================
drm_fb_helper_sys_write
=======================

*man drm_fb_helper_sys_write(9)*

*4.6.0-rc1*

wrapper around fb_sys_write


Synopsis
========

.. c:function:: ssize_t drm_fb_helper_sys_write( struct fb_info * info, const char __user * buf, size_t count, loff_t * ppos )

Arguments
=========

``info``
    fb_info struct pointer

``buf``
    userspace buffer to write to framebuffer memory

``count``
    number of bytes to write to framebuffer memory

``ppos``
    write offset within framebuffer memory


Description
===========

A wrapper around fb_sys_write implemented by fbdev core
