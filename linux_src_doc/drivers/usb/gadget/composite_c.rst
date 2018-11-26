.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/gadget/composite.c

.. _`usb_os_string`:

struct usb_os_string
====================

.. c:type:: struct usb_os_string

    represents OS String to be reported by a gadget

.. _`usb_os_string.definition`:

Definition
----------

.. code-block:: c

    struct usb_os_string {
        __u8 bLength;
        __u8 bDescriptorType;
        __u8 qwSignature[OS_STRING_QW_SIGN_LEN];
        __u8 bMS_VendorCode;
        __u8 bPad;
    }

.. _`usb_os_string.members`:

Members
-------

bLength
    total length of the entire descritor, always 0x12

bDescriptorType
    USB_DT_STRING

qwSignature
    the OS String proper

bMS_VendorCode
    code used by the host for subsequent requests

bPad
    not used, must be zero

.. _`function_descriptors`:

function_descriptors
====================

.. c:function:: struct usb_descriptor_header **function_descriptors(struct usb_function *f, enum usb_device_speed speed)

    get function descriptors for speed

    :param f:
        the function
    :type f: struct usb_function \*

    :param speed:
        the speed
    :type speed: enum usb_device_speed

.. _`function_descriptors.description`:

Description
-----------

Returns the descriptors or NULL if not set.

.. _`next_ep_desc`:

next_ep_desc
============

.. c:function:: struct usb_descriptor_header** next_ep_desc(struct usb_descriptor_header **t)

    advance to the next EP descriptor

    :param t:
        currect pointer within descriptor array
    :type t: struct usb_descriptor_header \*\*

.. _`next_ep_desc.return`:

Return
------

next EP descriptor or NULL

Iterate over \ ``t``\  until either EP descriptor found or
NULL (that indicates end of list) encountered

.. _`config_ep_by_speed`:

config_ep_by_speed
==================

.. c:function:: int config_ep_by_speed(struct usb_gadget *g, struct usb_function *f, struct usb_ep *_ep)

    configures the given endpoint according to gadget speed.

    :param g:
        pointer to the gadget
    :type g: struct usb_gadget \*

    :param f:
        usb function
    :type f: struct usb_function \*

    :param _ep:
        the endpoint to configure
    :type _ep: struct usb_ep \*

.. _`config_ep_by_speed.return`:

Return
------

error code, 0 on success

This function chooses the right descriptors for a given
endpoint according to gadget speed and saves it in the
endpoint desc field. If the endpoint already has a descriptor
assigned to it - overwrites it with currently corresponding
descriptor. The endpoint maxpacket field is updated according
to the chosen descriptor.

.. _`config_ep_by_speed.note`:

Note
----

the supplied function should hold all the descriptors
for supported speeds

.. _`usb_add_function`:

usb_add_function
================

.. c:function:: int usb_add_function(struct usb_configuration *config, struct usb_function *function)

    add a function to a configuration

    :param config:
        the configuration
    :type config: struct usb_configuration \*

    :param function:
        the function being added
    :type function: struct usb_function \*

.. _`usb_add_function.context`:

Context
-------

single threaded during gadget setup

.. _`usb_add_function.description`:

Description
-----------

After initialization, each configuration must have one or more
functions added to it.  Adding a function involves calling its \ ``bind``\ ()
method to allocate resources such as interface and string identifiers
and endpoints.

This function returns the value of the function's \ :c:func:`bind`\ , which is
zero for success else a negative errno value.

.. _`usb_function_deactivate`:

usb_function_deactivate
=======================

.. c:function:: int usb_function_deactivate(struct usb_function *function)

    prevent function and gadget enumeration

    :param function:
        the function that isn't yet ready to respond
    :type function: struct usb_function \*

.. _`usb_function_deactivate.description`:

Description
-----------

Blocks response of the gadget driver to host enumeration by
preventing the data line pullup from being activated.  This is
normally called during \ ``bind``\ () processing to change from the
initial "ready to respond" state, or when a required resource
becomes available.

For example, drivers that serve as a passthrough to a userspace
daemon can block enumeration unless that daemon (such as an OBEX,
MTP, or print server) is ready to handle host requests.

Not all systems support software control of their USB peripheral
data pullups.

Returns zero on success, else negative errno.

.. _`usb_function_activate`:

usb_function_activate
=====================

.. c:function:: int usb_function_activate(struct usb_function *function)

    allow function and gadget enumeration

    :param function:
        function on which \ :c:func:`usb_function_activate`\  was called
    :type function: struct usb_function \*

.. _`usb_function_activate.description`:

Description
-----------

Reverses effect of \ :c:func:`usb_function_deactivate`\ .  If no more functions
are delaying their activation, the gadget driver will respond to
host enumeration procedures.

