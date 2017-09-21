.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/rc/rc-main.c

.. _`ir_create_table`:

ir_create_table
===============

.. c:function:: int ir_create_table(struct rc_map *rc_map, const char *name, u64 rc_proto, size_t size)

    initializes a scancode table

    :param struct rc_map \*rc_map:
        the rc_map to initialize

    :param const char \*name:
        name to assign to the table

    :param u64 rc_proto:
        ir type to assign to the new table

    :param size_t size:
        initial size of the table

.. _`ir_create_table.description`:

Description
-----------

This routine will initialize the rc_map and will allocate
memory to hold at least the specified number of elements.

.. _`ir_free_table`:

ir_free_table
=============

.. c:function:: void ir_free_table(struct rc_map *rc_map)

    frees memory allocated by a scancode table

    :param struct rc_map \*rc_map:
        the table whose mappings need to be freed

.. _`ir_free_table.description`:

Description
-----------

This routine will free memory alloctaed for key mappings used by given
scancode table.

.. _`ir_resize_table`:

ir_resize_table
===============

.. c:function:: int ir_resize_table(struct rc_map *rc_map, gfp_t gfp_flags)

    resizes a scancode table if necessary

    :param struct rc_map \*rc_map:
        the rc_map to resize

    :param gfp_t gfp_flags:
        gfp flags to use when allocating memory

.. _`ir_resize_table.description`:

Description
-----------

This routine will shrink the rc_map if it has lots of
unused entries and grow it if it is full.

.. _`ir_update_mapping`:

ir_update_mapping
=================

.. c:function:: unsigned int ir_update_mapping(struct rc_dev *dev, struct rc_map *rc_map, unsigned int index, unsigned int new_keycode)

    set a keycode in the scancode->keycode table

    :param struct rc_dev \*dev:
        the struct rc_dev device descriptor

    :param struct rc_map \*rc_map:
        scancode table to be adjusted

    :param unsigned int index:
        index of the mapping that needs to be updated

    :param unsigned int new_keycode:
        *undescribed*

.. _`ir_update_mapping.description`:

Description
-----------

This routine is used to update scancode->keycode mapping at given
position.

.. _`ir_establish_scancode`:

ir_establish_scancode
=====================

.. c:function:: unsigned int ir_establish_scancode(struct rc_dev *dev, struct rc_map *rc_map, unsigned int scancode, bool resize)

    set a keycode in the scancode->keycode table

    :param struct rc_dev \*dev:
        the struct rc_dev device descriptor

    :param struct rc_map \*rc_map:
        scancode table to be searched

    :param unsigned int scancode:
        the desired scancode

    :param bool resize:
        controls whether we allowed to resize the table to
        accommodate not yet present scancodes

.. _`ir_establish_scancode.description`:

Description
-----------

This routine is used to locate given scancode in rc_map.
If scancode is not yet present the routine will allocate a new slot
for it.

.. _`ir_setkeycode`:

ir_setkeycode
=============

.. c:function:: int ir_setkeycode(struct input_dev *idev, const struct input_keymap_entry *ke, unsigned int *old_keycode)

    set a keycode in the scancode->keycode table

    :param struct input_dev \*idev:
        the struct input_dev device descriptor

    :param const struct input_keymap_entry \*ke:
        *undescribed*

    :param unsigned int \*old_keycode:
        *undescribed*

.. _`ir_setkeycode.description`:

Description
-----------

This routine is used to handle evdev EVIOCSKEY ioctl.

.. _`ir_setkeytable`:

ir_setkeytable
==============

.. c:function:: int ir_setkeytable(struct rc_dev *dev, const struct rc_map *from)

    sets several entries in the scancode->keycode table

    :param struct rc_dev \*dev:
        the struct rc_dev device descriptor

    :param const struct rc_map \*from:
        the struct rc_map to copy entries from

.. _`ir_setkeytable.description`:

Description
-----------

This routine is used to handle table initialization.

