.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/apple-gmux.h

.. _`apple_gmux_present`:

apple_gmux_present
==================

.. c:function:: bool apple_gmux_present( void)

    detect if gmux is built into the machine

    :param void:
        no arguments
    :type void: 

.. _`apple_gmux_present.description`:

Description
-----------

Drivers may use this to activate quirks specific to dual GPU MacBook Pros
and Mac Pros, e.g. for deferred probing, runtime pm and backlight.

.. _`apple_gmux_present.return`:

Return
------

\ ``true``\  if gmux is present and the kernel was configured
with CONFIG_APPLE_GMUX, \ ``false``\  otherwise.

.. This file was automatic generated / don't edit.