Returns zero on success, else negative errno.

.. _`usb_interface_id`:

usb_interface_id
================

.. c:function:: int usb_interface_id(struct usb_configuration *config, struct usb_function *function)

    allocate an unused interface ID

    :param config:
        configuration associated with the interface
    :type config: struct usb_configuration \*

    :param function:
        function handling the interface
    :type function: struct usb_function \*

.. _`usb_interface_id.context`:

Context
-------

single threaded during gadget setup

.. _`usb_interface_id.description`:

Description
-----------

\ :c:func:`usb_interface_id`\  is called from usb_function.bind() callbacks to
allocate new interface IDs.  The function driver will then store that
ID in interface, association, CDC union, and other descriptors.  It
will also handle any control requests targeted at that interface,
particularly changing its altsetting via \ :c:func:`set_alt`\ .  There may
also be class-specific or vendor-specific requests to handle.

All interface identifier should be allocated using this routine, to
ensure that for example different functions don't wrongly assign
different meanings to the same identifier.  Note that since interface
identifiers are configuration-specific, functions used in more than
one configuration (or more than once in a given configuration) need
multiple versions of the relevant descriptors.

Returns the interface ID which was allocated; or -ENODEV if no
more interface IDs can be allocated.

.. _`bos_desc`:

bos_desc
========

.. c:function:: int bos_desc(struct usb_composite_dev *cdev)

    prepares the BOS descriptor.

    :param cdev:
        pointer to usb_composite device to generate the bos
        descriptor for
    :type cdev: struct usb_composite_dev \*

.. _`bos_desc.description`:

Description
-----------

This function generates the BOS (Binary Device Object)
descriptor and its device capabilities descriptors. The BOS
descriptor should be supported by a SuperSpeed device.

.. _`usb_add_config`:

usb_add_config
==============

.. c:function:: int usb_add_config(struct usb_composite_dev *cdev, struct usb_configuration *config, int (*bind)(struct usb_configuration *))

    add a configuration to a device.

    :param cdev:
        wraps the USB gadget
    :type cdev: struct usb_composite_dev \*

    :param config:
        the configuration, with bConfigurationValue assigned
    :type config: struct usb_configuration \*

    :param int (\*bind)(struct usb_configuration \*):
        the configuration's bind function

.. _`usb_add_config.context`:

Context
-------

single threaded during gadget setup

.. _`usb_add_config.description`:

Description
-----------

One of the main tasks of a composite \ ``bind``\ () routine is to
add each of the configurations it supports, using this routine.

This function returns the value of the configuration's \ ``bind``\ (), which
is zero for success else a negative errno value.  Binding configurations
assigns global resources including string IDs, and per-configuration
resources such as interface IDs and endpoints.

.. _`usb_remove_config`:

usb_remove_config
=================

.. c:function:: void usb_remove_config(struct usb_composite_dev *cdev, struct usb_configuration *config)

    remove a configuration from a device.

    :param cdev:
        wraps the USB gadget
    :type cdev: struct usb_composite_dev \*

    :param config:
        the configuration
    :type config: struct usb_configuration \*

.. _`usb_remove_config.description`:

Description
-----------

Drivers must call usb_gadget_disconnect before calling this function
to disconnect the device from the host and make sure the host will not
try to enumerate the device while we are changing the config list.

.. _`usb_string_id`:

usb_string_id
=============

.. c:function:: int usb_string_id(struct usb_composite_dev *cdev)

    allocate an unused string ID

    :param cdev:
        the device whose string descriptor IDs are being allocated
    :type cdev: struct usb_composite_dev \*

.. _`usb_string_id.context`:

Context
-------

single threaded during gadget setup

.. _`usb_string_id.description`:

Description
-----------

\ ``usb_string_id``\ () is called from \ :c:func:`bind`\  callbacks to allocate
string IDs.  Drivers for functions, configurations, or gadgets will
then store that ID in the appropriate descriptors and string table.

All string identifier should be allocated using this,
\ ``usb_string_ids_tab``\ () or \ ``usb_string_ids_n``\ () routine, to ensure
that for example different functions don't wrongly assign different
meanings to the same identifier.

.. _`usb_string_ids_tab`:

usb_string_ids_tab
==================

.. c:function:: int usb_string_ids_tab(struct usb_composite_dev *cdev, struct usb_string *str)

    allocate unused string IDs in batch

    :param cdev:
        the device whose string descriptor IDs are being allocated
    :type cdev: struct usb_composite_dev \*

    :param str:
        an array of usb_string objects to assign numbers to
    :type str: struct usb_string \*

.. _`usb_string_ids_tab.context`:

Context
-------

single threaded during gadget setup

.. _`usb_string_ids_tab.description`:

Description
-----------

