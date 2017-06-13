.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/rtl8723bs/os_dep/ioctl_linux.c

.. _`hwaddr_aton_i`:

hwaddr_aton_i
=============

.. c:function:: int hwaddr_aton_i(const char *txt, u8 *addr)

    Convert ASCII string to MAC address

    :param const char \*txt:
        MAC address as a string (e.g., "00:11:22:33:44:55")

    :param u8 \*addr:
        Buffer for the MAC address (ETH_ALEN = 6 bytes)

.. _`hwaddr_aton_i.return`:

Return
------

0 on success, -1 on failure (e.g., string not a MAC address)

.. This file was automatic generated / don't edit.

