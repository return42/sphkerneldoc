.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/include/asm/iosf_mbi.h

.. _`iosf_mbi_read`:

iosf_mbi_read
=============

.. c:function:: int iosf_mbi_read(u8 port, u8 opcode, u32 offset, u32 *mdr)

    MailBox Interface read command

    :param u8 port:
        port indicating subunit being accessed

    :param u8 opcode:
        port specific read or write opcode

    :param u32 offset:
        register address offset

    :param u32 \*mdr:
        register data to be read

.. _`iosf_mbi_read.description`:

Description
-----------

Locking is handled by spinlock - cannot sleep.

.. _`iosf_mbi_read.return`:

Return
------

Nonzero on error

.. _`iosf_mbi_write`:

iosf_mbi_write
==============

.. c:function:: int iosf_mbi_write(u8 port, u8 opcode, u32 offset, u32 mdr)

    MailBox unmasked write command

    :param u8 port:
        port indicating subunit being accessed

    :param u8 opcode:
        port specific read or write opcode

    :param u32 offset:
        register address offset

    :param u32 mdr:
        register data to be written

.. _`iosf_mbi_write.description`:

Description
-----------

Locking is handled by spinlock - cannot sleep.

.. _`iosf_mbi_write.return`:

Return
------

Nonzero on error

.. _`iosf_mbi_modify`:

iosf_mbi_modify
===============

.. c:function:: int iosf_mbi_modify(u8 port, u8 opcode, u32 offset, u32 mdr, u32 mask)

    MailBox masked write command

    :param u8 port:
        port indicating subunit being accessed

    :param u8 opcode:
        port specific read or write opcode

    :param u32 offset:
        register address offset

    :param u32 mdr:
        register data being modified

    :param u32 mask:
        mask indicating bits in mdr to be modified

.. _`iosf_mbi_modify.description`:

Description
-----------

Locking is handled by spinlock - cannot sleep.

.. _`iosf_mbi_modify.return`:

Return
------

Nonzero on error

.. This file was automatic generated / don't edit.

