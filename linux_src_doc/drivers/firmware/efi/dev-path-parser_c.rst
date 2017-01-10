.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/firmware/efi/dev-path-parser.c

.. _`efi_get_device_by_path`:

efi_get_device_by_path
======================

.. c:function:: struct device *efi_get_device_by_path(struct efi_dev_path **node, size_t *len)

    find device by EFI Device Path

    :param struct efi_dev_path \*\*node:
        EFI Device Path

    :param size_t \*len:
        maximum length of EFI Device Path in bytes

.. _`efi_get_device_by_path.description`:

Description
-----------

Parse a series of EFI Device Path nodes at \ ``node``\  and find the corresponding
device.  If the device was found, its reference count is incremented and a
pointer to it is returned.  The caller needs to drop the reference with
\ :c:func:`put_device`\  after use.  The \ ``node``\  pointer is updated to point to the
location immediately after the "End of Hardware Device Path" node.

If another Device Path instance follows, \ ``len``\  is decremented by the number
of bytes consumed.  Otherwise \ ``len``\  is set to \ ``0``\ .

If a Device Path node is malformed or its corresponding device is not found,
\ ``node``\  is updated to point to this offending node and an ERR_PTR is returned.

If \ ``len``\  is initially \ ``0``\ , the function returns \ ``NULL``\ .  Thus, to iterate over
all instances in a path, the following idiom may be used:

while (!IS_ERR_OR_NULL(dev = efi_get_device_by_path(&node, \ :c:type:`struct len <len>`\ ))) {
// do something with dev
put_device(dev);
}
if (IS_ERR(dev))
// report error

Devices can only be found if they're already instantiated. Most buses
instantiate devices in the "subsys" initcall level, hence the earliest
initcall level in which this function should be called is "fs".

Returns the device on success or
\ ``ERR_PTR``\ (-ENODEV) if no device was found,
\ ``ERR_PTR``\ (-EINVAL) if a node is malformed or exceeds \ ``len``\ ,
\ ``ERR_PTR``\ (-ENOTSUPP) if support for a node type is not yet implemented.

.. This file was automatic generated / don't edit.

