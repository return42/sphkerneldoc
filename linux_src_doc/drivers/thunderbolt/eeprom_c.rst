.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thunderbolt/eeprom.c

.. _`tb_eeprom_ctl_write`:

tb_eeprom_ctl_write
===================

.. c:function:: int tb_eeprom_ctl_write(struct tb_switch *sw, struct tb_eeprom_ctl *ctl)

    write control word

    :param sw:
        *undescribed*
    :type sw: struct tb_switch \*

    :param ctl:
        *undescribed*
    :type ctl: struct tb_eeprom_ctl \*

.. _`tb_eeprom_ctl_read`:

tb_eeprom_ctl_read
==================

.. c:function:: int tb_eeprom_ctl_read(struct tb_switch *sw, struct tb_eeprom_ctl *ctl)

    read control word

    :param sw:
        *undescribed*
    :type sw: struct tb_switch \*

    :param ctl:
        *undescribed*
    :type ctl: struct tb_eeprom_ctl \*

.. _`tb_eeprom_active`:

tb_eeprom_active
================

.. c:function:: int tb_eeprom_active(struct tb_switch *sw, bool enable)

    enable rom access

    :param sw:
        *undescribed*
    :type sw: struct tb_switch \*

    :param enable:
        *undescribed*
    :type enable: bool

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

    :param sw:
        *undescribed*
    :type sw: struct tb_switch \*

    :param ctl:
        *undescribed*
    :type ctl: struct tb_eeprom_ctl \*

    :param direction:
        *undescribed*
    :type direction: enum tb_eeprom_transfer

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

    :param sw:
        *undescribed*
    :type sw: struct tb_switch \*

    :param val:
        *undescribed*
    :type val: u8

.. _`tb_eeprom_in`:

tb_eeprom_in
============

.. c:function:: int tb_eeprom_in(struct tb_switch *sw, u8 *val)

    read one byte from the bus

    :param sw:
        *undescribed*
    :type sw: struct tb_switch \*

    :param val:
        *undescribed*
    :type val: u8 \*

.. _`tb_eeprom_read_n`:

tb_eeprom_read_n
================

.. c:function:: int tb_eeprom_read_n(struct tb_switch *sw, u16 offset, u8 *val, size_t count)

    read count bytes from offset into val

    :param sw:
        *undescribed*
    :type sw: struct tb_switch \*

    :param offset:
        *undescribed*
    :type offset: u16

    :param val:
        *undescribed*
    :type val: u8 \*

    :param count:
        *undescribed*
    :type count: size_t

.. _`tb_eeprom_get_drom_offset`:

tb_eeprom_get_drom_offset
=========================

.. c:function:: int tb_eeprom_get_drom_offset(struct tb_switch *sw, u16 *offset)

    get drom offset within eeprom

    :param sw:
        *undescribed*
    :type sw: struct tb_switch \*

    :param offset:
        *undescribed*
    :type offset: u16 \*

.. _`tb_drom_read_uid_only`:

tb_drom_read_uid_only
=====================

.. c:function:: int tb_drom_read_uid_only(struct tb_switch *sw, u64 *uid)

    read uid directly from drom

    :param sw:
        *undescribed*
    :type sw: struct tb_switch \*

    :param uid:
        *undescribed*
    :type uid: u64 \*

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

    :param sw:
        *undescribed*
    :type sw: struct tb_switch \*

.. _`tb_drom_parse_entries.description`:

Description
-----------

Drom must have been copied to sw->drom.

.. _`tb_drom_copy_efi`:

tb_drom_copy_efi
================

.. c:function:: int tb_drom_copy_efi(struct tb_switch *sw, u16 *size)

    copy drom supplied by EFI to sw->drom if present

    :param sw:
        *undescribed*
    :type sw: struct tb_switch \*

    :param size:
        *undescribed*
    :type size: u16 \*

.. _`tb_drom_read`:

tb_drom_read
============

.. c:function:: int tb_drom_read(struct tb_switch *sw)

    copy drom to sw->drom and parse it

    :param sw:
        *undescribed*
    :type sw: struct tb_switch \*

.. This file was automatic generated / don't edit.

