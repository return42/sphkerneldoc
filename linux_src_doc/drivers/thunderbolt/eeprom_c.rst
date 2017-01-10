.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thunderbolt/eeprom.c

.. _`tb_eeprom_ctl_write`:

tb_eeprom_ctl_write
===================

.. c:function:: int tb_eeprom_ctl_write(struct tb_switch *sw, struct tb_eeprom_ctl *ctl)

    write control word

    :param struct tb_switch \*sw:
        *undescribed*

    :param struct tb_eeprom_ctl \*ctl:
        *undescribed*

.. _`tb_eeprom_ctl_read`:

tb_eeprom_ctl_read
==================

.. c:function:: int tb_eeprom_ctl_read(struct tb_switch *sw, struct tb_eeprom_ctl *ctl)

    read control word

    :param struct tb_switch \*sw:
        *undescribed*

    :param struct tb_eeprom_ctl \*ctl:
        *undescribed*

.. _`tb_eeprom_active`:

tb_eeprom_active
================

.. c:function:: int tb_eeprom_active(struct tb_switch *sw, bool enable)

    enable rom access

    :param struct tb_switch \*sw:
        *undescribed*

    :param bool enable:
        *undescribed*

.. _`tb_eeprom_active.warning`:

WARNING
-------

Always disable access after usage. Otherwise the controller will
fail to reprobe.

.. _`tb_eeprom_transfer`:

tb_eeprom_transfer
==================

.. c:function:: int tb_eeprom_transfer(struct tb_switch *sw, struct tb_eeprom_ctl *ctl, enum tb_eeprom_transfer direction)

    transfer one bit

    :param struct tb_switch \*sw:
        *undescribed*

    :param struct tb_eeprom_ctl \*ctl:
        *undescribed*

    :param enum tb_eeprom_transfer direction:
        *undescribed*

.. _`tb_eeprom_transfer.description`:

Description
-----------

If TB_EEPROM_IN is passed, then the bit can be retrieved from ctl->data_in.
If TB_EEPROM_OUT is passed, then ctl->data_out will be written.

.. _`tb_eeprom_out`:

tb_eeprom_out
=============

.. c:function:: int tb_eeprom_out(struct tb_switch *sw, u8 val)

    write one byte to the bus

    :param struct tb_switch \*sw:
        *undescribed*

    :param u8 val:
        *undescribed*

.. _`tb_eeprom_in`:

tb_eeprom_in
============

.. c:function:: int tb_eeprom_in(struct tb_switch *sw, u8 *val)

    read one byte from the bus

    :param struct tb_switch \*sw:
        *undescribed*

    :param u8 \*val:
        *undescribed*

.. _`tb_eeprom_read_n`:

tb_eeprom_read_n
================

.. c:function:: int tb_eeprom_read_n(struct tb_switch *sw, u16 offset, u8 *val, size_t count)

    read count bytes from offset into val

    :param struct tb_switch \*sw:
        *undescribed*

    :param u16 offset:
        *undescribed*

    :param u8 \*val:
        *undescribed*

    :param size_t count:
        *undescribed*

.. _`tb_eeprom_get_drom_offset`:

tb_eeprom_get_drom_offset
=========================

.. c:function:: int tb_eeprom_get_drom_offset(struct tb_switch *sw, u16 *offset)

    get drom offset within eeprom

    :param struct tb_switch \*sw:
        *undescribed*

    :param u16 \*offset:
        *undescribed*

.. _`tb_drom_read_uid_only`:

tb_drom_read_uid_only
=====================

.. c:function:: int tb_drom_read_uid_only(struct tb_switch *sw, u64 *uid)

    read uid directly from drom

    :param struct tb_switch \*sw:
        *undescribed*

    :param u64 \*uid:
        *undescribed*

.. _`tb_drom_read_uid_only.description`:

Description
-----------

Does not use the cached copy in sw->drom. Used during resume to check switch
identity.

.. _`tb_drom_parse_entries`:

tb_drom_parse_entries
=====================

.. c:function:: int tb_drom_parse_entries(struct tb_switch *sw)

    parse the linked list of drom entries

    :param struct tb_switch \*sw:
        *undescribed*

.. _`tb_drom_parse_entries.description`:

Description
-----------

Drom must have been copied to sw->drom.

.. _`tb_drom_copy_efi`:

tb_drom_copy_efi
================

.. c:function:: int tb_drom_copy_efi(struct tb_switch *sw, u16 *size)

    copy drom supplied by EFI to sw->drom if present

    :param struct tb_switch \*sw:
        *undescribed*

    :param u16 \*size:
        *undescribed*

.. _`tb_drom_read`:

tb_drom_read
============

.. c:function:: int tb_drom_read(struct tb_switch *sw)

    copy drom to sw->drom and parse it

    :param struct tb_switch \*sw:
        *undescribed*

.. This file was automatic generated / don't edit.