.. _`ir_lookup_by_scancode`:

ir_lookup_by_scancode
=====================

.. c:function:: unsigned int ir_lookup_by_scancode(const struct rc_map *rc_map, unsigned int scancode)

    locate mapping by scancode

    :param const struct rc_map \*rc_map:
        the struct rc_map to search

    :param unsigned int scancode:
        scancode to look for in the table

.. _`ir_lookup_by_scancode.description`:

Description
-----------

This routine performs binary search in RC keykeymap table for
given scancode.

.. _`ir_getkeycode`:

ir_getkeycode
=============

.. c:function:: int ir_getkeycode(struct input_dev *idev, struct input_keymap_entry *ke)

    get a keycode from the scancode->keycode table

    :param struct input_dev \*idev:
        the struct input_dev device descriptor

    :param struct input_keymap_entry \*ke:
        *undescribed*

.. _`ir_getkeycode.description`:

Description
-----------

This routine is used to handle evdev EVIOCGKEY ioctl.

.. _`rc_g_keycode_from_table`:

rc_g_keycode_from_table
=======================

.. c:function:: u32 rc_g_keycode_from_table(struct rc_dev *dev, u32 scancode)

    gets the keycode that corresponds to a scancode

    :param struct rc_dev \*dev:
        the struct rc_dev descriptor of the device

    :param u32 scancode:
        the scancode to look for

.. _`rc_g_keycode_from_table.description`:

Description
-----------

This routine is used by drivers which need to convert a scancode to a
keycode. Normally it should not be used since drivers should have no
interest in keycodes.

.. _`ir_do_keyup`:

ir_do_keyup
===========

.. c:function:: void ir_do_keyup(struct rc_dev *dev, bool sync)

    internal function to signal the release of a keypress

    :param struct rc_dev \*dev:
        the struct rc_dev descriptor of the device

    :param bool sync:
        whether or not to call input_sync

.. _`ir_do_keyup.description`:

Description
-----------

This function is used internally to release a keypress, it must be
called with keylock held.

.. _`rc_keyup`:

rc_keyup
========

.. c:function:: void rc_keyup(struct rc_dev *dev)

    signals the release of a keypress

    :param struct rc_dev \*dev:
        the struct rc_dev descriptor of the device

.. _`rc_keyup.description`:

Description
-----------

This routine is used to signal that a key has been released on the
remote control.

.. _`ir_timer_keyup`:

ir_timer_keyup
==============

.. c:function:: void ir_timer_keyup(unsigned long cookie)

    generates a keyup event after a timeout

    :param unsigned long cookie:
        a pointer to the struct rc_dev for the device

.. _`ir_timer_keyup.description`:

Description
-----------

This routine will generate a keyup event some time after a keydown event
is generated when no further activity has been detected.

.. _`rc_repeat`:

rc_repeat
=========

.. c:function:: void rc_repeat(struct rc_dev *dev)

    signals that a key is still pressed

    :param struct rc_dev \*dev:
        the struct rc_dev descriptor of the device

.. _`rc_repeat.description`:

Description
-----------

This routine is used by IR decoders when a repeat message which does
not include the necessary bits to reproduce the scancode has been
received.

.. _`ir_do_keydown`:

ir_do_keydown
=============

.. c:function:: void ir_do_keydown(struct rc_dev *dev, enum rc_proto protocol, u32 scancode, u32 keycode, u8 toggle)

    internal function to process a keypress

    :param struct rc_dev \*dev:
        the struct rc_dev descriptor of the device

    :param enum rc_proto protocol:
        the protocol of the keypress

    :param u32 scancode:
        the scancode of the keypress

    :param u32 keycode:
        the keycode of the keypress

    :param u8 toggle:
        the toggle value of the keypress

.. _`ir_do_keydown.description`:

Description
-----------

This function is used internally to register a keypress, it must be
called with keylock held.

.. _`rc_keydown`:

rc_keydown
==========

