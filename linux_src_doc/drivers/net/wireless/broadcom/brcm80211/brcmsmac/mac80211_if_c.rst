.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/broadcom/brcm80211/brcmsmac/mac80211_if.c

.. _`brcms_free`:

brcms_free
==========

.. c:function:: void brcms_free(struct brcms_info *wl)

    device resources.

    :param struct brcms_info \*wl:
        *undescribed*

.. _`brcms_free.description`:

Description
-----------

This function frees resources owned by the WL device pointed to
by the wl parameter.

.. _`brcms_free.precondition`:

precondition
------------

can both be called locked and unlocked

.. _`brcms_attach`:

brcms_attach
============

.. c:function:: struct brcms_info *brcms_attach(struct bcma_device *pdev)

    :param struct bcma_device \*pdev:
        *undescribed*

.. _`brcms_attach.description`:

Description
-----------

Attach to the WL device identified by vendor and device parameters.
regs is a host accessible memory address pointing to WL device registers.

is called in \ :c:func:`brcms_bcma_probe`\  context, therefore no locking required.

.. _`brcms_bcma_probe`:

brcms_bcma_probe
================

.. c:function:: int brcms_bcma_probe(struct bcma_device *pdev)

    :param struct bcma_device \*pdev:
        *undescribed*

.. _`brcms_bcma_probe.description`:

Description
-----------

This function determines if a device pointed to by pdev is a WL device,
and if so, performs a \ :c:func:`brcms_attach`\  on it.

Perimeter lock is initialized in the course of this function.

.. _`brcms_driver_init`:

brcms_driver_init
=================

.. c:function:: void brcms_driver_init(struct work_struct *work)

    :param struct work_struct \*work:
        *undescribed*

.. _`brcms_driver_init.description`:

Description
-----------

This function is scheduled upon module initialization and
does the driver registration, which result in \ :c:func:`brcms_bcma_probe`\ 
call resulting in the driver bringup.

.. _`brcms_module_exit`:

brcms_module_exit
=================

.. c:function:: void __exit brcms_module_exit( void)

    :param  void:
        no arguments

.. _`brcms_module_exit.description`:

Description
-----------

This function unconditionally unloads the brcmsmac driver module from the
system.

.. This file was automatic generated / don't edit.

