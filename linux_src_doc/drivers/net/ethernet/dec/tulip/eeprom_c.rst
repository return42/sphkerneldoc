.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/dec/tulip/eeprom.c

.. _`tulip_build_fake_mediatable`:

tulip_build_fake_mediatable
===========================

.. c:function:: void tulip_build_fake_mediatable(struct tulip_private *tp)

    Build a fake mediatable entry.

    :param tp:
        Ptr to the tulip private data.
    :type tp: struct tulip_private \*

.. _`tulip_build_fake_mediatable.description`:

Description
-----------

Some cards like the 3x5 HSC cards (J3514A) do not have a standard
srom and can not be handled under the fixup routine.  These cards
still need a valid mediatable entry for correct csr12 setup and
mii handling.

Since this is currently a parisc-linux specific function, the
#ifdef \__hppa_\_ should completely optimize this function away for
non-parisc hardware.

.. This file was automatic generated / don't edit.