.. c:function:: void rc_keydown(struct rc_dev *dev, enum rc_proto protocol, u32 scancode, u8 toggle)

    generates input event for a key press

    :param struct rc_dev \*dev:
        the struct rc_dev descriptor of the device

    :param enum rc_proto protocol:
        the protocol for the keypress

    :param u32 scancode:
        the scancode for the keypress

    :param u8 toggle:
        the toggle value (protocol dependent, if the protocol doesn't
        support toggle values, this should be set to zero)

.. _`rc_keydown.description`:

Description
-----------

This routine is used to signal that a key has been pressed on the
remote control.

.. _`rc_keydown_notimeout`:

rc_keydown_notimeout
====================

.. c:function:: void rc_keydown_notimeout(struct rc_dev *dev, enum rc_proto protocol, u32 scancode, u8 toggle)

    generates input event for a key press without an automatic keyup event at a later time

    :param struct rc_dev \*dev:
        the struct rc_dev descriptor of the device

    :param enum rc_proto protocol:
        the protocol for the keypress

    :param u32 scancode:
        the scancode for the keypress

    :param u8 toggle:
        the toggle value (protocol dependent, if the protocol doesn't
        support toggle values, this should be set to zero)

.. _`rc_keydown_notimeout.description`:

Description
-----------

This routine is used to signal that a key has been pressed on the
remote control. The driver must manually call \ :c:func:`rc_keyup`\  at a later stage.

.. _`rc_validate_filter`:

rc_validate_filter
==================

.. c:function:: int rc_validate_filter(struct rc_dev *dev, struct rc_scancode_filter *filter)

    checks that the scancode and mask are valid and provides sensible defaults

    :param struct rc_dev \*dev:
        the struct rc_dev descriptor of the device

    :param struct rc_scancode_filter \*filter:
        the scancode and mask

.. _`rc_filter_attribute`:

struct rc_filter_attribute
==========================

.. c:type:: struct rc_filter_attribute

    Device attribute relating to a filter type.

.. _`rc_filter_attribute.definition`:

Definition
----------

.. code-block:: c

    struct rc_filter_attribute {
        struct device_attribute attr;
        enum rc_filter_type type;
        bool mask;
    }

.. _`rc_filter_attribute.members`:

Members
-------

attr
    Device attribute.

type
    Filter type.

mask
    false for filter value, true for filter mask.

.. _`show_protocols`:

show_protocols
==============

.. c:function:: ssize_t show_protocols(struct device *device, struct device_attribute *mattr, char *buf)

    shows the current IR protocol(s)

    :param struct device \*device:
        the device descriptor

    :param struct device_attribute \*mattr:
        the device attribute struct

    :param char \*buf:
        a pointer to the output buffer

.. _`show_protocols.description`:

Description
-----------

This routine is a callback routine for input read the IR protocol type(s).
it is trigged by reading /sys/class/rc/rc?/protocols.
It returns the protocol names of supported protocols.
Enabled protocols are printed in brackets.

dev->lock is taken to guard against races between
store_protocols and show_protocols.

.. _`parse_protocol_change`:

parse_protocol_change
=====================

.. c:function:: int parse_protocol_change(u64 *protocols, const char *buf)

    parses a protocol change request

    :param u64 \*protocols:
        pointer to the bitmask of current protocols

    :param const char \*buf:
        pointer to the buffer with a list of changes

.. _`parse_protocol_change.description`:

Description
-----------

Writing "+proto" will add a protocol to the protocol mask.
Writing "-proto" will remove a protocol from protocol mask.
Writing "proto" will enable only "proto".
Writing "none" will disable all protocols.
Returns the number of changes performed or a negative error code.

.. _`store_protocols`:

store_protocols
===============

.. c:function:: ssize_t store_protocols(struct device *device, struct device_attribute *mattr, const char *buf, size_t len)

    changes the current/wakeup IR protocol(s)

    :param struct device \*device:
        the device descriptor

    :param struct device_attribute \*mattr:
        the device attribute struct

    :param const char \*buf:
        a pointer to the input buffer

    :param size_t len:
        length of the input buffer