\ ``usb_string_ids``\ () is called from \ :c:func:`bind`\  callbacks to allocate
string IDs.  Drivers for functions, configurations, or gadgets will
then copy IDs from the string table to the appropriate descriptors
and string table for other languages.

All string identifier should be allocated using this,
\ ``usb_string_id``\ () or \ ``usb_string_ids_n``\ () routine, to ensure that for
example different functions don't wrongly assign different meanings
to the same identifier.

.. _`usb_gstrings_attach`:

usb_gstrings_attach
===================

.. c:function:: struct usb_string *usb_gstrings_attach(struct usb_composite_dev *cdev, struct usb_gadget_strings **sp, unsigned n_strings)

    attach gadget strings to a cdev and assign ids

    :param cdev:
        the device whose string descriptor IDs are being allocated
        and attached.
    :type cdev: struct usb_composite_dev \*

    :param sp:
        an array of usb_gadget_strings to attach.
    :type sp: struct usb_gadget_strings \*\*

    :param n_strings:
        number of entries in each usb_strings array (sp[]->strings)
    :type n_strings: unsigned

.. _`usb_gstrings_attach.description`:

Description
-----------

This function will create a deep copy of usb_gadget_strings and usb_string
and attach it to the cdev. The actual string (usb_string.s) will not be
copied but only a referenced will be made. The struct usb_gadget_strings
array may contain multiple languages and should be NULL terminated.
The ->language pointer of each struct usb_gadget_strings has to contain the
same amount of entries.
For instance: sp[0] is en-US, sp[1] is es-ES. It is expected that the first
usb_string entry of es-ES contains the translation of the first usb_string
entry of en-US. Therefore both entries become the same id assign.

.. _`usb_string_ids_n`:

usb_string_ids_n
================

.. c:function:: int usb_string_ids_n(struct usb_composite_dev *c, unsigned n)

    allocate unused string IDs in batch

    :param c:
        the device whose string descriptor IDs are being allocated
    :type c: struct usb_composite_dev \*

    :param n:
        number of string IDs to allocate
    :type n: unsigned

.. _`usb_string_ids_n.context`:

Context
-------

single threaded during gadget setup

.. _`usb_string_ids_n.description`:

Description
-----------

Returns the first requested ID.  This ID and next \ ``n``\ -1 IDs are now
valid IDs.  At least provided that \ ``n``\  is non-zero because if it
is, returns last requested ID which is now very useful information.

\ ``usb_string_ids_n``\ () is called from \ :c:func:`bind`\  callbacks to allocate
string IDs.  Drivers for functions, configurations, or gadgets will
then store that ID in the appropriate descriptors and string table.

All string identifier should be allocated using this,
\ ``usb_string_id``\ () or \ ``usb_string_ids_n``\ () routine, to ensure that for
example different functions don't wrongly assign different meanings
to the same identifier.

.. _`usb_composite_probe`:

usb_composite_probe
===================

.. c:function:: int usb_composite_probe(struct usb_composite_driver *driver)

    register a composite driver

    :param driver:
        the driver to register
    :type driver: struct usb_composite_driver \*

.. _`usb_composite_probe.context`:

Context
-------

single threaded during gadget setup

.. _`usb_composite_probe.description`:

Description
-----------

This function is used to register drivers using the composite driver
framework.  The return value is zero, or a negative errno value.
Those values normally come from the driver's \ ``bind``\  method, which does
all the work of setting up the driver to match the hardware.

On successful return, the gadget is ready to respond to requests from
the host, unless one of its components invokes \ :c:func:`usb_gadget_disconnect`\ 
while it was binding.  That would usually be done in order to wait for
some userspace participation.

.. _`usb_composite_unregister`:

usb_composite_unregister
========================

.. c:function:: void usb_composite_unregister(struct usb_composite_driver *driver)

    unregister a composite driver

    :param driver:
        the driver to unregister
    :type driver: struct usb_composite_driver \*

.. _`usb_composite_unregister.description`:

Description
-----------

This function is used to unregister drivers using the composite
driver framework.

.. _`usb_composite_setup_continue`:

usb_composite_setup_continue
============================

.. c:function:: void usb_composite_setup_continue(struct usb_composite_dev *cdev)

    Continue with the control transfer

    :param cdev:
        the composite device who's control transfer was kept waiting
    :type cdev: struct usb_composite_dev \*

.. _`usb_composite_setup_continue.description`:

Description
-----------

This function must be called by the USB function driver to continue
with the control transfer's data/status stage in case it had requested to
delay the data/status stages. A USB function's setup handler (e.g. \ :c:func:`set_alt`\ )
can request the composite framework to delay the setup request's data/status
stages by returning USB_GADGET_DELAYED_STATUS.

.. This file was automatic generated / don't edit.

