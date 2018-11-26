.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/hotplug/cpqphp_ctrl.c

.. _`cpqhp_find_slot`:

cpqhp_find_slot
===============

.. c:function:: struct slot *cpqhp_find_slot(struct controller *ctrl, u8 device)

    find the struct slot of given device

    :param ctrl:
        scan lots of this controller
    :type ctrl: struct controller \*

    :param device:
        the device id to find
    :type device: u8

.. _`sort_by_size`:

sort_by_size
============

.. c:function:: int sort_by_size(struct pci_resource **head)

    sort nodes on the list by their length, smallest first.

    :param head:
        list to sort
    :type head: struct pci_resource \*\*

.. _`sort_by_max_size`:

sort_by_max_size
================

.. c:function:: int sort_by_max_size(struct pci_resource **head)

    sort nodes on the list by their length, largest first.

    :param head:
        list to sort
    :type head: struct pci_resource \*\*

.. _`do_pre_bridge_resource_split`:

do_pre_bridge_resource_split
============================

.. c:function:: struct pci_resource *do_pre_bridge_resource_split(struct pci_resource **head, struct pci_resource **orig_head, u32 alignment)

    find node of resources that are unused

    :param head:
        new list head
    :type head: struct pci_resource \*\*

    :param orig_head:
        original list head
    :type orig_head: struct pci_resource \*\*

    :param alignment:
        max node size (?)
    :type alignment: u32

.. _`do_bridge_resource_split`:

do_bridge_resource_split
========================

.. c:function:: struct pci_resource *do_bridge_resource_split(struct pci_resource **head, u32 alignment)

    find one node of resources that aren't in use

    :param head:
        list head
    :type head: struct pci_resource \*\*

    :param alignment:
        max node size (?)
    :type alignment: u32

.. _`get_io_resource`:

get_io_resource
===============

.. c:function:: struct pci_resource *get_io_resource(struct pci_resource **head, u32 size)

    find first node of given size not in ISA aliasing window.

    :param head:
        list to search
    :type head: struct pci_resource \*\*

    :param size:
        size of node to find, must be a power of two.
    :type size: u32

.. _`get_io_resource.description`:

Description
-----------

This function sorts the resource list by size and then returns
returns the first node of "size" length that is not in the ISA aliasing
window.  If it finds a node larger than "size" it will split it up.

.. _`get_max_resource`:

get_max_resource
================

.. c:function:: struct pci_resource *get_max_resource(struct pci_resource **head, u32 size)

    get largest node which has at least the given size.

    :param head:
        the list to search the node in
    :type head: struct pci_resource \*\*

    :param size:
        the minimum size of the node to find
    :type size: u32

.. _`get_max_resource.description`:

Description
-----------

Gets the largest node that is at least "size" big from the
list pointed to by head.  It aligns the node on top and bottom
to "size" alignment before returning it.

.. _`get_resource`:

get_resource
============

.. c:function:: struct pci_resource *get_resource(struct pci_resource **head, u32 size)

    find resource of given size and split up larger ones.

    :param head:
        the list to search for resources
    :type head: struct pci_resource \*\*

    :param size:
        the size limit to use
    :type size: u32

.. _`get_resource.description`:

Description
-----------

This function sorts the resource list by size and then
returns the first node of "size" length.  If it finds a node
larger than "size" it will split it up.

size must be a power of two.

.. _`cpqhp_resource_sort_and_combine`:

cpqhp_resource_sort_and_combine
===============================

.. c:function:: int cpqhp_resource_sort_and_combine(struct pci_resource **head)

    sort nodes by base addresses and clean up

    :param head:
        the list to sort and clean up
    :type head: struct pci_resource \*\*

.. _`cpqhp_resource_sort_and_combine.description`:

Description
-----------

Sorts all of the nodes in the list in ascending order by
their base addresses.  Also does garbage collection by
combining adjacent nodes.

Returns \ ``0``\  if success.

.. _`cpqhp_slot_create`:

cpqhp_slot_create
=================

.. c:function:: struct pci_func *cpqhp_slot_create(u8 busnumber)

    Creates a node and adds it to the proper bus.

    :param busnumber:
        bus where new node is to be located
    :type busnumber: u8

.. _`cpqhp_slot_create.description`:

Description
-----------

Returns pointer to the new node or \ ``NULL``\  if unsuccessful.

.. _`slot_remove`:

slot_remove
===========

.. c:function:: int slot_remove(struct pci_func *old_slot)

    Removes a node from the linked list of slots.

    :param old_slot:
        slot to remove
    :type old_slot: struct pci_func \*

.. _`slot_remove.description`:

Description
-----------

Returns \ ``0``\  if successful, !0 otherwise.

.. _`bridge_slot_remove`:

bridge_slot_remove
==================

.. c:function:: int bridge_slot_remove(struct pci_func *bridge)

    Removes a node from the linked list of slots.

    :param bridge:
        bridge to remove
    :type bridge: struct pci_func \*

.. _`bridge_slot_remove.description`:

Description
-----------

Returns \ ``0``\  if successful, !0 otherwise.

.. _`cpqhp_slot_find`:

cpqhp_slot_find
===============