.. _`store_protocols.description`:

Description
-----------

This routine is for changing the IR protocol type.
It is trigged by writing to /sys/class/rc/rc?/[wakeup_]protocols.
See \ :c:func:`parse_protocol_change`\  for the valid commands.
Returns \ ``len``\  on success or a negative error code.

dev->lock is taken to guard against races between
store_protocols and show_protocols.

.. _`show_filter`:

show_filter
===========

.. c:function:: ssize_t show_filter(struct device *device, struct device_attribute *attr, char *buf)

    shows the current scancode filter value or mask

    :param struct device \*device:
        the device descriptor

    :param struct device_attribute \*attr:
        the device attribute struct

    :param char \*buf:
        a pointer to the output buffer

.. _`show_filter.description`:

Description
-----------

This routine is a callback routine to read a scancode filter value or mask.
It is trigged by reading /sys/class/rc/rc?/[wakeup_]filter[_mask].
It prints the current scancode filter value or mask of the appropriate filter
type in hexadecimal into \ ``buf``\  and returns the size of the buffer.

Bits of the filter value corresponding to set bits in the filter mask are
compared against input scancodes and non-matching scancodes are discarded.

dev->lock is taken to guard against races between
store_filter and show_filter.

.. _`store_filter`:

store_filter
============

.. c:function:: ssize_t store_filter(struct device *device, struct device_attribute *attr, const char *buf, size_t len)

    changes the scancode filter value

    :param struct device \*device:
        the device descriptor

    :param struct device_attribute \*attr:
        the device attribute struct

    :param const char \*buf:
        a pointer to the input buffer

    :param size_t len:
        length of the input buffer

.. _`store_filter.description`:

Description
-----------

This routine is for changing a scancode filter value or mask.
It is trigged by writing to /sys/class/rc/rc?/[wakeup_]filter[_mask].
Returns -EINVAL if an invalid filter value for the current protocol was
specified or if scancode filtering is not supported by the driver, otherwise
returns \ ``len``\ .

Bits of the filter value corresponding to set bits in the filter mask are
compared against input scancodes and non-matching scancodes are discarded.

dev->lock is taken to guard against races between
store_filter and show_filter.

.. _`show_wakeup_protocols`:

show_wakeup_protocols
=====================

.. c:function:: ssize_t show_wakeup_protocols(struct device *device, struct device_attribute *mattr, char *buf)

    shows the wakeup IR protocol

    :param struct device \*device:
        the device descriptor

    :param struct device_attribute \*mattr:
        the device attribute struct

    :param char \*buf:
        a pointer to the output buffer

.. _`show_wakeup_protocols.description`:

Description
-----------

This routine is a callback routine for input read the IR protocol type(s).
it is trigged by reading /sys/class/rc/rc?/wakeup_protocols.
It returns the protocol names of supported protocols.
The enabled protocols are printed in brackets.

dev->lock is taken to guard against races between
store_wakeup_protocols and show_wakeup_protocols.

.. _`store_wakeup_protocols`:

store_wakeup_protocols
======================

.. c:function:: ssize_t store_wakeup_protocols(struct device *device, struct device_attribute *mattr, const char *buf, size_t len)

    changes the wakeup IR protocol(s)

    :param struct device \*device:
        the device descriptor

    :param struct device_attribute \*mattr:
        the device attribute struct

    :param const char \*buf:
        a pointer to the input buffer

    :param size_t len:
        length of the input buffer

.. _`store_wakeup_protocols.description`:

Description
-----------

This routine is for changing the IR protocol type.
It is trigged by writing to /sys/class/rc/rc?/wakeup_protocols.
Returns \ ``len``\  on success or a negative error code.

dev->lock is taken to guard against races between
store_wakeup_protocols and show_wakeup_protocols.

.. This file was automatic generated / don't edit.

