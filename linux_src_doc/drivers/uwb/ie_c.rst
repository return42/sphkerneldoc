.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/uwb/ie.c

.. _`uwb_ie_next`:

uwb_ie_next
===========

.. c:function:: struct uwb_ie_hdr *uwb_ie_next(void **ptr, size_t *len)

    get the next IE in a buffer

    :param ptr:
        start of the buffer containing the IE data
    :type ptr: void \*\*

    :param len:
        length of the buffer
    :type len: size_t \*

.. _`uwb_ie_next.description`:

Description
-----------

Both \ ``ptr``\  and \ ``len``\  are updated so subsequent calls to \ :c:func:`uwb_ie_next`\ 
will get the next IE.

NULL is returned (and \ ``ptr``\  and \ ``len``\  will not be updated) if there
are no more IEs in the buffer or the buffer is too short.

.. _`uwb_ie_dump_hex`:

uwb_ie_dump_hex
===============

.. c:function:: int uwb_ie_dump_hex(const struct uwb_ie_hdr *ies, size_t len, char *buf, size_t size)

    print IEs to a character buffer

    :param ies:
        the IEs to print.
    :type ies: const struct uwb_ie_hdr \*

    :param len:
        length of all the IEs.
    :type len: size_t

    :param buf:
        the destination buffer.
    :type buf: char \*

    :param size:
        size of \ ``buf``\ .
    :type size: size_t

.. _`uwb_ie_dump_hex.description`:

Description
-----------

Returns the number of characters written.

.. _`uwb_rc_get_ie`:

uwb_rc_get_ie
=============

.. c:function:: ssize_t uwb_rc_get_ie(struct uwb_rc *uwb_rc, struct uwb_rc_evt_get_ie **pget_ie)

    :param uwb_rc:
        UWB Radio Controller
    :type uwb_rc: struct uwb_rc \*

    :param pget_ie:
        *undescribed*
    :type pget_ie: struct uwb_rc_evt_get_ie \*\*

.. _`uwb_rc_get_ie.description`:

Description
-----------

We don't need to lock the uwb_rc's mutex because we don't modify
anything. Once done with the iedata buffer, call
uwb_rc_ie_release(iedata). Don't call kfree on it.

.. _`uwb_rc_set_ie`:

uwb_rc_set_ie
=============

.. c:function:: int uwb_rc_set_ie(struct uwb_rc *rc, struct uwb_rc_cmd_set_ie *cmd)

    :param rc:
        *undescribed*
    :type rc: struct uwb_rc \*

    :param cmd:
        pointer to the SET-IE command with the IEs to set
    :type cmd: struct uwb_rc_cmd_set_ie \*

.. _`uwb_rc_ie_setup`:

uwb_rc_ie_setup
===============

.. c:function:: int uwb_rc_ie_setup(struct uwb_rc *uwb_rc)

    setup a radio controller's IE manager

    :param uwb_rc:
        the radio controller.
    :type uwb_rc: struct uwb_rc \*

.. _`uwb_rc_ie_setup.description`:

Description
-----------

The current set of IEs are obtained from the hardware with a GET-IE
command (since the radio controller is not yet beaconing this will
be just the hardware's MAC and PHY Capability IEs).

Returns 0 on success; -ve on an error.

.. _`uwb_rc_ie_add`:

uwb_rc_ie_add
=============

.. c:function:: int uwb_rc_ie_add(struct uwb_rc *uwb_rc, const struct uwb_ie_hdr *ies, size_t size)

    add new IEs to the radio controller's beacon

    :param uwb_rc:
        the radio controller.
    :type uwb_rc: struct uwb_rc \*

    :param ies:
        the buffer containing the new IE or IEs to be added to
        the device's beacon.
    :type ies: const struct uwb_ie_hdr \*

    :param size:
        length of all the IEs.
    :type size: size_t

.. _`uwb_rc_ie_add.description`:

Description
-----------

According to WHCI 0.95 [4.13.6] the driver will only receive the RCEB
after the device sent the first beacon that includes the IEs specified
in the SET IE command. We thus cannot send this command if the device is
not beaconing. Instead, a SET IE command will be sent later right after
we start beaconing.

Setting an IE on the device will overwrite all current IEs in device. So
we take the current IEs being transmitted by the device, insert the
new one, and call SET IE with all the IEs needed.

Returns 0 on success; or -ENOMEM.

.. _`uwb_rc_ie_rm`:

uwb_rc_ie_rm
============

.. c:function:: int uwb_rc_ie_rm(struct uwb_rc *uwb_rc, enum uwb_ie element_id)

    remove an IE from the radio controller's beacon

    :param uwb_rc:
        the radio controller.
    :type uwb_rc: struct uwb_rc \*

    :param element_id:
        the element ID of the IE to remove.
    :type element_id: enum uwb_ie

.. _`uwb_rc_ie_rm.description`:

Description
-----------

Only IEs previously added with \ :c:func:`uwb_rc_ie_add`\  may be removed.

Returns 0 on success; or -ve the SET-IE command to the radio
controller failed.

.. This file was automatic generated / don't edit.