.. c:function:: struct pci_func *cpqhp_slot_find(u8 bus, u8 device, u8 index)

    Looks for a node by bus, and device, multiple functions accessed

    :param bus:
        bus to find
    :type bus: u8

    :param device:
        device to find
    :type device: u8

    :param index:
        is \ ``0``\  for first function found, \ ``1``\  for the second...
    :type index: u8

.. _`cpqhp_slot_find.description`:

Description
-----------

Returns pointer to the node if successful, \ ``NULL``\  otherwise.

.. _`set_controller_speed`:

set_controller_speed
====================

.. c:function:: u8 set_controller_speed(struct controller *ctrl, u8 adapter_speed, u8 hp_slot)

    set the frequency and/or mode of a specific controller segment.

    :param ctrl:
        controller to change frequency/mode for.
    :type ctrl: struct controller \*

    :param adapter_speed:
        the speed of the adapter we want to match.
    :type adapter_speed: u8

    :param hp_slot:
        the slot number where the adapter is installed.
    :type hp_slot: u8

.. _`set_controller_speed.description`:

Description
-----------

Returns \ ``0``\  if we successfully change frequency and/or mode to match the
adapter speed.

.. _`board_replaced`:

board_replaced
==============

.. c:function:: u32 board_replaced(struct pci_func *func, struct controller *ctrl)

    Called after a board has been replaced in the system.

    :param func:
        PCI device/function information
    :type func: struct pci_func \*

    :param ctrl:
        hotplug controller
    :type ctrl: struct controller \*

.. _`board_replaced.description`:

Description
-----------

This is only used if we don't have resources for hot add.
Turns power on for the board.
Checks to see if board is the same.
If board is same, reconfigures it.
If board isn't same, turns it back off.

.. _`board_added`:

board_added
===========

.. c:function:: u32 board_added(struct pci_func *func, struct controller *ctrl)

    Called after a board has been added to the system.

    :param func:
        PCI device/function info
    :type func: struct pci_func \*

    :param ctrl:
        hotplug controller
    :type ctrl: struct controller \*

.. _`board_added.description`:

Description
-----------

Turns power on for the board.
Configures board.

.. _`remove_board`:

remove_board
============

.. c:function:: u32 remove_board(struct pci_func *func, u32 replace_flag, struct controller *ctrl)

    Turns off slot and LEDs

    :param func:
        PCI device/function info
    :type func: struct pci_func \*

    :param replace_flag:
        whether replacing or adding a new device
    :type replace_flag: u32

    :param ctrl:
        target controller
    :type ctrl: struct controller \*

.. _`cpqhp_pushbutton_thread`:

cpqhp_pushbutton_thread
=======================

.. c:function:: void cpqhp_pushbutton_thread(struct timer_list *t)

    handle pushbutton events

    :param t:
        *undescribed*
    :type t: struct timer_list \*

.. _`cpqhp_pushbutton_thread.description`:

Description
-----------

Scheduled procedure to handle blocking stuff for the pushbuttons.
Handles all pending events and exits.

.. _`switch_leds`:

switch_leds
===========

.. c:function:: void switch_leds(struct controller *ctrl, const int num_of_slots, u32 *work_LED, const int direction)

    switch the leds, go from one site to the other.

    :param ctrl:
        controller to use
    :type ctrl: struct controller \*

    :param num_of_slots:
        number of slots to use
    :type num_of_slots: const int

    :param work_LED:
        LED control value
    :type work_LED: u32 \*

    :param direction:
        1 to start from the left side, 0 to start right.
    :type direction: const int

.. _`cpqhp_hardware_test`:

cpqhp_hardware_test
===================

.. c:function:: int cpqhp_hardware_test(struct controller *ctrl, int test_num)

    runs hardware tests

    :param ctrl:
        target controller
    :type ctrl: struct controller \*

    :param test_num:
        the number written to the "test" file in sysfs.
    :type test_num: int

.. _`cpqhp_hardware_test.description`:

Description
-----------

For hot plug ctrl folks to play with.

.. _`configure_new_device`:

configure_new_device
====================

.. c:function:: u32 configure_new_device(struct controller *ctrl, struct pci_func *func, u8 behind_bridge, struct resource_lists *resources)

    Configures the PCI header information of one board.

    :param ctrl:
        pointer to controller structure
    :type ctrl: struct controller \*

    :param func:
        pointer to function structure
    :type func: struct pci_func \*

    :param behind_bridge:
        1 if this is a recursive call, 0 if not
    :type behind_bridge: u8

    :param resources:
        pointer to set of resource lists
    :type resources: struct resource_lists \*

.. _`configure_new_device.description`:

Description
-----------

Returns 0 if success.

.. _`configure_new_function`:

configure_new_function
======================

.. c:function:: int configure_new_function(struct controller *ctrl, struct pci_func *func, u8 behind_bridge, struct resource_lists *resources)

    Configures the PCI header information of one device

    :param ctrl:
        pointer to controller structure
    :type ctrl: struct controller \*

    :param func:
        pointer to function structure
    :type func: struct pci_func \*

    :param behind_bridge:
        1 if this is a recursive call, 0 if not
    :type behind_bridge: u8

    :param resources:
        pointer to set of resource lists
    :type resources: struct resource_lists \*

.. _`configure_new_function.description`:

Description
-----------

Calls itself recursively for bridged devices.
Returns 0 if success.

.. This file was automatic generated / don't edit.

