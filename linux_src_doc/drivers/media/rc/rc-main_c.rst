.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/rc/rc-main.c

.. _`ir_create_table`:

ir_create_table
===============

.. c:function:: int ir_create_table(struct rc_dev *dev, struct rc_map *rc_map, const char *name, u64 rc_proto, size_t size)

    initializes a scancode table

    :param dev:
        the rc_dev device
    :type dev: struct rc_dev \*

    :param rc_map:
        the rc_map to initialize
    :type rc_map: struct rc_map \*

    :param name:
        name to assign to the table
    :type name: const char \*

    :param rc_proto:
        ir type to assign to the new table
    :type rc_proto: u64

    :param size:
        initial size of the table
    :type size: size_t

.. _`ir_create_table.description`:

Description
-----------

This routine will initialize the rc_map and will allocate
memory to hold at least the specified number of elements.

.. _`ir_create_table.return`:

Return
------

zero on success or a negative error code

.. _`ir_free_table`:

ir_free_table
=============

.. c:function:: void ir_free_table(struct rc_map *rc_map)

    frees memory allocated by a scancode table

    :param rc_map:
        the table whose mappings need to be freed
    :type rc_map: struct rc_map \*

.. _`ir_free_table.description`:

Description
-----------

This routine will free memory alloctaed for key mappings used by given
scancode table.

.. _`ir_resize_table`:

ir_resize_table
===============

.. c:function:: int ir_resize_table(struct rc_dev *dev, struct rc_map *rc_map, gfp_t gfp_flags)

    resizes a scancode table if necessary

    :param dev:
        the rc_dev device
    :type dev: struct rc_dev \*

    :param rc_map:
        the rc_map to resize
    :type rc_map: struct rc_map \*

    :param gfp_flags:
        gfp flags to use when allocating memory
    :type gfp_flags: gfp_t

.. _`ir_resize_table.description`:

Description
-----------

This routine will shrink the rc_map if it has lots of
unused entries and grow it if it is full.

.. _`ir_resize_table.return`:

Return
------

zero on success or a negative error code

.. _`ir_update_mapping`:

ir_update_mapping
=================

.. c:function:: unsigned int ir_update_mapping(struct rc_dev *dev, struct rc_map *rc_map, unsigned int index, unsigned int new_keycode)

    set a keycode in the scancode->keycode table

    :param dev:
        the struct rc_dev device descriptor
    :type dev: struct rc_dev \*

    :param rc_map:
        scancode table to be adjusted
    :type rc_map: struct rc_map \*

    :param index:
        index of the mapping that needs to be updated
    :type index: unsigned int

    :param new_keycode:
        the desired keycode
    :type new_keycode: unsigned int

.. _`ir_update_mapping.description`:

Description
-----------

This routine is used to update scancode->keycode mapping at given
position.

.. _`ir_update_mapping.return`:

Return
------

previous keycode assigned to the mapping

.. _`ir_establish_scancode`:

ir_establish_scancode
=====================

.. c:function:: unsigned int ir_establish_scancode(struct rc_dev *dev, struct rc_map *rc_map, unsigned int scancode, bool resize)

    set a keycode in the scancode->keycode table

    :param dev:
        the struct rc_dev device descriptor
    :type dev: struct rc_dev \*

    :param rc_map:
        scancode table to be searched
    :type rc_map: struct rc_map \*

    :param scancode:
        the desired scancode
    :type scancode: unsigned int

    :param resize:
        controls whether we allowed to resize the table to
        accommodate not yet present scancodes
    :type resize: bool

.. _`ir_establish_scancode.description`:

Description
-----------

This routine is used to locate given scancode in rc_map.
If scancode is not yet present the routine will allocate a new slot
for it.

.. _`ir_establish_scancode.return`:

Return
------

index of the mapping containing scancode in question
or -1U in case of failure.

.. _`ir_setkeycode`:

ir_setkeycode
=============

.. c:function:: int ir_setkeycode(struct input_dev *idev, const struct input_keymap_entry *ke, unsigned int *old_keycode)

    set a keycode in the scancode->keycode table

    :param idev:
        the struct input_dev device descriptor
    :type idev: struct input_dev \*

    :param ke:
        Input keymap entry
    :type ke: const struct input_keymap_entry \*

    :param old_keycode:
        result
    :type old_keycode: unsigned int \*

.. _`ir_setkeycode.description`:

Description
-----------

This routine is used to handle evdev EVIOCSKEY ioctl.

.. _`ir_setkeycode.return`:

Return
------

-EINVAL if the keycode could not be inserted, otherwise zero.

.. _`ir_setkeytable`:

ir_setkeytable
==============

.. c:function:: int ir_setkeytable(struct rc_dev *dev, const struct rc_map *from)

    sets several entries in the scancode->keycode table

    :param dev:
        the struct rc_dev device descriptor
    :type dev: struct rc_dev \*

    :param from:
        the struct rc_map to copy entries from
    :type from: const struct rc_map \*

.. _`ir_setkeytable.description`:

Description
-----------

This routine is used to handle table initialization.

.. _`ir_setkeytable.return`:

Return
------

-ENOMEM if all keycodes could not be inserted, otherwise zero.

.. _`ir_lookup_by_scancode`:

ir_lookup_by_scancode
=====================

.. c:function:: unsigned int ir_lookup_by_scancode(const struct rc_map *rc_map, unsigned int scancode)

    locate mapping by scancode

    :param rc_map:
        the struct rc_map to search
    :type rc_map: const struct rc_map \*

    :param scancode:
        scancode to look for in the table
    :type scancode: unsigned int

.. _`ir_lookup_by_scancode.description`:

Description
-----------

This routine performs binary search in RC keykeymap table for
given scancode.

.. _`ir_lookup_by_scancode.return`:

Return
------

index in the table, -1U if not found

.. _`ir_getkeycode`:

ir_getkeycode
=============

.. c:function:: int ir_getkeycode(struct input_dev *idev, struct input_keymap_entry *ke)

    get a keycode from the scancode->keycode table

    :param idev:
        the struct input_dev device descriptor
    :type idev: struct input_dev \*

    :param ke:
        Input keymap entry
    :type ke: struct input_keymap_entry \*

.. _`ir_getkeycode.description`:

Description
-----------

This routine is used to handle evdev EVIOCGKEY ioctl.

.. _`ir_getkeycode.return`:

Return
------

always returns zero.

.. _`rc_g_keycode_from_table`:

rc_g_keycode_from_table
=======================

.. c:function:: u32 rc_g_keycode_from_table(struct rc_dev *dev, u32 scancode)

    gets the keycode that corresponds to a scancode

    :param dev:
        the struct rc_dev descriptor of the device
    :type dev: struct rc_dev \*

    :param scancode:
        the scancode to look for
    :type scancode: u32

.. _`rc_g_keycode_from_table.description`:

Description
-----------

This routine is used by drivers which need to convert a scancode to a
keycode. Normally it should not be used since drivers should have no
interest in keycodes.

.. _`rc_g_keycode_from_table.return`:

Return
------

the corresponding keycode, or KEY_RESERVED

.. _`ir_do_keyup`:

ir_do_keyup
===========

.. c:function:: void ir_do_keyup(struct rc_dev *dev, bool sync)

    internal function to signal the release of a keypress

    :param dev:
        the struct rc_dev descriptor of the device
    :type dev: struct rc_dev \*

    :param sync:
        whether or not to call input_sync
    :type sync: bool

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

    :param dev:
        the struct rc_dev descriptor of the device
    :type dev: struct rc_dev \*

.. _`rc_keyup.description`:

Description
-----------

This routine is used to signal that a key has been released on the
remote control.

.. _`ir_timer_keyup`:

ir_timer_keyup
==============

.. c:function:: void ir_timer_keyup(struct timer_list *t)

    generates a keyup event after a timeout

    :param t:
        a pointer to the struct timer_list
    :type t: struct timer_list \*

.. _`ir_timer_keyup.description`:

Description
-----------

This routine will generate a keyup event some time after a keydown event
is generated when no further activity has been detected.

.. _`ir_timer_repeat`:

ir_timer_repeat
===============

.. c:function:: void ir_timer_repeat(struct timer_list *t)

    generates a repeat event after a timeout

    :param t:
        a pointer to the struct timer_list
    :type t: struct timer_list \*

.. _`ir_timer_repeat.description`:

Description
-----------

This routine will generate a soft repeat event every REP_PERIOD
milliseconds.

.. _`rc_repeat`:

rc_repeat
=========

