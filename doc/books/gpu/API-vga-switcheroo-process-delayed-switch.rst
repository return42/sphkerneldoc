
.. _API-vga-switcheroo-process-delayed-switch:

=====================================
vga_switcheroo_process_delayed_switch
=====================================

*man vga_switcheroo_process_delayed_switch(9)*

*4.6.0-rc1*

helper for delayed switching


Synopsis
========

.. c:function:: int vga_switcheroo_process_delayed_switch( void )

Arguments
=========

``void``
    no arguments


Manual switching and manual power control
=========================================

Process a delayed switch if one is pending. DRM drivers should call this from their ->lastclose callback.


Return
======

0 on success. -EINVAL if no delayed switch is pending, if the client has unregistered in the meantime or if there are other clients blocking the switch. If the actual switch fails,
an error is reported and 0 is returned.
