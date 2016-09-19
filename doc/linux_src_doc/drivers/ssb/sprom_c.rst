.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ssb/sprom.c

.. _`ssb_arch_register_fallback_sprom`:

ssb_arch_register_fallback_sprom
================================

.. c:function:: int ssb_arch_register_fallback_sprom(int (*sprom_callback)(struct ssb_bus *bus, struct ssb_sprom *out))

    Registers a method providing a fallback SPROM if no SPROM is found.

    :param int (\*sprom_callback)(struct ssb_bus \*bus, struct ssb_sprom \*out):
        The callback function.

.. _`ssb_arch_register_fallback_sprom.description`:

Description
-----------

With this function the architecture implementation may register a
callback handler which fills the SPROM data structure. The fallback is
only used for PCI based SSB devices, where no valid SPROM can be found
in the shadow registers.

This function is useful for weird architectures that have a half-assed
SSB device hardwired to their PCI bus.

Note that it does only work with PCI attached SSB devices. PCMCIA
devices currently don't use this fallback.
Architectures must provide the SPROM for native SSB devices anyway, so
the fallback also isn't used for native devices.

This function is available for architecture code, only. So it is not
exported.

.. This file was automatic generated / don't edit.