.. c:function:: void rc_repeat(struct rc_dev *dev)

    signals that a key is still pressed

    :param dev:
        the struct rc_dev descriptor of the device
    :type dev: struct rc_dev \*

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

    :param dev:
        the struct rc_dev descriptor of the device
    :type dev: struct rc_dev \*

    :param protocol:
        the protocol of the keypress
    :type protocol: enum rc_proto

    :param scancode:
        the scancode of the keypress
    :type scancode: u32

    :param keycode:
        the keycode of the keypress
    :type keycode: u32

    :param toggle:
        the toggle value of the keypress
    :type toggle: u8

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

    :param dev:
        the struct rc_dev descriptor of the device
    :type dev: struct rc_dev \*

    :param protocol:
        the protocol for the keypress
    :type protocol: enum rc_proto

    :param scancode:
        the scancode for the keypress
    :type scancode: u32

    :param toggle:
        the toggle value (protocol dependent, if the protocol doesn't
        support toggle values, this should be set to zero)
    :type toggle: u8

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

    :param dev:
        the struct rc_dev descriptor of the device
    :type dev: struct rc_dev \*

    :param protocol:
        the protocol for the keypress
    :type protocol: enum rc_proto

    :param scancode:
        the scancode for the keypress
    :type scancode: u32

    :param toggle:
        the toggle value (protocol dependent, if the protocol doesn't
        support toggle values, this should be set to zero)
    :type toggle: u8

.. _`rc_keydown_notimeout.description`:

Description
-----------

This routine is used to signal that a key has been pressed on the
remote control. The driver must manually call \ :c:func:`rc_keyup`\  at a later stage.

.. _`rc_validate_scancode`:

rc_validate_scancode
====================

.. c:function:: bool rc_validate_scancode(enum rc_proto proto, u32 scancode)

    checks that a scancode is valid for a protocol. For nec, it should do the opposite of \ :c:func:`ir_nec_bytes_to_scancode`\ 

    :param proto:
        protocol
    :type proto: enum rc_proto

    :param scancode:
        scancode
    :type scancode: u32

.. _`rc_validate_filter`:

rc_validate_filter
==================

.. c:function:: int rc_validate_filter(struct rc_dev *dev, struct rc_scancode_filter *filter)

    checks that the scancode and mask are valid and provides sensible defaults

    :param dev:
        the struct rc_dev descriptor of the device
    :type dev: struct rc_dev \*

    :param filter:
        the scancode and mask
    :type filter: struct rc_scancode_filter \*

.. _`rc_validate_filter.return`:

Return
------

0 or -EINVAL if the filter is not valid

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

    :param device:
        the device descriptor
    :type device: struct device \*

    :param mattr:
        the device attribute struct
    :type mattr: struct device_attribute \*

    :param buf:
        a pointer to the output buffer
    :type buf: char \*

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

.. c:function:: int parse_protocol_change(struct rc_dev *dev, u64 *protocols, const char *buf)

    parses a protocol change request

    :param dev:
        rc_dev device
    :type dev: struct rc_dev \*

    :param protocols:
        pointer to the bitmask of current protocols
    :type protocols: u64 \*

    :param buf:
        pointer to the buffer with a list of changes
    :type buf: const char \*

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

    :param device:
        the device descriptor
    :type device: struct device \*

    :param mattr:
        the device attribute struct
    :type mattr: struct device_attribute \*

    :param buf:
        a pointer to the input buffer
    :type buf: const char \*

    :param len:
        length of the input buffer
    :type len: size_t

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

    :param device:
        the device descriptor
    :type device: struct device \*

    :param attr:
        the device attribute struct
    :type attr: struct device_attribute \*

    :param buf:
        a pointer to the output buffer
    :type buf: char \*

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

    :param device:
        the device descriptor
    :type device: struct device \*

    :param attr:
        the device attribute struct
    :type attr: struct device_attribute \*

    :param buf:
        a pointer to the input buffer
    :type buf: const char \*

    :param len:
        length of the input buffer
    :type len: size_t

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

    :param device:
        the device descriptor
    :type device: struct device \*

    :param mattr:
        the device attribute struct
    :type mattr: struct device_attribute \*

    :param buf:
        a pointer to the output buffer
    :type buf: char \*

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

    :param device:
        the device descriptor
    :type device: struct device \*

    :param mattr:
        the device attribute struct
    :type mattr: struct device_attribute \*

    :param buf:
        a pointer to the input buffer
    :type buf: const char \*

    :param len:
        length of the input buffer
    :type len: size_t

.. _`store_wakeup_protocols.description`:

Description
-----------

This routine is for changing the IR protocol type.
It is trigged by writing to /sys/class/rc/rc?/wakeup_protocols.
Returns \ ``len``\  on success or a negative error code.

dev->lock is taken to guard against races between
store_wakeup_protocols and show_wakeup_protocols.

.. This file was automatic generated / don't edit.

