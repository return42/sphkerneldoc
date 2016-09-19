.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/bcma/sprom.c

.. _`bcma_arch_register_fallback_sprom`:

bcma_arch_register_fallback_sprom
=================================

.. c:function:: int bcma_arch_register_fallback_sprom(int (*sprom_callback)(struct bcma_bus *bus, struct ssb_sprom *out))

    Registers a method providing a fallback SPROM if no SPROM is found.

    :param int (\*sprom_callback)(struct bcma_bus \*bus, struct ssb_sprom \*out):
        The callback function.

.. _`bcma_arch_register_fallback_sprom.description`:

Description
-----------

With this function the architecture implementation may register a
callback handler which fills the SPROM data structure. The fallback is
used for PCI based BCMA devices, where no valid SPROM can be found
in the shadow registers and to provide the SPROM for SoCs where BCMA is
to controll the system bus.

This function is useful for weird architectures that have a half-assed
BCMA device hardwired to their PCI bus.

This function is available for architecture code, only. So it is not
exported.

.. This file was automatic generated / don't edit.

